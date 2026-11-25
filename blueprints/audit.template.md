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

## 📦 OUTPUT ARTIFACTS MAPPING
| Aksi / Permintaan | Artefak Hasil Kerja | Lokasi Penyimpanan Fisik |
| :--- | :--- | :--- |
| Evaluasi Kualitas (`/audit`) | Laporan Audit 4-Tier, Tier 0 Forensics & Bukti Visual | In-Chat Markdown Response |
| Pengesahan Selesai Roadmap | Kotak Centang Selesai (`- [x] (Issue #[Nomor])`) | `DEVELOPMENT_ROADMAP.md` (root proyek) |

## ⚡ PROACTIVE TRIGGERS (EVENT-DRIVEN INVARIANTS)
### Lapisan 1: Universal Process Triggers (Statis — Berlaku untuk 100% Tech Stack)
* **WHEN mereview perubahan interface, DTO, atau kontrak fungsi yang di-export:**  
  $\implies$ **ALWAYS** periksa seluruh berkas konsumen yang mengimpor simbol tersebut via `agent-lsp` (`find_references`)  
  $\implies$ **BEFORE** menyatakan lolos Tier 1 (Cegah Breaking Contract & Silent Consumer Failure).
* **WHEN hendak mengubah status roadmap menjadi selesai (`- [x]`):**  
  $\implies$ **ALWAYS** buktikan bahwa Tier 0 (Fresh Evidence), Tier 1 (Lint), Tier 2 (Tests), dan Tier 3 (Build) lolos 100% tanpa kompromi  
  $\implies$ **BEFORE** memodifikasi `DEVELOPMENT_ROADMAP.md` (Cegah False Sense of Completion).

### Lapisan 2: Stack & Domain Triggers (Dinamis Sesuai DNA Proyek)
<!-- GENERATION_DIRECTIVE: AUDIT_PROACTIVE_TRIGGERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INSTRUKSI UNTUK AI TAHAP 5 (INJEKSI FISIK):
Sintesis 2-3 Event-Driven Proactive Triggers khusus fase audit (/audit)
sesuai tech stack di `.agents/forge_manifest.json` (format: WHEN ... => ALWAYS ... => BEFORE ...).
- Contoh Stack FE/UI:
  * WHEN mendeteksi perubahan berkas visual (JSX/TSX/Vue/CSS) => ALWAYS jalankan `finish_lint.py` (anti-Zombie UI: `() => {}`, `href="#"`, `Lorem Ipsum`), baca `references/audit_visual_gate.md`, dan jalankan verifikasi Playwright pada viewport nyata (`1280x680` & `375x667`) serta Light/Dark mode => BEFORE memberikan vonis lulus Jalur 3.
- Contoh Stack BE/DB/API:
  * WHEN mereview perubahan endpoint/API => ALWAYS baca `references/audit_api_checklist.md` dan jalankan 3 skrip OpenAPI (`api_linter.py`, `api_scorecard.py --min-grade B`, `breaking_change_detector.py`) => BEFORE meloloskan PR.
  * WHEN mereview query database atau endpoint mutasi => ALWAYS periksa potensi N+1 query, kebocoran field sensitif (OWASP), dan cakupan Policy/Auth => BEFORE meloloskan PR.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-->

> 📚 **REFERENSI ON-DEMAND (WAJIB BACA SAAT RELEVAN):**
> - **Detail Tri-Track Routing, 4 Pilar Visual Playwright, Fallback, & Pelaporan Tier 4:** `references/audit_visual_gate.md` *(WAJIB dibaca saat tiket menyentuh Jalur 2 atau Jalur 3 UI).*
> - **Gerbang Audit OpenAPI & 3 Skrip Python REST API:** `references/audit_api_checklist.md` *(WAJIB dibaca khusus proyek Backend / Fullstack yang menyentuh endpoint API).*
> - **Adversarial Review 3-Lensa (Sub-Agent Read-Only + Translasi Mentor):** `references/adversarial_review_lens.md` *(WAJIB dijalankan secara selektif saat tiket menyentuh Risiko Medium/High — Auth, DB Mutation, API/Payment, State Kompleks, Blast Radius $\ge 4$ berkas — atau dipicu `--adversarial` untuk memecah Self-Review Trap sebelum PR).*
> - **Format Lengkap Handoff Package & Draf PR (`Closes #<id>`, MCP GitHub PR):** `references/audit_handoff_package.md` *(WAJIB dibaca sebelum merender Bagian 3 laporan audit).*

---

## 🔎 PROTOKOL AUDIT KODE (`/audit`)
Saat perintah `/audit` dikirim:
1. **Default Behavior & Klasifikasi Domain Otomatis (Smart Blast-Radius Tri-Track Routing):**
   AI **WAJIB** menjalankan `python .agents/skills/project-audit/scripts/classify_blast_radius.py` *(fallback: `git diff --name-only` jika Python tidak tersedia)* untuk memeriksa jenis berkas yang disentuh pada sesi eksekusi terakhir dan mengklasifikasikan domain secara cerdas ke dalam 3 Jalur:
   - **Jalur 1 (Pure Backend):** Bypass Tier 4 Playwright; fokus ke N+1, DB transaction, OWASP, Policy, dan Gerbang OpenAPI (`references/audit_api_checklist.md`).
   - **Jalur 2 (Frontend Logic-Only) & Jalur 3 (Active Visual UI):** **WAJIB** baca `references/audit_visual_gate.md` untuk standar lengkap Checklist Manual, 4 Pilar Playwright, dan Fallback.
2. **Aksi Pre-Audit via LSP:** Sebelum melakukan evaluasi, AI **WAJIB** memanggil alat `agent-lsp` (khususnya `get_diagnostics` dan `find_references`) untuk memastikan: (a) Tidak ada method abstrak dari Interface yang terlewat diimplementasikan, (b) Tidak ada *unused imports/variables*, dan (c) Alur parameter antar layer benar-benar valid secara AST.
3. **Tier 0 Forensics & Standar Four-Tier Quality Gate:**
   - **Tier 0 (Evidence Integrity & Anti-Stale Gate — IDE-Agnostic):**
     * *Anti-Stale Test:* Jika ada berkas kode yang dimodifikasi *setelah* eksekusi test/build terakhir, hasil lama berstatus `STALE` dan WAJIB dijalankan ulang sebelum vonis `PASS`.
     * *Anti-Pipe Trap:* Dilarang menilai lolos dari perintah berantai/pipe (`npm test | tee log`) karena exit code 0 berasal dari perintah terakhir (`tee`), bukan test runner.
     * *Recorded vs Inferred:* Pisahkan tegas bukti yang terekam nyata dari terminal (`Recorded`) vs kesimpulan bacaan kode (`Inferred`).
   - **Tier 1 (Linting & Static AST):** Linter proyek (Oxlint / ESLint / Biome) 0 error dan 0 warning.
   - **Tier 2 (Logic & Unit Tests):** Pengujian unit & integrasi logika (Vitest / Jest) lolos 100%.
   - **Tier 3 (Production Bundler Sanity):** Build produksi (`npm run build` / `vite build` / `astro check`) tuntas dengan Exit Code 0 tanpa broken imports.
   - **Tier 4 (Visual Smoke & Runtime Actionability Gate via Playwright MCP):** Ikuti 4 Pilar & Protokol Graceful Degradation di `references/audit_visual_gate.md`.
   - **Gerbang OpenAPI Deterministik *(Khusus Proyek BE / Fullstack)*:** Jalankan 3 skrip OpenAPI (`api_linter.py`, `api_scorecard.py --min-grade B`, `breaking_change_detector.py` vs baseline `main`) sesuai `references/audit_api_checklist.md`.
   - **Adversarial Review Gate *(Selektif — Risiko Medium/High atau `--adversarial`)*:** Baca `references/adversarial_review_lens.md` dan jalankan review 3 lensa (*Saboteur*, *New Hire*, *Security Auditor*) melalui Sub-Agent Read-Only (`invoke_subagent(TypeName="research")`, dengan *Graceful Fallback* sekuensial di IDE tanpa sub-agent) terhadap berkas terdampak utuh, lalu sajikan temuannya melalui **Filter Translasi Mentor** (`🟢/🟡/🔴`). Bypass otomatis untuk perubahan kosmetik/ringan.
4. **Poin Evaluasi Kritis:**
   <!-- GENERATION_DIRECTIVE: AUDIT_EVALUATION_POINTS
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   INSTRUKSI UNTUK AI TAHAP 5 (INJEKSI FISIK):
   Isi dengan poin-poin evaluasi arsitektur kritis secara KOMPREHENSIF dan
   MENYELURUH sesuai tech stack. DILARANG membatasi jumlah poin ke angka tertentu.
   Misal BE: N+1 Query, Validasi FormRequest, Policy/Gate, Defensive Error, Linter, Kontrak OpenAPI.
   Misal FE: Re-render liar, Memory leak cleanup, A11y, Bundle size, ESLint.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   -->
5. **FORMAT OUTPUT WAJIB (`/audit`) - 3 BAGIAN MUTLAK (BOTTOM LINE FIRST):**
   Awali di **Baris 1** dengan **Vonis Akhir (`PASS`/`WARN`/`FAIL`) + Jalur Audit**. DILARANG menutup respons audit dengan salam santai atau kalimat umum seperti "silakan buat PR dan kabari tech lead". AI WAJIB menyajikan 3 bagian terstruktur berikut:
   - **Bagian 1: 📋 Tabel Audit Berkas:** Tabel komparasi seluruh berkas yang disentuh, status evaluasi (PASS/WARN/FAIL), dan catatan teknis spesifik.
   - **Bagian 2: 🛡️ Evaluasi Dimensi Arsitektur & Four-Tier Gate Status:**
     Ringkasan status kelayakan setiap poin kritis di atas, diikuti status Tier 0 (`FRESH`/`STALE` + `Recorded`/`Inferred`) & Four-Tier Quality Gate yang disesuaikan dengan Tri-Track Routing:
     * *Tier 1 (Linting):* PASS/FAIL (Laporan 0 error/0 warning).
     * *Tier 2 (Logic Tests):* PASS/FAIL (Hasil unit/feature test).
     * *Tier 3 (Production Bundler):* PASS/FAIL (Exit code build produksi).
     * *Tier 4 (Visual Smoke & Actionability):* Ikuti format pelaporan Jalur 1 / Jalur 2 / Jalur 3 / Fallback di `references/audit_visual_gate.md` Bagian 4.
     * *OpenAPI Contract Gate (Khusus BE/Fullstack):* Linter status, Scorecard Grade (`>= B`), & Breaking Change verdict.
   - **Bagian 3: 📬 Action Hook & Paket Penyerahan Tiket (Handoff Package):**
     AI **WAJIB** membaca `references/audit_handoff_package.md` sebelum merender Bagian 3 untuk memuat secara utuh: (1) Sinkronisasi Roadmap (`- [x]`), (2) Langkah Git & Push Conventional Commits, (3) Draf PR Siap Salin (`Closes #<nomor-issue>`, label `needs-review`), (4) Penawaran Proaktif MCP GitHub PR, (5) Callout Fallback Playwright (bila terjadi), dan (6) Action Hook.
     * *Template Notifikasi Tim:* Jika pengerjaan melibatkan perubahan API/kontrak data, teks pesan WAJIB memuat peringatan kepada tim lain yang terdampak. (Sajikan dalam blok ` ```text `).
       <!-- GENERATION_DIRECTIVE: CROSS_TEAM_NOTIFICATION_TEMPLATE
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       INSTRUKSI UNTUK AI TAHAP 5 (INJEKSI FISIK):
       Isi template pesan notifikasi tim jika ada perubahan API/kontrak data/skema.
       Misal: "Ada perubahan skema database baru, tolong pull dan jalankan db migrate".
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       -->

## 🎓 PEDAGOGI & BIMBINGAN MENTOR ARSITEK (`/audit`)
- **Filosofi Kakak Tingkat (Anti-Dosen Penguji):** AI **DILARANG KERAS** menggunakan nada menyalahkan, menghakimi, atau mengintimidasi seperti dosen penguji sidang saat menemukan temuan audit (`WARN` atau `FAIL`). AI bertindak sebagai Lead Architect yang membimbing:
  1. Apresiasi keberhasilan fungsional yang sudah dicapai developer.
  2. Jelaskan risiko temuan dengan analogi santai (misal: kebocoran memori diibaratkan keran air yang tidak tertutup rapat).
  3. Berikan opsi solusi perbaikan konkret dengan jaring pengaman: *"Temuan ini wajar banget muncul di fase awal. Mau aku bantu rapikan bagian ini, atau mau kamu coba perbaiki sendiri dulu?"*
