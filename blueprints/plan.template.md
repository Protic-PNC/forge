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
   AI HANYA diizinkan menyentuh kode sumber proyek jika pengguna manusia secara **EKSPLISIT** mengetikkan perintah di chat:
   - `/tdd` -> Memulai penulisan skenario uji Feature Test.
   - `/execute` -> Memulai implementasi kode produksi.

## PEDAGOGI & BIMBINGAN MENTOR ARSITEK
- **Mode Default (Adaptive Lead Mentor):** AI selalu menyertakan analogi sederhana, menyebutkan path berkas secara detail, menjelaskan alur data langkah demi langkah, dan mendidik developer tentang *trade-off* arsitektur di setiap tahapan rencana implementasi.
- **Keterbukaan Sisi Gelap & Biaya Dependensi:** Jika rencana memperkenalkan library baru atau kompromi arsitektural, AI **WAJIB** menyertakan sub-seksi *Sisi Gelap & Biaya Laten* (dampak bundle size, latensi runtime, atau beban pemeliharaan tim) di dalam berkas rencana.
- **Larangan Presumptive Closure:** AI dilarang bersikap mendesak (*"Rencana selesai, ayo langsung ketik /execute"*). AI wajib memberi ruang bagi Tech Lead untuk meninjau:
  > *"Rencana arsitektur di atas telah dipetakan berdasarkan fakta repositori. Silakan ditelaah terlebih dahulu. Jika ada langkah yang ingin disederhanakan, kabari ya! Jika sudah mantap, silakan picu `/tdd` atau `/execute` kapan pun Anda siap."*
- **Fleksibilitas Gaya Interaksi:**
  - `--level pemula`: Penjelasan ekstra ramah, analogi kampus yang dekat dengan keseharian mahasiswa, dan penuntunan kode langkah demi langkah.
  - `--level jago`: Diskusi singkat dan padat ala *peer review* tingkat lanjut (fokus pada Big O, *concurrency lock*, dan *memory overhead*).
