---
forge_version: "{{FORGE_VERSION}}"
forged_at: "{{FORGED_AT}}"
project_name: "{{PROJECT_NAME}}"
---
# MASTER RULES: {{PROJECT_NAME}}

> 🚨 **HUKUM TERTINGGI REPOSITORI INI**
> Dokumen ini adalah konstitusi absolut. AI yang beroperasi di repositori ini WAJIB mematuhi seluruh pasal di bawah ini tanpa kecuali. Setiap interaksi AI harus tunduk pada *Two-Gateway Pipeline*.
>
> ⚙️ **META-RULE MUTLAK (KENDALI KOGNITIF & ANTI-HALUSINASI):**
> 1. **Algoritma State-Machine, Bukan Referensi Opsional:** AI WAJIB memperlakukan seluruh file `<SKILL>` yang dimuat sebagai algoritma *State-Machine* harfiah. Dilarang memperlakukan instruksi SOP iteratif sebagai teks referensi santai atau melompati tahapan (*state jumping*).
> 2. **LSP Tool-First Audit:** AI **DIHARAMKAN** merender jawaban naratif/analisis arsitektur sebelum secara fisik mengeksekusi *tool* eksplorasi jika SOP meminta Audit. Prioritaskan penggunaan MCP `agent-lsp` (`find_symbol`, `get_tests_for_file`, `go_to_definition`) sebagai pelacak struktur utama (jauh lebih presisi dibanding sekadar *grep* teks). Dilarang menebak ketersediaan komponen/modul tanpa verifikasi fisik.
> 3. **Circuit Breaker & Hard Stops:** AI WAJIB menaati peringatan **HARD STOP** pada instruksi skill iteratif. AI harus menahan diri dari menyambung jawaban (*context bleed*) dan harus mutlak berhenti hingga mendapat konfirmasi/ACC resmi dari developer.

## 1. Identitas Proyek
- **Domain Bisnis:** {{BUSINESS_DOMAIN_SUMMARY}}
- **Tech Stack:** {{TECH_STACK_SUMMARY}}

## 2. Kedisiplinan AI & Pipeline Eksekusi
- **Otoritas:** AI adalah eksekutor dan mentor, Developer adalah Tech Lead. AI tidak boleh mengambil keputusan arsitektural sepihak tanpa memberikan opsi.
- **Gerbang Hulu (`/edeate`):** DILARANG merancang database atau API jika fitur belum didefinisikan secara konseptual melalui `/edeate`. Seluruh sesi `/edeate` wajib berpijak pada daftar Epik di `DEVELOPMENT_ROADMAP.md`. Satu sesi `/edeate` menghasilkan TEPAT SATU Tiket Level 3 terukur dan menautkan nomor tiket pada sub-poin terkait di `DEVELOPMENT_ROADMAP.md` (status: `- [ ] (Issue #[Nomor])`) tanpa mencentang tanda selesai. AI DILARANG KERAS menulis kode produksi, membuat skema database, atau menawarkan Pull Request otomatis di Gerbang Hulu.
- **Gerbang Hilir:** DILARANG memberikan kode implementasi masif (di atas 50 baris) jika developer belum menggunakan `/plan` untuk merumuskan langkah isolasi. Seluruh eksekusi kode wajib dimulai dengan `/grill-me`.

## 3. Hukum Pengujian (Testing)
- **Tingkat Komitmen:** {{TDD_STRICTNESS_DECISION}}
- **Aturan Praktis:** (Contoh: AI dilarang menulis kode produksi sebelum tes ditulis).
- **Four-Tier Quality Gate & Tri-Track Routing (Khusus Audit):**
  1. *Tier 1 (Linting):* Oxlint / ESLint 0 error dan 0 warning.
  2. *Tier 2 (Logic Tests):* Unit/Integration logic test passing 100%.
  3. *Tier 3 (Production Bundler):* Build produksi sukses dengan Exit Code 0.
  4. *Tier 4 (Visual Smoke & Actionability Gate via Playwright MCP):*
     - **Jalur 1: Pure Backend (Zero UI Footprint):** Otomatis BYPASS Tier 4 (tanpa Playwright, tanpa tangkapan layar).
     - **Jalur 2: Frontend Refactor / Logic-Only (Zero Visual Delta):** Static verification + Mandat Checklist Verifikasi Manual Manusia (Human-in-the-Loop Smoke Checklist).
     - **Jalur 3: Active Visual & Interactive UI (Active Visual Delta):** Wajib eksekusi Playwright + Mandat Penjabaran Bukti Visual Fisik (In-Chat Visual Evidence) mencakup multi-viewport (Desktop & Mobile) serta Light/Dark mode dengan observasi tata letak riil.
- **Hukum Anti-Kebutaan Visual & Metrik Geometri (Anti-Visual Blindness Protocol):**
  * **Viewport-First Screenshot (`1280 × 680` Real Inner-Viewport):** Haram menggunakan `element.screenshot()` terisolasi sebagai bukti utama tata letak. Wajib menggunakan `page.screenshot({ fullPage: false })` pada ukuran ruang baca bersih laptop nyata (`1280 × 680` atau `1366 × 680`) dan mobile (`375 × 667`) agar batas *above-the-fold*, tinggi *Sticky Navbar*, dan seksi tetangga terlihat utuh.
  * **Zero Test-Tampering Law:** Haram memanipulasi gaya produksi di dalam skrip tes (seperti mengubah `header.style.position = 'static'` atau menyembunyikan elemen via `page.evaluate()`) demi mengakali tangkapan layar.
  * **Real Anchor-Click & Sticky Collision Gate:** Wajib menguji klik nyata pada tautan navigasi (`header a[href^="#"]`) dan memastikan bagian atas seksi tidak tertelan *Sticky Navbar*.
  * **Metrik Geometri Sebelum Opini:** AI dilarang menyimpulkan keselarasan tampilan hanya dari pencocokan semantik. Rasio wadah wajib selaras dengan rasio asli gambar (`naturalWidth/naturalHeight`) untuk mencegah sayap putih (*pillarbox*).
  * **Uji Dua Tema Ekstrem (Dual-Theme Bleed):** Verifikasi tangkapan layar elemen pada Light Mode dan Dark Mode untuk mendeteksi balok semen kontras tak diinginkan.
  * **Penjabaran Bukti Nyata di Obrolan:** Pada tiket dengan perubahan visual, AI wajib menyertakan tangkapan layar lokal dan observasi visual konkret di respons audit, bukan sekadar menyatakan exit code 0.
  * **Penyelamat Laptop Fresh Clone (Graceful Fallback):** Jika lingkungan lokal belum memiliki Playwright / Chromium, AI dilarang membatalkan audit atau memblokir PR; AI wajib beralih ke inspeksi kode statis (*conditional unmount & adaptive bounds*) dengan catatan edukatif ramah.

## 4. Standar Kode & Kualitas
- **Ketegasan Audit:** {{CODE_AUDIT_STRICTNESS_DECISION}}
- **Protokol Matriks Enterprise (Contextual DNA):** Setiap kali AI memberikan rekomendasi arsitektur, menjawab pertanyaan, atau merancang struktur, AI **WAJIB** mengevaluasinya berdasarkan 5 Dimensi Enterprise berikut secara *proporsional* (jangan menceramahi developer pada tugas sepele, namun pantang kompromi pada fitur inti):
  1. **Arsitektur Skala Besar:** (*Soft Delete, Audit Trails, Race Conditions, Rate Limiting, Observability*).
  2. **Kebersihan Struktur:** (*Separation of Concerns, anti-God Component, zero dead-code*).
  3. **Keamanan & Integritas:** (*Otorisasi terpusat, validasi skema/payload mutasi, Database Transactions*).
  4. **Performa Runtime:** (*Anti N+1 Query, cegah memory bloat, optimasi letak Client/Server boundaries*).
  5. **UX & Stabilitas:** (*Graceful Degradation/Error Boundaries, cegah layar putih, standar A11y*).

## 5. Hukum Panca Indera AI (MCP & LSP Policy)

<!-- GENERATION_DIRECTIVE: MCP_POLICY_SECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INSTRUKSI UNTUK AI TAHAP 5 (INJEKSI FISIK):

Bagian ini TIDAK BOLEH diisi dengan placeholder variabel.
AI WAJIB MENULIS SENDIRI isi pasal ini berdasarkan keputusan
developer di Fase 4.1 (Katalog Panca Indera).

STRUKTUR YANG HARUS DIIKUTI:

### 5.1 MCP yang Diotorisasi
[Daftar MCP yang dipilih developer, beserta fungsinya]

### 5.2 Mandat Penggunaan (Kapan WAJIB Dipanggil)
[Untuk setiap MCP yang diotorisasi, tuliskan aturan kapan
AI WAJIB memanggilnya. Contoh: "Jika audit melibatkan
struktur database, AI WAJIB menggunakan MCP MySQL
(mysql_describe_table) dan DILARANG menebak dari migrasi."]

### 5.3 MCP yang DITOLAK & Konsekuensinya
[Daftar MCP yang developer tolak. Untuk setiap penolakan,
tuliskan kompensasi manual yang harus dilakukan. Contoh:
"MCP GitHub DITOLAK → AI dilarang membuat PR otomatis,
wajib mencetak draf PR dalam blok markdown untuk disalin
manual oleh developer."]

CATATAN: Jika developer mengotorisasi semua rekomendasi,
bagian 5.3 boleh dikosongkan dengan catatan "Semua MCP
diotorisasi. Tidak ada pembatasan."
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-->

## 6. Protokol Pedagogi & Kode Etik Mentor Arsitek (WHO — Terpisah di `.agents/rules/PERSONA_MENTOR.md`)
Seluruh 8 Hukum Mutlak Pedagogi & Kode Etik *Kakak Senior / Principal Mentor* (*Anti-Strawman & Deferred Recommendation*, *2-Ketukan*, *Sisi Gelap & Biaya Laten*, *Student Empowerment Gate*, *Grounded Reality Gate*, *Curiosity Hook & Tech Lead Bridge*, *Bottom Line First*, dan *Confidence Tagging 🟢/🟡/🔴*) telah dipisahkan secara utuh (*100% verbatim*) ke berkas rule *Always-On* mandiri **`.agents/rules/PERSONA_MENTOR.md`** agar terlindungi saat aturan teknis diperbarui melalui `/forge-update`. Kedua dokumen (`MASTER_RULES.md` sebagai *HOW* dan `PERSONA_MENTOR.md` sebagai *WHO*) berlaku serempak dan sama-sama mengikat seluruh interaksi AI di repositori ini.

## 7. Standar Tiket GitHub Issue V2 (7 Pilar Defensif)
Seluruh tiket GitHub Issue yang diterbitkan dari `/edeate` WAJIB mengadopsi 7 pilar defensif:
1. **Identitas Tiket & Panduan Branch:** Nomor issue target, pola penamaan branch resmi (`<prefix>/issue-<nomor>-<nama>`), domain modul, kondisi eksisting faktual, dan hasil akhir terukur.
2. **Matriks Spesifikasi Domain:** Pemetaan tegas kontrak sistem sesuai jenis tiket:
   - *Tiket Backend / Data Mutation:* **Matriks Otorisasi & Hak Akses (Policy Matrix)** (Admin, Owner, Tamu per aksi).
   - *Tiket Frontend / Komponen:* **Matriks Interaksi & Status UI (UI State Matrix)** (State, Mode Hidrasi, A11y, Responsivitas).
   - *Tiket Fondasi / Toolchain:* **Matriks NFR & Batasan Kompatibilitas** (Metrik Target, Config Impact, Verification Command).
3. **Batasan Bisnis & Integritas Data (Business Invariants):** Anti-spoofing server injection, immutability kolom kekal, penanganan race conditions, dan sanitasi data sensitif (OWASP).
4. **Peta Berkas Terdampak (Blast Radius):** Pemisahan tegas antara berkas eksisting yang dimodifikasi (waspada regresi) vs berkas baru yang dibuat.
5. **Spesifikasi Teknis Defensif:** Rincian implementasi yang menyatukan aksi koding dengan alasan keamanan/defensifnya.
6. **Jaring Pengaman Uji (Definition of Done):** Checklist linter 100%, automated tests pass, zero N+1 queries, dan perlindungan error trace.
7. **Poin Kunci Pemahaman Teknis (Technical Talking Points):** Narasi alasan rekayasa (*The "Why"*) untuk bekal presentasi dan pemahaman mahasiswa.
