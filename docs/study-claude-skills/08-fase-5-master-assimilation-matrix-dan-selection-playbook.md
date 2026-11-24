# Fase 5: Master Assimilation Matrix & Selection Playbook
**Puncak Studi Komparasi:** Peta Kurasi Komprehensif Seluruh Skill Engineering & Buku Panduan Eksekusi Asimilasi ke dalam Plugin FORGE.  
**Tujuan Dokumen:** Menyediakan inventaris lengkap, klasifikasi prioritas berbasis ROI, dan resep konkret bagaimana menyuntikkan skill terpilih ke 7 Gerbang FORGE (`/explore`, `/edeate`, `/plan`, `/execute`, `/audit`, `/debug`, `/ship`).

---

## 1. Konteks & Cara Membaca Fase 5

Setelah menempuh:
* **Fase 1:** Memahami Standar Anatomi (10 Pola, 10KB Rule, Context-First).
* **Fase 2:** Memahami Sistem Rem & Kontrol (Forensik Transkrip, Human Gate, Retro).
* **Fase 3:** Memahami Rekayasa Teknis (API Review, Database RLS, Focused Fix, TDD).
* **Fase 4:** Memahami Orkestrasi Tim (Triad Persona/Skill/Task, Adversarial Review, Handoff).

Maka **Fase 5 adalah Fase Eksekusi & Pengambilan Keputusan**:  
Kita menyaring seluruh 126 skill engineering yang ada di repositori enterprise ke dalam **Corong 3 Tier (The 3-Tier Assimilation Funnel)** agar kamu bisa memutuskan dengan presisi tanpa keraguan.

```
                    CORONG SELEKSI ASIMILASI FORGE
                                  │
    ┌───────────────────────────────────────────────────────────┐
    │ TIER 1: High-ROI / Emas Murni Wajib Asimilasi             │ ──► Langsung Disuntikkan ke FORGE
    │ (Menutup celah fatal, 0 redundansi, akurasi deterministik) │
    ├───────────────────────────────────────────────────────────┤
    │ TIER 2: Domain-Specific / On-Demand                       │ ──► Disimpan sebagai Modul Opsional
    │ (Sangat bagus, tapi hanya untuk proyek teknologi khusus)  │
    ├───────────────────────────────────────────────────────────┤
    │ TIER 3: Redundan / Ditolak                                │ ──► DIABAIKAN (FORGE Sudah Lebih Unggul)
    │ (Kalah ketat dibanding aturan emas yang sudah ada di FORGE)│
    └───────────────────────────────────────────────────────────┘
```

---

## 2. Klasifikasi 3 Tier: Mana yang Wajib Diambil vs Ditolak

---

### TIER 1: HIGH-ROI (Emas Murni Wajib Asimilasi)
*Skill yang membawa lompatan kualitas deterministik, menghemat ribuan token, dan menutup celah fatal di alur kerja FORGE.*

| Nama Skill | Senjata Fisik / Metode | Stasiun FORGE Target | Dampak Langsung pada Mahasiswa & Proyek |
| :--- | :--- | :---: | :--- |
| **`codebase-onboarding`** | Skrip pemetaan pohon file & AST | **`/explore` (Baru)** | Mahasiswa baru tidak bingung lagi; peta denah kode terbit otomatis. |
| **`api-design-reviewer`** | `api_linter.py`, `breaking_change_detector.py`, `api_scorecard.py` | **`/audit`** | Audit API otomatis berbobot Nilai A–F dan pencegahan crash aplikasi client. |
| **`database-schema-designer`** | Checklist RLS multi-tenant, Partial Index, Expand-Contract DDL | **`/plan`** | Mencegah kebocoran data antar-organisasi dan server lemot karena full scan. |
| **`focused-fix`** | Protokol 5 Fase (*The Iron Law of Diagnosis*) | **`/debug`** | Melenyapkan *Shotgun Debugging*; AI dilarang edit kode sebelum root cause terbukti. |
| **`agent-run-forensics`** | Parser log transkrip sistem (`transcript.jsonl`) | **`/audit`** *(Tier 0)* | Mengaudit kebohongan AI; mendeteksi *STALE test* (kode dirusak setelah tes lulus). |
| **`human-gate`** | Kontrak review fisik (`.review.md`) & Exit Code 2 | **`/plan`** $\rightarrow$ **`/execute`** | Mengunci AI agar tidak melompat ke koding sebelum spek ditandatangani manusia. |
| **`adversarial-reviewer`** | Persona penguji skenario terburuk (*worst-case*) | **`/plan` / `/grill-me`** | Mengeliminasi bias konfirmasi; rencana diserang dulu sebelum dieksekusi. |
| **`changelog-generator`** | Parser Conventional Commits & SemVer bumper | **`/ship` (Baru)** | Otomasi pembuatan `CHANGELOG.md` dan stempel versi resmi tugas mahasiswa. |
| **`ship-gate`** | Pre-flight audit scanner (8 kategori) | **`/ship` (Baru)** | Menjamin tidak ada password `.env` bocor sebelum tugas di-deploy ke Vercel/Netlify. |
| **`session-handoff`** | Template handoff padat & linter privasi | **Handoff Antar-Tiket** | Mencegah *Context Drift*; sesi baru langsung paham tugas hanya dalam 200 token. |

---

### TIER 2: DOMAIN-SPECIFIC (Modul Tambahan Sesuai Kebutuhan Topik)
*Skill berkualitas enterprise yang disimpan di laci perpustakaan FORGE, dan hanya diaktifkan jika mata kuliah / topik tugas mahasiswa menyentuh domain tersebut.*

| Nama Skill | Domain Topik | Kapan Diaktifkan |
| :--- | :--- | :--- |
| **`stripe-integration-expert`** | Finansial / E-Commerce | Tugas yang memiliki fitur pembayaran kartu kredit atau webhook payment gateway. |
| **`ci-cd-pipeline-builder`** | DevOps Lanjutan | Ketika mahasiswa sudah semester menengah dan mulai belajar GitHub Actions. |
| **`docker-development`** | Containerization | Ketika tugas akhir mewajibkan deployment berbasis Docker container. |
| **`rag-architect`** | AI / Data Engineering | Proyek yang membangun pencarian semantik atau chatbot berbasis dokumen vector. |
| **`a11y-audit`** | Frontend Accessibility | Evaluasi khusus kepatuhan aksesibilitas tunanetra (standar WCAG 2.1). |
| **`i18n-localization`** | Aplikasi Multi-Bahasa | Proyek aplikasi yang mendukung pergantian bahasa (Indonesia / Inggris). |
| **`secrets-vault-manager`** | Keamanan Lanjutan | Integrasi dengan HashiCorp Vault atau AWS Secrets Manager. |

---

### TIER 3: REDUNDAN / DITOLAK (FORGE Sudah Lebih Unggul)
*Skill dari repositori luar yang **TIDAK PERLU diambil** karena filosofi dan konstitusi FORGE kita saat ini justru sudah jauh lebih ketat dan lebih baik.*

| Nama Skill Luar | Alasan Mengapa Ditolak (Kelebihan FORGE) |
| :--- | :--- |
| **`playwright-pro`** | **Kalah ketat dari FORGE.** FORGE v1.3.6 sudah memiliki *Four-Tier Quality Gate* dengan aturan anti-manipulasi yang jauh lebih superior: pengujian pada *Real Inner-Viewport 1280x680*, *Real Anchor-Click Sticky Collision Gate*, dan *Zero Test-Tampering Law*. |
| **`senior-architect`** | **Terlalu kaku.** FORGE sudah memiliki *The Principal Engineer & Mentor* di `00-router.md` yang dilengkapi *The Trade-Off Balance Scale* dan *The Safe Harbor* yang jauh lebih ramah mahasiswa. |
| **`claude-coach`** | **Redundan.** Gaya bimbingan Socratic FORGE di `/edeate` dan `/grill-me` sudah mencakup fungsi pelatihan ini dengan konteks proyek lokal yang lebih rekat. |
| **`systematic-debugging`** | **Tergantikan.** Protokol *The Iron Law of Diagnosis* pada `focused-fix` (Tier 1) jauh lebih lengkap dan mencakup graf dependensi 2 arah. |

---

## 3. Matriks Indeks Lengkap: 8 Gerbang FORGE yang Diberdayakan

Berikut adalah peta menyeluruh bagaimana **8 Gerbang Alur Kerja FORGE Terpadu** (termasuk gerbang Prototyping Penpot) diperkuat oleh skill-skill enterprise terpilih:

```
┌───────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                          PETA 8 GERBANG ALUR KERJA FORGE TERINTEGRASI                                 │
└───────────────────────────────────────────────────────────────────────────────────────────────────────┘

1. GERBANG AWAL: /explore (Orientasi Kode Baru)
   ├── Basis Alur: Codebase Reality Grounding (Hari Pertama Clone Repo)
   ├── Injeksi Skill: `codebase-onboarding`, `monorepo-navigator`, `code-tour`
   └── Deliverable Fisik: `.agents/rules/PROJECT_DNA.md` & Peta Dependensi Visual

2. GERBANG HULU: /edeate (Ekstraksi Kebutuhan Bisnis)
   ├── Basis Alur: Socratic Mentoring & Two-Gateway Pipeline FORGE
   ├── Injeksi Skill: Context-First Check (Pattern 1), `epic-design`
   └── Deliverable Fisik: GitHub Issue / Draf Tiket Arsitektur Level 3 (Bebas Anchoring Bias)

3. GERBANG HILIR: /plan & /grill-me (Spesifikasi Teknis & Pre-Mortem)
   ├── Basis Alur: Hard Gating & Dual-Storage Plan FORGE
   ├── Injeksi Skill: `database-schema-designer` (RLS + Partial Index), `adversarial-reviewer`, `human-gate`
   └── Deliverable Fisik: `.docs/plan/issue-<nomor>-<slug>.md` & Kontrak UI Checklist

4. GERBANG DESAIN: /prototype (Kanvas Penpot & Vibe Design) [BARU!]
   ├── Basis Alur: Eksplorasi Visual Sesuai Kurikulum "Desain Antarmuka Interaktif"
   ├── Injeksi Skill: `ui-design-system` (Tokens), `copywriting` (Headline Scorer), `content-humanizer`
   ├── Jaring Pengaman: Visual Contract Gate (Validasi kesesuaian elemen kanvas vs kontrak di /plan)
   └── Deliverable Fisik: Kanvas Desain Penpot (Web Standards Flexbox/Grid) + File Token CSS

5. GERBANG IMPLEMENTASI: /execute & /tdd (Koding Berdisiplin)
   ├── Basis Alur: TDD Red-Green-Refactor FORGE
   ├── Injeksi Skill: `red-green-proof` (Wajib Red Proof), Proactive Triggers di Header (Pattern 6)
   └── Deliverable Fisik: Kode Sumber Bersih + Unit Test Lolos

6. GERBANG PENJAMIN MUTU: /audit (Quality Gate Pra-PR)
   ├── Basis Alur: Four-Tier Quality Gate FORGE (Static, Unit, Arch, Visual Smoke Playwright)
   ├── Injeksi Skill: `api_linter.py`, `breaking_change_detector.py`, `api_scorecard.py`, `agent-run-forensics`
   └── Deliverable Fisik: Laporan Audit 4-Tier + Scorecard API + Handoff PR Terverifikasi

7. GERBANG REGRESI: /debug (Investigasi & Bedah Mikro Bug)
   ├── Basis Alur: Deferred Recommendation Protocol FORGE
   ├── Injeksi Skill: `focused-fix` (The Iron Law: SCOPE ──► TRACE ──► DIAGNOSE ──► FIX ──► VERIFY)
   └── Deliverable Fisik: Patch Terfokus Tanpa Efek Samping Regresi

8. GERBANG AKHIR: /ship (Kertas Kado Rilis & Wisuda Tugas)
   ├── Basis Alur: Release Readiness & Versioning (Akhir Semester / Jelang Demo UAS)
   ├── Injeksi Skill: `ship-gate` (Pre-flight Scanner), `changelog-generator` (SemVer Bump)
   └── Deliverable Fisik: Tag Rilis `v1.0.0` + Berkas `CHANGELOG.md` Resmi untuk Portofolio
```

---

## 4. The Assimilation Playbook: Langkah Teknis Eksekusi Refactoring FORGE

Bagaimana cara mengeksekusi asimilasi ini ke repositori dapur FORGE (`d:/exe/HERD/SIM/FORGE`) secara terukur? Kita gunakan **4 Langkah Rilis Bertahap**:

### Langkah 1: Refactoring Struktur Berkas (Penerapan The 10KB Rule)
* **Tindakan:**
  * Di folder `skills/forge-constitution/`: Pindahkan teks pedagogi dan ekstraksi bisnis ke folder `references/`.
  * Di folder `blueprints/`: Buat folder `references/` untuk menampung teks panduan panjang dari `edeate.template.md`.
  * Buat folder persona terpisah: `blueprints/personas/kakak-tingkat-mentor.md`.
* **Hasil:** Ukuran berkas `SKILL.md` utama menyusut dari 31–49 KB menjadi $\le$8 KB.

### Langkah 2: Pembuatan Gerbang Baru `/explore` dan `/ship`
* **Tindakan:**
  * Buat template blueprint baru: `blueprints/explore.template.md` (mengadopsi alur `codebase-onboarding`).
  * Buat template blueprint baru: `blueprints/ship.template.md` (mengadopsi `ship-gate` dan `changelog-generator`).
  * Daftarkan kedua slash command baru ini ke dalam `blueprints/00-router.template.md` dan `plugin.json`.

### Langkah 3: Injeksi Skrip Python Deterministik (Stdlib-Only)
* **Tindakan:**
  * Buat folder `skills/forge-constitution/scripts/` dan salin modul mandiri:
    1. `breaking_change_detector.py`
    2. `api_scorecard.py`
    3. `api_linter.py`
    4. `classify_blast_radius.py`
* **Hasil:** Modul `/audit` kini memiliki kemampuan verifikasi otomatis dalam hitungan milidetik tanpa memboroskan token.

### Langkah 4: Penyempurnaan Konstitusi `MASTER_RULES.md`
* **Tindakan:**
  * Tambahkan taksonomi severitas review Google: `BLOCKER`, `MAJOR`, `MINOR`, `NIT`.
  * Tambahkan aturan *Confidence Tagging*: 🟢 *Verified*, 🟡 *Medium*, 🔴 *Assumed*.
  * Tambahkan aturan *Bottom Line First* pada setiap respon AI.

---

## 5. Kesimpulan Akhir: Transformasi FORGE

Dengan selesainya dokumen Fase 5 ini, proses belajar dan kurasi kita telah tuntas:
1. **Identitas FORGE Tetap Utuh:** Jiwa mentor pedagogis ramah mahasiswa dan disiplin alur Two-Gateway Pipeline tetap menjadi fondasi utama.
2. **Kekuatan Enterprise Terserap Penuh:** Kecepatan deterministik, efisiensi token The 10KB Rule, kepastian keamanan RLS, audit API modern, serta gerbang rilis `/ship` kini menjadi bagian dari ekosistem FORGE.

FORGE kini siap melangkah ke fase implementasi nyata: **berevolusi menjadi Framework Konstitusi AI paling matang, terstruktur, dan ramah mahasiswa di dunia!**

---
*Dokumen ini merupakan penutup resmi dari rangkaian modul pembelajaran repositori `claude-skills`.*
