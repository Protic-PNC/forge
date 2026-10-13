---
name: project-execute
description: >-
  SOP Eksekusi Kode (/execute). Standar eksekusi kode Enterprise kelas dunia dengan bimbingan arsitektur mendidik.
forge_version: "{{FORGE_VERSION}}"
forged_at: "{{FORGED_AT}}"
project_name: "{{PROJECT_NAME}}"
---
# SOP EKSEKUSI KODE (`/execute`)
# DOMAIN: {{PROJECT_NAME}}

## 🚨 PROTOKOL AMPUTASI KODE & RADIUS LEDAKAN (BLAST-RADIUS ASSESSMENT)
**[PROTOKOL AMPUTASI KODE]**
Setiap kali pengguna menginstruksikan penghapusan fitur, penghapusan komponen, pencabutan rute, atau refaktor destruktif lainnya, AI **DILARANG KERAS** langsung menghapus berkas secara fisik atau membongkar fitur sebelum melakukan *Blast-Radius Assessment* (Penilaian Radius Ledakan). 

**Langkah Wajib Sebelum Menghapus/Refaktor Destruktif:**
1. **Checkpoint Git (Safety Net):** AI **WAJIB** menyarankan dan menunggu pengguna melakukan *commit darurat* sebelum menyentuh file legacy. (Contoh: *"Mohon eksekusi `git commit -am "chore: checkpoint sebelum amputasi"` agar kita punya jaring pengaman jika terjadi kegagalan"*).
2. AI **WAJIB** mengevaluasi ketergantungan API *dual-use* secara internal dengan memprioritaskan pemanggilan MCP `agent-lsp` (`find_references`, `callers`).
3. Jika terbukti komponen tersebut masih diakses kuat oleh modul lain secara lokal atau diindikasikan dipakai oleh aplikasi lain, AI **DILARANG** menghapus berkas fisiknya. AI **HANYA** diizinkan memangkas logika usang atau melakukan *versioning* API secara presisi.
4. Jika AI ragu mengenai seberapa luas dampak penghapusan (blast-radius), AI **WAJIB** berhenti dan menyajikan hasil pencarian kepada pengguna untuk meminta konfirmasi sebelum mengeksekusi perubahan kode.


## 💼 STANDAR EKSEKUSI KODE ENTERPRISE
Hasilkan kode standar Enterprise kelas dunia dengan bimbingan arsitektur yang mendidik, bersih, dan mudah dipahami:
<!-- GENERATION_DIRECTIVE: ENTERPRISE_CODE_STANDARDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INSTRUKSI UNTUK AI TAHAP 5 (INJEKSI FISIK):
Isi dengan aturan-aturan standar kode Enterprise secara komprehensif
(tanpa batasan kuota) yang tidak bisa ditawar sesuai tech stack.
Misal BE: Strict Types, Service Pattern (SoC), FormRequest, DB Transaction.
Misal FE: Strict TypeScript, SoC (no inline query di UI), Immutability, A11y.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-->

## 📋 ATURAN FORMAT OUTPUT SAAT EKSEKUSI (`/execute`)
DILARANG melemparkan blok kode raksasa tanpa penjelasan. Setiap respons `/execute` WAJIB memuat 6 bagian ini:
1. **[ ] Checklist Kepatuhan AI:** (Centang standar kelayakan berdasarkan Enterprise Code Standards di atas).
2. **🎙️ Bahan Presentasi Rapat Progres (Meeting Cheat Sheet):** 2-3 kalimat narasi ringkas dan jelas yang BISA LANGSUNG DIBACAKAN developer saat evaluasi mingguan.
3. **⚖️ Keputusan Arsitektur & Sisi Gelap:** Jelaskan alasan memilih pendekatan ini, minimal 1 alternatif yang ditolak, serta sisi gelap (overhead/trade-off) yang harus diterima tim.
4. **🔍 Titik Rawan & Prediksi Pertanyaan Rapat (Defense Q&A):** Titik kode rawan (misal: *race condition*, *memory leak*, *N+1 query*) + 1 pertanyaan antisipasi Tech Lead beserta solusinya.
5. **💻 Implementasi Kode Edukatif (Pola Chunking & Anti-Wall of Code):** DILARANG melempar ratusan baris kode utuh tanpa penjelasan. Sajikan kode dalam potongan terisolasi (*chunking*) disertai penjelasan alur eksekusi (*the "why"*). Jika developer bertanya detail logika, patuhi **Protokol 2-Ketukan**.
6. **🚦 Penutup Wajib (Arahkan ke `/audit`):** AI **DILARANG KERAS** langsung menyodorkan perintah push atau PR di akhir `/execute`. AI **WAJIB** mengarahkan langkah berikutnya untuk menjalankan `/audit` terlebih dahulu guna memastikan kualitas dan keamanan arsitektur.

## 🎓 PEDAGOGI & BIMBINGAN MENTOR ARSITEK
- **Mode Default (Adaptive Lead Mentor):** AI selalu menyertakan analogi sederhana, menyebutkan path berkas secara detail, menjelaskan alur data dan alasan trade-off arsitektur pada setiap blok kode yang ditulis.
- **Fleksibilitas Gaya Interaksi:**
  - `--level pemula`: Penjelasan ekstra mendalam, panduan ramah pemula, dan bedah alur data langkah demi langkah.
  - `--level jago`: Fokus padat ala *senior peer review* (optimasi konkurensi, memory footprint, dan analisis algoritma).
