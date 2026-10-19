---
name: forge-update
description: >-
  Declarative Constitution Re-render Engine.
  Menyinkronkan file konstitusi lokal proyek dengan blueprint terbaru dari Forge global
  menggunakan sistem Declarative Re-render berbasis forge_manifest.json,
  tanpa membebani memori kerja AI dan 100% menjamin integritas DNA proyek.
---
# SOP SINKRONISASI KONSTITUSI (`/forge-update`)

> **PERAN UTAMA ANDA (AI): THE DECLARATIVE RE-RENDER ENGINE**
> Anda adalah mesin sinkronisasi presisi tinggi. Tugas Anda adalah memperbarui "hukum operasional" repositori ini agar selaras dengan rilis terbaru Forge global, **TANPA** mengandalkan ingatan obrolan yang rapuh dan **TANPA** menimpa keputusan DNA proyek.
>
> **3 PILAR ARSITEKTUR DECLARATIVE RE-RENDER:**
> 1. **Zero Memory Burden:** AI DILARANG menebak atau menahan DNA proyek di memori obrolan. Sumber kebenaran tunggal (*Single Source of Truth*) DNA proyek adalah berkas fisik `.agents/forge_manifest.json` di disk.
> 2. **Targeted Invalidation (Hemat Token 70%+):** AI TIDAK BOLEH membaca atau menyentuh semua blueprint. AI HANYA memproses berkas yang terdaftar di `releases` dalam `plugin.json` Forge global.
> 3. **Declarative Re-render (Git Menghitung Diff):** AI TIDAK PERLU membandingkan teks baris demi baris. AI cukup mengambil blueprint terbaru, menyuntikkan DNA dari manifest, dan menulis ulang berkas. Biarkan Git yang menyajikan garis hijau/merah bagi developer!
> 4. **Isolasi 1 Berkas per Respons:** AI DILARANG mencetak lebih dari satu berkas per giliran untuk menjamin perhatian (*attention*) LLM tetap 100% prima dan bebas *summarization bias*.
>
> 🛑 **HARD STOP MACRO:** Di setiap akhir respons Anda (setiap kali selesai merender 1 fase/aksi), Anda WAJIB mencetak persis kalimat ini:
> `[TUGAS AI BERHENTI DI SINI. DILARANG MERENDER FASE SELANJUTNYA SEBELUM ADA BALASAN USER]`

---

## 🗺️ PETA MAPPING BLUEPRINT KE BERKAS LOKAL

| Nama Blueprint di `plugin.json` | Jalur Berkas Fisik di Proyek Lokal |
|:---|:---|
| `00-router.template.md` | `.agents/rules/00-router.md` |
| `master_rules.template.md` | `.agents/rules/MASTER_RULES.md` |
| `meta_rules.template.md` | `.agents/rules/META_RULES.md` |
| `architecture.template.md` | `.agents/rules/ARCHITECTURE.md` |
| `git_workflow.template.md` | `.agents/rules/GIT_WORKFLOW.md` |
| `edeate.template.md` | `.agents/skills/project-edeate/SKILL.md` |
| `grill-me.template.md` | `.agents/skills/project-grill-me/SKILL.md` |
| `plan.template.md` | `.agents/skills/project-plan/SKILL.md` |
| `tdd.template.md` | `.agents/skills/project-tdd/SKILL.md` |
| `execute.template.md` | `.agents/skills/project-execute/SKILL.md` |
| `audit.template.md` | `.agents/skills/project-audit/SKILL.md` |
| `debug.template.md` | `.agents/skills/project-debug/SKILL.md` |
| `epic_persistence.template.md` | `.agents/skills/project-epic-persistence/SKILL.md` |

---

## 🔬 FASE 0: FAST VERSION & MANIFEST CHECK

**Aksi:**
0. **Pre-Flight Remote Sync Check (Anti-Stale Cache):**
   Sebelum membaca berkas versi global, AI **WAJIB** memastikan repositori Forge global di disk lokal (`$LOCALAPPDATA/hermes/forge` atau direktori clone Forge terkait) selalu mutakhir dengan upstream GitHub:
   - Jalankan sinkronisasi hening melalui terminal:
     ```bash
     git -C "$LOCALAPPDATA/hermes/forge" pull origin main
     ```
   - Ini menjamin bahwa jika ada commit rilis baru di GitHub dari mesin/sesi lain, cache lokal di laptop langsung ter-refresh secara otomatis sebelum evaluasi versi dimulai.
1. Periksa keberadaan berkas fisik `.agents/forge_manifest.json` di repositori lokal menggunakan tools pembaca file:
   - **Jika TIDAK ADA:** AI wajib menginformasikan: *"Berkas `.agents/forge_manifest.json` belum ditemukan (proyek ini di-forge sebelum versi 1.1.0). Jalankan `/forge-constitution` sekali lagi untuk menggenerasi manifest DNA resmi proyek ini."* → **STOP.**
2. Baca `forge_version` dari `.agents/forge_manifest.json`.
3. Baca `version` global dan riwayat `releases` dari berkas `plugin.json` Forge global.
4. **Evaluasi Versi & Force Bypass:**
   - **Pemeriksaan Opsi Force Re-sync:** Jika developer menyertakan argumen `--force` (misal: `/forge-update --force`), atau secara eksplisit meminta perbaikan/sinkronisasi ulang berkas:
     Abaikan perbandingan versi sama, tetapkan daftar target ke seluruh `updated_blueprints` pada rilis versi aktif saat ini (atau seluruh blueprint jika diminta perbaikan total), dan **Lanjutkan ke Fase 1**.
   - **Evaluasi Normal:**
     - Jika `local_version == global_version`:
       Sajikan pesan:
       > *"✅ Konstitusi proyek Anda sudah berada di versi terbaru (**v{{GLOBAL_VERSION}}**). Tidak ada pembaruan blueprint yang diperlukan. (Gunakan `/forge-update --force` jika ingin memaksa render ulang blueprint versi ini)."*
       → **STOP.**
     - Jika `local_version < global_version`:
       Lanjutkan ke **Fase 1**.

`[TUGAS AI BERHENTI DI SINI. DILARANG MERENDER FASE SELANJUTNYA SEBELUM ADA BALASAN USER]`

---

## 📦 FASE 1: RESOLUSI RENTANG RILIS & PEMETAAN TARGET (Target Invalidation)

**Tujuan:** Menemukan secara presisi HANYA berkas yang berubah antara `local_version` hingga `global_version`. Mengabaikan berkas lainnya untuk menghemat token dan waktu.

**Aksi:**
1. Telusuri objek `releases` di `plugin.json` untuk semua versi yang berada di antara `local_version` (eksklusif) hingga `global_version` (inklusif).
2. Kumpulkan seluruh `updated_blueprints` secara unik (deduplikasi).
3. Kumpulkan seluruh `summary` pembaruan dari versi-versi terkait.
4. Petakan nama blueprint ke jalur berkas lokal menggunakan **Tabel Mapping** di atas.
5. **Deteksi Berkas Baru (New File Ingestion):** Periksa apakah berkas target lokal sudah ada di disk. Jika berkas fisik target belum ada (misal ada blueprint baru yang ditambahkan di rilis Forge global), tandai statusnya sebagai `[BERKAS BARU]`. Jika sudah ada, tandai sebagai `[PEMBARUAN]`.

---

## 🛡️ FASE 2: PRESENTASI TARGET & GIT SAFETY NET (The Gate)

**Aksi:**
1. Tampilkan laporan pembaruan ringkas kepada developer:
   ```markdown
   ## 🚀 Pembaruan Konstitusi Tersedia: v{{LOCAL_VERSION}} ➔ v{{GLOBAL_VERSION}}
   
   ### 📝 Catatan Rilis:
   - [Rangkuman dari summary release terkait]
   
   ### 🎯 Berkas Blueprint yang Terdampak ({{JUMLAH_BERKAS}} Berkas):
   | # | Blueprint Asal | Target Berkas Lokal | Status |
   |:--|:---|:---|:---|
   | 1 | `master_rules.template.md` | `.agents/rules/MASTER_RULES.md` | [PEMBARUAN] |
   | 2 | `grill-me.template.md` | `.agents/skills/project-grill-me/SKILL.md` | [PEMBARUAN] |
   | 3 | `debug.template.md` | `.agents/skills/project-debug/SKILL.md` | [PEMBARUAN] |
   | 4 | `arsip.template.md` | `.agents/rules/ARSIP.md` | [BERKAS BARU] |
   
   *(Berkas lainnya tidak terdampak dan akan diabaikan demi efisiensi).*
   ```

2. **Mandat Jaring Pengaman Git (Wajib):**
   AI **WAJIB** meminta developer melakukan commit darurat sebelum melanjutkan:
   > *"🛡️ **Jaring Pengaman Git:** Sebelum saya menulis ulang berkas di atas, mohon jalankan perintah ini di terminal Anda:*
   > ```bash
   > git add -A && git commit -m "chore: checkpoint sebelum forge-update ke v{{GLOBAL_VERSION}}"
   > ```
   > *Ketik **'Lanjut'** setelah commit selesai untuk memulai Declarative Re-render berkas pertama."*

3. AI DILARANG menulis berkas apa pun sebelum developer mengetik izin lanjutan.

`[TUGAS AI BERHENTI DI SINI. DILARANG MERENDER FASE SELANJUTNYA SEBELUM ADA BALASAN USER]`

---

## ⚡ FASE 3: ISOLATED DECLARATIVE RE-RENDER LOOP (1 File per Response)

**Prinsip Kerja:**
AI memproses berkas yang terdampak **SATU PER SATU PER RESPONS**. 
Di setiap iterasi:
1. Baca berkas template terbaru dari direktori global: `blueprints/{{NAMA_BLUEPRINT}}`.
2. **Preservasi Zona Kustom (Anti-Data Loss):**
   Jika berkas target lokal sudah ada di disk, AI **WAJIB** memeriksa apakah berkas tersebut memuat zona riwayat dinamis (misalnya `<!-- ADR_LOG_START -->` hingga `<!-- ADR_LOG_END -->` pada `ARCHITECTURE.md`). Jika ada entri catatan yang dibuat developer/tim di dalamnya, ekstrak dan simpan teks tersebut agar tidak hilang saat ditimpa.
3. **Penanganan Berkas Baru & Celah Variabel (Micro-Interview):**
   Jika berkas berstatus `[BERKAS BARU]`:
   - AI memeriksa apakah template berkas baru tersebut memuat placeholder variabel `{{VAR}}` atau `<!-- GENERATION_DIRECTIVE: ... -->` yang belum terdaftar di dalam `dna` atau `directives` manifest lokal.
   - Jika ada variabel baru yang belum diketahui: AI **WAJIB BERHENTI** dan mengajukan 1 pertanyaan wawancara terarah (disertai 3 spektrum opsi + rekomendasi) kepada developer. Setelah disetujui, simpan nilai tersebut ke `.agents/forge_manifest.json` sebelum melanjutkan render.
4. Baca data dari `.agents/forge_manifest.json` (lokal):
   - Metadata Front-Matter (sudah ada di template):
     - `{{FORGE_VERSION}}` ➔ `{{GLOBAL_VERSION}}`
     - `{{FORGED_AT}}` ➔ `{{FORGED_AT_DARI_MANIFEST}}`
     - `{{PROJECT_NAME}}` ➔ `{{PROJECT_NAME_DARI_MANIFEST}}`
     - Sisipkan baris `updated_at: "{{TANGGAL_HARI_INI}}"` tepat di bawah `forged_at` pada blok front-matter.
   - Variabel `dna`: substitusikan langsung ke seluruh placeholder `{{VAR}}` di template.
   - Blok `directives`: gantikan blok `<!-- GENERATION_DIRECTIVE: NAMA_DIRECTIVE ... -->` dengan konten string yang tersimpan di field `directives.NAMA_DIRECTIVE` manifest.
   - Zona Kustom yang diekstrak: tempelkan kembali ke dalam blok tag yang sesuai (misal di antara `<!-- ADR_LOG_START -->` dan `<!-- ADR_LOG_END -->`).
5. Tulis atau buat berkas target di disk lokal (misal: `.agents/rules/MASTER_RULES.md`).
6. Berikan laporan bahwa berkas tersebut telah selesai dirender, lalu minta konfirmasi developer sebelum melanjutkan ke berkas berikutnya dalam antrean.

`[TUGAS AI BERHENTI DI SINI. DILARANG MERENDER FASE SELANJUTNYA SEBELUM ADA BALASAN USER]`

---

## 🏁 FASE 4: PEMBARUAN MANIFEST & GIT HANDOFF

Setelah seluruh berkas terdampak selesai dirender ulang:
1. **Perbarui Manifest:**
   Buka `.agents/forge_manifest.json` lokal dan perbarui:
   - `"forge_version"`: ubah ke `{{GLOBAL_VERSION}}`.
   - `"last_updated_at"`: isi dengan tanggal hari ini.
2. **Git Handoff (Serahkan Diff ke Git):**
   AI **DILARANG** mencoba menjelaskan diff baris per baris. AI menyerahkan peninjauan perubahan kepada Git asli:
   ```markdown
   ## 🎉 Pembaruan Konstitusi Selesai!
   Konstitusi repositori ini telah berhasil diperbarui ke **Forge v{{GLOBAL_VERSION}}**.
   Seluruh DNA proyek dan kebijakan MCP tetap utuh 100%.
   
   ### 🔍 Cara Meninjau Perubahan:
   Jalankan perintah ini di terminal untuk melihat apa saja klausul baru yang ditambahkan oleh Forge:
   ```bash
   git diff
   ```
   
   Jika Anda puas dengan hasil pembaruan, kunci perubahan ini dengan commit:
   ```bash
   git add -A && git commit -m "chore: sync konstitusi ke Forge v{{GLOBAL_VERSION}}"
   ```
   
   *(Catatan Transparansi: Setelah commit dieksekusi, status Source Control di panel IDE Anda akan otomatis kembali bersih/clean working tree tanpa tanda modified. Anda dapat memeriksa riwayat perubahan yang baru saja di-commit kapan saja dengan `git show HEAD` atau `git log -1 -p`).*
   ```

---

## ⚠️ HUKUM ANTI-PATTERN (LARANGAN MUTLAK)

| Anti-Pattern | Dampak Buruk | Tindakan Mutlak AI |
|:---|:---|:---|
| **Menebak DNA dari Riwayat Chat** | Halusinasi variabel, salah nama DB/stack | Wajib membaca data murni dari `.agents/forge_manifest.json` |
| **Membaca Seluruh Blueprint Sekaligus** | Menghabiskan token, memicu *lost in the middle* | Wajib hanya membaca blueprint yang ada di daftar `updated_blueprints` rilis |
| **Mencetak Lebih dari 1 File per Turn** | *Summarization bias*, AI memotong tabel SOP | Wajib Hard Stop setelah mencetak 1 berkas dan menunggu konfirmasi |
| **Menyentuh Berkas Non-Blueprint** | Menimpa Roadmap, Onboarding, atau MCP config | DILARANG menyentuh `DEVELOPMENT_ROADMAP.md`, `ONBOARDING.md`, atau `mcp_config.json` |