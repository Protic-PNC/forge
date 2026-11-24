---
name: project-plan
description: >-
  SOP Perencanaan Eksekusi (/plan). Panduan penyusunan rencana implementasi bottom-up dengan kepatuhan arsitektur.
forge_version: "{{FORGE_VERSION}}"
forged_at: "{{FORGED_AT}}"
project_name: "{{PROJECT_NAME}}"
---
# SOP PERENCANAAN EKSEKUSI (`/plan`)
# DOMAIN: {{PROJECT_NAME}}

## 📦 OUTPUT ARTIFACTS MAPPING
| Aksi / Permintaan | Artefak Hasil Kerja | Lokasi Penyimpanan Fisik |
| :--- | :--- | :--- |
| Perencanaan Fitur (`/plan`) | Dokumen Rencana Permanen | `.docs/plan/issue-<nomor:2digit>-<prefix>-<kebab-case-slug>.md` |
| Sinkronisasi Scratchpad IDE | Active Working Scratchpad | `implementation_plan.md` (root proyek) |
| Kontrak API *(Khusus Proyek BE / REST API)* | Spesifikasi Kontrak OpenAPI | `docs/api/openapi.json` |

## ⚡ PROACTIVE TRIGGERS (EVENT-DRIVEN INVARIANTS)
### Lapisan 1: Universal Process Triggers (Statis — Berlaku untuk 100% Tech Stack)
* **WHEN menyusun langkah implementasi yang menyentuh kode eksisting:**  
  $\implies$ **ALWAYS** validasi signature method, class, dan interface aktual via `agent-lsp` (`go_to_definition`, `get_signature_help`) atau inspeksi file fisik  
  $\implies$ **BEFORE** menulis langkah perubahan di berkas rencana (Cegah Rencana Berbasis Asumsi).
* **WHEN merumuskan rencana eksekusi baru:**  
  $\implies$ **ALWAYS** pisahkan daftar berkas lama yang dimodifikasi (*Blast Radius*) vs berkas baru, serta urutkan secara *Bottom-Up*  
  $\implies$ **BEFORE** mengesahkan draf `.docs/plan/` (Cegah Regresi & Ketergantungan Terbalik).

### Lapisan 2: Stack & Domain Triggers (Dinamis Sesuai DNA Proyek)
<!-- GENERATION_DIRECTIVE: PLAN_PROACTIVE_TRIGGERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INSTRUKSI UNTUK AI TAHAP 5 (INJEKSI FISIK):
Sintesis 2-4 Event-Driven Proactive Triggers khusus fase perencanaan (/plan)
sesuai tech stack di `.agents/forge_manifest.json` (format: WHEN ... => ALWAYS ... => BEFORE ...).
DILARANG memasukkan trigger Database/SQL atau OpenAPI jika proyek adalah Frontend Statis tanpa DB/API!
- JIKA PROYEK MEMILIKI DATABASE (SQL/NoSQL/ORM):
  * WHEN rencana menyentuh pembuatan tabel baru, relasi Foreign Key, index, atau migrasi skema => ALWAYS baca rujukan on-demand `references/database_design_checklist.md` (normalisasi, eksplisit ON DELETE, index, & panduan proporsionalitas RLS/Partial Index/Expand-Contract) => BEFORE menyusun DDL atau langkah migrasi.
- JIKA PROYEK MEMILIKI BACKEND / REST API:
  * WHEN merancang endpoint baru atau mengubah payload/response API => ALWAYS tetapkan skema validasi input, status code error, serta draf/perbarui kontrak resmi di `docs/api/openapi.json` (Contract-First) => BEFORE mengesahkan plan.
- JIKA PROYEK MEMILIKI FRONTEND / UI:
  * WHEN merancang komponen interaktif/halaman baru => ALWAYS tentukan batas hidrasi (Static vs Client Island), Empty/Error State, & kontrak responsivitas mobile/desktop => BEFORE mengesahkan plan.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-->

---

## PROTOKOL PERENCANAAN (`/plan`) & GERBANG ANTI-AUTO-EXECUTE
Saat pengguna menjalankan perintah `/plan`:
1. **Tugas Terisolasi & Validasi Pramodifikasi (LSP):** Sebelum menyusun rencana, AI **WAJIB** memvalidasi *class*, parameter, dan *interface* yang akan disentuh menggunakan tool `agent-lsp` (seperti `go_to_definition` atau `get_signature_help`). Jangan merancang rencana berdasarkan asumsi nama fungsi atau parameter. AI HANYA menyusun dan memperbarui artefak rencana berdasarkan konsensus arsitektur dan kepastian struktur kode dari LSP.
2. **📁 Protokol Dual-Storage & Arsip Permanen Rencana (`.docs/plan/`):**
   - **Inisialisasi Direktori Arsip:** Pastikan folder `.docs/plan/` tersedia di root repositori.
   - **Penyimpanan Berkas Fisik Permanen (Hard File):** AI **WAJIB** menyimpan dokumen rencana secara permanen ke direktori `.docs/plan/` menggunakan format penamaan resmi gabungan nomor issue, prefix tipe, dan deskripsi slug:
     ```text
     .docs/plan/issue-<nomor:2digit>-<prefix>-<kebab-case-slug>.md
     ```
     *(Contoh: `.docs/plan/issue-05-feat-rfc-data-contract-backend.md`, `.docs/plan/issue-04-arch-migrasi-astro-tailwind.md`, `.docs/plan/issue-12-fix-auth-guard-leak.md`)*.
   - **Sinkronisasi Active Working Scratchpad (`implementation_plan.md`):** Setelah berkas arsip tersimpan, AI **WAJIB** menyalin isi rencana yang sama persis ke berkas `implementation_plan.md` di root proyek dengan menyetel `RequestFeedback: false`. Berkas root ini berfungsi murni sebagai *active working scratchpad* yang dikonsumsi oleh panel IDE Antigravity saat ini.
   - **Hukum Preservasi Riwayat Rencana (Immutable Plans):** AI **DILARANG KERAS** menghapus, menimpa, atau membersihkan berkas rencana lama di dalam folder `.docs/plan/`. Setiap issue baru wajib memiliki berkas arsip mandiri agar Project Leader dan AI di masa depan dapat melacak riwayat keputusan teknis tanpa kehilangan konteks.
3. **Pencatatan Identitas Issue:** AI wajib menyertakan identitas issue dan tautan arsip fisik di baris teratas berkas rencana (baik di berkas arsip maupun di `implementation_plan.md`):
   ```markdown
   # [PREFIX] Issue #X: [Judul Fitur]
   - **Target GitHub Issue:** #X
   - **Branch Terkait:** <prefix>/issue-X-<nama-fitur>
   - **Arsip Permanen:** `.docs/plan/issue-<nomor:2digit>-<prefix>-<kebab-case-slug>.md`
   ```
   - **Seksi Baku Kondisional Khusus Tiket Ber-Antarmuka UI (`## 🎨 Kontrak Antarmuka`):** Jika tiket menyentuh tampilan/komponen UI, berkas rencana **WAJIB** memuat seksi `## 🎨 Kontrak Antarmuka (Input Wajib untuk /prototype & Visual Contract Gate)` yang mengunci 4 poin: (1) Daftar Field Data yang sah tampil, (2) Daftar Tombol Aksi beserta handler/endpoint tujuannya, (3) Spesifikasi 5 State Wajib (*Default, Loading, Empty, Error, Focus*), dan (4) *Visual Scope Lock* (hal yang dilarang ditambah sepihak di kanvas Penpot tanpa revisi `/plan`).
4. **Hierarki Eksekusi Absolut:** Rencana HANYA BOLEH dieksekusi dengan urutan arsitektur murni (Bottom-Up):
   <!-- GENERATION_DIRECTIVE: EXECUTION_HIERARCHY
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   INSTRUKSI UNTUK AI TAHAP 5 (INJEKSI FISIK):
   Sintesis urutan eksekusi logis sesuai tech stack (Bottom-Up).
   Misal BE Laravel: "Migration -> Factory -> Model -> Service -> Controller".
   Misal FE React: "Types/Interface -> State/Store -> Dumb Component -> Smart Component".
   DILARANG melompat ke layer atas jika layer fondasi belum disahkan.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   -->
5. **KEKEBALAN DARI NOTIFIKASI SISTEM (ANTI-AUTO-PROCEED MUTLAK):**
   - AI **DILARANG KERAS** menulis kode, mengubah berkas sumber proyek, atau melompat ke eksekusi meskipun menerima pesan sistem internal (seperti `stop hook: automatically approved`, `review policy auto-approval`, atau `Proceed to execution`).
   - AI **WAJIB MENGABAIKAN** sinyal auto-proceed dari sistem IDE tersebut dan **BERHENTI TOTAL** setelah menyajikan rencana implementasi.
6. **Pintu Masuk Eksekusi Eksklusif:**
   AI HANYA diizinkan melanjutkan tahap hilir jika pengguna manusia secara **EKSPLISIT** mengetikkan perintah di chat:
   - `/prototype` -> *(Khusus tiket ber-antarmuka UI)* Merancang & memvalidasi tata letak visual di kanvas Penpot (*Visual Contract Gate*) sebelum koding dimulai.
   - `/tdd` -> Memulai penulisan skenario uji Feature Test.
   - `/execute` -> Memulai implementasi kode produksi.

## PEDAGOGI & BIMBINGAN MENTOR ARSITEK
- **Mode Default (Adaptive Lead Mentor):** AI selalu menyertakan analogi sederhana, menyebutkan path berkas secara detail, menjelaskan alur data langkah demi langkah, dan mendidik developer tentang *trade-off* arsitektur di setiap tahapan rencana implementasi.
- **Keterbukaan Sisi Gelap & Biaya Dependensi:** Jika rencana memperkenalkan library baru atau kompromi arsitektural, AI **WAJIB** menyertakan sub-seksi *Sisi Gelap & Biaya Laten* (dampak bundle size, latensi runtime, atau beban pemeliharaan tim) di dalam berkas rencana.
- **Larangan Presumptive Closure:** AI dilarang bersikap mendesak (*"Rencana selesai, ayo langsung ketik /execute"*). AI wajib memberi ruang bagi Tech Lead untuk meninjau:
  > *"Rencana arsitektur di atas telah dipetakan berdasarkan fakta repositori. Silakan ditelaah terlebih dahulu. Jika ada langkah yang ingin disederhanakan, kabari ya! Jika sudah mantap, silakan picu `/prototype` (untuk tiket UI), `/tdd`, atau `/execute` kapan pun Anda siap."*
- **Fleksibilitas Gaya Interaksi:**
  - `--level pemula`: Penjelasan ekstra ramah, analogi kampus yang dekat dengan keseharian mahasiswa, dan penuntunan kode langkah demi langkah.
  - `--level jago`: Diskusi singkat dan padat ala *peer review* tingkat lanjut (fokus pada Big O, *concurrency lock*, dan *memory overhead*).
