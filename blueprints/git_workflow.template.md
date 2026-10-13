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
  - `feat/<nomor-issue>-<ringkasan-fitur>` (Contoh: `feat/12-setup-prisma`)
  - `fix/<nomor-issue>-<ringkasan-bug>` (Contoh: `fix/44-typo-header`)
  - `refactor/<nomor-issue>-<nama-modul>` (Contoh: `refactor/09-cleanup-service`)

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
