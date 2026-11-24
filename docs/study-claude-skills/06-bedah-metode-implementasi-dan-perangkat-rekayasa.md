# Bedah Mendalam: Metode Implementasi, Perangkat API, Focused Fix & Arsitektur Database
**Dokumen Studi Lanjutan Fase 3:** Menjawab rasa ingin tahu mengenai *bagaimana* repositori enterprise mengimplementasikan nilai-nilainya secara teknis, membedah 3 perkakas review API, merinci metodologi *Focused Fix*, memperkuat arsitektur database, dan mengomparasikan **metode implementasi deterministik vs pure LLM prompting**.

---

## 1. Mengapa Perbedaan "Metode Implementasi" Menghasilkan Hasil yang Berbeda?

Sebelum membedah alat-alatnya, kita harus menjawab pertanyaan mendasar:  
> *"Mengapa kita tidak cukup menyuruh AI di prompt saja: 'Tolong review API ini dan cek apakah ada breaking change'?"*

Di dunia rekayasa agen AI, ada **2 Metode Implementasi yang Bertolak Belakang**:

```
[ METODE 1: Pure LLM Prompting (Metode FORGE Saat Ini) ]
User Kirim File ──► Dimasukkan ke Prompt AI ──► LLM Membaca & Menebak ──► Hasil Narasi Teks

[ METODE 2: Deterministic Hybrid (Metode Standar Enterprise) ]
User Kirim File ──► Skrip Python (AST Parser) ──► Hitung Algoritma Matematis ──► Exit Code Gate
                                                          │
                                                          ▼
                                                  Output JSON Terstruktur ──► AI Merangkum ke User
```

| Parameter | Metode 1: Pure LLM Prompting (FORGE) | Metode 2: Deterministic Hybrid (Enterprise) |
| :--- | :--- | :--- |
| **Media Eksekusi** | Narasi teks instruksi di file markdown besar. | Skrip Python lokal (Standard Library) + file schema AST. |
| **Akurasi & Deteksi** | **Probabilistik (Bisa Berhalusinasi):** LLM bisa melewatkan tipe data yang berubah dari `int` ke `string` jika dokumen JSON panjang. | **Deterministik (100% Eksak):** Script membandingkan key JSON secara rekursif via code. 0 kemungkinan terlewat. |
| **Konsumsi Token** | **Sangat Boros:** Seluruh file OpenAPI v1 dan v2 (bisa 10.000 token) harus masuk ke jendela konteks LLM. | **Nol Token Prompt:** Script berjalan di terminal lokal (CPU). Hanya kesimpulan JSON akhir yang dibaca AI. |
| **Kecepatan** | 10 – 30 detik (menunggu inferensi LLM streaming). | 5 – 20 milidetik (kecepatan CPU Python). |
| **Penegakan Gate** | **Himbauan Moral Teks:** AI berkata *"Ini kayaknya breaking change, jangan dideploy ya"*, tapi user/AI bisa lupa. | **Hard Terminal Gate:** Skrip keluar dengan `exit code 1`. CI/CD atau terminal langsung menolak jalan secara fisik. |

---

## 2. Bedah 3 Alat Uji API (`api-design-reviewer`): Mekanisme & Dampak

Di katalog enterprise, skill `api-design-reviewer` tidak sekadar memberi saran kosmetik. Ia mempersenjatai agen dengan **3 skrip Python deterministik**:

---

### Alat 1: `api_linter.py` (Penegak Konvensi & Higienitas REST)

* **Mekanisme Kerja Algoritma:**
  1. Skrip mem-parsing spesifikasi `openapi.json` / `swagger.json` menjadi Abstract Syntax Tree (AST).
  2. **Regex Naming Validation:** Mengecek path URI dengan regex:
     * Resource URL **wajib `kebab-case`** (contoh: `/order-items`, bukan `/orderItems` atau `/order_items`).
     * Field request/response JSON **wajib `camelCase`** (contoh: `customerId`).
  3. **HTTP Verb Semantic Audit:**
     * Menolak penggunaan kata kerja di dalam path URL (contoh: `POST /getUsers` atau `GET /deleteUser` langsung di-flag sebagai pelanggaran berat).
  4. **Status Code Compliance:**
     * Memastikan request `POST` menghasilkan `201 Created` (bukan sekadar `200 OK`).
     * Memastikan endpoint `DELETE` menghasilkan `204 No Content` atau `200 OK`.
     * Memastikan respon error memiliki struktur baku (memiliki field `error.code`, `error.message`, dan `error.details`).
* **Dampak Teknis & Bisnis (Impact):**
  * Menghilangkan perdebatan subjektif saat PR review antar-developer.
  * Menjamin seluruh developer di tim membuat endpoint dengan gaya penamaan yang seragam 100%.

---

### Alat 2: `breaking_change_detector.py` (Pencegah Bencana Klien Mobile & SDK)

* **Mekanisme Kerja Algoritma:**
  Skrip menerima 2 argumen: file versi lama (`v1.json`) dan versi baru (`v2.json`), lalu melakukan deep-diff terstruktur pada skema:
  1. **Removed Endpoints:** Mendeteksi jika ada path atau HTTP method yang dihapus. *(Severity: CRITICAL)*.
  2. **Type Mutation:** Mendeteksi jika tipe data field berubah (misal: field `age` tadinya `integer`, di v2 diubah jadi `string`). *(Severity: CRITICAL)*.
  3. **New Required Fields:** Mendeteksi jika ada field request baru yang diberi status `required: true`. Jika klien lama mengirim request tanpa field ini, server akan me-reject. *(Severity: HIGH)*.
  4. **Removed Response Fields:** Mendeteksi jika field di respon JSON dihapus padahal klien lama masih bergantung membaca field tersebut. *(Severity: HIGH)*.
  5. **Status Code Mutation:** Mendeteksi jika respon sukses diubah dari `200` ke `202`. *(Severity: MEDIUM)*.
  * **Mekanisme Exit Gate:** Jika dijalankan dengan flag `--exit-on-breaking`, skrip akan melempar **Exit Code 1**, otomatis mematikan proses build pipeline jika ada breaking change yang tidak dinaikkan versinya (`v2`).
* **Dampak Teknis & Bisnis (Impact):**
  * **Zero Mobile App Crash:** Mencegah insiden di mana ribuan pengguna aplikasi Android/iOS lama mengalami crash massal karena backend mengubah format respon JSON tanpa sengaja.

---

### Alat 3: `api_scorecard.py` (Audit Mutu Kuantitatif Berbobot)

Inilah alat yang sangat menarik! Alih-alih opini *"API ini kayaknya sudah bagus"*, skrip ini menghitung **skor matematis 0–100 dan menerbitkan Nilai Huruf (Letter Grade A s.d. F)** berdasarkan 5 Dimensi Terbobot:

```
                  BOBOT PENILAIAN API SCORECARD
                               │
       ┌───────────────┬───────┴───────┬───────────────┐
       ▼               ▼               ▼               ▼
 Consistency    Documentation       Security       Usability &
    (30%)           (20%)            (20%)      Performance (30%)
```

* **Mekanisme 5 Dimensi Penilaian:**
  1. **Consistency (Bobot 30%):** Kepatuhan konvensi penamaan field, keseragaman payload error, dan konsistensi header HTTP.
  2. **Documentation (Bobot 20%):** Kelengkapan deskripsi endpoint, ada/tidaknya contoh request/response (*examples*), dan penjelasan status code 4xx/5xx.
  3. **Security (Bobot 20%):** Ada/tidaknya definisi skema autentikasi (Bearer/OAuth2), proteksi HTTPS, dan pelarangan query parameter sensitif (misal: melarang `?token=` di URL).
  4. **Usability (Bobot 15%):** Kemudahan developer (*Developer Experience*), kepatuhan REST, dan kejelasan navigasi relasi ID.
  5. **Performance (Bobot 15%):** Adanya standarisasi parameter pagination (`limit`, `offset`/`cursor`), filtering, dan header caching (`ETag`, `Cache-Control`).
* **Mekanisme Ambang Batas Gate (`--min-grade`):**
  ```bash
  python3 scripts/api_scorecard.py openapi.json --min-grade B
  ```
  Jika skor total berada di bawah 80 (Grade C, D, atau F), skrip akan melempar exit code failure dan mengeluarkan rekomendasi konkret:
  > *"Skor 74/100 (Grade C). Masalah: 12 endpoint tidak memiliki pagination, 4 endpoint tidak memiliki dokumentasi error 401. Perbaiki 2 hal ini untuk mencapai Grade B."*
* **Dampak Teknis & Bisnis (Impact):**
  * Memberi Tech Lead tolak ukur objektif dan kuantitatif untuk menolak atau menyetujui rilis API.

---

## 3. Bedah Metodologi `focused-fix`: Anti-Shotgun Debugging

Di FORGE, kamu memiliki `/debug`. Namun, repositori enterprise memiliki skill perbaikan fitur bernama `focused-fix` dengan disiplin yang sangat ketat:

### The Iron Law (Hukum Besi)
> ```
> NO FIXES WITHOUT COMPLETING: SCOPE ──► TRACE ──► DIAGNOSE FIRST
> ```
> *AI DIHARAMKAN menyentuh atau mengedit satu baris kode pun sebelum Fase 1, 2, dan 3 selesai 100%.*

### 5 Fase Berurutan (Strictly Sequential):

```
[ Fase 1: SCOPE ] ──► [ Fase 2: TRACE ] ──► [ Fase 3: DIAGNOSE ] ──► [ Fase 4: FIX ] ──► [ Fase 5: VERIFY ]
  Petakan folder        Petakan Inbound &     Temukan akar masalah   Perbaiki urut:       Jalankan tes modul
  & manifest berkas     Outbound dependency    bukan gejala           Tipe -> Logika       & tes consumer
```

1. **Fase 1 (SCOPE):** AI wajib menginventarisasi batas modul:
   * Menghasilkan *Feature Manifest*: file mana yang menjadi *Entry Point* (diekspor ke luar), file mana yang *Internal*, berapa total baris.
2. **Fase 2 (TRACE):** AI wajib memetakan graf dependensi 2 arah:
   * **Inbound:** Apa saja yang diimpor oleh modul ini? (Library luar, database model, file env).
   * **Outbound:** Siapa saja file di luar sana yang mengimpor modul ini? (Consumer files).
3. **Fase 3 (DIAGNOSE):** AI membuktikan akar masalah (*Root Cause*), bukan menambal gejala:
   * Membaca log error nyata, membuat test case yang mereproduksi crash secara konsisten.
4. **Fase 4 (FIX):** AI memperbaiki dengan urutan ketat:  
   *Perbaiki dependensi $\rightarrow$ Perbaiki tipe data $\rightarrow$ Perbaiki logika bisnis $\rightarrow$ Perbaiki unit test.*
5. **Fase 5 (VERIFY):**  
   AI tidak hanya menjalankan tes pada modul yang diperbaiki, **tetapi wajib menjalankan tes pada seluruh file konsumen (Outbound Consumers)** untuk menjamin tidak ada efek samping regresi.

---

## 4. Penguatan Arsitektur Database (`database-schema-designer`)

Skill `database-schema-designer` di enterprise mengimplementasikan standar data tingkat tinggi yang wajib kita asimilasikan ke FORGE:

### A. Tiga Lapisan Standar Desain Skema
1. **Multi-Tenancy via Row-Level Security (RLS) di Level Database:**
   * AI amatir membatasi data organisasi via query aplikasi: `SELECT * FROM tasks WHERE org_id = 1`. *(Bahaya: jika developer lupa menulis `WHERE org_id`, data lintas perusahaan bocor!)*
   * Standar Enterprise: Database PostgreSQL mengunci isolasi di level kernel DB:
     ```sql
     ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;
     CREATE POLICY tasks_org_isolation ON tasks
       FOR ALL TO app_user
       USING (organization_id = current_setting('app.current_org_id')::uuid);
     ```
2. **Strategi Indeks Komposit & Partial Index:**
   * **Leftmost Prefix Rule:** Jika query sering mencari `WHERE status = 'active' AND created_at > '2026-01-01'`, urutan kolom di indeks komposit **sangat menentukan**: `CREATE INDEX idx_status_created ON tasks(status, created_at)`.
   * **Partial Index (Hemat RAM):** Jika tabel memiliki soft-delete (`deleted_at`), jangan mengindeks seluruh tabel! Buat partial index:
     ```sql
     CREATE INDEX idx_active_tasks ON tasks(project_id) WHERE deleted_at IS NULL;
     ```
     *Dampak:* Ukuran indeks di RAM 80% lebih kecil, query 5x lebih cepat.
3. **Pola Migrasi Tanpa Downtime (Expand & Contract Pattern):**
   * Jika ingin mengubah kolom `name` menjadi `first_name` dan `last_name` pada tabel dengan 10 juta baris:
     * *Langkah 1 (Expand):* Tambahkan kolom `first_name` dan `last_name` (nullable), biarkan kolom `name` tetap ada.
     * *Langkah 2 (Dual Write):* Backend menulis ke kedua kolom secara bersamaan.
     * *Langkah 3 (Backfill):* Script background menyalin data lama ke kolom baru secara bertahap (batch per 1.000 baris agar tidak lock tabel).
     * *Langkah 4 (Contract):* Hapus kolom `name` lama setelah seluruh traffic stabil.

---

## 5. Blueprint Asimilasi: Bagaimana Kita Memasukkan Metode Ini ke FORGE?

Kita tidak perlu mengubah struktur Two-Gateway FORGE yang sudah hebat. Yang kita lakukan adalah **mengganti "Tangan Kosong" AI dengan "Perkakas Skrip & Protokol Nyata"**:

```
[ FORGE GATEWAY ]       [ INJEKSI PERKAKAS ENTERPRISE ]
/edeate (Hulu)    ──►   Inject: Context-First auto-check (Pattern 1)
/plan (Hilir)     ──►   Inject: database-schema-designer (RLS + Partial Index Checklist)
/execute (Hilir)  ──►   Inject: Proactive Triggers di Header (Unmounted guard, sticky bounds)
/audit (Hilir)    ──►   Inject: api_linter.py + breaking_change_detector.py + api_scorecard.py
/debug (Regresi)  ──►   Inject: The Iron Law of Diagnosis (SCOPE -> TRACE -> DIAGNOSE dari focused-fix)
```

Dengan mengawinkan **Disiplin Alur Kerja FORGE** dengan **Metode Deterministik Enterprise**, kita menghasilkan sistem AI rekayasa software yang tercepat, terhemat token, dan mustahil menghasilkan kode halusinasi!

---
*Dokumen ini merupakan analisis mendalam implementasi teknis untuk penyempurnaan Fase 3.*
