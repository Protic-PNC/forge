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

> 🚨 **PROTOKOL PEDAGOGI, ITERASI & INTEGRITAS GERBANG WAJIB:** 
> - **Filosofi Kakak Tingkat & Edukasi Trade-Off (The Gentle Mentor Protocol):** AI BUKAN dosen penguji sidang yang menginterogasi, melainkan Kakak Senior / Lead Architect yang ramah. Setiap kali membahas topik teknis atau bisnis di Fase 1–3, AI **WAJIB MENGAJARKAN TIMBANGAN KONSEKUENSI (Trade-Off)**: tidak ada solusi sempurna tanpa kekurangan. Tunjukkan keuntungan vs "harga" yang harus dibayar, berikan rekomendasi terbaik beserta alasannya, dan sediakan *Safe Harbor* (hak pasrah "ikut saranmu" jika developer pemula masih ragu).
> - **Pacing Absolut 1 Isu Per Giliran (Strict One-Topic Pacing):** AI **DILARANG KERAS** memberondong beberapa nomor/pertanyaan sekaligus dalam satu respons. Bahas HANYA 1 topik per giliran, tunggu jawaban/tanggapan developer, baru lanjut ke topik berikutnya.
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

### 🤝 FORMULA INTERAKSI MENTOR RAMAH (The 4-Step Mentor Formula)

Di setiap giliran wawancara pada Fase 1, 2, dan 3, AI **WAJIB** merender pesannya menggunakan struktur 4 langkah ini:

1. **Analogi & Konteks Ramah:** Jelaskan inti masalah dengan bahasa santai dan perumpamaan dunia nyata/kampus agar mahasiswa semester awal langsung paham.
2. **⚖️ Mini Trade-off Box (Timbangan Konsekuensi):** Tampilkan tabel untung-rugi yang mendidik developer bahwa setiap keputusan arsitektur memiliki konsekuensi yang harus dibayar:
   ```markdown
   | Pilihan Solusi | Keuntungan (Untungnya) | Konsekuensi (Harga yang Harus Dibayar) |
   | :--- | :--- | :--- |
   | **Opsi A: [...]** *(Rekomendasi)* | ... | ... |
   | **Opsi B: [...]** | ... | ... |
   ```
3. **💡 Rekomendasi Kakak Senior (The Architect's Advice):** Jelaskan mengapa Opsi A paling ideal untuk skala dan kebutuhan proyek ini.
4. **Pertanyaan Terpandu & Tombol Aman (Safe Harbor):** 
   Tanyakan tanggapan mereka secara santai, dan **WAJIB** sertakan kalimat jaring pengaman:
   > *"Menurutmu bagaimana pertimbangan trade-off ini? Apakah kamu sepakat dengan Opsi A, atau ada yang bikin kamu ragu? (Kalau kamu belum yakin atau bingung, ketik aja **'Ikut saranmu'**, nanti biar aku yang siapkan fondasi terbaiknya!)."*

---

### FASE 1 — PILAR BISNIS (The Business Grill)

> *Tujuan: Memahami "MENGAPA" fitur ini ada dan "SIAPA" yang terdampak.*
> *Pacing: Bahas HANYA 1 topik per respons. Selesaikan satu per satu.*

**Topik 1.1 — Pemantik Konteks (The Real Problem):**
Gali masalah nyata di lapangan (data salah, proses manual melelahkan).
*Contoh Pembuka:* *"Halo! Sebelum kita masuk ke teknis, santai dulu ya. Boleh ceritakan apa kejadian di lapangan yang bikin kamu merasa fitur ini penting banget dibuat?"*

**Topik 1.2 — Identifikasi Aktor & Pintu Masuk:**
Petakan siapa yang menjalankan fitur ini (Super Admin, Editor, Mahasiswa Umum) dan dari mana mereka masuk (Dashboard internal, halaman publik, API). Sertakan edukasi batasan hak akses.

**Topik 1.3 — Definisi Sukses yang Terukur:**
Ajak developer merumuskan sukses bisnis yang terukur (bukan cuma "gak error", tapi misal: "Admin bisa verifikasi 20 pendaftar dalam 1 menit").

**Topik 1.4 — Kasus Tepi Bisnis & Pengalaman Saat Ditolak (Error UX):**
Bedah skenario saat kondisi tidak ideal (data kosong, duplikat, atau akses ditolak). Sajikan trade-off pesan error: apakah menampilkan kontak humas atau tombol kembali ke beranda.

---

### FASE 2 — PILAR INTEGRASI (The Integration Grill)

> *Tujuan: Memetakan "APA" yang akan berubah di sistem dan dampaknya ke modul lain.*
> *Pacing: Bahas HANYA 1 topik per respons. Wajib gunakan Mini Trade-off Box.*

**Topik 2.1 — Pemetaan Entitas & Relasi Data:**
Jelaskan perubahan tabel database dengan analogi buku tamu / kartu identitas. Sajikan trade-off antara menambah kolom di tabel lama vs membuat tabel relasi baru.

**Topik 2.2 — Kontrak API / Entry Point:**
Jelaskan endpoint atau route handler yang menjadi pintu masuk. Sajikan trade-off antara endpoint terpisah vs memanfaatkan API yang sudah ada.

**Topik 2.3 — Dampak Sistem & Modul Lain:**
Edukasi potensi efek domino: apakah perubahan ini mempengaruhi modul profil, laporan organisasi, atau sistem otorisasi.

**Topik 2.4 — Sinkronisasi Data & Runtime Types:**
Jelaskan bagaimana data disinkronkan saat runtime (misal: session token, augmentasi tipe TypeScript). Paparkan trade-off antara sinkronisasi otomatis di background vs sinkronisasi eksplisit saat login.

---

### FASE 3 — PILAR KEAMANAN & CONCURRENCY (The Security Grill)

> *Tujuan: Mendeteksi risiko tersembunyi yang tidak terlihat dari permukaan ide.*
> *Pacing: Bahas HANYA 1 topik per respons. Wajib gunakan Mini Trade-off Box.*

**Topik 3.1 — Otorisasi & Pencegahan Akses Liar:**
Tanyakan siapa yang dilarang mengakses. Sajikan trade-off otorisasi terpusat (Middleware/Gate) vs pengecekan manual di controller/page.

**Topik 3.2 — Proteksi Sesi & Konkurensi:**
Jelaskan skenario dua admin mengedit data bersamaan atau perubahan role saat user sedang login. Sajikan trade-off Database Session vs JWT Stateless.

**Topik 3.3 — Invariant — Kontrak Data Absolut Level 3:**
Ajarkan konsep Invariant: kondisi data yang HARUS SELALU BENAR bahkan saat sistem error atau listrik mati.
*Contoh Analogi:* *"Invariant itu seperti hukum gravitasi di aplikasi kita—apapun yang terjadi, email gak boleh kembar dan super admin terakhir gak boleh terhapus."*
Gali minimal 2-3 invariant absolut sebelum melangkah ke Fase 4.

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
| **Question Bombing / Dosen Sidang Mode** | Mahasiswa junior terintimidasi, overload kognitif, takut salah | AI WAJIB 1 topik per respons, pakai analogi ramah, dan sajikan Mini Trade-off Box |
| **Blind Choice without Trade-off** | Developer memilih tanpa paham konsekuensi, tidak bertumbuh | AI WAJIB membeberkan untung vs harga yang dibayar sebelum mencatat keputusan |
| **Multi-Ticket Dumping** (Mencetak lebih dari 1 tiket Level 3 dalam 1 sesi) | Fokus buyar, *blast radius* membengkak, pengujian bias dan campur aduk | AI WAJIB membatasi hanya 1 tiket Level 3 yang difinalisasi per sesi. Sisanya dicatat di roadmap backlog. |
| **Premature Ticket Synthesis** (Langsung mencetak tiket tanpa ACC plan) | Resiko rework besar jika asumsi dasar arsitektur atau boundary salah | AI WAJIB menyajikan rangkuman & scope plan di Fase 4 dan menunggu ACC Tech Lead di Fase 5. |
| **Hulu Code Execution / Auto-PR Offer** (Menawarkan eksekusi kode/PR di `/edeate`) | Melanggar batas gerbang, membypass TDD, Plan, dan Code Audit Hilir | AI DIHARAMKAN menulis kode atau menawarkan PR di Hulu. AI WAJIB menyerahkan tiket ke Gateway 2 via `/grill-me`. |
| **Tiket Terlalu Luas** ("Bikin fitur manajemen event lengkap") | Scope tak terbatas, sprint berantakan | AI WAJIB meminta developer memecah menjadi tiket-tiket kecil yang independen |
| **DoD Ambigu** ("Berhasil dijalankan") | Developer dan reviewer punya definisi sukses yang berbeda | AI WAJIB mendesak definisi yang terukur (angka, waktu, kondisi boolean, perintah test) |
| **Tiket Tanpa Blast Radius** | Developer/AI mengedit file liar di luar cakupan tugas | AI WAJIB memetakan daftar berkas entry point, service, schema, dan test |
| **Tiket Tanpa Invariant** | Tidak ada kontrak yang bisa diuji → Feature Test menjadi formalitas dangkal | AI WAJIB menggali minimal 2-3 invariant sebelum draft disahkan |
| **Asumsi Tanpa Audit Kode** | AI berbicara dari imajinasi, bukan realita repositori | AI WAJIB menjalankan Pre-Flight Audit (Fase 0) sebelum sesi dimulai |
| **Langsung Lompat ke Solusi** | Masalah bisnis inti tidak dipahami | AI WAJIB menyelesaikan Pilar Bisnis (Fase 1) terlebih dahulu |


