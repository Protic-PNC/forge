# Rencana Eksekusi: TAHAP 3 — Ekspansi 3 Gerbang Baru (`/explore`, `/prototype`, & `/ship`)
**Dokumen Diskusi & Persetujuan:** Tahap 3 dari 4 (Setelah Tahap 2 Tuntas & Di-commit di `4028ef6`)  
**Target:** Melengkapi siklus hidup FORGE menjadi **End-to-End Lifecycle** dengan 3 gerbang baru + Konstitusi Visual `.agents/rules/DESIGN.md`, seluruhnya **bebas beban kognitif harian**, **bebas bias stack (*Stack-Aware*)**, dan **berbasis riset skill GitHub terverifikasi API**.  
**Lokasi Berkas Sasaran:** `blueprints/` (`explore`, `prototype`, `ship`, `design`, `00-router`, `grill-me`, `plan`), `blueprints/references/`, `skills/forge-constitution/scripts/`, `skills/forge-constitution/references/`, dan `skills/forge-update/SKILL.md`.

---

## 1. Keputusan yang Sudah DIKUNCI (Hasil Diskusi & Validasi Live GitHub API)

> ✅ **Seluruh butir berikut telah diverifikasi langsung ke `api.github.com` & `raw.githubusercontent.com` (24 Nov 2026) dan disepakati bersama:**

1. **Gerbang `/explore` (DIKUNCI):**
   * **TIDAK mencetak file `.docs/CODEBASE_MAP.md`** (dihapus untuk mencegah *stale doc* dan duplikasi dengan `ARCHITECTURE.md`).
   * Dirancang sebagai **Tur Pedagogi Interaktif 4 Lapisan + *Active Recall* di Chat**:
     1. *Lapisan 1:* Orientasi bisnis (*The "Why"*) + 1 diagram Mermaid makro + deteksi *drift* terhadap `ARCHITECTURE.md` (🟢/🟡/🔴). Dilarang memuntahkan ratusan baris *folder tree*.
     2. *Lapisan 2:* Menu pilihan 3–4 alur fitur nyata + **Hard Stop** (mahasiswa memilih jalur tur sendiri).
     3. *Lapisan 3:* Bedah 1 alur *End-to-End* (*Request-to-Screen Trace*, Protokol 2-Ketukan + analogi eksistensial).
     4. *Lapisan 4:* *Active Recall Check* (1 skenario tebak santai tanpa menghakimi agar pemahaman menempel di kepala).
2. **Optimasi Hulu Kondisional Khusus UI (DIKUNCI):**
   * **`blueprints/grill-me.template.md`:** Menambahkan 3 dimensi keputusan UI di dalam `DYNAMIC_GRILL_QUESTIONS` khusus proyek/tiket UI (*Brand Tone & Arah Visual*, *Hierarki Aksi & 5 State UX*, *Batas Field Data di Layar*).
   * **`blueprints/plan.template.md`:** Menambahkan seksi baku kondisional **`## 🎨 Kontrak Antarmuka (Input Wajib untuk /prototype & Visual Contract Gate)`** pada `.docs/plan/issue-XX-...md` + menambahkan pintu masuk `/prototype` sebelum `/tdd` & `/execute`.
3. **Matriks Seleksi Skill Eksternal GitHub (Terverifikasi Live API & Baca Kode Mentah):**

| Sumber GitHub (Terverifikasi API) | Bintang (⭐) | Status | Peran di FORGE Tahap 3 |
| :--- | :---: | :---: | :--- |
| **`anthropics/skills` (`skills/frontend-design/SKILL.md`)** | **199.687** | ✅ **ADOPSI INTI** | Prinsip *Ground in Subject Matter*, larangan visual slop, & *review against brief* ke `references/anti_slop_design_guide.md`. |
| **`nextlevelbuilder/ui-ux-pro-max-skill`** | **153.555** | ✅ **ADOPSI SEBAGAI ALAT BANTU 1X** | Alat bantu opsional (1x di awal proyek oleh 1 UI Lead) untuk memanen rekomendasi 194 industri (palet, Google Fonts berlisensi, UX rules) guna mengisi `.agents/rules/DESIGN.md`; dicatat di `ONBOARDING.md` (0 bloat di repo mahasiswa). |
| **`pbakaus/impeccable`** | **115.940** | ✅ **ADOPSI POLA `DESIGN.md` SAJA** | **Tolak** engine Rust & 24 perintah eksternalnya. **Adopsi penuh** arsitektur 7 Pilar `.agents/rules/DESIGN.md` (Creative North Star, Named Rules, Typography, Elevation/Shapes, Component Anatomy, Do's/Don'ts, Where Tokens Live + blok `<!-- DDR_LOG_START -->`). |
| **`blader/humanizer`** *(Wikipedia WikiProject AI Cleanup)* | **72.947** | ✅ **ADOPSI INTISARI** | Taksonomi pola tulisan AI berbasis editor manusia Wikipedia (lintas bahasa ID/EN, bebas *self-grading bias*) ke `references/anti_slop_design_guide.md` (atribusi MIT). |
| **`github/awesome-copilot` (`skills/penpot-uiux-design`)** + **`penpot/penpot-mcp`** | **41.509** + **537** | ✅ **ADOPSI UTAMA** | Tulang punggung `/prototype`: 4 tool MCP resmi (`execute_code`, `export_shape` self-review, `import_image`, `penpot_api_info`), *Graceful Fallback*, + troubleshooting port `4400–4402` di `ONBOARDING.md`. |
| **`vercel-labs/agent-skills` (`skills/web-design-guidelines`)** | **34.842** | ✅ **ADOPSI INTISARI** | Aturan objektif A11y, focus ring, `prefers-reduced-motion`, *tabular-nums*, & format laporan `file:line`. |
| **`alirezarezvani/claude-skills` (4 Skrip Stdlib)** | **30.400** | ✅ **ADOPSI 4 SKRIP** | `design_token_generator.py` (21 KB), `finish_lint.py` (18.5 KB), `state_matrix_checker.py` (12.3 KB), & `changelog_generator.py` (5.1 KB) — murni matematika warna, regex tombol mati, 5-state check, & Git log. |
| **`ar27111994/penpot-mcp`** | **31** | ❌ **DITOLAK / CORET** | Bintang terlalu kecil & path root 404; digantikan penuh oleh `github/awesome-copilot`. |
| **`ui_copy_linter.py`** *(buatan AI)* & **`headline/humanizer_scorer.py`** | — | ❌ **DIBATALKAN / TOLAK** | Menghindari *self-grading bias* & kamus English-only (yang justru menyukai buzzword klise *"ultimate/world-class"*). |

---

## 2. Alur Siklus Hidup Terintegrasi & Rencana 2 Micro-Batch

```text
[ HARI PERTAMA (1x) ]      [ SIKLUS RUTIN MINGGUAN FORGE ]                              [ DEMO UAS / RILIS (1x) ]

      /explore        ──►  /edeate ──► /grill-me ──► /plan ──► [/prototype*] ──► /execute ──► /audit  ──►  /ship
 (Tur Pedagogi 4-Lapis)                                          ▲                                      (Kertas Kado)
                                            (*Hanya untuk proyek/tiket yang memiliki UI!)
```

### ✅ BATCH 3A: Gerbang Awal `/explore`, Gerbang Akhir `/ship`, & `changelog_generator.py` (STATUS: SELESAI DIEKSEKUSI)
* `blueprints/explore.template.md` *(Baru — $\le$8 KB)*: Tur Pedagogi Interaktif 4 Lapisan + *Active Recall* (0 file baru dicetak, 100% Read-Only).
* `blueprints/ship.template.md` *(Baru — $\le$8 KB)*: Pre-Flight Secret/Env Hygiene, Build Sanity, SemVer, `CHANGELOG.md` via `changelog_generator.py`, & *Demo UAS Cheat Sheet* (tanpa `git tag`/`--tags` agar ramah pemula, tetap Hard Stop sebelum `git commit`/`push`).
* `skills/forge-constitution/scripts/changelog_generator.py` *(Diadopsi dari `claude-skills`, Pure Stdlib, lolos uji `--help` di Windows)*.
* Pembaruan `blueprints/00-router.template.md`, `physical_injection_spec.md` (Langkah 17–18), & `forge-update/SKILL.md`.

### ✅ BATCH 3B: Epik 0 (Bootstrap), Konstitusi Visual `DESIGN.md`, Gerbang `/prototype` (Penpot + Anti-Slop), Optimasi Hulu (`/grill-me` & `/plan`), & 3 Skrip UI (STATUS: SELESAI DIEKSEKUSI)
* `blueprints/design.template.md` *(Baru — $\le$8 KB, khusus proyek FE/Fullstack)*: Template 7 Pilar `.agents/rules/DESIGN.md` + blok `<!-- DDR_LOG_START --> ... <!-- DDR_LOG_END -->` (dilindungi saat `/forge-update`). Lahir sebagai kerangka v0 di `/forge-constitution` Tahap 5 sejajar `ARCHITECTURE.md`.
* `skills/forge-constitution/references/interview_guide.md`: Menambahkan **Epik 0: Pra-Sprint & Bootstrap Lingkungan (Bypass SOP `/edeate`–`/audit`)** tepat di atas Epik 1 (memuat eksekusi `ONBOARDING.md`, setup OpenAPI Exporter BE, & kalibrasi final `DESIGN.md` + `design-tokens.css` FE — dengan pagar keras dilarang menyelundupkan fitur bisnis ke Epik 0!), +1 pertanyaan ringan *Brand Tone* untuk FE/Fullstack, serta Katalog MCP Penpot & setup opsional `ui-ux-pro-max` di Fase 4.1/4.4.
* `blueprints/prototype.template.md` *(Baru — $\le$8 KB, khusus proyek FE/Fullstack)*: Silent Inspection `.agents/rules/DESIGN.md` (murni per-fitur!), Ekstraksi Kontrak Antarmuka `/plan`, 4 Tool MCP Penpot (`execute_code`, `export_shape`, `import_image`, `penpot_api_info`) + *Graceful Fallback*, dan **The Visual Contract Gate** (2 opsi rekonsiliasi jika kanvas menyimpang dari `/plan`).
* `blueprints/references/anti_slop_design_guide.md` *(Baru — Index + Suplemen ID + CLI 3 Skrip)* & **`blueprints/references/upstream/`** *(100% Lossless Bahasa Inggris Asli — diunduh langsung bit-for-bit: `anthropic_frontend_design.md`, `vercel_web_design_guidelines.md`, `blader_humanizer.md`)*.
* `skills/forge-constitution/scripts/copy_static_assets.py` *(Baru — Deterministik `shutil.copy2` + verifikasi SHA-256 + larangan keras `write_file` untuk aset statis di `physical_injection_spec.md` & `forge-update/SKILL.md`)*.
* 3 Skrip Stdlib UI (`skills/forge-constitution/scripts/`): `design_token_generator.py`, `finish_lint.py`, & `state_matrix_checker.py`.
* Optimasi Hulu Kondisional UI: `blueprints/grill-me.template.md` & `blueprints/plan.template.md`.
* Sinkronisasi penuh: `physical_injection_spec.md` & `forge-update/SKILL.md` (termasuk preservasi blok `<!-- DDR_LOG_START -->`).

---

## 3. Keputusan Terkunci: Kelahiran 2-Tahap `DESIGN.md` & **Epik 0 (Bootstrap — Bypass SOP)**
> ✅ **Status: DIKUNCI**
> 1. **Kelahiran Kerangka di `/forge-constitution`:** Khusus proyek FE/Fullstack, AI mengajukan 1 pertanyaan ringan *Brand Tone* lalu mencetak `.agents/rules/DESIGN.md` (v0 Kerangka 7 Pilar) sejajar dengan `ARCHITECTURE.md` di Tahap 5.
> 2. **Eksekusi `ONBOARDING.md` & Kalibrasi Final di Epik 0 (*Bypass SOP*):** `DEVELOPMENT_ROADMAP.md` dibuka dengan **Epik 0: Pra-Sprint & Bootstrap Lingkungan** yang secara eksplisit melewati SOP `/edeate`–`/audit` (untuk eksekusi `ONBOARDING.md`, setup OpenAPI Exporter, & kalibrasi final `.agents/rules/DESIGN.md` + `design-tokens.css` 1x oleh Lead) — dengan pagar keras **HARAM memasukkan fitur bisnis/halaman ke Epik 0** agar Epik 1 tetap murni berisi Fondasi Aplikasi & MVP!
> 3. **Di Seluruh Tiket Fitur Rutin (`/prototype`):** Murni bekerja di level per-fitur dengan membaca `.agents/rules/DESIGN.md` secara senyap (*Silent Inspection*).
