# Dokumen Prioritas Pembenahan Arsitektur Skill FORGE
**Status:** Dokumen Keputusan Strategis & Rencana Aksi Pembenahan  
**Dasar Analisis:** Hasil audit komparasi 10 Pola Enterprise terhadap skill riil di `eco-enzyme-landing/.agents/`  
**Tujuan:** Mengeliminasi celah kritis arsitektur, menurunkan pemborosan token, dan meningkatkan presisi eksekusi AI ke level industri tanpa menghilangkan kedalaman filosofi FORGE.

---

## 1. Ringkasan Eksekutif & Daftar Celah yang Diprioritaskan

Dari 10 Pola Arsitektur Enterprise, telah diputuskan **7 Celah Kunci** yang menjadi prioritas mutlak untuk diimplementasikan ke dalam blueprint dan skill FORGE:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       7 PILAR PRIORITAS PEMBENAHAN FORGE                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. [Pola 1]  Pembuatan & Standardisasi `project-context.md` (Gap-Only Q&A)  │
│ 2. [Pola 5]  Pemisahan Monolitik / The 10KB Rule (Folder references/)       │
│ 3. [Pola 6]  Proactive Triggers (Peringatan Bahaya Otomatis di Header)      │
│ 4. [Pola 7]  Output Artifacts Mapping (Tabel Kontrak Deliverable)           │
│ 5. [Pola 8]  Keyakinan Bukti (Confidence Tagging: 🟢 / 🟡 / 🔴)             │
│ 6. [Pola 9]  Kesimpulan di Baris Pertama (Bottom Line First / Anti-Fatigue) │
│ 7. [Pola 10] Skrip Otomasi Python Lokal (Stdlib-Only / Zero Halusinasi)     │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Rincian Bedah Tiap Prioritas: Masalah, Standar Solusi & Rencana Aksi

---

### Prioritas 1 (Pola 1): Pembuatan & Standardisasi `project-context.md` (Gap-Only Q&A)

* **Masalah Saat Ini di FORGE:**  
  Meskipun FORGE memiliki `ARCHITECTURE.md` dan `00-router.md`, saat developer memanggil `/edeate` atau `/forge-constitution`, AI masih sering mengajukan pertanyaan umum (*"Apa tech stack yang ingin kamu gunakan?"*, *"Siapa pengguna website ini?"*) yang sebenarnya sudah terdokumentasi di dalam repository. Hal ini memboroskan waktu dan menimbulkan rasa kesal bagi developer.
* **Standar Enterprise yang Diadopsi:**
  1. **Silent Inspection:** Agen **wajib membaca `project-context.md`** secara hening sebelum mencetak satu kata pun di jendela chat.
  2. **Gap-Only Response:** Agen hanya diperbolehkan menanyakan variabel yang belum tertulis di berkas konteks.
  3. **Auto-Drafting:** Jika berkas belum ada, agen mengekstrak data dari `package.json`, Git log, dan skema database, lalu membuatkan draf `project-context.md` secara otomatis.
* **Target Implementasi di FORGE:**
  * Buat template standar `.agents/rules/project-context.template.md`.
  * Tambahkan protokol *Silent Inspection* di baris paling atas `project-edeate`, `project-plan`, dan `project-grill-me`.

---

### Prioritas 2 (Pola 5): Pemisahan Monolitik / The 10KB Rule (Folder `references/`)

* **Masalah Saat Ini di FORGE:**  
  File `project-edeate/SKILL.md` berukuran **49.5 KB (604 baris)** dan `project-audit/SKILL.md` **17.6 KB**.  
  *Dampak Ilmiah:* Terjadi fenomena **Lost in the Middle** (Stanford, 2023). Kemampuan AI mengingat instruksi yang diletakkan di baris 150–450 anjlok hingga 50%. Selain itu, 12.000–14.000 token terbuang setiap kali skill dipanggil.
* **Standar Enterprise yang Diadopsi:**
  * Aturan keras: `SKILL.md` wajib $\le$ **10 KB**.
  * `SKILL.md` hanya berisi: Router state-machine, ringkasan alur kerja, dan pemicu aksi.
  * Pengetahuan detail dipisahkan ke dalam folder `references/` dan dibaca oleh AI **hanya saat dibutuhkan (on-demand)**.
* **Target Implementasi di FORGE:**
  * Pecah `project-edeate/SKILL.md` (49.5KB) menjadi:
    * `SKILL.md` ($\le$8KB): Alur Gateway Hulu 5 Tahap & State Machine.
    * `references/dual_track_protocol.md`: Aturan pemisahan Track A (FEAT) vs Track B (ARCH/NFR).
    * `references/ticket_templates.md`: Contoh dan varian struktur Tiket Level 3.
    * `references/anti_patterns.md`: Tabel penjaga kualitas (Camouflage trap, Anchoring, dll).
  * Struktur ini menghemat hingga **75% kuota token context** di awal giliran.

---

### Prioritas 3 (Pola 6): Proactive Triggers (Peringatan Bahaya Otomatis di Header)

* **Masalah Saat Ini di FORGE:**  
  FORGE memiliki aturan proteksi luar biasa di `MASTER_RULES.md` (seperti *Default Unmounted Guard `if (!isOpen) return null;`*, *Real Anchor-Click Sticky Collision Gate*, dan *Zero Test-Tampering Law*). Namun, aturan-aturan ini terkubur dalam ribuan kata di file 16KB. Akibatnya, agen yang sedang menulis kode di `/execute` sering kali melupakannya dan baru ketahuan salah saat fase `/audit`.
* **Standar Enterprise yang Diadopsi:**
  * Menyajikan **4–6 Proactive Triggers** eksplisit di bagian atas `SKILL.md`.
  * Format baku: `[Kondisi Terdeteksi di Kode] -> [Bahaya Tersembunyi] -> [Tindakan Langsung AI Tanpa Menunggu Ditanya]`.
* **Target Implementasi di FORGE:**
  * Cantumkan seksi `## Proactive Triggers` di `project-execute/SKILL.md` dan `project-plan/SKILL.md`:
    1. *Modal/Drawer terbuka tanpa check state* $\rightarrow$ Langsung cegah memory leak dengan unmounted guard.
    2. *Tinggi container statis (`h-[600px]`) pada konten dinamis* $\rightarrow$ Langsung ubah ke adaptive bounds.
    3. *Tombol fixed/sticky menabrak elemen floating* $\rightarrow$ Langsung tambahkan offset scroll margin.

---

### Prioritas 4 (Pola 7): Output Artifacts Mapping (Tabel Kontrak Deliverable)

* **Masalah Saat Ini di FORGE:**  
  Spesifikasi artefak deliverable tersebar di dalam teks naratif panjang. Developer baru atau agen AI yang baru aktif sering kali tidak memiliki gambaran instan mengenai bentuk output akhir apa yang akan terbit dari sebuah sesi.
* **Standar Enterprise yang Diadopsi:**
  * Tabel ringkas di awal skill yang memetakan jenis permintaan dengan berkas fisik yang dihasilkan.
* **Target Implementasi di FORGE:**
  * Tambahkan tabel berikut di awal setiap skill:
    | Saat Kamu Meminta... | Yang Dihasilkan AI... | Lokasi Berkas Fisik |
    | :--- | :--- | :--- |
    | *"Ideasi fitur baru"* (`/edeate`) | Spesifikasi Tiket Arsitektur Level 3 | GitHub Issue / `.docs/issues/` |
    | *"Rancang rencana teknis"* (`/plan`) | Dokumen Rencana Eksekusi Ber-Issue | `.docs/plan/issue-<nomor>-<slug>.md` |
    | *"Audit kualitas kode"* (`/audit`) | Laporan 4-Tier Gate & Handoff PR | Markdown Laporan di Chat + Checklist |

---

### Prioritas 5 (Pola 8): Keyakinan Bukti (Confidence Tagging: 🟢 / 🟡 / 🔴)

* **Masalah Saat Ini di FORGE:**  
  Dalam sesi `/edeate`, `/grill-me`, atau evaluasi teknis, AI sering mencampuradukkan antara **fakta kode yang nyata** dengan **asumsi spekulatif**. Developer kesulitan membedakan mana klaim yang sudah 100% terbukti di repository vs mana yang baru tebakan AI.
* **Standar Enterprise yang Diadopsi:**
  Setiap temuan, rekomendasi, dan klaim teknis wajib dilabeli simbol keyakinan:
  * 🟢 **Verified (Terverifikasi):** Terbukti secara faktual dari file kode sumber, AST, atau dokumentasi resmi.
  * 🟡 **Medium (Standar Praktik):** Rekomendasi berdasarkan best practice industri yang belum divalidasi dengan beban riil database.
  * 🔴 **Assumed (Asumsi Spekulatif):** Asumsi sementara karena data/logika bisnis belum diberikan oleh developer (wajib konfirmasi sebelum eksekusi).
* **Target Implementasi di FORGE:**
  * Masukkan aturan pelabelan 🟢/🟡/🔴 ke dalam `MASTER_RULES.md` untuk semua output analisis arsitektur dan audit.

---

### Prioritas 6 (Pola 9): Kesimpulan di Baris Pertama (Bottom Line First / Anti-Fatigue)

* **Masalah Saat Ini di FORGE:**  
  **Verbosity Fatigue (Kelelahan Membaca).** Karena FORGE memegang filosofi *Mentor Socratic*, AI sering memberikan 3–4 paragraf kuliah pengantar, analogi kampus, dan latar belakang teori sebelum akhirnya memberikan jawaban intinya di bagian paling bawah. Ini membuat developer frustrasi saat butuh keputusan cepat.
* **Standar Enterprise yang Diadopsi:**
  * **Bottom Line First:** Vonis/kesimpulan/rekomendasi teknis diletakkan di **baris pertama**.
  * Diikuti oleh rumus **What + Why + How to Act**.
  * Analogi edukatif diletakkan di bagian catatan kaki atau *collapsible section*, bukan menghalangi jawaban utama.
* **Target Implementasi di FORGE:**
  * Modifikasi template respon di `MASTER_RULES.md`:
    ```markdown
    **VONIS / KEPUTUSAN:** [1 kalimat jawaban langsung di baris pertama]
    **MENGAPA (WHY):** [Dampak arsitektur / trade-off utama]
    **LANGKAH TINDAKAN (HOW):** [Langkah teknis konkret berurutan]
    ```

---

### Prioritas 7 (Pola 10): Skrip Otomasi Python Lokal (Stdlib-Only / Zero Halusinasi)

* **Masalah Saat Ini di FORGE:**  
  Saat ini, skill FORGE di `eco-enzyme-landing` memiliki **0 file skrip**. Semua hal mekanis (seperti membaca `git diff --name-only` untuk menentukan Jalur 1/2/3 di `/audit`) diserahkan pada kemampuan membaca teks LLM. Hal ini lambat, memboroskan token, dan rawan salah tebak (*hallucination*).
* **Standar Enterprise yang Diadopsi:**
  * Membuat skrip Python ringan (menggunakan modul bawaan Python / Standard Library saja, tanpa `pip install`).
  * CLI-First dengan keluaran terstruktur JSON yang selesai dieksekusi dalam $\le$10 milidetik.
* **Target Implementasi di FORGE:**
  * Buat folder `scripts/` di dalam skill FORGE:
    1. `skills/project-audit/scripts/classify_blast_radius.py`: Membaca `git diff` secara deterministik dan langsung mengembalikan output `{"jalur": 1/2/3}` tanpa halusinasi.
    2. `skills/project-plan/scripts/validate_plan_format.py`: Memvalidasi kelengkapan seksi dokumen plan sebelum di-approve.

---

## 3. Matriks Rencana Eksekusi & Dampak Perubahan

| No | Pilar Prioritas | File Sasaran di FORGE | Tingkat Kesulitan | Dampak Penghematan & Keandalan |
| :---: | :--- | :--- | :---: | :--- |
| **1** | **Pola 5 (10KB Rule)** | `edeate.template.md`, `audit.template.md` | Sedang | 🟢 **Sangat Tinggi:** Hemat 70–80% token, eliminasi *Lost in the Middle*. |
| **2** | **Pola 1 (Context-First)** | `00-router.template.md`, `edeate.template.md` | Mudah | 🟢 **Tinggi:** Menghilangkan pertanyaan basi yang sudah ada di repo. |
| **3** | **Pola 9 (Bottom Line First)**| `master_rules.template.md`, `audit.template.md`| Mudah | 🟢 **Tinggi:** Lenyapkan *Verbosity Fatigue*, respon to-the-point. |
| **4** | **Pola 8 (Confidence Tag)** | `master_rules.template.md`, `grill-me.template.md`| Mudah | 🟡 **Sedang:** Transparansi fakta vs tebakan AI terjamin 100%. |
| **5** | **Pola 6 (Proactive Triggers)**| `execute.template.md`, `master_rules.template.md`| Mudah | 🟢 **Tinggi:** Menangkap bug visual & memori *sebelum* masuk audit. |
| **6** | **Pola 7 (Artifacts Table)** | Semua file template skill | Mudah | 🟡 **Sedang:** Ekspektasi deliverable jelas sejak detik pertama. |
| **7** | **Pola 10 (Python Stdlib)** | Folder `skills/*/scripts/` baru | Sedang | 🟢 **Sangat Tinggi:** Klasifikasi deterministik 0 token, 0 halusinasi. |

---

## 4. Blueprint Injeksi Perkakas Enterprise ke Stasiun Gerbang FORGE

Untuk merealisasikan prioritas di atas tanpa merusak alur kerja Two-Gateway Pipeline FORGE, kita menggunakan strategi **Injeksi Perkakas Spesifik ke Stasiun Gerbang yang Bersesuaian**:

```
[ STASIUN GERBANG FORGE ]         [ PERKAKAS ENTERPRISE YANG DIINJEKSIKAN ]
──────────────────────────────────────────────────────────────────────────────────────────
1. /edeate (Gerbang Hulu)   ───►  • Context-First Auto-Check (Pattern 1): Baca ARCHITECTURE.md diam-diam.
                                  • Socratic Framing tanpa pertanyaan basi yang sudah ada di repo.

2. /plan (Gerbang Hilir)    ───►  • database-schema-designer: Checklist RLS, Partial Indexing,
                                    dan pola Expand & Contract pada migrasi database.
                                  • Output Artifacts Mapping (Pattern 7): Tabel kontrak deliverable.

3. /execute (Gerbang Hilir) ───►  • Proactive Triggers (Pattern 6): Menampilkan 4–6 bahaya tersembunyi
                                    (Unmounted guard, sticky collision, adaptive bounds) langsung di header.

4. /audit (Gerbang Hilir)   ───►  • api_linter.py: Penegak konvensi penamaan & semantik REST.
                                  • breaking_change_detector.py: Deteksi pemutus backward compatibility.
                                  • api_scorecard.py: Audit mutu berbobot nilai A s.d. F (--min-grade B).
                                  • Tier 0 Harness Forensics: Cek log transkrip asli (Anti-Stale Test).

5. /debug (Regresi/Fix)     ───►  • focused-fix: Menegakkan The Iron Law of Diagnosis
                                    (Dilarang edit kode sebelum fase SCOPE ──► TRACE ──► DIAGNOSE selesai).
──────────────────────────────────────────────────────────────────────────────────────────
```

---

## 5. Ekspansi Alur Kerja Baru (Bebas Bias De Facto): Gerbang `/explore` & `/ship`

### A. Pertimbangan Pedagogis untuk Mahasiswa Semester Awal
Untuk mencegah **kelebihan konsumsi ilmu (cognitive overload)** pada mahasiswa pemula, penambahan alur baru **TIDAK DIJADIKAN RUTINITAS HARIAN TIKET**. 

Alur produksi berat (seperti SRE, incident response, dan OpenTelemetry) sengaja ditiadakan dari alur harian. Sebagai gantinya, kita mengadopsi **2 Gerbang Khusus Bersifat Event-Driven**:
* Satu gerbang dipanggil **sekali di awal proyek** (`/explore`).
* Satu gerbang dipanggil **sekali di akhir proyek / menjelang UAS** (`/ship`).
* Alur pengerjaan tugas mingguan mahasiswa tetap santai menggunakan alur Two-Gateway FORGE biasa (`/edeate` $\rightarrow$ `/plan` $\rightarrow$ `/execute` $\rightarrow$ `/audit`).

```
[ HARI PERTAMA PROYEK ]           [ SIKLUS MINGGUAN TUGAS MAHASISWA ]             [ DEMO AKHIR / UAS ]
     (Dipanggil 1x)                          (Alur Rutin FORGE)                       (Dipanggil 1x)

       /explore          ───►      /edeate ──► /plan ──► /execute ──► /audit    ───►       /ship
  (Tur Kampus Kode)                 (Ideasi)    (Rencana) (Koding/TDD) (Review)        (Kertas Kado Rilis)
                                                   ▲             │
                                                   └─── /debug ──┘
```

---

### B. Rincian & Strategi Sosialisasi ke Mahasiswa

#### 1. Gerbang Awal: `/explore` (Codebase Reality Grounding)
* **Kapan Dipanggil:** 
  * Cukup **1 kali di awal proyek**, saat mahasiswa baru selesai `git clone` repository template atau repo lama.
  * Saat mahasiswa merasa bingung: *"Kak/Pak, filenya banyak banget, aku harus mulai koding di mana dulu?"*
* **Fungsi Teknis:**  
  Melakukan *Codebase Archeology*: membaca struktur folder, entry point, database schema, dan menghasilkan peta visual relasi berkas ke `PROJECT_DNA.md`.
* **Narasi Sosialisasi (Gaya Kakak Tingkat):**
  > *"Bayangkan kamu mahasiswa baru yang baru pertama masuk gerbang kampus. Kamu belum tahu gedung kelas di mana, lab komputer di mana, dan kantin di mana. Kalau langsung lari, kamu pasti nyasar. Perintah `/explore` adalah **Google Maps Kampus**. Dia akan memandu kamu keliling kode: 'Ini pintu masuknya, ini tempat databasenya, dan ini tombol-tombolnya'. Setelah kamu kenal denah rumahnya, baru kita mulai merancang ide tugas!"*

#### 2. Gerbang Akhir: `/ship` (Release Readiness Gate)
* **Kapan Dipanggil:** 
  * Cukup **1 kali di akhir sprint / akhir semester**, saat seluruh fitur tugas sudah selesai dan lulus `/audit`.
  * Menjelang demo UAS atau sebelum deploy ke hosting gratis (Vercel, Netlify, GitHub Pages).
* **Fungsi Teknis:**  
  * *Pre-Flight Check:* Memastikan tidak ada token/password `.env` yang tertinggal, build production sukses, dan skema database siap.
  * *SemVer & Changelog:* Menentukan nomor versi resmi (`v1.0.0`) dan men-generate berkas `CHANGELOG.md` otomatis dari git commit.
* **Narasi Sosialisasi (Gaya Kakak Tingkat):**
  > *"Kalian sudah capek-capek begadang 2 minggu bikin aplikasi tugas yang keren. Masa karya sekeren ini kalian kumpulkan ke dosen cuma pakai zip mentah acak-acakan? Perintah `/ship` ini tugasnya **membungkus aplikasimu pakai kertas kado rapi dan pita cantik**. Dia otomatis merapikan riwayat catatan rilis (`CHANGELOG.md`), memberi stempel versi resmi (`v1.0.0`), dan memastikan karyamu siap dipamerkan ke dosen atau portofolio LinkedIn dengan standar industri!"*

---

## 6. Asimilasi Strategi Multi-Agent & Modularitas Persona (Fase 4)

Berdasarkan hasil studi orkestrasi di Fase 4, telah diputuskan **2 Strategi Asimilasi Tambahan** untuk memperkuat ketahanan sistem dan modularitas berkas FORGE:

### Strategi 1: Suntikkan Sub-Agent "Adversarial Reviewer" ke Gerbang `/plan` & `/grill-me`
* **Masalah yang Diselesaikan:**  
  Saat ini, agen yang sama merancang rencana di `/plan` sekaligus memvalidasinya. Hal ini rawan memicu bias konfirmasi (*Self-Confirmation Bias*) di mana AI cenderung membela rancangannya sendiri dan mengabaikan celah arsitektur.
* **Metode Asimilasi:**  
  Di akhir sesi `/plan` (atau saat memanggil `/grill-me`), sistem mengaktifkan sub-agent independen berpersona **`adversarial-reviewer`**.
  * Agen penyerang ini bertugas mencari skenario terburuk (*worst-case scenario*), beban batas memori, race conditions, dan potensi bottleneck sebelum developer diizinkan melangkah ke fase koding `/execute`.
  * Menghadirkan ketegangan dialektika kritis yang objektif tanpa mengintimidasi mahasiswa (karena yang dikritik adalah rencana sistem, bukan mahasiswa secara personal).

### Strategi 2: Pisahkan Persona Mentor dari Berkas `SKILL.md`
* **Masalah yang Diselesaikan:**  
  Instruksi kepribadian *"Principal Engineer / Kakak Tingkat Senior"* saat ini tertanam langsung menyatu di dalam berkas alur kerja teknis (`edeate.template.md` dan `forge-constitution/SKILL.md`). Inilah yang membuat ukuran file membengkak hingga **31–49 KB**.
* **Metode Asimilasi:**  
  Menerapkan prinsip pemisahan **WHO (Persona) vs HOW (Skill)**:
  * **Folder Persona (`.agents/personas/kakak-tingkat-mentor.md`):** Menyimpan nilai-nilai pedagogi, gaya bahasa ramah, empati pada mahasiswa pemula, dan *The Safe Harbor Protocol*.
  * **Berkas Skill (`SKILL.md`):** Murni hanya memuat alur state-machine teknis, tabel gating, dan pemanggilan tool.
  * **Dampak:** Berkas `SKILL.md` otomatis mengecil drastis ke batas aman $\le$**10 KB** (memenuhi *The 10KB Rule*), bebas dari *Attention Dilution*, namun agen tetap berbicara dengan kehangatan seorang mentor senior.

---

## 7. Integrasi Gerbang `/prototype` (Kanvas Penpot) & The Visual Contract Gate

### A. Latar Belakang & Keselarasan Kurikulum
* **Kebutuhan Pedagogis:**  
  Menunjang mata kuliah kurikulum *"Dasar-Dasar Desain Antarmuka Interaktif"*. Mahasiswa dilatih merasakan atmosfer **Vibe Coding & Design** (bereksperimen secara visual tanpa harus dipusingkan dengan baris kode mentah di awal).
* **Alasan Pemilihan Kanvas Penpot:**  
  100% berbasis standar web terbuka (**CSS Flexbox & CSS Grid murni**). Mahasiswa belajar logika tata letak CSS yang sebenarnya, bukan sekadar koordinat grafis bebas. Gratis, open-source, dan bebas dari pembatasan akun berbayar.

### B. Mekanisme Jaring Pengaman: "The Visual Contract Gate"
Agar kebebasan berkreasi di kanvas visual tidak merusak arsitektur backend, gerbang ini dilengkapi **Satpam Validasi Kontrak Otomatis** sebelum masuk ke `/execute`:

```
[ GERBANG /plan ] ──► Menghasilkan "Kontrak Antarmuka" (Daftar field, data, & tombol aksi)
         │
         ▼
[ KANVAS PENPOT ] ──► Mahasiswa bebas mendesain tata letak visual, warna, spacing, & hierarki
         │
         ▼
[ THE VISUAL CONTRACT GATE ] ──► AI membandingkan: Apakah elemen Penpot == Kontrak di /plan?
         ├── JIKA COCOK ────────► Lolos ke /execute (AI mengonversi Penpot ke Tailwind/Astro)
         └── JIKA ADA DEVIASI ──► AI MENGUNCI EKSEKUSI & memberi 2 opsi rekonsiliasi:
                                   Opsi 1: Hapus elemen ekstra di Penpot agar patuh ke /plan.
                                   Opsi 2: Buka kembali /plan untuk update skema database.
```

### C. Manfaat bagi Mahasiswa
1. **Belajar Traceability:** Memahami secara dini bahwa setiap kotak visual di layar membawa konsekuensi logika di database.
2. **Presentasi Memukau:** Mahasiswa dapat memamerkan papan kanvas Penpot + Dokumen `/plan` + Hasil kodingan nyata saat demo di depan dosen penguji.

---
*Dokumen ini merupakan acuan resmi untuk proyek refactoring konstitusi dan blueprint FORGE berikutnya.*
