# PANDUAN REFERENSI: DATABASE DESIGN CHECKLIST (ON-DEMAND)
**Direktori Rujukan On-Demand untuk Gerbang Perencanaan (`/plan`) — KHUSUS PROYEK DENGAN DATABASE**

> 💡 **Aturan Proporsionalitas Mentor:**
> Tidak semua proyek kampus butuh arsitektur database kelas raksasa. Checklist ini dibagi menjadi **Tingkat 1 (Wajib Dasar di Semua Proyek DB)** dan **Tingkat 2 (Skala Produksi — lengkap dengan panduan kapan wajib vs kapan boleh dilewati)**.

---

## 🧱 TINGKAT 1: STANDAR WAJIB DASAR (Berlaku di 100% Proyek Ber-Database)

Sebelum mengesahkan DDL / file migrasi di `/plan`, AI **WAJIB** memverifikasi 5 fondasi berikut:

1. **Normalisasi & Pemisahan Entitas (Anti-God Table):**
   - Pastikan relasi *Many-to-Many* menggunakan *junction/pivot table* eksplisit (contoh: `task_labels` dengan composite unique key `(task_id, label_id)`), bukan menyimpan array ID dalam satu kolom string koma (`"1,2,3"`).
   - Pisahkan data yang berubah cepat (transaksi/log) dari data master (profil/katalog).
2. **Integritas Referensial & Klausul `ON DELETE` Eksplisit:**
   - Setiap kolom Foreign Key **WAJIB** menentukan perilaku penghapusan secara sadar:
     * `ON DELETE RESTRICT` (Default aman untuk data penting/keuangan/riwayat: cegah penghapusan induk jika masih punya anak).
     * `ON DELETE CASCADE` (Hanya untuk entitas anak yang mutlak tidak bermakna tanpa induknya, misal `order_items` atau `sessions`).
     * `ON DELETE SET NULL` (Untuk relasi opsional seperti `assigned_to`).
3. **Audit Timestamps & Tipe Data Presisi:**
   - Sertakan `created_at` dan `updated_at` (gunakan tipe `TIMESTAMPTZ` / UTC-aware agar aman lintas zona waktu).
   - **Larangan `FLOAT/DOUBLE` untuk Uang:** Untuk harga, saldo, atau nominal rupiah/mata uang, **WAJIB** gunakan `BIGINT` (satuan terkecil/integer) atau `DECIMAL(15, 2)` agar bebas bug pembulatan floating-point.
4. **Strategi Indexing Dasar (Cegah Full Table Scan):**
   - Setiap kolom Foreign Key (`user_id`, `category_id`) wajib memiliki index (PostgreSQL tidak otomatis meng-index FK!).
   - Setiap kolom yang sering masuk klausa `WHERE`, `ORDER BY`, atau `JOIN` (seperti `slug`, `email`, `status`) wajib direncanakan index-nya.
   - Untuk filter multi-kolom yang sering dipakai bersamaan (misal `WHERE status = 'active' ORDER BY created_at DESC`), gunakan **Composite Index** dengan urutan *Equality column* di depan, *Range/Sort column* di belakang: `(status, created_at DESC)`.
5. **Pencegahan Duplikasi & Race Condition di Level DB:**
   - Jangan hanya mengandalkan validasi aplikasi (`if exists`) untuk keunikan data — kunci dengan `UNIQUE CONSTRAINT` di level database (misal `UNIQUE(email)` atau `UNIQUE(student_nim, event_id)`).

---

## 🏗️ TINGKAT 2: POLA ENTERPRISE & SKALA PRODUKSI (Proporsional)

### 1. Soft Delete & Partial Indexing (`WHERE deleted_at IS NULL`)
* **Masalah yang Diselesaikan:** Jika tabel memakai *Soft Delete* (`deleted_at`), `UNIQUE(email)` biasa akan memblokir user mendaftar ulang dengan email yang akun lamanya sudah dihapus, dan index membengkak menampung baris sampah.
* **Pola Solusi:**
  ```sql
  -- Hanya mengunci keunikan & meng-index baris yang masih aktif
  CREATE UNIQUE INDEX idx_users_active_email
    ON users (email)
    WHERE deleted_at IS NULL;
  ```
* 🎓 **Kapan Wajib vs Kapan Lewati:**
  - **Wajib Pakai Jika:** Tabel menggunakan *Soft Delete* (`deleted_at`) di PostgreSQL/SQLite modern dan memiliki kolom unik (`email`, `slug`, `kode`).
  - **Boleh Lewati Jika:** Tabel menggunakan *Hard Delete* biasa, atau menggunakan MySQL lama yang belum mendukung *filtered/partial index* (di MySQL, kompensasikan dengan kolom bantu atau aturan unik pada status aktif).

### 2. Row-Level Security (RLS) & Multi-Tenant Isolation
* **Masalah yang Diselesaikan:** Pada aplikasi SaaS / multi-organisasi (misal 1 platform dipakai banyak UKM/Ormawa sekaligus), lupa menulis `WHERE organization_id = ?` di satu query saja bisa membocorkan data rahasia organisasi lain.
* **Pola Solusi:**
  - Wajib tambahkan `organization_id` / `tenant_id` pada semua tabel milik tenant.
  - Pada PostgreSQL/Supabase, aktifkan kebijakan RLS di level engine database sebagai benteng lapis kedua di luar middleware aplikasi:
    ```sql
    ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
    CREATE POLICY tenant_isolation ON documents
      USING (organization_id = current_setting('app.current_org_id')::uuid);
    ```
* 🎓 **Kapan Wajib vs Kapan Lewati:**
  - **Wajib Pakai Jika:** Aplikasi bersifat *multi-tenant* (banyak organisasi/toko/instansi terisolasi dalam 1 database) atau memakai Supabase dengan akses client langsung.
  - **Boleh Lewati Jika:** Aplikasi hanya milik 1 organisasi tunggal (*single-tenant*) dengan autentikasi backend Laravel/Express terpusat via Policy/Middleware.

### 3. Pola Migrasi Aman Tanpa Downtime (*Expand & Contract*)
* **Masalah yang Diselesaikan:** Mengubah nama kolom (`RENAME COLUMN`) atau menghapus kolom (`DROP COLUMN`) secara langsung pada database produksi yang sedang aktif akan langsung membuat aplikasi lama *crash* (`500 Internal Server Error`) selama jeda deploy.
* **Pola 3 Langkah Aman:**
  1. **Expand:** Tambah kolom/tabel baru (`nullable`) tanpa menghapus kolom lama; tulis data ke keduanya (*dual-write*).
  2. **Migrate & Switch:** Backfill data lama ke kolom baru, lalu ubah kode aplikasi membaca dari kolom baru.
  3. **Contract:** Setelah kode baru stabil 100%, barulah jalankan migrasi terpisah untuk menghapus kolom lama.
* 🎓 **Kapan Wajib vs Kapan Lewati:**
  - **Wajib Pakai Jika:** Aplikasi sudah *live* dipakai pengguna nyata di produksi dan tidak boleh ada *downtime* atau kehilangan data.
  - **Boleh Lewati Jika:** Proyek masih tahap awal pengembangan lokal / belum rilis ke produksi (migrasi langsung diperbolehkan selama tercatat bersih di file migration).

---

## 📊 Format Wajib Diagram Relasi di `/plan`

Saat merancang tabel baru di `/plan`, AI wajib menyertakan ringkasan **Mermaid `erDiagram`** singkat agar mahasiswa langsung melihat peta relasi antar tabel sebelum menulis migration.
