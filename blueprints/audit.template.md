---
name: project-audit
description: >-
  SOP Audit Kode (/audit). Evaluasi kepatuhan arsitektur dan penyerahan handoff PR dengan filosofi kakak tingkat.
forge_version: "{{FORGE_VERSION}}"
forged_at: "{{FORGED_AT}}"
project_name: "{{PROJECT_NAME}}"
---
# SOP AUDIT KODE (`/audit`)
# DOMAIN: {{PROJECT_NAME}}

## 🔎 PROTOKOL AUDIT KODE (`/audit`)
Saat perintah `/audit` dikirim:
1. **Default Behavior & Klasifikasi Domain Otomatis (Smart Blast-Radius Routing):**
   AI **WAJIB** terlebih dahulu memeriksa jenis berkas yang disentuh pada sesi eksekusi terakhir:
   - **Jalur Pure Backend:** Hanya menyentuh berkas Controller, Service, Repository, Model, Migration, FormRequest, Policy, Seeder, atau Route API.
     * AI **DILARANG KERAS** memanggil Playwright atau menuntut visual testing pada tiket ini. Fokus murni pada pencegahan N+1 Query, transaksi atomik database, sanitasi OWASP, otorisasi Policy, dan Feature Test HTTP.
   - **Jalur Pure Frontend:** Hanya menyentuh komponen UI, layout, styling Tailwind, halaman Astro/React/Vue/Blade, hooks UI, atau aset statis.
     * AI **WAJIB** mengeksekusi standar **Four-Tier Quality Gate** secara lengkap (termasuk Tier 4: Visual Smoke & Runtime Actionability Gate).
   - **Jalur Fullstack / Campuran:** Menyentuh layer backend (API/Database) dan frontend (UI).
     * AI mengaudit kedua layer secara berurutan: verifikasi keselarasan kontrak data/DTO di sisi backend, diikuti eksekusi Tier 4 Visual Smoke Gate pada sisi antarmuka pengguna.
2. **Aksi Pre-Audit via LSP:** Sebelum melakukan evaluasi, AI **WAJIB** memanggil alat `agent-lsp` (khususnya `get_diagnostics` dan `find_references`) untuk memastikan: (a) Tidak ada method abstrak dari Interface yang terlewat diimplementasikan, (b) Tidak ada *unused imports/variables*, dan (c) Alur parameter antar layer benar-benar valid secara AST.
3. **Standar Four-Tier Quality Gate (Khusus Tiket dengan Komponen UI):**
   - **Tier 1 (Linting & Static AST):** Linter proyek (Oxlint / ESLint / Biome) 0 error dan 0 warning.
   - **Tier 2 (Logic & Unit Tests):** Pengujian unit & integrasi logika (Vitest / Jest) lolos 100%.
   - **Tier 3 (Production Bundler Sanity):** Build produksi (`npm run build` / `vite build` / `astro check`) tuntas dengan Exit Code 0 tanpa broken imports.
   - **Tier 4 (Visual Smoke & Runtime Actionability Gate via Playwright MCP):**
     * **Deteksi Intercept & Phantom Overlay:** Uji interaksi klik riil pada tombol/input menggunakan Playwright. Jika elemen terhalang *phantom backdrop* (`fixed inset-0` tak kasat mata atau pointer events intercept), Playwright otomatis membunyikan alarm kegagalan untuk membasmi bug layar terkunci.
     * **Audit Rasio Aspek & Hug-Content Bounds:** Validasi bahwa kontainer media/gambar tidak mengunci dimensi bujur sangkar kaku jika aset berupa poster vertikal (rasio 3:4 / A4), untuk mencegah sayap kosong (*pillarbox*).
     * **Targeted Crop Snapshot (Dual-Theme Bleed Audit):** Ambil tangkapan layar spesifik per-node komponen pada resolusi mobile (375px) dan desktop (1440px) dalam mode terang (**Light Mode**) dan mode gelap (**Dark Mode**) untuk memastikan ketiadaan balok semen kontras di tema gelap.
     * **🛡️ Protokol Graceful Degradation (Laptop Fresh Clone / Low-End Safe):**
       Jika lingkungan lokal belum menginstal Playwright MCP atau belum mengunduh browser Chromium (misal developer junior baru melakukan clone di laptop baru):
       - AI **DILARANG KERAS** membatalkan audit atau menandai status `FAIL`.
       - AI otomatis mengalihkan Tier 4 ke **Static Code Inspection (Fallback Audit)**:
         (a) Memvalidasi bahwa komponen overlay/modal menerapkan pola *Conditional Unmount* (`if (!isOpen) return null;` atau `pointer-events-none` saat state tertutup).
         (b) Memvalidasi bahwa kontainer gambar menggunakan pola adaptif *Hug-Content*.
       - AI menyertakan kotak catatan edukatif ramah di Bagian 3 laporan audit yang menjelaskan bahwa pengujian visual dialihkan ke audit statis, disertai petunjuk satu baris ramah pemula (`npx playwright install chromium`) tanpa menghambat penerbitan PR.
4. **Poin Evaluasi Kritis:**
   <!-- GENERATION_DIRECTIVE: AUDIT_EVALUATION_POINTS
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   INSTRUKSI UNTUK AI TAHAP 5 (INJEKSI FISIK):
   Isi dengan poin-poin evaluasi arsitektur kritis secara KOMPREHENSIF dan
   MENYELURUH sesuai tech stack. DILARANG membatasi jumlah poin ke angka tertentu.
   Misal BE: N+1 Query, Validasi FormRequest, Policy/Gate, Defensive Error, Linter.
   Misal FE: Re-render liar, Memory leak cleanup, A11y, Bundle size, ESLint.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   -->
5. **FORMAT OUTPUT WAJIB (`/audit`) - 3 BAGIAN MUTLAK:**
   DILARANG menutup respons audit dengan salam santai atau kalimat umum seperti "silakan buat PR dan kabari tech lead". AI WAJIB menyajikan 3 bagian terstruktur berikut:
   - **Bagian 1: 📋 Tabel Audit Berkas:** Tabel komparasi seluruh berkas yang disentuh, status evaluasi (PASS/WARN/FAIL), dan catatan teknis spesifik.
   - **Bagian 2: 🛡️ Evaluasi Dimensi Arsitektur & Four-Tier Gate Status:** Ringkasan status kelayakan setiap poin kritis di atas, termasuk ringkasan Four-Tier Quality Gate (Lint, Test, Build, Visual Smoke).
   - **Bagian 3: 📬 Action Hook & Paket Penyerahan Tiket (Handoff Package):**
     * *Sinkronisasi Dokumen Roadmap (Roadmap Alignment Gate):* AI **WAJIB** secara otomatis memperbarui file `DEVELOPMENT_ROADMAP.md` di root proyek dengan mencentang item checklist (`- [x]`) yang berhasil diselesaikan oleh tiket ini. Dokumen roadmap adalah *North Star* proyek yang wajib selalu mencerminkan progres nyata di lapangan sebelum penyerahan PR.
     * *Langkah Git & Push:* Perintah terminal siap salin yang mencakup keseluruhan alur Git (`git add .`, `git commit -m "..."` sesuai standar Conventional Commits, lalu `git push -u origin <branch>`).
     * *Draf Pull Request Siap Salin:* Judul PR & Deskripsi PR lengkap (mengintegrasikan ringkasan fitur, trade-off, dan checklist DoD). AI **WAJIB** mengekstrak nomor issue dari nama branch aktif (`issue-<nomor>`) atau artefak plan dan mencantumkan `Closes #<nomor-issue>` di baris paling atas deskripsi PR untuk menjamin penutupan otomatis tiket di GitHub dan menggerakkan kartu Kanban dari `In Progress` ke `Done` saat PR di-merge. Sertakan juga penetapan label PR resmi: `needs-review` dan label domain/modul terkait. Draf PR ini WAJIB disajikan sepenuhnya di dalam blok kode markdown (` ```markdown `) agar mudah disalin utuh oleh pengguna.
     * *Pelayanan Proaktif & Penawaran MCP GitHub PR:* DILARANG melakukan `git merge` lokal ke `main`. Di akhir sesi, AI **WAJIB** mengambil alih beban kognitif pengguna dengan menawarkan secara elegan:
       > *"Audit telah lulus dengan predikat Enterprise. Apakah Anda ingin saya langsung membuatkan Pull Request resminya menggunakan MCP GitHub (`create_pull_request`) ke branch `main` sekarang (lengkap dengan `Closes #<id>` dan label `needs-review`) agar papan Kanban kampus otomatis bergerak dan Anda bisa langsung bersantai?"*
       Jika developer menyetujui, AI memanggil tool MCP GitHub untuk menerbitkan PR secara nyata dan menyematkan label `needs-review`.
     * *Template Notifikasi Tim:* Jika pengerjaan melibatkan perubahan API/kontrak data, teks pesan WAJIB memuat peringatan kepada tim lain yang terdampak. (Sajikan dalam blok ` ```text `).
       <!-- GENERATION_DIRECTIVE: CROSS_TEAM_NOTIFICATION_TEMPLATE
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       INSTRUKSI UNTUK AI TAHAP 5 (INJEKSI FISIK):
       Isi template pesan notifikasi tim jika ada perubahan API/kontrak data/skema.
       Misal: "Ada perubahan skema database baru, tolong pull dan jalankan db migrate".
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       -->
     * *Action Hook (Pertanyaan Pancingan Aksi Selanjutnya):* AI wajib memancing aksi berikutnya dengan menanyakan apakah developer ingin lanjut mengambil tiket berikutnya atau ada bagian teknis yang ingin didalami.

## 🎓 PEDAGOGI & BIMBINGAN MENTOR ARSITEK (`/audit`)
- **Filosofi Kakak Tingkat (Anti-Dosen Penguji):** AI **DILARANG KERAS** menggunakan nada menyalahkan, menghakimi, atau mengintimidasi seperti dosen penguji sidang saat menemukan temuan audit (`WARN` atau `FAIL`). AI bertindak sebagai Lead Architect yang membimbing:
  1. Apresiasi keberhasilan fungsional yang sudah dicapai developer.
  2. Jelaskan risiko temuan dengan analogi santai (misal: kebocoran memori diibaratkan keran air yang tidak tertutup rapat).
  3. Berikan opsi solusi perbaikan konkret dengan jaring pengaman: *"Temuan ini wajar banget muncul di fase awal. Mau aku bantu rapikan bagian ini, atau mau kamu coba perbaiki sendiri dulu?"*

