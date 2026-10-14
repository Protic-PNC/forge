---
name: epic-01-forge-v1-3-0-evolution
description: >-
  Roadmap Evolusi Arsitektur Konstitusi Forge v1.3.0. Mengadopsi aturan emas dari SIM
  (00-router, epic-persistence, smart handshake di grill-me, format tiket V2, dan auto-kanban bridge di audit)
  serta menyempurnakan Two-Gateway Pipeline.
target_version: "1.3.0"
status: "READY_FOR_EXECUTION"
created_at: "2026-10-13"
---

# EPIC-01: EVOLUSI ARSITEKTUR KONSTITUSI FORGE (V1.2.0 ➔ V1.3.0)
## *Enterprise-Grade Cognitive Guardrails, Context Hydration, & Two-Gateway Automation*

---

## 🧭 FILOSOFI & LATAR BELAKANG REKAYASA

### 1. Evaluasi Psikologis: Pembatalan Usulan Flag `--mode` (Junior vs Fast)
Pada evaluasi awal, sempat muncul usulan flag `--mode` (`--junior` vs `--fast`). Namun, berdasarkan analisis pedagogis dan psikologi mahasiswa, usulan ini **DIBATALKAN TOTAL** karena membawa dampak kontraproduktif:
- **Stigmatisasi & Beban Mental:** Mahasiswa merasa dilabeli inferior jika harus mengetik `--junior`, atau sebaliknya memaksakan `--fast` demi gengsi sehingga berujung *burnout* dan kegagalan memahami arsitektur.
- **Pemisahan Palsu:** Jika mode cepat meniadakan jembatan pemahaman, mahasiswa kehilangan esensi belajar. Jika mode junior meniadakan istilah industri, mahasiswa tidak siap menghadapi dunia kerja nyata.

**Pilihan Desain Definitif: Unified Dual-Layer Pedagogical Structure**
Forge menetapkan satu standar interaksi terpadu:
1. **Lapisan Atas (Standar Industri Nyata):** Menyajikan istilah teknis asli software engineer (latensi, konkurensi, Big O, O(1), memory bloat) agar mahasiswa terbiasa dengan standar enterprise tanpa direndahkan.
2. **Lapisan Bawah (Jembatan Logika Mahasiswa):** Menyandingkannya dengan klausul *Pilih Opsi Ini Jika*, *Hindari Opsi Ini Jika*, serta *Safe Harbor ("Ikut saranmu")* agar mahasiswa tidak pernah terjebak kebuntuan (*burnout*).

### 2. Penegasan Batas Two-Gateway Pipeline
- **Gerbang 1 — Hulu (`/edeate`):**
  - Zona imajinasi bebas dan perancangan tiket.
  - **DILARANG KERAS** menjalankan perintah Git atau meminta nomor issue.
  - Penawaran pembuatan issue resmi via MCP GitHub (`create_issue`) **HANYA DAN EKSKLUSIF** dilakukan di penutup sesi `/edeate` setelah draf Tiket Level 3 disahkan oleh pengguna.
- **Gerbang 2 — Hilir (`/grill-me` ➔ `/plan` ➔ `/tdd` ➔ `/execute` ➔ `/audit`):**
  - Pintu masuk resmi pengerjaan tiket adalah `/grill-me`.
  - Refleks pencetakan perintah Git di baris pertama respons (`git checkout main && git pull && git checkout -b ...`) **HANYA BERLAKU DI `/grill-me`** (dan `/debug`).
  - Cabang kerja terkunci selama pengerjaan; dilarang berpindah cabang hingga tahap `/audit`.
  - Di akhir `/audit`, PR dibuat via MCP GitHub lengkap dengan klausa penutup issue (`Closes #<id>`) dan label kanban (`needs-review`) agar papan proyek berpindah otomatis secara realtime.

---

## 📜 ATURAN MAIN PENGERJAAN ROADMAP (GROUND RULES)

1. **Mandat Audit Pra-Eksekusi:**
   Sebelum memulai pengerjaan satu poin checklist, AI dan Developer **WAJIB SECARA FISIK MEMBACA & MENGANALISIS** berkas blueprint/skill terkait di Forge dan berkas referensi di `manajemen-protik\.agents`. Dilarang mengedit berdasarkan asumsi ingatan.
2. **Mandat Centang Bertahap & Verifikasi Ad-Hoc:**
   Dilarang mencentang kotak `[x]` sebelum dilakukan verifikasi fisik mandiri (menggunakan skrip pengujian atau parser lokal) dan dipastikan lulus 100%. Selesaikan dan centang satu per satu.

---

## 📋 MASTER CHECKLIST EVOLUSI V1.3.0

### FASE 0: The Socratic Co-Design & Physical Roadmap Sync (Pondasi Epik & Hulu)
*Tujuan: Mengikat perancangan DEVELOPMENT_ROADMAP.md secara interaktif dengan developer dan menjadikannya kompas hulu di /edeate.*
- [x] **Task 0.1 — Socratic Co-Design Protocol di `forge-constitution`:** Rombak Tahap 2 `skills/forge-constitution/SKILL.md` dengan protokol 3 ketukan (Page Inventory ➔ CRUD Dapur vs Etalase ➔ Review Gate Draf Epik).
- [x] **Task 0.2 — Audit Roadmap di Langkah 0.2 `/edeate`:** Wajibkan AI membaca `DEVELOPMENT_ROADMAP.md` di root untuk memetakan ide ke Epik Level 1 dan sub-poin bersangkutan sebelum wawancara dimulai.
- [x] **Task 0.3 — Milestone & Sub-Poin di Tiket Level 3:** Sisipkan `milestone: "Epik [X]: [Nama Epik]"` di frontmatter dan deskripsi tiket `blueprints/edeate.template.md`.
- [x] **Task 0.4 — Refleks Centang Fisik Otomatis:** AI wajib memperbarui `DEVELOPMENT_ROADMAP.md` dari `- [ ]` ke `- [x] ... (Issue #[Nomor])` begitu tiket resmi disahkan di akhir `/edeate`.
- [x] **Task 0.5 — Mandat Konstitusi Master:** Tambahkan penegasan bahwa seluruh sesi `/edeate` wajib berpijak pada `DEVELOPMENT_ROADMAP.md` di `blueprints/master_rules.template.md`.

---

### FASE 1: Blueprint `00-router.template.md` (Penyelamat Context Window Antigravity)
*Tujuan: Mencegah Attention Dilution pada IDE Antigravity dengan memisahkan Always-On Invariants dengan On-Demand Skills.*
- [x] **Task 1.1 — Analisis Komparasi:** Baca dan bedah `manajemen-protik/.agents/rules/00-router.md` terhadap cara kerja pembacaan context IDE Antigravity.
- [x] **Task 1.2 — Konstruksi Blueprint:** Buat berkas `blueprints/00-router.template.md` (maksimal 25–30 baris):
  - Penjelasan mitigasi *Attention Dilution*.
  - 4 Hukum Always-On: Dilarang Berasumsi Prosedur (baca skill), Rujuk Arsitektur, Anti Yes-Man, dan Otomasi MCP Berbasis Konsensus.
  - Front-matter YAML seragam di baris 1.
- [x] **Task 1.3 — Verifikasi Ad-hoc Mandiri:** Validasi sintaks berkas dan verifikasi bahwa router mengarahkan ke `.agents/skills/`.

---

### FASE 2: Blueprint `epic-persistence.template.md` (Protokol Anti-Amnesia Sesi)
*Tujuan: Mengamankan kelanjutan fitur multi-fase di sesi baru tanpa kehilangan konsensus arsitektur.*
- [x] **Task 2.1 — Analisis Komparasi:** Baca `manajemen-protik/.agents/skills/protik-epic-persistence/SKILL.md`.
- [x] **Task 2.2 — Konstruksi Blueprint:** Buat berkas `blueprints/epic_persistence.template.md`:
  - Protokol penciptaan fisik berkas `.agents/epics/<nama-epic>.md` jika `/edeate` menghasilkan roadmap multi-fase.
  - Struktur Prasasti Epik: Latar Belakang, Konsensus Arsitektur, dan Master Checklist `[ ]` Fase 1..N.
  - Mandat Context Hydration fisik: Di sesi baru, AI diwajibkan membaca file epik tersebut sebelum menjawab.
- [x] **Task 2.3 — Penyelarasan Blueprint `/edeate`:** Perbarui `blueprints/edeate.template.md` agar mewajibkan pembuatan berkas epik jika hasil ideasi memuat lebih dari 1 fase.
- [x] **Task 2.4 — Verifikasi Ad-hoc Mandiri:** Uji sintaksis template dan verifikasi penanda direktif.

---

### FASE 3: Smart Git Handshake Eksklusif di `/grill-me` & Integrasi Issue di `/edeate`
*Tujuan: Memastikan alur version control disiplin, aman, dan tidak bocor ke fase hulu.*
- [x] **Task 3.1 — Analisis Komparasi:** Baca `manajemen-protik/.agents/skills/protik-git-handshake/SKILL.md` dan `blueprints/git_workflow.template.md`.
- [x] **Task 3.2 — Refleks Baris Pertama Eksklusif di `/grill-me`:** Perbarui `blueprints/grill-me.template.md`:
  - AI wajib mencetak blok perintah Git di baris pertama respons (`git checkout main && git pull origin main && git checkout -b <prefix>/issue-<nomor>-<nama>`).
  - Jika nomor issue belum ada di prompt, tanyakan nomor issue sebelum membuat branch.
- [x] **Task 3.3 — Klausa Pengecualian `/edeate` & Penawaran Issue MCP:** Perbarui `blueprints/edeate.template.md`:
  - Larangan mutlak memicu perintah git di dalam sesi `/edeate`.
  - HANYA setelah draf Tiket Level 3 disahkan, AI menawarkan pembuatan tiket via **MCP GitHub (`create_issue`)**.
- [x] **Task 3.4 — Kunci Branch (*Stick to Current Branch*):** Perbarui `blueprints/git_workflow.template.md`:
  - Menegaskan pembuatan branch isolasi hanya dilakukan 1x di `/grill-me`.
  - Larangan berpindah branch selama tahapan `/plan`, `/tdd`, `/execute`, dan `/audit`.
- [x] **Task 3.5 — Verifikasi Ad-hoc Mandiri:** Uji alur pencetakan perintah git dan isolasi sesi hulu.

---

### FASE 4: Meta-Rule Kendali Kognitif & Spesifikasi Tiket Issue V2
*Tujuan: Mengunci perilaku AI agar patuh pada state-machine dan menghasilkan tiket berstandar arsitektur industri.*
- [x] **Task 4.1 — Analisis Komparasi:** Baca `manajemen-protik/.agents/rules/master-rules.md` (bagian Meta-Rule & Template V2).
- [x] **Task 4.2 — Injeksi Meta-Rule di `master_rules.template.md`:**
  - Tambahkan klausul: *Algoritma State-Machine, Bukan Referensi Opsional* (AI wajib patuh kaku pada SOP).
  - Tambahkan klausul: *LSP Tool-First Audit* (diharamkan memberikan narasi arsitektur sebelum memanggil alat pemindai fisik AST/LSP).
- [x] **Task 4.3 — Standardisasi Format Tiket GitHub Issue V2:** Perbarui spesifikasi tiket di `blueprints/master_rules.template.md` dan `blueprints/edeate.template.md`:
  1. Identitas Tiket & Pola Branch
  2. Matriks Otorisasi & Hak Akses (*Policy Matrix*)
  3. Batasan Bisnis & Integritas Data (*Anti-Spoofing, Immutability, Concurrency, OWASP*)
  4. Peta Berkas Terdampak (*Blast Radius: Eksisting vs Baru*)
  5. Spesifikasi Teknis Defensif
  6. Definition of Done (DoD)
  7. Technical Talking Points (Meeting Defense)
- [x] **Task 4.4 — Verifikasi Ad-hoc Mandiri:** Validasi kelengkapan 7 pilar tiket V2.

---

### FASE 5: Auto-Closing Kanban Bridge & Labeling di `/audit`
*Tujuan: Mengotomatiskan sinkronisasi status Kanban GitHub secara realtime tanpa intervensi manual developer.*
- [x] **Task 5.1 — Analisis Komparasi:** Baca `blueprints/audit.template.md` Bagian 3 (Paket Penyerahan Tiket).
- [x] **Task 5.2 — Otomasi PR via MCP GitHub:**
  - Wajib menyertakan kata kunci otomatisasi penutupan issue (`Closes #<id>` atau `Resolves #<id>`) di baris paling atas deskripsi PR.
  - Menambahkan penetapan label PR otomatis: `needs-review` dan label modul terkait saat AI menawarkan pembuatan PR via MCP GitHub.
- [x] **Task 5.3 — Verifikasi Ad-hoc Mandiri:** Uji struktur deskripsi PR dan parameter pemanggilan tool MCP GitHub.

---

### FASE 6: Penyelarasan Engine Forge, Manifest Tracking, & Release Bump
*Tujuan: Memastikan /forge-update dan /forge-constitution mampu menyuntikkan dan menyinkronkan seluruh blueprint baru secara deterministik.*
- [x] **Task 6.1 — Penyelarasan Injektor (`skills/forge-constitution/SKILL.md`):**
  - Daftarkan `00-router.template.md` ke dalam urutan injeksi Tahap 5 sebagai berkas `.agents/rules/00-router.md`.
  - Daftarkan `meta_rules.template.md` sebagai berkas `.agents/rules/META_RULES.md`.
  - Daftarkan `epic_persistence.template.md` sebagai skill `.agents/skills/project-epic-persistence/SKILL.md`.
- [x] **Task 6.2 — Penyelarasan Engine Update (`skills/forge-update/SKILL.md`):**
  - Pastikan parser mengenali blueprint baru dan mampu menginjeksi berkas baru `[BERKAS BARU]` ke proyek lama (`comprof-protic`).
- [x] **Task 6.3 — Bump Versi & Catatan Rilis:**
  - Perbarui `plugin.json` ke versi `1.3.0`.
  - Rangkum seluruh peningkatan arsitektur pada catatan rilis.
- [x] **Task 6.4 — Verifikasi End-to-End Ad-Hoc:** Jalankan skrip validasi komprehensif untuk memastikan seluruh file valid, konsisten, dan bebas galat sintaks.

---

## 📌 LOG PROGRESS EKSEKUSI
*(Catat setiap kemajuan tugas di sini setelah verifikasi ad-hoc lolos)*

- **2026-10-13:** Berkas Roadmap Epik resmi dibuat dan disahkan.
- **2026-10-13:** **FASE 0 TUNTAS 100% (VERIFIED):**
  - Mengintegrasikan *The Socratic Co-Design Protocol (3 Ketukan Interaktif)* di `skills/forge-constitution/SKILL.md` Tahap 2.
  - Memasang audit fisik `DEVELOPMENT_ROADMAP.md` di Langkah 0.2 `blueprints/edeate.template.md`.
  - Memasukkan atribut `milestone` di frontmatter dan deskripsi Tiket Level 3.
  - Menetapkan penawaran pembuatan Issue via MCP GitHub dan *Refleks Centang Otomatis* pada `DEVELOPMENT_ROADMAP.md` di akhir `/edeate`.
  - Mengesahkan kewajiban pijakan `DEVELOPMENT_ROADMAP.md` di `blueprints/master_rules.template.md`.
  - Lulus verifikasi ad-hoc mandiri. Siap melanjutkan ke FASE 1.
- **2026-10-13:** **FASE 1 TUNTAS 100% (VERIFIED):**
  - Mengonstruksi berkas `blueprints/00-router.template.md` (26 baris).
  - Menetapkan 4 hukum Always-On (Dilarang Berasumsi Prosedur, Rujuk Arsitektur, Anti Yes-Man, Otomasi MCP Konsensus).
  - Terverifikasi ad-hoc mandiri lulus 100%. Siap melanjutkan ke FASE 2.
- **2026-10-13:** **FASE 2 TUNTAS 100% (VERIFIED):**
  - Mengonstruksi berkas `blueprints/epic_persistence.template.md`.
  - Mengintegrasikan protokol penciptaan berkas `.agents/epics/<nama-epic>.md` dan Autonomous Context Hydration.
  - Memutakhirkan `blueprints/edeate.template.md` pada penanganan epik multi-fase.
  - Terverifikasi ad-hoc mandiri lulus 100%. Siap melanjutkan ke FASE 3.
- **2026-10-13:** **FASE 3 TUNTAS 100% (VERIFIED):**
  - Memasang Refleks Baris Pertama Smart Git Handshake di `blueprints/grill-me.template.md` (Kasus A & Kasus B).
  - Mengintegrasikan aturan Stick to Current Branch & Larangan Git di `/edeate` pada `blueprints/git_workflow.template.md` dan `blueprints/edeate.template.md`.
  - Terverifikasi ad-hoc mandiri lulus 100%. Siap melanjutkan ke FASE 4.
- **2026-10-13:** **FASE 4 TUNTAS 100% (VERIFIED):**
  - Menginjeksi Meta-Rule Kendali Kognitif & Anti-Halusinasi (State-Machine, Tool-First LSP, Circuit Breaker) di `blueprints/master_rules.template.md` dan `blueprints/meta_rules.template.md`.
  - Menstandardisasi Spesifikasi Tiket GitHub Issue V2 (7 Pilar Defensif) di `blueprints/master_rules.template.md` dan `blueprints/edeate.template.md`.
  - Terverifikasi ad-hoc mandiri lulus 100%. Siap melanjutkan ke FASE 5.
- **2026-10-13:** **FASE 5 TUNTAS 100% (VERIFIED):**
  - Mengintegrasikan penutupan otomatis `Closes #<nomor-issue>` di baris teratas draf PR `blueprints/audit.template.md`.
  - Menanamkan pelabelan PR otomatis `needs-review` dan penawaran pembuatan PR via MCP GitHub `create_pull_request`.
  - Terverifikasi ad-hoc mandiri lulus 100%. Siap melanjutkan ke FASE 6.
- **2026-10-13:** **FASE 6 TUNTAS 100% (VERIFIED):**
  - Menyelaraskan urutan injeksi di `skills/forge-constitution/SKILL.md` (Tahap 5).
  - Menyelaraskan tabel mapping dan deteksi `[BERKAS BARU]` di `skills/forge-update/SKILL.md`.
  - Bump versi ke `1.3.0` di `plugin.json` beserta catatan rilis komprehensif.
  - Lolos uji integrasi end-to-end 100% (6/6 suite pengujian ad-hoc mandiri).
  - **STATUS EPIK: SELESAI (COMPLETED).**
