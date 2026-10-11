# SOP IDEASI & PENEMUAN TIKET (`/edeate`)
# DOMAIN: {{PROJECT_NAME}}

> **Dokumen ini adalah hukum domain Hulu (Ideasi).**
> Ia berpasangan dengan `MASTER_RULES.md` (domain Hilir/Implementasi) dan `GIT_WORKFLOW.md` (domain Version Control). Ketiganya membentuk **Two-Gateway Pipeline** lengkap dari ide mentah hingga kode produksi.

---

## 🗺️ GAMBARAN BESAR: TWO-GATEWAY PIPELINE

```
IDE MENTAH
    │
    ▼
┌──────────────────────────────────────┐
│  GATEWAY 1 — HULU (Dokumen Ini)      │
│  Slash Command: /edeate              │
│                                      │
│  0. Pre-Flight Audit (Codebase)      │
│  1. Pilar Bisnis                     │
│  2. Pilar Integrasi                  │
│  3. Pilar Keamanan & Concurrency     │
│  4. Draft Tiket Level 3              │
│  5. Verifikasi & Pengesahan          │
└──────────────────┬───────────────────┘
                   │   GitHub Issue dibuat (dapat nomor Issue)
                   ▼
┌──────────────────────────────────────┐
│  GATEWAY 2 — HILIR (MASTER_RULES)    │
│  /grill-me → /plan → /tdd →          │
│  /execute → /audit → PR              │
└──────────────────────────────────────┘
                   │
                   ▼
            KODE PRODUKSI
```

> **Aturan Fundamental:** Sebuah ide **DILARANG** masuk ke Gateway 2 sebelum lulus Gateway 1.
> Ini mencegah "tiket mentah Level 1" yang memaksa developer menebak-nebak konteks di tengah eksekusi.

---

## 🚦 SLASH COMMAND: `/edeate`

**Definisi:** `/edeate` (singkatan dari **Ideate**) adalah perintah yang memulai sesi penemuan dan pembentukan ide secara terstruktur sebelum sebuah tiket ditulis.

**Kapan Digunakan:**
- Developer atau Tech Lead punya gambaran kasar tentang sebuah fitur/perbaikan.
- Ide belum cukup konkret untuk ditulis sebagai GitHub Issue yang bisa langsung dikerjakan.
- Perlu konfirmasi apakah ide tersebut *feasible* secara arsitektur dan tidak memiliki risiko tersembunyi.

**Kapan TIDAK Digunakan:**
- Tiket sudah ada di GitHub dan nomor Issue sudah ditetapkan → langsung `/grill-me #<nomor>`.
- Hanya ada pertanyaan teknis singkat tanpa pembentukan fitur baru.

---

## 📐 TINGKAT KEMATANGAN TIKET (Ticket Maturity Levels)

Sebelum menjalankan `/edeate`, AI dan developer harus memahami target kematangan yang ingin dicapai:

| Level | Nama | Karakteristik | Boleh ke Gateway 2? |
|-------|------|---------------|---------------------|
| **1** | **Mentah (Idea Dump)** | "Bikin sync CSV untuk event committee." Tidak ada konteks, tidak ada DoD. | ❌ TOLAK |
| **2** | **Setengah Matang (Story)** | Ada use case dan kriteria penerimaan umum, tapi DoD masih ambigu ("berhasil sync"). | ⚠️ Revisi dulu |
| **3** | **Matang — Sweet Spot** | Ada **invariant** yang terukur, DoD berbasis uji (testable), dan kontrak API terdefinisi. | ✅ IZINKAN |

> **Target `/edeate`:** Selalu menghasilkan tiket **Level 3**.

---

## 🔬 PROTOKOL `/edeate` — ALUR IDE DARI HULU KE TIKET

> 🚨 **PROTOKOL ITERASI & INTEGRITAS GERBANG WAJIB:** 
> - **Satu Fase Per Respons:** AI **DILARANG KERAS** memborong seluruh Fase atau semua pertanyaan sekaligus dalam satu respons. AI **WAJIB** membahas HANYA 1 Fase per giliran dan berhenti menunggu jawaban Tech Lead.
> - **Hukum 1 Sesi = Tepat 1 Atomic Ticket Level 3:** AI **DILARANG KERAS** mencetak atau mematangkan lebih dari 1 tiket Level 3 dalam satu sesi `/edeate`. Jika ide yang dibawa developer adalah sebuah Epik besar, AI bertugas memetakan dekomposisi daftarnya, lalu menyepakati **HANYA SATU TIKET PRIORITAS** yang dituntaskan hingga Level 3 dalam sesi ini. Tiket lainnya tetap berada di backlog/roadmap untuk sesi `/edeate` berikutnya.
> - **Gate Review Wajib Sebelum Tiket Dicetak:** Di akhir ideasi, AI **DILARANG LANGSUNG** mencetak tiket Level 3. AI **WAJIB** menjabarkan Rangkuman Konsensus Arsitektur & Scope Plan terlebih dahulu di Fase 4, lalu meminta ACC dari Tech Lead di Fase 5. Tiket Level 3 HANYA boleh dicetak setelah mendapatkan ACC resmi.
> - **Larangan Mutlak Eksekusi Kode di Hulu (Gateway 1 is Code-Free):** AI **DIHARAMKAN KERAS** menulis kode produksi, membuat file skema/migrasi, atau menawarkan pembuatan Pull Request otomatis di dalam sesi `/edeate`. Output `/edeate` murni berupa spesifikasi tiket GitHub Issue. Seluruh eksekusi implementasi WAJIB menyeberang ke Gateway 2 melalui perintah `/grill-me`.

### FASE 0 — Penerimaan & Klasifikasi Awal (AI)

Ketika developer mengetik `/edeate [deskripsi ide]`, AI **WAJIB** melakukan hal berikut **sebelum** mengajukan pertanyaan apa pun:

**Langkah 0.1 — Klasifikasi Tiket Otomatis:**
AI mengidentifikasi tipe tiket berdasarkan kata kunci ide:
- *"sync", "CSV", "import", "sinkronisasi"* → Tipe: **[FEAT] External I/O**
- *"bug", "error", "gagal", "salah"* → Tipe: **[FIX]**
- *"refactor", "standarisasi", "pisah", "bersihkan"* → Tipe: **[REFACTOR]**
- *"test", "coverage", "uji"* → Tipe: **[TEST]**

**Langkah 0.2 — Pre-Flight Codebase Audit (WAJIB, Sebelum Giliran Pertanyaan):**
AI **WAJIB** memanggil tool `grep_search` atau `view_file` ke modul yang relevan terlebih dahulu. Tujuannya adalah memastikan AI berbicara dari fakta repositori, bukan asumsi.

Pola audit berdasarkan tipe tiket:
- **External I/O / Sync:** Baca controller saudara yang sudah punya `sync` (misal `UserController`, `AgendaController`) untuk memetakan pola `Cache::lock` + `DB::transaction` yang berlaku.
- **Fitur Baru pada Entitas Existing:** Baca model terkait + migration terakhir untuk memahami skema data saat ini.
- **Otorisasi / Policy:** Baca `routes/api.php` dan `Policy` yang relevan.
- **Pengujian:** Baca `tests/Feature/` terkait untuk menghindari duplikasi skenario.

**Output Langkah 0.2 — Blok Bukti Fisik Audit Wajib:**

```markdown
### 🔍 Konteks Repositori Aktual (Pre-Flight Audit)
- **Modul Referensi:** [`app/Http/Controllers/XyzController.php`](file:///...) (baris A–B):
  Pola `Cache::lock` + `upsert()` sudah ada. Fitur baru harus mengikuti pola ini.
- **Kontrak Data Existing:** Tabel `xyz_table` memiliki kolom `[...]`.
  Kolom baru apa pun harus dibuatkan migrasinya.
- **Celah yang Terdeteksi:** [Ada/Tidak ada] potensi konflik atau duplikasi dengan kode existing.
```

---

### FASE 1 — PILAR BISNIS (The Business Grill)

> *Tujuan: Memahami "MENGAPA" fitur ini ada dan "SIAPA" yang terdampak.*

AI mengajukan pertanyaan berikut, **satu per giliran**, menunggu jawaban sebelum lanjut:

**1. Pemantik Konteks:**
> *"Apa kejadian spesifik yang membuatmu menyadari fitur ini perlu ada? (misal: ada data yang salah, ada proses manual yang melelahkan, ada laporan yang tidak akurat)"*

**2. Identifikasi Aktor:**
> *"Siapa yang akan menjalankan fitur ini? (Admin, Tech Lead, Anggota Biasa, Sistem Otomatis?) Dan dari 'pintu' mana mereka masuk? (Dashboard, API, Cron Job?)"*

**3. Definisi Sukses yang Terukur:**
> *"Bagaimana kamu tahu fitur ini 'berhasil'? Bukan dalam arti 'tidak error', tapi dalam arti bisnis. Misal: 'Data 50 anggota committee ter-sync dalam 5 detik' atau 'Laporan keuangan menampilkan angka yang sama dengan Google Sheet.'"*

**4. Kasus Tepi Bisnis:**
> *"Apa yang seharusnya terjadi kalau: (a) file CSV-nya kosong? (b) ada data duplikat di CSV? (c) koneksi terputus di tengah proses?"*

---

### FASE 2 — PILAR INTEGRASI (The Integration Grill)

> *Tujuan: Memetakan "APA" yang akan berubah di sistem dan dampaknya ke modul lain.*

**5. Pemetaan Entitas & Relasi:**
> *"Entitas (tabel database) apa saja yang terlibat? Apakah ada relasi pivot (many-to-many) yang perlu diubah? Misal: apakah `event_committees` perlu kolom baru, atau hanya mengisi data yang sudah ada?"*

**6. Kontrak API:**
> *"Endpoint HTTP apa yang akan menjadi pintu masuk? Apakah ada endpoint existing yang harus dimodifikasi, atau kita butuh endpoint baru sama sekali? Format request-nya seperti apa? (multipart/form-data untuk upload file, JSON untuk data biasa)"*

**7. Dampak ke Modul Lain:**
> *"Setelah fitur ini berjalan, modul lain mana yang bisa terdampak? Misalnya: apakah sync committee ini akan mempengaruhi perhitungan iuran bulanan, laporan kehadiran, atau sistem otorisasi BPH?"*

---

### FASE 3 — PILAR KEAMANAN & CONCURRENCY (The Security Grill)

> *Tujuan: Mendeteksi risiko tersembunyi yang tidak terlihat dari permukaan ide.*

**8. Otorisasi:**
> *"Siapa saja yang TIDAK BOLEH mengakses atau menjalankan fitur ini? Apakah hanya Admin/Tech Lead? Apakah ada kondisi di mana anggota biasa bisa memicu ini secara tidak sengaja?"*

**9. Proteksi Konkurensi:**
> *"Bisakah dua orang Admin menjalankan fitur ini pada saat yang bersamaan? Kalau iya, apa yang terjadi pada data? Apakah kita butuh mekanisme pengunci (locking)?"*

**10. Invariant — Pertanyaan Kunci Level 3:**
> *"Properti data apa yang harus SELALU BENAR, bahkan kalau terjadi error di tengah proses? Misal: 'Tidak boleh ada committee yang terdaftar dua kali di event yang sama' atau 'Jika sync gagal di baris ke-30, data 1-29 harus di-rollback.'"*

---

### FASE 4 — RANGKUMAN KONSENSUS ARSITEKTUR & SCOPE PLAN (The Scope Pitch)

Setelah Pilar 1, 2, dan 3 tuntas dijawab, AI **DILARANG KERAS LANGSUNG MENCETAK TIKET FINAL**.
AI **WAJIB** terlebih dahulu menyajikan **Rangkuman Konsensus Arsitektur & Rencana Pemecahan Tiket** untuk disetujui Tech Lead:

```markdown
## 📋 RANGKUMAN KONSENSUS ARSITEKTUR & TICKET PLAN

### 1. Konsensus Keputusan Arsitektur
* **Masalah Bisnis Nyata:** [Rangkuman mengapa fitur ini ada dan siapa aktor utamanya]
* **Fakta Repositori Aktual:** [Kutipan temuan Pre-Flight Audit dari Fase 0]
* **Strategi Arsitektur:** [Pola arsitektur, pemisahan layer Controller-Service-Request, dan mitigasi risiko]

### 2. Rencana Dekomposisi & Pemilihan Tiket
* **Status Ide:** [Atomic Feature / Bagian dari Epik Besar]
* **Daftar Pemecahan Tiket (Jika Epik):**
  - [ ] Tiket 1: [Nama Tiket 1]
  - [ ] Tiket 2: [Nama Tiket 2]
  - [ ] Tiket 3: [Nama Tiket 3]
* **Tiket yang Difokuskan pada Sesi Ini:** ⭐ **[Nama Tiket yang Dipilih]** (Hanya 1 tiket yang dimatangkan hingga Level 3!)

### 3. Batasan Cakupan (Scope Boundaries)
* **✅ Scope IN:** [Daftar berkas dan modul spesifik yang akan disentuh]
* **❌ Scope OUT:** [Hal-hal yang secara sadar ditunda ke tiket berikutnya agar tidak terjadi scope creep]

### 4. Rencana Invariant & Keamanan Data
* [Daftar kondisi absolut yang wajib dipertahankan]
```

---

### FASE 5 — REVIEW GATE, EVALUASI, & ACC TECH LEAD (Interactive Alignment Gate)

Setelah menyajikan Rangkuman & Plan di Fase 4, AI **WAJIB BERHENTI** dan mengajukan pertanyaan persetujuan:

> *"Rangkuman Konsensus Arsitektur dan Scope Plan tiket di atas siap dievaluasi. Apakah rencana arsitektur dan batasan ruang lingkup ini sudah disetujui untuk kita rumuskan menjadi 1 Tiket Level 3 Sempurna? Jika ada evaluasi, koreksi, atau pertanyaan arsitektural, silakan sampaikan. Kita akan selesaikan diskusi ini sebelum tiket Level 3 difinalisasi."*

> 🛑 **HARD STOP MACRO:**
> AI **DILARANG KERAS** mencetak Tiket Level 3 sebelum Tech Lead memberikan persetujuan eksplisit.
> - Jika Tech Lead mengajukan revisi, evaluasi, atau pertanyaan: AI **WAJIB** merespons, merevisi plan, dan mengonfirmasi ulang.
> - HANYA setelah Tech Lead menyatakan **"ACC"**, **"Setuju"**, atau **"Lanjut"**, AI diizinkan melanjutkan ke Fase 6.

---

### FASE 6 — SINTESIS 1 TIKET LEVEL 3 SEMPURNA & HANDOVER GATEWAY 2

Setelah otorisasi ACC diberikan di Fase 5, AI mencetak **TEPAT SATU (1) TIKET LEVEL 3 SEMPURNA** menggunakan format standar Enterprise berikut:

````markdown
```yaml
---
name: "[TIPE_TIKET]: [Nama Tiket yang Jelas]"
about: "Spesifikasi tugas teknis arsitektur Enterprise"
title: "[TIPE_TIKET]: [Nama Tiket yang Jelas]"
labels: ["[kompleksitas: s/m/l/xl]", "[domain/layer]"]
assignees: ""
---

### 1. Konteks & Masalah Teknis
* **Domain / Modul:** [Nama modul, Controller/Service/Model utama yang menjadi pusat masalah]
* **Kondisi Eksisting (Hasil Pre-Flight Audit):** 
  - [Temuan fisik 1 dari repositori nyata: misal Fat Controller / Query N+1 / Celah kebocoran raw error]
  - [Temuan fisik 2: misal Ketiadaan validasi FormRequest / Kurang Index / Beban agregasi belum di-cache]
* **Hasil yang Diharapkan:** 
  - [Transformasi arsitektur yang diinginkan secara konkret dan terukur]

---

### 2. Peta Berkas Terdampak (Blast Radius)
* **Entry Points (Controllers / Handlers / Routes):**
  - `path/to/FileController.ext`
* **Core Logic (Services / Actions / Repositories):**
  - `path/to/FileService.ext` *(BARU / OPTIMASI)*
* **Data Contracts (Requests / DTO / Schemas / Migrations):**
  - `path/to/ValidationOrSchema.ext` *(BARU)*
* **Automated Tests:**
  - `tests/.../FeatureTest.ext`

---

### 3. Spesifikasi Teknis & Langkah Implementasi
- [ ] 1. [Langkah 1: Signature method/fungsi baru, parameter input, dan return type yang konkret]
- [ ] 2. [Langkah 2: Pemindahan logika bisnis dari Controller ke Service & perampingan Controller]
- [ ] 3. [Langkah 3: Pembuatan FormRequest / Schema validasi input dengan aturan ketat]
- [ ] 4. [Langkah 4: Pemasangan mekanisme proteksi: Cache::remember / DB::transaction / Cache::lock]

---

### 4. Kontrak Invariant (Contract & Data Integrity)
> *Properti data yang HARUS SELALU BENAR dalam kondisi apa pun, wajib dibuktikan oleh Automated Test.*
1. `INV-1:` [Kondisi absolut integritas data, misal: Unik, format email kampus terisolasi]
2. `INV-2:` [Kondisi rollback jika proses gagal di tengah jalan]
3. `INV-3:` [Kondisi proteksi otorisasi / access control]

---

### 5. Kriteria Kelayakan (Definition of Done)
- [ ] **Linter & Standar Gaya:** Lolos 100% format linter proyek (`./vendor/bin/pint` atau `npm run lint`) tanpa peringatan.
- [ ] **Automated Test:** Jalankan perintah test spesifik `[Perintah test --filter=...]` dan wajib 100% Pass.
- [ ] **Keamanan Error:** Response tidak pernah mengekspos nomor baris kode internal atau trace database.
- [ ] **Batas Kompleksitas Kode:** [Misal: Controller berkurang menjadi <= 30 baris, tanpa query di dalam loop].

---

### 6. Kriteria Penolakan PR (Rejection Criteria)
- PR ditolak jika: Tidak ada automated test yang membuktikan semua INVARIANT di atas.
- PR ditolak jika: Mengubah berkas di luar daftar **Peta Berkas Terdampak (Blast Radius)** tanpa izin Tech Lead.
- PR ditolak jika: Ada N+1 query atau tidak ada transaksi atomik pada mutasi sensitif.

---

### 7. Poin Kunci Pemahaman Teknis (Technical Talking Points)
* **Mengapa Arsitektur Ini Dipilih?** [Edukasi prinsip Separation of Concerns / Single Responsibility di balik tiket ini].
* **Bahaya Laten yang Dicegah:** [Penjelasan risiko fatal seperti Information Disclosure atau Race Condition jika dikerjakan serampangan].
* **Dampak Performa / Skalabilitas:** [Penjelasan optimasi query, efisiensi memori, atau peran cache].
```
````

#### 🛑 LARANGAN MUTLAK EKSEKUSI DI HULU (Anti-Bypass Gateway 2):
Setelah mencetak Tiket Level 3 di atas, AI **DIHARAMKAN KERAS** menawarkan untuk membuat skema, menulis kode, atau membuat Pull Request otomatis!
AI **WAJIB** menutup sesi dengan kalimat mandat pemindahan gerbang:

> *"Tiket Level 3 resmi disahkan. Silakan salin tiket di atas ke GitHub Issue proyek untuk mendapatkan nomor Issue resmi (misal: `#12`). Setelah itu, buat branch baru dan panggil Gateway 2: `/grill-me #<nomor>` untuk memulai perancangan arsitektur eksekusi."*

---

## ⚠️ PENJAGA KUALITAS (Anti-Pattern yang Harus Ditolak AI)

| Anti-Pattern | Dampak | Tindakan Wajib AI |
|---|---|---|
| **Multi-Ticket Dumping** (Mencetak lebih dari 1 tiket Level 3 dalam 1 sesi) | Fokus buyar, *blast radius* membengkak, pengujian bias dan campur aduk | AI WAJIB membatasi hanya 1 tiket Level 3 yang difinalisasi per sesi. Sisanya dicatat di roadmap backlog. |
| **Premature Ticket Synthesis** (Langsung mencetak tiket tanpa ACC plan) | Resiko rework besar jika asumsi dasar arsitektur atau boundary salah | AI WAJIB menyajikan rangkuman & scope plan di Fase 4 dan menunggu ACC Tech Lead di Fase 5. |
| **Hulu Code Execution / Auto-PR Offer** (Menawarkan eksekusi kode/PR di `/edeate`) | Melanggar batas gerbang, membypass TDD, Plan, dan Code Audit Hilir | AI DIHARAMKAN menulis kode atau menawarkan PR di Hulu. AI WAJIB menyerahkan tiket ke Gateway 2 via `/grill-me`. |
| **Tiket Terlalu Luas** ("Bikin fitur manajemen event lengkap") | Scope tak terbatas, sprint berantakan | AI WAJIB meminta developer memecah menjadi tiket-tiket kecil yang independen |
| **DoD Ambigu** ("Berhasil dijalankan") | Developer dan reviewer punya definisi sukses yang berbeda | AI WAJIB mendesak definisi yang terukur (angka, waktu, kondisi boolean, perintah test) |
| **Tiket Tanpa Blast Radius** | Developer/AI mengedit file liar di luar cakupan tugas | AI WAJIB memetakan daftar berkas entry point, service, schema, dan test |
| **Tiket Tanpa Invariant** | Tidak ada kontrak yang bisa diuji → Feature Test menjadi formalitas dangkal | AI WAJIB menggali minimal 2-3 invariant sebelum draft disahkan |
| **Asumsi Tanpa Audit Kode** | AI berbicara dari imajinasi, bukan realita repositori | AI WAJIB menjalankan Pre-Flight Audit (Fase 0) sebelum sesi dimulai |
| **Langsung Lompat ke Solusi** | Masalah bisnis inti tidak dipahami | AI WAJIB menyelesaikan Pilar Bisnis (Fase 1) terlebih dahulu |

