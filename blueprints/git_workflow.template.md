# GIT WORKFLOW PROTOCOL

> Dokumen ini mendikte bagaimana kode dikelola, diamankan, dan digabungkan oleh tim di repositori ini.

## 1. Strategi Kolaborasi
- **Model Percabangan Utama:** {{GIT_BRANCHING_STRATEGY_DECISION}}
- **Aturan Penamaan Branch:** Wajib menggunakan awalan tipe dan nomor issue. (Contoh: `feat/12-user-auth`, `fix/44-typo-header`).

## 2. Kebijakan Pull Request (The Security Gate)
- **Otorisasi Merge:** {{PULL_REQUEST_APPROVAL_POLICY}}
- **Syarat Mutlak Lolos PR:** 
  1. Seluruh pengujian (Tes Otomatis) harus lulus.
  2. Kode tidak merusak fitur eksisting.
  3. Wajib diperiksa menggunakan perintah `/audit` sebelum di-*merge*. AI akan memblokir proses jika ada cacat arsitektur atau keamanan.

## 3. Semantic Commit Messages
Semua pesan *commit* harus bermakna dan mematuhi konvensi *Angular/Conventional Commits*:
- `feat:` (Penambahan fitur baru)
- `fix:` (Perbaikan bug)
- `chore:` (Pembaruan dependencies, konfigurasi)
- `refactor:` (Perubahan kode tanpa mengubah logika fitur/bug)
- `docs:` (Pembaruan dokumentasi)
