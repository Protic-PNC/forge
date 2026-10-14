---
forge_version: "{{FORGE_VERSION}}"
forged_at: "{{FORGED_AT}}"
project_name: "{{PROJECT_NAME}}"
---
# GIT WORKFLOW PROTOCOL: {{PROJECT_NAME}}

> Dokumen ini mendikte bagaimana kode dikelola, diamankan, dan digabungkan oleh tim di repositori ini.
> Seluruh anggota tim dan AI WAJIB mematuhi protokol isolasi dan perlindungan branch ini tanpa kompromi.

---

## 1. Strategi Kolaborasi & Isolasi
- **Model Percabangan Utama:** {{GIT_BRANCHING_STRATEGY_DECISION}}
- **Hukum Kesucian Branch Utama (`main`):**
  - **DILARANG KERAS** melakukan `git commit` atau `git push` langsung ke branch `main`.
  - Seluruh pengerjaan fitur baru atau perbaikan bug wajib diisolasi di dalam branch kerja khusus.
- **Aturan Penamaan Branch:** Wajib menggunakan awalan tipe dan nomor issue resmi:
  - `feature/issue-<nomor>-<nama-fitur>` (Contoh: `feature/issue-12-setup-prisma`)
  - `fix/issue-<nomor>-<nama-bug>` (Contoh: `fix/issue-44-typo-header`)
  - `refactor/issue-<nomor>-<nama-modul>` (Contoh: `refactor/issue-09-cleanup-service`)

### 1.1 Kunci Branch Selama Siklus Pengerjaan (Stick to Current Branch)
- **Pembuatan Branch Hanya di Pintu Masuk:** Pembuatan branch isolasi **HANYA BERLAKU SATU KALI DI PINTU MASUK TIKET (`/grill-me` atau `/debug`)**.
- **Kunci Branch Aktif:** Pada tahapan `/plan`, `/tdd`, `/execute`, dan `/audit`, AI **DILARANG KERAS** menyodorkan perintah `git checkout main`, `git pull`, atau `git checkout -b` lagi. Developer dan AI **WAJIB TETAP BERADA** di branch isolasi aktif tersebut hingga seluruh siklus selesai.
- **Klausa Pengecualian Sandbox (`/edeate`):** Sesi `/edeate` adalah zona aman ideasi hulu. AI **DILARANG KERAS** memicu perintah Git apa pun (`git checkout`, `git pull`, `git checkout -b`) di dalam sesi `/edeate`.
- **Posisi Pasca-PR (Tetap di Branch Tiket):** Setelah tahap `/audit` dan pembuatan PR selesai, developer **TETAP BERADA** di branch tiket aktif tersebut untuk bersiap jika ada revisi dari Tech Lead. Perpindahan kembali ke `main` (`git checkout main && git pull origin main`) **HANYA DAN EKSKLUSIF** dilakukan saat membuka tiket baru di `/grill-me`.

---

## 2. Kebijakan Pull Request (The Security Gate)
- **Otorisasi Merge:** {{PULL_REQUEST_APPROVAL_POLICY}}
- **Syarat Mutlak Lolos PR (Gerbang Karantina):** 
  1. **Zero Failing Tests:** Seluruh pengujian otomatis wajib 100% lulus (Green).
  2. **Audit Approval:** Wajib diperiksa menggunakan perintah `/audit` dari AI sebelum di-*merge*. AI akan memblokir proses jika ada cacat arsitektur atau celah keamanan.
  3. **Zero Merge Conflict:** Branch kerja wajib disinkronkan dengan `main` terbaru sebelum evaluasi PR final.
  4. **Hygiene Check:** Tidak ada file rahasia (`.env`), file sampah lokal (`.DS_Store`, build cache), atau `console.log` yang lolos.
- **Strategi Penggabungan (Merge Strategy):**
  - Gunakan **Squash and Merge** saat menggabungkan PR ke `main` agar histori produksi tetap linier dan atomik per-fitur.
- **Kebijakan Pelestarian Branch (Learning & Presentation Archive):**
  - **DILARANG MENGHAPUS BRANCH SETELAH MERGE.**
  - Seluruh branch kerja tetap dilestarikan di repositori remote sebagai artefak portofolio, bahan evaluasi/presentasi progres tim, serta laboratorium *reverse engineering* bagi anggota baru dan adik tingkat.

---

## 3. Semantic Commit Messages
Semua pesan commit wajib bermakna dan mematuhi konvensi *Conventional Commits*:
- `feat:` (Penambahan fitur atau komponen baru)
- `fix:` (Perbaikan bug atau anomali sistem)
- `test:` (Penambahan atau perbaikan skenario pengujian otomatis)
- `refactor:` (Perubahan kode tanpa mengubah logika fitur/bug)
- `chore:` (Pembaruan dependencies, konfigurasi, atau build tools)
- `docs:` (Pembaruan dokumentasi atau panduan onboarding)
