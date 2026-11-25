# SPESIFIKASI INJEKSI FISIK & BRANKAS DNA
**Direktori Rujukan On-Demand untuk Tahap 5 (`/forge-constitution`)**

---

## 🏗️ TAHAP 5: INJEKSI PROGRESIF (The Grand Scaffolding)

Jika otorisasi Tahap 4.4 diberikan, AI bertransformasi menjadi "Injector".

- **Artefak Ke-0 Mutlak: Brankas DNA Fisik (`.agents/forge_manifest.json`):**
  Sebelum mencetak berkas Markdown apa pun, AI **WAJIB MUTLAK** mencetak file `.agents/forge_manifest.json` ke disk lokal. File ini adalah *Physical Source of Truth* permanen yang menyimpan 100% keputusan DNA hasil wawancara Tahap 1–4, sehingga pembaruan di masa depan (`/forge-update`) tidak memerlukan AI menebak-nebak atau mengingat riwayat obrolan.
  Format wajib `.agents/forge_manifest.json`:
  ```json
  {
    "forge_version": "2.0.0",
    "forged_at": "YYYY-MM-DD",
    "project_name": "{{PROJECT_NAME}}",
    "dna": {
      "BUSINESS_DOMAIN_SUMMARY": "...",
      "TECH_STACK_SUMMARY": "...",
      "ACTORS_AND_ROLES_DESCRIPTION": "...",
      "SYSTEM_ARCHITECTURE_APPROACH": "...",
      "FRONTEND_BACKEND_SEPARATION_STRATEGY": "...",
      "SECURITY_AND_AUTHENTICATION_STRATEGY": "...",
      "BUSINESS_GAPS_AND_RESOLUTIONS": "...",
      "INFRASTRUCTURE_AND_3RD_PARTY_INTEGRATIONS": "...",
      "TDD_STRICTNESS_DECISION": "...",
      "CODE_AUDIT_STRICTNESS_DECISION": "...",
      "GIT_BRANCHING_STRATEGY_DECISION": "...",
      "PULL_REQUEST_APPROVAL_POLICY": "...",
      "VISUAL_BRAND_TONE": "... (Khusus Proyek FE/Fullstack, isi 'N/A - Pure Backend' jika tanpa UI)"
    },
    "directives": {
      "MCP_POLICY_SECTION": "...",
      "DYNAMIC_AUDIT_PATTERNS": "...",
      "DYNAMIC_GRILL_QUESTIONS": "...",
      "EXECUTION_HIERARCHY": "...",
      "ENTERPRISE_CODE_STANDARDS": "...",
      "DESIGN_SYSTEM_FOUNDATION": "... (Khusus Proyek FE/Fullstack)",
      "PLAN_PROACTIVE_TRIGGERS": "...",
      "EXECUTE_PROACTIVE_TRIGGERS": "...",
      "AUDIT_PROACTIVE_TRIGGERS": "...",
      "AUDIT_EVALUATION_POINTS": "...",
      "CROSS_TEAM_NOTIFICATION_TEMPLATE": "...",
      "PRODUCTION_CODE_LAYERS": "...",
      "MANDATORY_TEST_SCOPE": "...",
      "TEST_DATA_FIXTURE_STRATEGY": "..."
    }
  }
  ```

- **Protokol Metadata Versi (Version Stamping Terintegrasi):**
  Seluruh berkas blueprint di direktori `blueprints/` kini telah memiliki blok front-matter YAML bawaan di baris paling atas. Saat melakukan injeksi, AI **WAJIB** mensubstitusikan variabel metadata tersebut secara deterministik:
  - `{{FORGE_VERSION}}`: Diambil dari field `version` di file `plugin.json` Forge global.
  - `{{FORGED_AT}}`: Tanggal hari ini saat injeksi dilakukan (format `YYYY-MM-DD`).
  - `{{PROJECT_NAME}}`: Nama proyek yang didapatkan dari Tahap 1.
  
  Metadata ini digunakan oleh `/forge-update` untuk mendeteksi apakah konstitusi lokal perlu disinkronkan dengan versi Forge terbaru. AI **DILARANG KERAS** menghapus blok front-matter ini saat mencetak berkas apa pun.

- **Aturan Injeksi & Analisis Celah (Gap Analysis):** 
  1. AI TIDAK BOLEH mencetak semua file sekaligus. AI harus membaca template, menyuntikkan variabel, dan mencetak **SATU FILE PER RESPONS** ke repositori lokal.
  2. **Wawancara Celah Keputusan (Micro-Decisions):** Di setiap *loop* sebelum mencetak sebuah file, AI **WAJIB** mengevaluasi: *"Apakah ada informasi teknis mikro yang belum saya ketahui untuk merender file ini dengan spesifik?"*
  3. Jika ada celah (contoh: belum tahu UI Component Library yang digunakan, atau Testing Framework spesifik antara Jest vs Vitest), Anda **DILARANG** mencetak file tersebut. Anda wajib melakukan wawancara singkat terlebih dahulu dengan memberikan opsi dan rekomendasi *best-practice* (misal: merekomendasikan `shadcn/ui` atau `Vitest`).
  4. Anda baru boleh mencetak file tersebut setelah developer menjawab pertanyaan wawancara celah informasi Anda.

- **Protokol Wajib Baca Template (Anti-Halusinasi):**
  Sebelum merender dan mencetak sebuah file, AI **DILARANG KERAS** menebak isi struktur file dari ingatannya sendiri. AI **WAJIB** secara eksplisit menggunakan *tools* (seperti `view_file` atau membaca file secara programatik) untuk membaca file `.template.md` yang bersangkutan di dalam direktori `blueprints/` terlebih dahulu. Jika AI langsung mencetak file tanpa membaca *blueprint* aslinya, itu adalah pelanggaran tingkat fatal.

- **Pagar Pembatas Konten (Strict Bounding Box):**
  AI harus memahami bahwa template *blueprint* terdiri dari 2 zona absolut:
  1. **Zona Statis & Variabel Substitusi (`{{VAR}}`):** Semua teks Markdown di luar tag direktif generasi **WAJIB DISALIN 100% APA ADANYA**. Anda **DILARANG KERAS** meringkas, merombak, atau memotong hukum statis (seperti protokol *Anti-Strawman*) yang ada di template. Ganti variabel langsung dengan nilai dari Tahap 1-4.
  2. **Zona Generasi Dinamis** (`<!-- GENERATION_DIRECTIVE: ... -->`): Anda HANYA diizinkan berkreasi dan menyusun kalimat sendiri tepat di area yang diapit oleh tag ini (berdasarkan keputusan developer). Di luar tag ini, bias peringkasan (*summarization bias*) bawaan LLM Anda **HARUS DIMATIKAN**.
- **🔒 HUKUM PENYALINAN BIT-FOR-BIT ASET STATIS (`references/` & `scripts/` — HARAM `write_file`!):**
  Seluruh berkas di `blueprints/references/*.md` dan `skills/forge-constitution/scripts/*.py` adalah **aset statis murni** (0 variabel `{{VAR}}`). AI **DIHARAMKAN KERAS** mengetiknya ulang menggunakan tool `write_file` (yang rawan *summarization bias* / pemotongan kode). AI **WAJIB** menyalinnya secara fisik tingkat sistem file menggunakan skrip deterministik SHA-256:
  ```bash
  python "<FORGE_ROOT>/skills/forge-constitution/scripts/copy_static_assets.py" --target-root "." --profile <fe|be|fullstack|minimal>
  ```
  dan memastikan keluaran terminal berstatus **`✅ 100% LOSSLESS SHA-256 VERIFIED`**.

- **Protokol Audit Integritas Pascakopi (Self-Correction):**
  Setelah Anda mencetak sebuah file, lakukan Audit Integritas internal: *"Apakah ada klausa, aturan, tabel spektrum, atau paragraf peringatan dari blueprint asli yang tidak sengaja saya ringkas atau hapus?"* Jika ada narasi asli yang menguap, Anda telah melanggar Konstitusi. Anda **WAJIB** membatalkan hasil tersebut dan mencetak ulang file dengan struktur statis yang 100% utuh.

- **Protokol Standar Enterprise (Hak Veto Batasan):**
  Jika Anda menemukan "Catatan Injektor" di dalam template yang menyuruh Anda membatasi kuota jumlah poin/isu (misalnya *"Isi dengan 4-5 poin"*), Anda **WAJIB MENGABAIKAN BATASAN ANGKA TERSEBUT**. Anda memiliki Hak Veto untuk menerobos batasan sempit tersebut demi merender poin evaluasi arsitektur secara ekstensif, komprehensif, dan tanpa batas kuota agar memenuhi standar mutu *Enterprise*.

- **Protokol Matriks Enterprise Mutlak (The 5 Enterprise Matrix Protocol):**
  Setiap kali Anda (AI) merancang solusi, merumuskan arsitektur, merespons interogasi `/grill-me`, menghasilkan standar kode, atau mendesain poin evaluasi, Anda **DILARANG KERAS** memberikan rekomendasi dangkal atau yang sekadar "bisa berjalan" (*just works*). Anda **WAJIB MUTLAK** membedah, menganalisis, dan memaksakan standar yang merata di dalam **5 Dimensi Enterprise** berikut:
  1. **Dimensi Bisnis & Arsitektur Skala Besar (Sistem):** (Wajib mencakup: *Soft Delete vs Hard Delete* untuk integritas riwayat, *Audit Trails*/Log Kepatuhan untuk mutasi sensitif, perlindungan *Race Conditions*/*Concurrency Control*, mitigasi *Abuse*/*Rate Limiting*, dan *Observability/Error Tracing* sentral).
  2. **Dimensi Kebersihan Struktur & Maintainability:** (Wajib mencakup: *Separation of Concerns*, pelacakan kode yatim/*dead code*, pemecahan komponen raksasa/anti *God-Component*, dan ekstraksi *magic strings*).
  3. **Dimensi Keamanan & Integritas Data:** (Wajib mencakup: proteksi *bypass* otorisasi terpusat, validasi ketat skema/payload mutasi dari *Client*, dan jaminan resiliensi mutasi berganda via *Database Transactions*).
  4. **Dimensi Performa & Skalabilitas (Runtime):** (Wajib mencakup: pencegahan mutlak *N+1 Query*, mitigasi kebocoran memori/*memory bloat*, dorongan maksimal *React Server Components* ke *leaf*, dan strategi *Cache Invalidation* yang akurat).
  5. **Dimensi UX & Stabilitas Aplikasi:** (Wajib mencakup: *Graceful Degradation* (loading/error boundary), pencegahan mutlak layar putih (*blank screen*), perlindungan *Core Web Vitals* (cegah CLS), dan kepatuhan *Accessibility*/A11y standar global).
  Anda wajib memastikan *output* rancangan/aturan Anda berlimpah, sangat brutal secara teknis, dan tidak menoleransi arsitektur level *hobbyist/junior*.

- **Protokol Kedisiplinan Ideasi Level 3 (The /edeate Golden Standard):**
  Saat menyuntikkan atau mengeksekusi `/edeate`, AI **WAJIB MUTLAK** mematuhi hukum integritas hulu berikut:
  1. **Hukum 1 Sesi = 1 Atomic Ticket Level 3:** DILARANG KERAS memborong banyak tiket sekaligus. Jika ide berupa Epik besar, lakukan dekomposisi dan fokuskan HANYA 1 tiket prioritas untuk dimatangkan hingga Level 3.
  2. **Review Gate Wajib Sebelum Finalisasi:** AI WAJIB menyajikan Rangkuman Arsitektur & Scope Plan di Fase 4, lalu menunggu ACC/evaluasi Tech Lead di Fase 5 sebelum mencetak tiket Level 3 di Fase 6.
  3. **Larangan Mutlak Eksekusi di Hulu (Code-Free Zone):** AI DIHARAMKAN menulis kode produksi, membuat file skema/migrasi, atau menawarkan PR otomatis di `/edeate`. Output `/edeate` murni berupa spesifikasi tiket GitHub Issue. Seluruh implementasi kode wajib menyeberang ke Gateway 2 melalui `/grill-me`.
  4. **The Golden Ticket Standard:** Format tiket Level 3 wajib komprehensif mencakup 7 pilar Enterprise: YAML Frontmatter, Konteks Eksisting vs Hasil Diharapkan, Blast Radius berkas terdampak, Spesifikasi Langkah & Signature Method, Kontrak Invariant, DoD Berlapis, Kriteria Penolakan PR, dan Poin Kunci Edukasi Teknis (Technical Talking Points).

- **Urutan Injeksi (Pastikan path menggunakan standar Antigravity Workspace Customizations):**
  0. Cetak `.agents/forge_manifest.json` (Brankas DNA Fisik). Tunggu izin.
  1. Cetak `DEVELOPMENT_ROADMAP.md` (di *root* proyek). Tunggu izin.
  2. Cetak `.agents/rules/00-router.md` (Router Induk Penangkal Attention Dilution). Tunggu izin.
  3. Cetak `.agents/rules/MASTER_RULES.md`. Tunggu izin.
  3b. Cetak `.agents/rules/PERSONA_MENTOR.md` (Identitas Jiwa *Kakak Tingkat Senior* — *WHO*, Always-On dari `blueprints/persona_mentor.template.md`). Tunggu izin.
  4. Cetak `.agents/rules/META_RULES.md` (Kendali Kognitif & Protokol Tool-First). Tunggu izin.
  5. Cetak `.agents/rules/ARCHITECTURE.md`. Tunggu izin.
  5b. *(Khusus Proyek FE / Fullstack; lewati untuk proyek Pure Backend)* Cetak `.agents/rules/DESIGN.md` (Konstitusi Visual 7 Pilar Draft v0 dari `blueprints/design.template.md` — dikalibrasi final di Epik 0). Tunggu izin.
  6. Cetak `.agents/rules/GIT_WORKFLOW.md`. Tunggu izin.
  7. Cetak `.agents/mcp_config.json`. Tunggu izin.
  8. Cetak `ONBOARDING.md` (di *root* proyek — wajib memuat verifikasi Python 3.8+ stdlib & catatan literasi *Adversarial Reviewer Sub-Agent* di semua proyek). Tunggu izin.
  9. Cetak file `.agents/skills/project-edeate/SKILL.md` beserta 3 berkas rujukan on-demand (salin bit-for-bit via `copy_static_assets.py`: `dual_track_protocol.md`, `ticket_variants.md`, `anti_patterns.md`). Tunggu izin.
  10. Cetak file `.agents/skills/project-grill-me/SKILL.md` beserta rujukan on-demand `references/grill_cards_and_guards.md` (disalin bit-for-bit via `copy_static_assets.py`). Tunggu izin.
  11. Cetak file `.agents/skills/project-plan/SKILL.md` beserta rujukan on-demand `references/adversarial_review_lens.md` (semua proyek) *(dan khusus proyek dengan Database: `references/database_design_checklist.md`; seluruhnya disalin via `copy_static_assets.py`)*. Tunggu izin.
  12. Cetak file `.agents/skills/project-tdd/SKILL.md`. Tunggu izin.
  13. Cetak file `.agents/skills/project-execute/SKILL.md`. Tunggu izin.
  14. Cetak file `.agents/skills/project-audit/SKILL.md` beserta skrip & rujukan kondisionalnya (seluruhnya disalin bit-for-bit via `copy_static_assets.py`):
      - **Wajib di Semua Proyek:** `scripts/classify_blast_radius.py`, `references/audit_handoff_package.md`, dan `references/adversarial_review_lens.md`.
      - **Khusus Proyek FE / Fullstack:** `references/audit_visual_gate.md` serta 2 skrip QA UI (`finish_lint.py`, `state_matrix_checker.py`).
      - **Khusus Proyek BE / Fullstack:** `references/audit_api_checklist.md` serta 3 skrip OpenAPI (`api_linter.py`, `breaking_change_detector.py`, `api_scorecard.py`).
      Tunggu izin.
  15. Cetak file `.agents/skills/project-debug/SKILL.md`. Tunggu izin.
  16. Cetak file `.agents/skills/project-epic-persistence/SKILL.md`. Tunggu izin.
  17. Cetak file `.agents/skills/project-explore/SKILL.md` (Gerbang Tur Pedagogi Codebase 1x di hari pertama). Tunggu izin.
  18. Cetak file `.agents/skills/project-ship/SKILL.md` beserta salinan skrip `scripts/changelog_generator.py` via `copy_static_assets.py` (Gerbang Kesiapan Rilis & Demo UAS). Tunggu izin.
  19. *(Khusus Proyek FE / Fullstack; lewati untuk proyek Pure Backend)* Cetak file `.agents/skills/project-prototype/SKILL.md` beserta rujukan `references/anti_slop_design_guide.md`, 3 berkas upstream lossless (`references/upstream/*`), dan 3 skrip UI (`design_token_generator.py`, `finish_lint.py`, `state_matrix_checker.py`) via `copy_static_assets.py`. Tunggu izin.
