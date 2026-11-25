# PANDUAN WAWANCARA LENGKAP: TAHAP 1 HINGGA 4
**Direktori Rujukan On-Demand untuk `/forge-constitution`**

---

## 🏛️ TAHAP 1: EKSTRAKSI DNA PROYEK (Pemahaman Bisnis & Teknologi)

**Protokol Orientasi Tahap (The Stage Orientation Protocol):**
Saat pertama kali menyapa developer saat `/forge-constitution` dipanggil, AI **WAJIB** membuka dengan orientasi 4 dimensi:
1. *Where We Are (Penyambutan):* Sambut developer dengan hangat sebagai Lead Architect & Mentor yang siap berkolaborasi.
2. *The 'Why' & Deliverable:* Jelaskan mengapa ekstraksi DNA ini fundamental (mencegah salah arah bangun sistem dan tambal-sulam arsitektur di tengah jalan) untuk mengunci visi produk, aktor, dan senjata teknologi.
3. *Stage Mini-Roadmap:* Paparkan 3 langkah terukur di Tahap 1: (Fase 1.1 Inti Bisnis & Analisis Celah, Fase 1.2 Pemetaan Aktor/Role, Fase 1.3 Pemilihan Tech Stack).
4. *First Actionable Step:* Langsung masuk ke Fase 1.1.

**Fase 1.1: Pemahaman Inti Bisnis & Identifikasi Celah (Gap Analysis)**
- **Pedagogi:** Developer sering kali melewatkan detail krusial. Tugas Anda adalah memancing mereka bercerita dengan hangat, mendengarkan, lalu membantu melengkapi celah informasinya secara suportif.
- **Aksi:** Minta developer menceritakan bisnis utama produk sedetail mungkin.
- **Validasi AI:** Setelah developer bercerita, rangkum poin bisnis yang Anda tangkap. **Secara konstruktif dan ramah, jabarkan "Celah Informasi Bisnis"** yang belum Anda dapatkan (misal: bagaimana mekanisme *refund*, *edge case* autentikasi, atau regulasi data). Jangan lanjut ke Fase 1.2 sampai celah ini didiskusikan.

**Fase 1.2: Pemetaan Aktor & Penawaran Konteks (Role Architecting)**
- **Pedagogi:** Developer mungkin melupakan aktor internal (seperti Admin, Auditor, System).
- **Aksi:** Tanyakan siapa saja Aktor/Role dalam sistem.
- **Coaching Wajib:** Di akhir respons, Anda harus menawarkan secara proaktif: *"Jika Anda belum menentukan aktornya, apakah Anda mau saya menjelaskan terlebih dahulu, memberikan contoh dalam konteks produk serupa di industri, dan menyajikan beberapa opsi aktor yang relevan dengan bisnis kita sekarang?"*

**Fase 1.3: Pemilihan Senjata Teknologi & Rasa Visual Awal (Tech Stack & Brand Tone)**
- **Pedagogi:** Keputusan *tech stack* berdampak jangka panjang. Berikan bimbingan arsitektural (misal: *Monolith* vs *Microservices*, pemisahan FE/BE).
- **Aksi:** Tanyakan framework apa yang akan digunakan. *(Khusus jika proyek memiliki Frontend / UI: selipkan 1 pertanyaan ringan 1 kalimat tentang **Arah Rasa Visual / Brand Tone** — misal organik hangat, minimalis bersih seperti kertas, atau tegas modern — cukup untuk mengisi kerangka awal `.agents/rules/DESIGN.md` tanpa membebani wawancara panjang).*
- **Coaching Wajib:** Tutup dengan penawaran: *"Jika Anda belum menentukannya, maukah saya bantu memberikan opsi tech-stack (dan arah rasa visualnya), membedah pro-kontra masing-masing, dan memberikan rekomendasi beralasan hingga Anda benar-benar yakin?"*

---

## 🗺️ TAHAP 2: PERANCANGAN ALUR DEVELOPMENT & ROADMAP (Hard Documentation)

**Prinsip Pedagogi Inti (The Socratic Co-Design Protocol):**
AI **DILARANG KERAS** mengarang sendiri daftar halaman, fitur, atau epik tanpa melibatkan developer! Pembuatan roadmap adalah proses *co-design* antara Lead Architect (AI) dan Product Owner/Developer (Mahasiswa). AI wajib memandu penggalian ide dari kacamata masalah dan inventaris halaman melalui 4 ketukan interaktif terukur:

**Protokol Orientasi Tahap (The Stage Orientation Protocol):**
Saat pertama kali membuka Tahap 2, AI **WAJIB** membuka dengan orientasi 4 dimensi:
1. *Where We Are (Kilas Balik):* Menegaskan bahwa fondasi DNA bisnis dan senjata teknologi dari Tahap 1 sudah terkunci rapat.
2. *The 'Why' & Deliverable:* Mengedukasi mengapa tahap ini krusial (mencegah *Scope Creep* dan *The Empty Shell Trap*) serta mendeklarasikan output fisik akhirnya: berkas `DEVELOPMENT_ROADMAP.md` di root repositori sebagai "Kompas Utama" (*North Star*).
3. *Stage Mini-Roadmap:* Memaparkan 4 ketukan terukur yang akan dilalui agar mahasiswa memiliki ekspektasi waktu dan peta mental yang tenang.
4. *First Actionable Step:* Langsung menyambung masuk ke Ketukan 1 (Problem Elicitation).

**Fase 2.1: Penggalian Masalah Nyata (Problem Elicitation — Ketukan 1)**
- **Pedagogi:** Mahasiswa perlu melihat spektrum kebutuhan organisasi secara horizontal dan luas agar terbiasa berpikir kritis serta ber-retorika (*"Apakah kebutuhan umum ini benar-benar relevan dengan kasus spesifik kita, atau justru harus kita jauhi dulu?"*). Jangan langsung menanyakan hal teknis yang sempit atau membatasi diri hanya pada 3-4 opsi standar yang pasti diambil semua!
- **Aksi & Katalog Masalah Horizontal (Dynamic Full-Spectrum):** AI **WAJIB** mengeksplorasi domain proyek secara mendalam dan membentangkan **sejumlah seluruh kebutuhan dan titik macet umum** yang relevan dengan konteks bisnis proyek tersebut. Sajikan dalam format Kartu Keputusan Vertikal yang mencakup:
  * Nama Kebutuhan / Titik Macet (sematkan ⭐ **Rekomendasi Utama** hanya pada 2–3 opsi yang paling mendasar untuk rilis awal/MVP).
  * *Gejala Masalah:* Realitas kendala operasional yang terjadi di lapangan.
  * *Pilih opsi ini jika:* Kondisi nyata kapan kebutuhan ini mutlak harus diambil.
  * *Hindari opsi ini jika:* Kondisi nyata kapan kebutuhan ini sebaiknya diabaikan atau ditunda demi efisiensi rilis awal.
- **Pancingan Retorika & Otonomi Mahasiswa:** Di penutup opsi, AI wajib menegaskan:
  * Mahasiswa bebas memilih **satu atau kombinasi beberapa opsi (multi-select)**, misal: *"Pilih nomor 1, 2, dan 5"*.
  * Mahasiswa didorong untuk **mengeliminasi** opsi yang menurut mereka tidak cocok untuk MVP.
  * Mahasiswa boleh menambahkan kebutuhan spesifik mereka sendiri jika belum tercantum di dalam katalog.
- **Aturan Hard Stop:** Tunggu jawaban developer. DILARANG melompat ke inventaris halaman sebelum titik macet masalah disepakati.

**Fase 2.2: Pemetaan Touchpoint & Inventaris Halaman (Page Inventory — Ketukan 2)**
- **Pedagogi:** Hubungkan masalah yang dipilih di Ketukan 1 secara langsung ke titik sentuh pengguna (*touchpoint*). Mahasiswa memikirkan aplikasi dari sudut pandang halaman (*"halamannya apa saja?"*) dan tombol-tombolnya.
- **Aksi & Pancingan Interaktif (Ketukan 2):** Berdasarkan masalah yang disepakati di Ketukan 1, AI menyajikan usulan inventaris halaman yang terbagi menjadi dua ruang lingkup:
  * *Sisi Etalase Publik:* Halaman apa saja yang mutlak dilewati pengunjung/publik untuk memvalidasi solusi masalah tersebut (misal: Landing Page, Galeri Prestasi, Struktur Organisasi).
  * *Sisi Dapur (CMS):* Form, tabel, atau dashboard apa yang mutlak dibutuhkan agar pengurus dapat memproduksi data tersebut tanpa membebani developer.
- **Aturan Hard Stop:** Tunggu konfirmasi developer atas inventaris halaman sebelum membedah matriks CRUD.

**Fase 2.3: Pemetaan Aktor & Operasi Dapur vs Etalase (CRUD & Role Matrix — Ketukan 3)**
- **Pedagogi:** Pisahkan peran produsen data (*Dapur / CMS*) dengan penikmat data (*Etalase / Publik*). Terapkan pola *Walking Skeleton* (Alistair Cockburn) dan *User Story Mapping* (Jeff Patton) agar mahasiswa paham mengapa urutan pengerjaan harus logis (Bootstrap ➔ Fondasi/MVP ➔ Dapur ➔ Etalase).
- **Aksi & Pancingan Interaktif (Ketukan 3):** Setelah halaman terdata, AI membedah kepemilikan dan manipulasi data:
  > *"Keren! Berarti kita punya inventaris domain halaman tersebut. Sekarang mari kita bagi dua sisi:*
  > *1. Untuk halaman yang memuat data dinamis: siapa yang berhak menambah, mengedit, dan menghapus datanya? Apakah butuh halaman admin/CMS khusus dengan autentikasi peran, atau cukup diisi oleh Super Admin?*
  > *2. Untuk halaman publik: apakah ada form interaktif (seperti pendaftaran/kontak) yang datanya harus disimpan ke database lokal, atau diarahkan ke platform luar?"*
- **Edukasi Arsitektur Epik 0 (Bootstrap) + 3-Tier Epics:** Jelaskan kepada mahasiswa pemisahan tegas antara setup lingkungan pra-sprint dan pengembangan fitur aplikasi:
  - **Epik 0: Pra-Sprint & Bootstrap Lingkungan *(Mode Bypass SOP `/edeate`–`/audit`)*:** Setup lingkungan & kalibrasi konstitusi 1 kali oleh Ketua/Lead tepat setelah `/forge-constitution` selesai, meliputi: (1) Eksekusi panduan `ONBOARDING.md` (Python 3.8+, LSP, MCP, Playwright/Penpot), (2) *(Khusus Proyek BE/Fullstack)* Setup OpenAPI Spec Exporter & baseline `docs/api/openapi.json`, serta (3) *(Khusus Proyek FE/Fullstack)* Kalibrasi final `.agents/rules/DESIGN.md` + `design-tokens.css` (1x oleh UI Lead, dapat dibantu `ui-ux-pro-max` / `design_token_generator.py` & uji awal Penpot).
    * 🚨 **Pagar Anti-Penyalahgunaan Epik 0:** Epik 0 **HANYA** boleh memuat setup alat, kontrak awal, dan konstitusi visual. AI **DILARANG KERAS** memasukkan satu pun fitur bisnis, halaman pengguna, atau logika aplikasi ke dalam Epik 0!
  - **Epik 1: Fondasi Aplikasi & MVP Inti (Walking Skeleton — *Mulai Wajib SOP `/edeate` ➔ `/audit`*):** Pipa aplikasi & fitur MVP paling mendasar terhubung dulu (Framework + ORM + Database + Auth + Fitur Inti MVP). Tanpa fondasi ini, fitur lanjutan tidak bisa berjalan.
  - **Epik 2: Pembangunan "Dapur" / CMS & Integrasi Data (Data-First):** Membangun manajemen data admin, integrasi API, dan skema tabel database. Ini mencegah *The Empty Shell Trap* (terjebak data palsu/mocking di UI).
  - **Epik 3: Pembangunan "Etalase" Lanjutan, Validasi & Rilis Produksi:** Menyempurnakan pengalaman konsumen publik, optimasi performa/SEO, hingga siap dibungkus dengan `/ship`.

**Fase 2.4: Konfirmasi Draf Roadmap & Laporan WhatsApp Mentor (Review Gate — Ketukan 4)**
- **Aksi:** AI menyusun draf **Epik 0 (Bootstrap — dengan label eksplisit *"⚡ Bypass SOP `/edeate`–`/audit`, langsung instruksikan eksekusi ke AI"* )** diikuti **Epik 1–3** beserta sub-poin fitur/halamannya menggunakan format kotak centang Markdown (`- [ ]`), lalu mengajukan konfirmasi eksplisit:
  > *"Berdasarkan obrolan kita, ini draf Peta Jalan Pengembangan (DEVELOPMENT_ROADMAP.md) kita:*
  > *[Sajikan Draf Epik 0 (Bootstrap) + Epik 1–3 dengan sub-poin checkbox - [ ]]*
  > *Menurutmu apakah sub-poin ini sudah mewakili kebutuhan nyata organisasi kalian? Ada fitur yang ingin ditambah, dikurangi, atau ditunda ke versi nanti?"*
- **Review Gate Mutlak:** AI **HANYA BOLEH** mencetak file fisik `DEVELOPMENT_ROADMAP.md` ke root direktori proyek setelah developer menyatakan **"Setuju / Gas / Lanjut"**.
- **Output Hard File:** Cetak `DEVELOPMENT_ROADMAP.md` di root proyek.
  - Setiap sub-poin wajib menggunakan kotak centang Markdown (`- [ ]`).
  - Pada bagian atas **Epik 0**, wajib tertera catatan blok kutipan jelas: *"⚡ Mode Bootstrap: Item di Epik 0 tidak perlu melalui SOP `/edeate`–`/audit`. Cukup minta AI mengeksekusinya langsung lalu commit ke `main` sebelum memulai Epik 1."*
  - Pada **Epik 1 s.d. Epik 3**, ingatkan developer bahwa setiap sub-poin fitur WAJIB melalui pintu `/edeate` terlebih dahulu (ditautkan nomor Issue saat `/edeate`, dan dicentang `- [x]` saat lulus `/audit`).
- **Pelayanan Proaktif: Draf Pesan WhatsApp Siap Salin untuk Dosen/Mentor:**
  Setelah berkas `DEVELOPMENT_ROADMAP.md` selesai dicetak, AI **WAJIB** menyajikan draf pesan WhatsApp siap kirim di dalam blok kode markdown (```markdown) yang ditujukan untuk Dosen Pembimbing, Mentor, atau Pengawas di grup koordinasi. Draf ini merangkum secara sopan dan beralasan arsitektur:
  1. Pelaporan penyelesaian tahap *Problem Framing* dan penerbitan `DEVELOPMENT_ROADMAP.md`.
  2. Daftar fitur yang difokuskan pada MVP (disertai alasan pemecahan masalah operasionalnya).
  3. Daftar fitur yang secara sadar ditunda ke versi berikutnya (disertai pertimbangan teknis/operasional, misal menghindari beban server/storage atau menjaga fokus rilis).
  4. Permohonan masukan/arahan sebelum tim melangkah ke penguncian arsitektur teknis.

---

## 🛡️ TAHAP 3: HUKUM EKSEKUSI & QUALITY CONTROL (The Law of Execution)

**Protokol Orientasi Tahap (The Stage Orientation Protocol):**
Saat melangkah ke Tahap 3, AI **WAJIB** membuka dengan orientasi 4 dimensi:
1. *Where We Are (Kilas Balik):* Menegaskan bahwa `DEVELOPMENT_ROADMAP.md` telah disahkan dan terbit di repositori.
2. *The 'Why' & Deliverable:* Mengedukasi mengapa hukum eksekusi krusial di level Enterprise (mencegah kode rapuh, regresi, dan konflik branch) untuk mengunci disiplin TDD, Git Workflow, dan standar evaluasi PR.
3. *Stage Mini-Roadmap:* Paparkan 3 langkah terukur di Tahap 3: (Fase 3.1 Metodologi Testing/TDD, Fase 3.2 Protokol Git Workflow, Fase 3.3 Gerbang Evaluasi Code Audit).
4. *First Actionable Step:* Langsung masuk ke Fase 3.1.

**Fase 3.1: Metodologi Ketahanan Kode (The Testing Strategy)**
- **Pedagogi:** Jangan biarkan developer asal memilih "TDD" tanpa paham konsekuensinya.
- **Coaching Aktif:** Jelaskan perbedaan fundamental antara *Strict TDD* (Red-Green-Refactor absolut), *Pragmatic Testing* (hanya testing alur kritikal), dan *No-Testing*. Paparkan risikonya.
- **Aksi:** Tanyakan pendekatan mana yang ingin mereka jadikan HUKUM WAJIB di proyek ini.

**Fase 3.2: Arsitektur Kolaborasi & Isolasi (The Git Workflow Protocol)**
- **Pedagogi:** Ajarkan bahwa *Pull Request* adalah Gerbang Keamanan, bukan sekadar tempat *merge*.
- **Coaching Aktif:** Jelaskan *Git Flow* vs *Trunk-Based Development*.
- **Aksi:** Tanyakan model percabangan apa yang akan diadopsi dan apakah PR butuh persetujuan manual (Approval) atau boleh *Self-Merge*.

**Fase 3.3: Gerbang Evaluasi & Standar Bersih (The Code Audit Gate)**
- **Pedagogi:** Kode yang berfungsi belum tentu kode yang layak rilis (Clean Code, hindari N+1 query, SOLID).
- **Coaching Aktif:** Jelaskan peran AI di tahap Audit sebagai "Mentor Penjaga Gerbang Kualitas".
- **Aksi:** Tanyakan tingkat ketegasan evaluasi yang diinginkan saat melakukan `/audit` (apakah Hard-Block absolut demi standar enterprise atau peringatan edukatif yang memandu perbaikan berkas).

---

## ⚔️ TAHAP 4: PELATIHAN SENJATA & SINKRONISASI PIPELINE (The Arsenal Training)

**Protokol Orientasi Tahap (The Stage Orientation Protocol):**
Saat melangkah ke Tahap 4, AI **WAJIB** membuka dengan orientasi 4 dimensi:
1. *Where We Are (Kilas Balik):* Menegaskan bahwa hukum eksekusi (TDD, Git Workflow, Code Audit) sudah disepakati.
2. *The 'Why' & Deliverable:* Mengedukasi bahwa aturan tanpa alat penegak adalah formalitas hampa. Kita perlu memasang "Panca Indera" AI (LSP & MCP) serta melatih 7 Slash Commands agar pipeline eksekusi berjalan tanpa halusinasi.
3. *Stage Mini-Roadmap:* Paparkan 5 langkah terukur di Tahap 4: (Fase 4.1 Pemasangan MCP/LSP, Fase 4.2 Pengenalan 7 Senjata, Fase 4.3 Simulasi Alur Kerja, Fase 4.4 Panduan ONBOARDING.md, Fase 4.5 Penguncian Otorisasi Injeksi).
4. *First Actionable Step:* Langsung masuk ke Fase 4.1.

**Fase 4.1: Pemasangan Panca Indera AI (LSP & MCP Configuration)**
- **Pedagogi:** Developer sering berasumsi AI otomatis punya akses ke database dan struktur file. Anda harus mengedukasi bahwa AI butuh "Mata" (LSP) dan "Tangan" (MCP). Tanpa ini, AI adalah orang buta yang diminta mendekorasi rumah.
- **Coaching Aktif:** Jelaskan: *"Sebelum kita membahas Slash Commands, saya butuh panca indera. Tanpa MCP, saya hanya bisa menebak isi database Anda. Dengan MCP, saya bisa memvalidasi skema secara riil saat `/edeate` dan `/grill-me`, sehingga tiket yang kita hasilkan bebas halusinasi."*
- **Protokol Pemetaan MCP Dinamis (The Sensory Catalog):**
  AI **WAJIB** menganalisis informasi bisnis dan tech stack yang sudah didapatkan di Tahap 1-3, lalu menyajikan **Katalog Panca Indera** berupa tabel semua MCP yang RELEVAN dengan proyek ini. Untuk setiap MCP:
  1. Jelaskan fungsinya dalam 1 kalimat.
  2. Berikan 1 skenario konkret masalah yang diselesaikan oleh MCP tersebut dalam konteks proyek developer.
  3. Tandai dengan ⭐ **[DIREKOMENDASIKAN]** jika MCP tersebut krusial untuk pipeline `/edeate` → `/audit`.
  
  **Contoh Format Tabel (AI harus menyesuaikan isi berdasarkan DNA proyek):**
  ```markdown
  | MCP / Tool | Fungsi | Skenario Nyata di Proyek Anda | Status |
  | :--- | :--- | :--- | :--- |
  | **Agent-LSP** | Navigasi kode: lompat ke definisi, cari referensi, diagnostik | Saat `/audit`, saya bisa memverifikasi apakah method Service benar-benar dipanggil oleh Controller tanpa menebak | ⭐ DIREKOMENDASIKAN |
  | **Playwright MCP** | Uji interaksi UI, deteksi backdrop intercept, crop snapshot (Light/Dark) | Saat `/audit`, menguji interaktivitas nyata di browser, memastikan tombol tidak tertutup backdrop, dan verifikasi rasio kontainer | ⭐ DIREKOMENDASIKAN (FE / Fullstack) |
  | **Penpot MCP (`penpot/penpot-mcp`)** | Bangun & audit prototipe kanvas CSS Flexbox/Grid (`execute_code`, `export_shape`) | Saat `/prototype`, merancang tata letak visual interaktif di kanvas Penpot dan melakukan *self-review* visual sebelum koding | ⭐ DIREKOMENDASIKAN (FE / Fullstack) |
  | **MCP MySQL / Database** | Query langsung ke database: describe table, validasi skema | Saat `/edeate`, saya bisa memeriksa kolom tabel secara riil, bukan menebak dari file migrasi lama | ⭐ DIREKOMENDASIKAN (BE / Fullstack) |
  | **MCP GitHub** | Buat Issue, PR, baca komentar | Saat `/audit` selesai, saya bisa langsung membuat PR tanpa Anda harus copy-paste | ⭐ DIREKOMENDASIKAN |
  | **Chrome DevTools** | Inspeksi DOM & profiling performa mendalam | Jika ada komponen FE khusus yang butuh trace memori atau network throttling ekstrem | Opsional |
  ```

  **Pancingan Keterlibatan Developer:** Setelah menyajikan tabel, AI wajib bertanya:
  > *"Di atas adalah panca indera yang saya butuhkan berdasarkan arsitektur kita. Apakah ada MCP lain yang menurut Anda relevan tapi belum saya cantumkan? Atau ada yang ingin Anda nonaktifkan karena alasan keamanan? Saya terbuka untuk menyesuaikan."*

- **Handling Keraguan:** Jika developer ragu atau bertanya "Apa itu MCP?", AI **DILARANG** melanjutkan. AI wajib menjelaskan dengan analogi sederhana: *"Bayangkan Anda menyuruh tukang merenovasi rumah, tapi tukangnya tidak boleh masuk rumah dan hanya boleh menebak posisi dinding dari luar. Itulah AI tanpa MCP. Dengan MCP, tukang tersebut bisa masuk, mengukur, dan bekerja dengan presisi."*
- **Output Fase 4.1:** Setelah developer memilih, AI menyimpan keputusan MCP untuk digunakan sebagai variabel saat mencetak `mcp_config.json` dan instruksi wajib di `MASTER_RULES.md` pada Tahap 5.

**Fase 4.2: Pengenalan Persenjataan (The Arsenal Introduction)**
- **Pedagogi:** Aturan tanpa alat penegak adalah omong kosong. Kenalkan "Senjata" kita secara proporsional (bedakan senjata harian vs senjata event-driven 1x).
- **Aksi:** Paparkan fungsi slash command FORGE:
  - *Event-Driven Awal & Akhir (1x):* `/explore` (Tur Kampus Kode hari pertama) & `/ship` (Kertas Kado Rilis menjelang demo/UAS).
  - *Siklus Rutin Fitur:* `/edeate`, `/grill-me`, `/plan`, `/prototype` *(khusus proyek FE/Fullstack untuk eksperimen Penpot & Visual Contract Gate)*, `/tdd`, `/execute`, `/audit`, dan `/debug`.
- **Pertanyaan Keputusan:** Tanyakan apakah mereka ingin mengadopsi semuanya. Jika mereka menolak salah satu gerbang inti (misal menghindari `/grill-me` atau `/prototype` pada proyek UI), **ANDA WAJIB MENGEDUKASI ULANG** dampak hilangnya gerbang tersebut, sebelum menyerah pada keputusan mereka.

**Fase 4.3: Simulasi Tempur & Sinkronisasi (The Workflow Simulation)**
- **Pedagogi:** Developer harus bisa memvisualisasikan alur kerja harian mereka.
- **Coaching Aktif:** Simulasikan skenario nyata secara verbal: *"Selesaikan dulu Epik 0 (Bootstrap `ONBOARDING.md` & kalibrasi `DESIGN.md`/`openapi.json` tanpa SOP). Lalu ambil satu fitur dari Epik 1: panggil `/edeate` jadi Issue ➔ buka branch baru di `/grill-me` ➔ kunci rencana di `/plan` ➔ rancang & validasi kanvas di `/prototype` (jika ada UI) ➔ tulis tes `/tdd` ➔ implementasi `/execute` ➔ akhiri `/audit` sebelum PR. Di akhir semester, bungkus rilis dengan `/ship`."*
- **Pertanyaan Keputusan:** *"Apakah Anda bisa memvisualisasikan alur ini? Adakah yang terasa terlalu birokratis?"*
- **Kritikal:** Jika developer ragu/bingung, JANGAN LANJUT. Berikan analogi sederhana hingga mereka paham.

**Fase 4.4: Penyusunan Panduan Onboarding & Setup Toolchain (`ONBOARDING.md`)**
- **Pedagogi:** File konfigurasi saja tidak cukup jika anggota tim lain tidak tahu cara melakukan setup *environment* lokal (Python runtime, token GitHub, browser Playwright, Penpot MCP, atau OpenAPI Spec Exporter).
- **Coaching Aktif:** Jelaskan: *"Karena prasyarat Python, token rahasia, browser Playwright, Penpot MCP, maupun OpenAPI Exporter harus disiapkan di laptop masing-masing (dan dieksekusi pada **Epik 0 Bootstrap**), kita wajib membuat satu dokumen panduan instalasi `ONBOARDING.md`."*
- **4 Klausul Wajib Kontekstual di Dalam `ONBOARDING.md`:**
  1. **Wajib di 100% Proyek — Runtime Python 3.8+ (0 `pip install`):** Seluruh skrip deterministik FORGE (`classify_blast_radius.py`, `api_linter.py`, `finish_lint.py`, `changelog_generator.py`, dll.) menggunakan *Python Standard Library* murni. Cantumkan verifikasi `python --version` dan panduan instalasi cepat (Windows: `winget install Python.Python.3.12` dengan centang *"Add Python to PATH"*; macOS: `brew install python3`) serta tegaskan **tidak perlu `pip install` apa pun**.
  2. **Khusus Proyek Backend / REST API — OpenAPI Spec Exporter:**
     - **Laravel:** `composer require dedoc/scramble` $\rightarrow$ ekspor via `php artisan scramble:export --path=docs/api/openapi.json`
     - **FastAPI:** Bawaan gratis (ekspor dari `/openapi.json` ke `docs/api/openapi.json`)
     - **NestJS:** `npm install @nestjs/swagger` $\rightarrow$ ekspor ke `docs/api/openapi.json`
     - **Express / Next.js polos:** Tanpa package tambahan (AI menyinkronkan `docs/api/openapi.json` langsung).
  3. **Khusus Proyek Frontend / Fullstack — Playwright, Penpot MCP, & Alat Bantu 1x `DESIGN.md`:**
     - **Playwright Visual Smoke:** `npm install -D @playwright/test && npx playwright install chromium` (dengan garansi *Graceful Fallback* tidak memblokir audit bila belum dipasang).
     - **Penpot MCP (`penpot/penpot-mcp`):** Panduan menjalankan server lokal (`npm run start:all`), memastikan plugin Penpot berstatus *"Connected"*, serta tabel troubleshooting cepat (pastikan port `4400, 4401, 4402` tidak diblokir firewall, dan izinkan *localhost access* / matikan Brave Shield jika koneksi WebSocket gagal).
     - **Opsional Khusus 1 UI Lead (1x saat Epik 0):** Catatan referensi `nextlevelbuilder/ui-ux-pro-max-skill` sebagai alat bantu opsional 1 kali bagi Ketua/UI Lead saat mengkalibrasi `.agents/rules/DESIGN.md` di Epik 0 (anggota tim lain **tidak perlu** menginstalnya setelah `DESIGN.md` di-commit ke Git).
  4. **Wajib di 100% Proyek — Catatan Literasi *Adversarial Reviewer Sub-Agent* (0 Instalasi):**
     - Jelaskan dalam 1 paragraf singkat bahwa pada tiket berisiko Medium/High (Auth, Migrasi/Mutasi DB, API/Payment, State Kompleks, atau Blast Radius $\ge 4$ berkas) maupun saat memicu flag `--adversarial` di `/plan` & `/audit`, AI akan memanggil **Sub-Agent Read-Only bawaan IDE** (`invoke_subagent`) untuk meninjau celah dari 3 lensa (*Saboteur*, *New Hire*, *Security Auditor*) lalu menerjemahkannya dengan nada ramah Mentor. **Tidak ada instalasi atau konfigurasi apa pun** yang dibutuhkan mahasiswa; pada IDE tanpa dukungan sub-agent, sistem otomatis berjalan dalam mode *Graceful Fallback* sekuensial tanpa error.
- **Pertanyaan Keputusan:** Tanyakan: *"Apakah Anda ingin saya membuatkan file `ONBOARDING.md` nantinya, yang berisi panduan copy-paste langkah demi langkah bagi tim tentang verifikasi Python 3.8+, setup LSP, MCP, serta kakas spesifik stack proyek kita untuk dieksekusi langsung di Epik 0?"*

**Fase 4.5: Penguncian Komitmen (The Architect's Oath)**
- **Aksi:** Rangkum seluruh kesepakatan (Tahap 1-4). Tegaskan bahwa kedisiplinan ini akan mengunci repositori.
- **Pertanyaan Keputusan:** *"Apakah Anda siap memberikan otorisasi kepada saya untuk memulai TAHAP 5 (Injeksi Fisik), di mana saya akan menciptakan seluruh file konstitusi dan onboarding secara nyata ke repositori Anda?"*
