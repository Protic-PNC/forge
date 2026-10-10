# SOP TEST-DRIVEN DEVELOPMENT (`/tdd`)
# DOMAIN: {{PROJECT_NAME}}

## 🧪 PROTOKOL TEST-DRIVEN DEVELOPMENT (`/tdd`)
Saat pengguna menjalankan perintah `/tdd`:

Ini adalah **"Fase Spesifikasi"**, BUKAN fase implementasi. AI dan developer HANYA fokus menyusun skenario pengujian berdasarkan *Plan* hingga tes tersebut dipastikan gagal (*Red*).

### 1. 🛑 LARANGAN MUTLAK KODE PRODUKSI (STRICT RED PHASE)
- Di dalam sesi `/tdd`, AI **DILARANG KERAS** menyajikan atau menulis kode produksi ({{PRODUCTION_CODE_LAYERS}}).
  *(Catatan Injektor: Isi dengan layer produksi sesuai tech stack. Misal BE Laravel: "Controller, Service, Model, FormRequest". Misal FE React: "Component, Hook, Store, API Client").*
- Jika pengguna meminta kode produksi untuk memperbaiki tes yang gagal, AI **WAJIB MENOLAK** dan mengarahkan mereka secara tegas: *"Tes kita sudah berhasil gagal (Red) sesuai ekspektasi. Silakan panggil perintah `/execute` untuk mulai menulis kode produksi agar tes ini menjadi hijau (Green)."*

### 2. 🎯 RUANG LINGKUP WAJIB (MANDATORY TEST SCOPE)
AI **WAJIB** membuat 2 jenis tes untuk setiap fitur/tiket:
{{MANDATORY_TEST_SCOPE}}
*(Catatan Injektor: Isi dengan jenis-jenis tes secara komprehensif dan berlapis (tanpa batas kuota) yang relevan sesuai standar Enterprise tech stack. Contoh:*
- *BE Laravel: "1. Feature Test (HTTP/E2E): Simulasi request HTTP ke endpoint, periksa respons JSON termasuk FormRequest validasi 422, verifikasi mutasi database (assertDatabaseHas). 2. Unit Test (Service Isolation): Tes class Service secara murni terisolasi dengan Mocking dependensi."*
- *FE React: "1. Integration Test (React Testing Library): Render komponen secara utuh, simulasi interaksi user (click, input), verifikasi perubahan DOM. 2. Unit Test (Hook/Store Isolation): Tes custom hook atau state store secara terisolasi dengan mock API response.")*

### 3. 🏭 MANDAT DATA DUMMY (DATA FIXTURE YANG SEHAT)
- AI **DILARANG** menggunakan data statis/manual untuk *setup* data tes.
- AI **WAJIB** menggunakan mekanisme *data fixture* standar tech stack ini:
  {{TEST_DATA_FIXTURE_STRATEGY}}
  *(Catatan Injektor: Isi sesuai tech stack. Misal BE Laravel: "Gunakan Factory (User::factory()->create()). Jika Factory belum ada, tugas pertama di sesi /tdd adalah menulis Factory tersebut." Misal FE React: "Gunakan MSW (Mock Service Worker) untuk mock API response dan fixture JSON untuk data dummy.")*

### 4. 🚑 PENANGANAN ERROR (DIRECT SOLUTION)
- Jika tes yang sudah ditulis dijalankan oleh pengguna dan mengalami *error* konfigurasi/teknis, AI **WAJIB langsung menyodorkan kode perbaikan/jawaban yang benar**.
- Dilarang memberikan jawaban berteka-teki (*Socratic Method/Hint*). AI harus langsung menjadi asisten *pair-programming* yang memberikan solusi presisi agar developer bisa kembali fokus pada *flow*.

### 5. SIKLUS PENUTUPAN `/tdd`
Setelah skenario tes ditulis dan dikonfirmasi gagal (*Red*) karena belum ada implementasinya:
1. AI merayakan status merah tersebut.
2. AI **WAJIB BERHENTI** bekerja dan memberikan pancingan *Action Hook*: *"Semua spesifikasi tes telah dirancang dan sukses menghasilkan pesan Error (Red). Ketik `/execute` untuk beralih ke fase implementasi agar kita bisa menghijaukannya (Green)!"*
