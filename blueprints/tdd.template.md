---
name: project-tdd
description: >-
  SOP Test-Driven Development (/tdd). Fase spesifikasi pengujian berlapis sebelum kode produksi.
forge_version: "{{FORGE_VERSION}}"
forged_at: "{{FORGED_AT}}"
project_name: "{{PROJECT_NAME}}"
---
# SOP TEST-DRIVEN DEVELOPMENT (`/tdd`)
# DOMAIN: {{PROJECT_NAME}}

## 🧪 PROTOKOL TEST-DRIVEN DEVELOPMENT (`/tdd`)
Saat pengguna menjalankan perintah `/tdd`:

Ini adalah **"Fase Spesifikasi"**, BUKAN fase implementasi. AI dan developer HANYA fokus menyusun skenario pengujian berdasarkan *Plan* hingga tes tersebut dipastikan gagal (*Red*).

### 1. 🛑 LARANGAN MUTLAK KODE PRODUKSI (STRICT RED PHASE)
- Di dalam sesi `/tdd`, AI **DILARANG KERAS** menyajikan atau menulis kode produksi:
<!-- GENERATION_DIRECTIVE: PRODUCTION_CODE_LAYERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INSTRUKSI UNTUK AI TAHAP 5 (INJEKSI FISIK):
Isi dengan layer produksi sesuai tech stack yang dilarang ditulis di fase TDD.
Misal BE: "Controller, Service, Model, FormRequest".
Misal FE: "Komponen React, API Routes, Server Actions, Schema ORM".
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-->
- Jika pengguna meminta kode produksi untuk memperbaiki tes yang gagal, AI **WAJIB MENOLAK** dan mengarahkan mereka secara tegas: *"Tes kita sudah berhasil gagal (Red) sesuai ekspektasi. Silakan panggil perintah `/execute` untuk mulai menulis kode produksi agar tes ini menjadi hijau (Green)."*

### 2. 🎯 RUANG LINGKUP WAJIB (MANDATORY TEST SCOPE)
AI **WAJIB** membuat jenis tes yang relevan untuk setiap fitur/tiket:
<!-- GENERATION_DIRECTIVE: MANDATORY_TEST_SCOPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INSTRUKSI UNTUK AI TAHAP 5 (INJEKSI FISIK):
Isi dengan jenis-jenis tes secara komprehensif dan berlapis (tanpa batas kuota)
yang relevan sesuai standar Enterprise tech stack.
Contoh BE: 1. Feature Test (HTTP/E2E), 2. Unit Test (Service Isolation).
Contoh FE: 1. Integration Test (Component RTL), 2. Unit Test (Hook/Store).
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-->

### 3. 🏭 MANDAT DATA DUMMY (DATA FIXTURE YANG SEHAT)
- AI **DILARANG** menggunakan data statis/manual untuk *setup* data tes.
- AI **WAJIB** menggunakan mekanisme *data fixture* standar tech stack ini:
<!-- GENERATION_DIRECTIVE: TEST_DATA_FIXTURE_STRATEGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INSTRUKSI UNTUK AI TAHAP 5 (INJEKSI FISIK):
Isi sesuai mekanisme fixture standar tech stack.
Misal BE: Factory (User::factory()->create()).
Misal FE: MSW (Mock Service Worker) dan fixture JSON dummy.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-->

### 4. 🚑 PENANGANAN ERROR (DIRECT SOLUTION)
- Jika tes yang sudah ditulis dijalankan oleh pengguna dan mengalami *error* konfigurasi/teknis, AI **WAJIB langsung menyodorkan kode perbaikan/jawaban yang benar**.
- Dilarang memberikan jawaban berteka-teki (*Socratic Method/Hint*). AI harus langsung menjadi asisten *pair-programming* yang memberikan solusi presisi agar developer bisa kembali fokus pada *flow*.

### 5. SIKLUS PENUTUPAN `/tdd`
Setelah skenario tes ditulis dan dikonfirmasi gagal (*Red*) karena belum ada implementasinya:
1. AI merayakan status merah tersebut.
2. AI **WAJIB BERHENTI** bekerja dan memberikan pancingan *Action Hook*: *"Semua spesifikasi tes telah dirancang dan sukses menghasilkan pesan Error (Red). Ketik `/execute` untuk beralih ke fase implementasi agar kita bisa menghijaukannya (Green)!"*
