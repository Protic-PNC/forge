# PANDUAN REFERENSI: FORMAT TIKET LEVEL 3 & TIGA VARIAN MATRIKS
**Direktori Rujukan On-Demand untuk Fase 6 (`/edeate`)**

---

## 📋 Anatomi Standar Tiket Level 3 Sempurna

Setelah otorisasi ACC diberikan di Fase 5, AI mencetak **TEPAT SATU (1) TIKET LEVEL 3 SEMPURNA** menggunakan format standar Enterprise berikut:

````markdown
```yaml
---
name: "[TIPE_TIKET]: [Nama Tiket yang Jelas]"
about: "Spesifikasi tugas teknis arsitektur Enterprise"
title: "[TIPE_TIKET]: [Nama Tiket yang Jelas]"
milestone: "Epik [X]: [Nama Epik]"
labels: ["[kompleksitas: s/m/l/xl]", "[domain/layer]"]
assignees: ""
---

### 1. Identitas Tiket & Panduan Branch
* **Target GitHub Issue:** `#<nomor-issue>` *(Wajib diisi setelah issue dibuat)*
* **Pola Branch Resmi:** `<prefix>/issue-<nomor>-<nama-fitur>` *(Contoh: feature/issue-12-auth-guard)*
* **Milestone / Induk Epik:** Epik [X] ([Nama Epik]) ➔ Sub-poin: `[Nama Sub-poin]`
* **Domain / Modul:** [Nama modul, Controller/Service/Model utama yang menjadi pusat masalah]
* **Kondisi Eksisting (Hasil Pre-Flight Audit):** 
  - [Temuan fisik 1 dari repositori nyata: misal Fat Controller / Query N+1 / Celah kebocoran raw error]
  - [Temuan fisik 2: misal Ketiadaan validasi FormRequest / Kurang Index / Beban agregasi belum di-cache]
* **Hasil yang Diharapkan:** 
  - [Transformasi arsitektur yang diinginkan secara konkret dan terukur]

---

### 2. Matriks Spesifikasi Domain (Pilih Varian yang Sesuai Jenis Tiket)

<!-- VARIAN A: KHUSUS TIKET BACKEND / DATA MUTATION -->
*Definisikan siapa yang berhak mengeksekusi setiap aksi untuk memandu pembuatan Policy / Access Control:*

| Aksi / Endpoint | Role Utama (Admin) | Hak Akses Kontekstual (Owner/Member) | Tamu / Publik |
| :--- | :--- | :--- | :--- |
| **View / Index** | Boleh | Semua user terautentikasi | Boleh (Public) / Ditolak (401/403) |
| **Create / Store** | Boleh | Khusus role terotorisasi (atau dilarang) | Ditolak (401/403) |
| **Update / Edit** | Boleh | Khusus pemilik data (Owner) | Ditolak (401/403) |
| **Delete / Destroy**| Boleh | Dilarang (Hanya Admin) | Ditolak (401/403) |

<!-- VARIAN B: KHUSUS TIKET FRONTEND UI / KOMPONEN -->
*Definisikan status interaktivitas, mode render/hidrasi, dan aksesibilitas antarmuka:*

| Komponen / Halaman | Mode Hidrasi (`client:*` / Static) | Status UI (Empty / Loading / Error / Data) | Aksesibilitas & Responsivitas (A11y) |
| :--- | :--- | :--- | :--- |
| `[Nama Komponen]` | [Static HTML / visible / idle / load] | [Tampilan saat data kosong atau fetching] | [Keyboard focus, ARIA, Mobile viewport] |

<!-- VARIAN C: KHUSUS TIKET TRACK B (FONDASI / TOOLCHAIN / RUNTIME / REFACTOR) -->
*Definisikan target performa objektif dan batasan integrasi toolchain:*

| Dimensi Rekayasa | Target Metrik Objektif | Batasan Kompatibilitas | Perintah Verifikasi Otomatis |
| :--- | :--- | :--- | :--- |
| **Performa / Bundle** | [Lighthouse > 95 / Zero JS leak] | [Komponen UI eksisting tidak regresi] | `npm run build` / CI check |
| **Toolchain & Runtime** | [Config tervalidasi / Type-safe] | [Versi package & plugin harmonis] | `npx astro check` / `npm test` |

---

### 3. Batasan Bisnis & Integritas Data (Business Invariants)
*Aturan ketat yang melindungi sistem dari korupsi data atau manipulasi:*
* **Anti-Spoofing (Server Injection):** [Atribut yang DILARANG diambil dari form input client dan WAJIB dari server, misal: `auth.user.id` untuk `creator_id`].
* **Immutability (Kolom Kekal):** [Atribut yang DILARANG diubah saat operasi UPDATE, misal: `user_id`, `created_at`, atau relasi induk].
* **Konkurensi & Anti-Race Condition:** [Apakah butuh `Cache::lock` / Database Transaction / UUID unik sementara untuk aksi tulis massal?].
* **Sanitasi Data Sensitif (OWASP):** [Daftar field yang WAJIB disaring/dibuang sebelum data dikirim ke client JSON, misal: `password`, `token`].

---

### 4. Peta Berkas Terdampak (Blast Radius)
*Pemisahan tegas antara berkas yang dimodifikasi vs berkas baru untuk memitigasi risiko regresi:*
* **Berkas Eksisting yang Dimodifikasi (Waspada Regresi):**
  - Routes / Handlers: `...`
  - Model / Entitas: `...`
  - Automated Tests Eksisting: `...`
* **Berkas Baru yang Dibuat:**
  - Services / Actions: `...`
  - Request / Schema / Policy: `...`
  - Automated Tests Baru: `...`

---

### 5. Spesifikasi Teknis Defensif & Langkah Implementasi
*(Instruksi teknis bernomor yang disesuaikan dengan varian tiket)*

<!-- VARIAN A: JIKA TIKET BACKEND / DATA MUTATION -->
- [ ] 1. **Policy / Guard:** Buat aturan otorisasi sesuai Matriks Otorisasi di Bagian 2.
- [ ] 2. **Request Validation:** Buat schema/FormRequest validasi input. Pastikan field anti-spoofing tidak diambil dari payload client.
- [ ] 3. **Service Layer:** Ekstraksi logika bisnis ke Service terisolasi dengan transaksi atomik dan proteksi konkurensi jika ada mutasi kritis.
- [ ] 4. **Controller / Handler Ramping:** Bersihkan controller dari validasi inline dan logika tebal; delegasikan ke Service.
- [ ] 5. **Resource Serialization:** Transformasikan entitas ke DTO/Resource JSON dengan sanitasi field sensitif.

<!-- VARIAN B: JIKA TIKET FRONTEND UI / KOMPONEN -->
- [ ] 1. **Komposisi Markup & Layout:** Susun hirarki markup semantik dan integrasikan Tailwind CSS.
- [ ] 2. **Boundary Interaktivitas & Hydration:** Isolasi komponen interaktif dengan direktif islands yang tepat (`client:visible` dsb) dan pastikan zero unnecessary client JS.
- [ ] 3. **Handling Empty & Error State:** Terapkan fallback visual anggun saat data kosong (*empty state*) atau fetch gagal.
- [ ] 4. **A11y & Kontrak Responsif:** Pastikan navigasi keyboard, kontras warna, dan tap-target mobile memenuhi standar.

<!-- VARIAN C: JIKA TIKET TRACK B (FONDASI / TOOLCHAIN / REFACTOR) -->
- [ ] 1. **Modifikasi Berkas Konfigurasi:** Update konfigurasi toolchain (misal: `astro.config.mjs`, `tailwind.config.ts`, `tsconfig.json`).
- [ ] 2. **Integrasi Paket Dependensi:** Pasang dan konfigurasi integrasi resmi (misal: `@astrojs/react`, plugin Tailwind).
- [ ] 3. **Audit Regresi Komponen Eksisting:** Uji render komponen eksisting untuk menjamin kompatibilitas runtime.
- [ ] 4. **Verifikasi Kinerja Otomatis:** Eksekusi build, linter, dan cek skor NFR sesuai kriteria DoD.

---

### 6. Jaring Pengaman Uji & Kriteria Kelayakan (Definition of Done)
- [ ] **Linter & Standar Gaya:** Lolos 100% format linter proyek tanpa peringatan.
- [ ] **Regresi Automated Test Eksisting:** Seluruh suite pengujian otomatis lama tetap HIJAU (Pass).
- [ ] **Automated Test Baru:** Mencakup skenario otorisasi lolos, otorisasi ditolak (403), validasi gagal (422), dan eksekusi sukses.
- [ ] **Keamanan & Integritas:** Bebas spoofing identitas, bebas kebocoran kredensial sensitif, dan bebas kueri N+1.
- [ ] **Kriteria Penolakan PR (Hard Rejection Triggers):**
  - PR ditolak jika tidak ada automated test yang memvalidasi business invariants.
  - PR ditolak jika mengubah berkas di luar daftar Blast Radius tanpa izin Tech Lead.

---

### 7. Poin Kunci Pemahaman Teknis (Technical Talking Points)
*Narasi alasan rekayasa (The "Why") yang dapat dibacakan mahasiswa saat presentasi atau evaluasi:*
* **Mengapa Arsitektur Ini Dipilih?** [Edukasi prinsip Separation of Concerns / Single Responsibility di balik tiket ini].
* **Bahaya Laten yang Dicegah:** [Penjelasan risiko fatal seperti Information Disclosure atau Race Condition jika dikerjakan serampangan].
* **Dampak Performa / Skalabilitas:** [Penjelasan optimasi query, efisiensi memori, atau peran cache].
```
````

---

## 🛑 PROTOKOL PENYERAHAN TIKET, OTOMASI ISSUE, & CENTANG ROADMAP

Setelah mencetak Tiket Level 3 di atas, AI **DIHARAMKAN KERAS** menawarkan untuk membuat skema database, menulis kode implementasi, atau membuat Pull Request otomatis di dalam sesi `/edeate`!

AI **WAJIB** mengeksekusi 3 langkah penutupan gerbang ini secara berurutan:

1. **Penawaran Otomasi GitHub Issue via MCP:**
   AI menawarkan bantuan pembuatan tiket resmi:
   > *"Draf Tiket Level 3 resmi disahkan. Apakah Anda ingin saya membuatkan Issue resminya ke GitHub menggunakan tool MCP GitHub (`create_issue`) dengan Milestone **'Epik [X]'** sekarang agar Anda tidak perlu copy-paste manual?"*

2. **Refleks Penautan Nomor Issue di `DEVELOPMENT_ROADMAP.md` (Physical Roadmap Linking - Tanpa Centang Selesai):**
   Begitu nomor Issue GitHub resmi didapatkan (baik dibuatkan langsung via MCP GitHub maupun disalin manual oleh developer dengan nomor misal `#12`), AI **WAJIB MEMPERBARUI `DEVELOPMENT_ROADMAP.md` di root proyek**:
   - Cari sub-poin yang bersesuaian di dalam Epik [X].
   - Pertahankan kotak centang TETAP KOSONG (`- [ ]`) karena kode implementasi belum ditulis, dan sematkan tautan nomor tiket:
     Ubah dari:
     `- [ ] [Nama Sub-Poin Fitur]`
     menjadi:
     `- [ ] [Nama Sub-Poin Fitur] (Issue #[Nomor])`
   - ⚠️ **HUKUM INTEGRITAS GERBANG (Anti-Premature Completion):** AI **DILARANG KERAS** mengubah kotak centang menjadi `[x]`. Kotak centang `[x]` adalah **HAK PREROGATIF MUTLAK sesi `/audit` di Hilir** setelah kode selesai diimplementasikan, diuji melalui Four-Tier Gate, dan diverifikasi sebelum PR. Memberi centang `[x]` di Hulu adalah cacat semantik fatal (*False Sense of Completion*).
   - ⚠️ **HUKUM ISOLASI GIT (Git-Free Zone):** AI **DILARANG** melakukan `git add`, `git commit`, atau manipulasi git apa pun di sesi `/edeate` agar tidak mencemari branch fitur aktif (*Branch Contamination*).

3. **Mandat Pemindahan Gerbang (Handover to Gateway 2):**
   AI menutup sesi dengan arahan tegas untuk berpindah ke gerbang hilir:
   > *"Tiket GitHub Issue #[Nomor] resmi terbit dan ditautkan ke `DEVELOPMENT_ROADMAP.md` (status: `- [ ] (Issue #[Nomor])`). Pengerjaan kode implementasi DILARANG dilakukan di sesi `/edeate` ini. Silakan buka branch baru dan panggil Gateway 2: `/grill-me #[Nomor]` untuk memulai perancangan arsitektur eksekusi!"*
