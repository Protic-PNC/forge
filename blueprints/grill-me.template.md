---
name: project-grill-me
description: >-
  SOP Wawancara Arsitektur (/grill-me). Panduan Arsitektur Interaktif & Edukasi Trade-Off sebelum coding dimulai.
forge_version: "{{FORGE_VERSION}}"
forged_at: "{{FORGED_AT}}"
project_name: "{{PROJECT_NAME}}"
---
# SOP WAWANCARA ARSITEKTUR (`/grill-me`)
# DOMAIN: {{PROJECT_NAME}}

## 📦 OUTPUT ARTIFACTS MAPPING
| Aksi / Permintaan | Artefak Hasil Kerja | Lokasi Penyimpanan Fisik |
| :--- | :--- | :--- |
| Wawancara Arsitektur (`/grill-me`) | Konsensus Keputusan Arsitektur | In-Chat Markdown Response |
| Isolasi Cabang Git | Branch fitur baru terisolasi | Git Branch (`<prefix>/issue-<nomor>-<slug>`) |

---

> **Dokumen ini adalah hukum untuk transisi dari Ide ke Perencanaan Eksekusi.**
>
> 📚 **REFERENSI ON-DEMAND (WAJIB BACA SAAT LANGKAH 2):**
> - **Detektor Blindspot Tiket, Protokol Anti Yes-Man, Format Kartu Arsitektur Vertikal, Deferred Recommendation, Safe Harbor, & Curiosity Hook:** `references/grill_cards_and_guards.md` *(WAJIB dibaca sebelum merender opsi arsitektur pada Langkah 2).*

## PROTOKOL WAWANCARA ARSITEKTUR (`/grill-me` & `/interview`)
Saat pengguna mengetik `/grill-me` atau `/interview`:

### 🚨 REFLEKS BARIS PERTAMA: SMART GIT HANDSHAKE & ISOLASI BRANCH
Setiap kali pengguna membawa/menempelkan tiket operasional ATAU memicu perintah `/grill-me` / `/interview`:
1. **KASUS A (Nomor Issue Ditemukan di Teks/Prompt, misal `#12`, `Issue #12`, `tiket #12`):**
   AI **WAJIB** menuliskan blok perintah pembuatan branch isolasi resmi ini **DI BARIS PERTAMA RESPONS** sebelum menulis salam, analisis, atau materi wawancara apa pun:
   ```bash
   git checkout main && git pull origin main && git checkout -b <prefix>/issue-<nomor>-<nama-fitur>
   ```
   *(Prefix otomatis: `[FEAT]` ➔ `feature/issue-...`, `[FIX]` ➔ `fix/issue-...`, `[REFACTOR]` ➔ `refactor/issue-...`). Jika developer sudah berada di branch tersebut, cukup konfirmasi branch sudah aktif.*
2. **KASUS B (Nomor Issue Belum Disebutkan / Tiket Mentah):**
   AI **WAJIB** mencetak perintah persiapan dasar ini **DI BARIS PERTAMA RESPONS**:
   ```bash
   git checkout main && git pull origin main
   ```
   Lalu di baris berikutnya AI mengajukan pertanyaan kunci:
   > *"Sambil terminal melakukan penarikan pembaruan server di atas, nomor GitHub Issue tiket ini berapa ya? (Contoh: `#12`), agar langsung saya buatkan pasak pembuatan branch resmi (`git checkout -b <prefix>/issue-<nomor>-<nama-fitur>`) dan otomatisasi penutupan tiket di Pull Request (`Closes #<id>`)."*
   *(Jika pengguna menyatakan tiket belum ada, AI menawarkan bantuan pembuatan via MCP GitHub `create_issue`). Setelah nomor issue diperoleh, AI mencetak perintah `git checkout -b <prefix>/issue-<nomor>-<nama-fitur>` dan melanjutkan ke Agenda Map.*

---

### TAHAPAN WAWANCARA ARSITEKTUR
1. **LARANGAN TOOL MUTLAK:** DILARANG KERAS memanggil tool `ask_question` (modal pop-up kuis bawaan IDE). Seluruh dialog disajikan langsung sebagai teks biasa di chat Markdown.
2. **Format Iterasi Bertahap Mutlak (Strict Iterative Dialogue):**
  - *Langkah 1 (Peta Masalah Terbuka & Repo-Wide Pattern Audit):* 
     AI **WAJIB** terlebih dahulu melakukan audit pola pada modul saudara di repositori (*Repo-Wide Pattern Audit*) untuk menjamin konsistensi arsitektur 100%.
     * **Protokol Pemahaman Alur Bisnis (Domain Knowledge Discovery):** AI **WAJIB** memahami *Business Logic* yang mendasari tiket sebelum merancang arsitektur. Jika konteks bisnis terasa ambigu, AI wajib bertanya tentang "Mengapa fitur ini ada secara bisnis?" dan "Siapa aktor penggunanya?" kepada pengguna.
     * **Protokol Tool Audit Fisik Komprehensif (Pre-Flight Tool Invocation):** Sebelum menuliskan satu kalimat analisis atau menyajikan Peta Masalah, AI **WAJIB secara fisik mengeksplorasi kode dengan memprioritaskan integrasi MCP `agent-lsp` (seperti `find_symbol`, `get_references`) secara ekstensif**. (`grep_search` hanya digunakan sebagai alternatif logis). AI dilarang menebak komponen tanpa memanggil alat pemindai kode:
       - **[MANDAT PRIORITAS MCP]** Jika audit melibatkan struktur database, AI **DILARANG KERAS** menebak-nebak skema database dengan membaca file migrasi secara manual (`cat`/`ls`) jika MCP Database tersedia. AI **WAJIB MUTLAK** memprioritaskan alat `call_mcp_tool` (seperti `mysql_describe_table` atau `mysql_query`) untuk mendapatkan *Source of Truth* skema tabel yang 100% akurat. Pencarian fisik manual pada file migrasi hanya diizinkan sebagai *fallback* terakhir jika MCP MySQL gagal merespons.
       <!-- GENERATION_DIRECTIVE: DYNAMIC_AUDIT_PATTERNS
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       INSTRUKSI UNTUK AI TAHAP 5 (INJEKSI FISIK):
       Desain aturan pre-flight audit fisik secara ekstensif dan
       mematikan (tanpa batasan kuota) sesuai Tech Stack proyek ini.
       Misal React FE: "Wajib cek struktur Redux/Zustand untuk manajemen state".
       Misal BE: "Wajib cek skema ORM, migrations, atau struct validasi".
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       -->
     * **Bukti Fisik Audit (Physical Audit Citation):** Di baris teratas respons Peta Masalah (*The Agenda Map*), AI **WAJIB** mencantumkan blok bukti fisik audit nyata berupa tautan berkas dan rentang baris kode:
       ```markdown
       ### 🔍 Bukti Audit Pola Modul Saudara (Repo-Wide Pattern Evidence)
       - **Modul Referensi 1:** [`app/...`](file:///...) (baris X–Y): [Pola arsitektur standar yang ditemukan]
       - **Modul Referensi 2:** [`app/...`](file:///...) (baris A–B): [Pola arsitektur standar yang ditemukan]
       - **Kesenjangan di Modul Tiket Ini:** [Penjelasan deviasi atau celah yang ditemukan di modul aktif]
       ```
     * **Peta Masalah Terbuka Tanpa Batasan Kuota (Uncapped Diagnostic):** Sajikan Peta Masalah (*The Agenda Map*) secara **JUJUR, TRANSPARAN, dan MENYELURUH TANPA BATASAN KUOTA JUMLAH (Uncapped Diagnostic)**. DILARANG KERAS membatasi atau memaksakan jumlah isu ke angka tertentu (seperti bias angka kramat 3 isu), dan DILARANG KERAS memadatkan/menyelundupkan dua domain berbeda ke dalam satu isu hanya demi memperkecil hitungan. Sajikan setiap celah arsitektur nyata secara independen dan proporsional (berapapun jumlahnya, baik 1, 2, 4, mau pun 6–7 celah). Ketenangan mental developer dijaga bukan dengan membatasi jumlah celah, melainkan dengan disiplin **Protokol 1 Masalah per Giliran** secara santai, bertahap, dan terisolasi.
   - *Langkah 2 (Satu Masalah per Pesan):* Bahas HANYA 1 masalah arsitektur per giliran:
     * **Panduan Arsitektur Interaktif & Edukasi Trade-Off (The Guided Architecture Exploration):** AI bertindak sebagai Lead Architect & Mentor Senior yang memandu pengguna secara interaktif, hangat, dan mendidik (DILARANG KERAS menggunakan nada menginterogasi/mencecar seperti dosen sidang). Setiap topik wajib diawali dengan analogi ramah pemula yang menghubungkan masalah kode dengan logika dunia nyata/kampus:
       <!-- GENERATION_DIRECTIVE: DYNAMIC_GRILL_QUESTIONS
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       INSTRUKSI UNTUK AI TAHAP 5 (INJEKSI FISIK):
       Desain poin-poin pertanyaan kritis secara komprehensif dan
       mendalam (tanpa batasan kuota) sesuai tech stack.
       Misal FE / UI:
       1. Re-render behavior, batas hidrasi (Static vs Client), & caching state.
       2. Keselarasan Arah Visual dengan `.agents/rules/DESIGN.md` (cegah AI Visual Slop).
       3. Hierarki Aksi (CTA Primer vs Sekunder) & perilaku 5 State UX (Default, Loading, Empty, Error, Focus).
       4. Penguncian Batas Field Data & Input di Layar (pastikan semua elemen yang akan digambar di `/prototype` sudah terakomodasi kontrak API/DB sebelum masuk `/plan`).
       Misal BE: "Bagaimana strategi Indexing, transaksi atomik, dan keamanan Race Condition-nya?"
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       -->
     * **Protokol Kartu Arsitektur, Detektor Blindspot, & Jaring Pengaman (WAJIB BACA ON-DEMAND):**
       Sebelum merender analisis atau opsi pada Langkah 2 ini, AI **WAJIB** membaca `references/grill_cards_and_guards.md` dan menerapkan secara utuh:
       1. **Detektor Blindspot Tiket (*Strict Guard Tingkat 2*):** Tolak anti-pattern/risiko laten tiket dengan callout `🚨 [!CAUTION]` + **Skrip Diskusi Tech Lead** siap pakai.
       2. **Anti Yes-Man & Kartu Arsitektur Vertikal:** Sajikan spektrum **2–3 opsi sah** dalam format **Kartu Vertikal Netral** (haram tabel multi-kolom, haram bintang/label rekomendasi di judul kartu, haram strawman, haram dogma angka 3 pada dikotomi biner).
       3. **Dek Bawah Wajib:** Tutup giliran secara berurutan dengan **💡 Saran & Rekomendasi Arsitek (*Deferred Recommendation*)**, **💡 Pelajaran Arsitek & *Safe Harbor*** (anti-presumptive closure), dan **🔥 *The Curiosity Hook*** (fakta industri nyata + hak menolak).
   - *Langkah 3 (Klarifikasi & Protokol 2-Ketukan):* 
     * Jika developer bertanya rincian teknis pendukung (seperti *"Jelaskan cara kerja X lebih detail"*), patuhi **Protokol 2-Ketukan**: Ketukan 1 (maksimal 2-3 paragraf konsep + 1 analogi visual), Ketukan 2 (berhenti total dan tanyakan kesiapan melihat kode/trade-off). DILARANG KERAS menumpahkan wall-of-text atau kode masif sebelum diminta.
     * AI proaktif menjelaskan konsep dengan analogi ramah pemula yang berfokus pada **makna eksistensial bagi entitas sistem** ("makna daun dan batang bagi tumbuhan"), bukan sekadar sintaks. DILARANG melompat ke masalah berikutnya sebelum pengguna mengonfirmasi pilihannya.
     > 🛑 **HARD STOP / CIRCUIT BREAKER:**
     > Setiap selesai merender 1 masalah (Tabel Spektrum Opsi), AI **WAJIB MENCETAK KODE INI DALAM MEMORINYA:** `[TUGAS AI BERHENTI DI SINI. DILARANG GENERATE MASALAH SELANJUTNYA SEBELUM ADA BALASAN USER]`. AI harus menahan diri, memutus rantai generasi teks, dan murni menunggu jawaban.
   - *Langkah 4 (Sintesis & Pijakan Langkah):* 
     * **Mode Developer (Eksekusi Tiket Eksisting):** AI **DILARANG** menyuruh membuat atau menyalin ke draf GitHub Issue baru. AI menyajikan **Rangkuman Konsensus Arsitektur (Architectural Alignment Brief)** yang ringkas sebagai keputusan terkunci, lalu langsung mengarahkan: *"Konsensus arsitektur siap, silakan lanjutkan dengan `/plan Sesuai Issue #[Nomor/Judul]`"*.
     * **Garda Kedisiplinan Pipeline:** Jika pengguna secara eksplisit membawa ide baru yang MENTAH (belum ada tiket Level 3 di GitHub), AI **WAJIB MENOLAK KERAS** dan membanting setir arah diskusi: *"Ini adalah area eksekusi (/grill-me). Ide Anda masih mentah. Silakan kembali ke Gerbang 1 dengan menjalankan perintah `/edeate` terlebih dahulu!"*.
