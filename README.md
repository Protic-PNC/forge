# 🛡️ Antigravity & Hermes Plugin: Forge

**Forge** adalah sebuah meta-plugin (Scaffolder) yang dirancang untuk menginjeksi "Mentalitas Mentor Arsitek Senior" ke dalam AI Antigravity IDE maupun Hermes Agent CLI pada proyek baru mana pun.

Dengan menjalankan *Forge Constitution*, Anda dapat secara otomatis membangun regulasi arsitektur, prosedur, dan rantai komando (Skill & Rules) standar Enterprise tanpa harus menulis ulang protokol dari nol.

## 🌟 Filosofi Inti
Forge tidak hanya menyalin file. Ia melakukan **Wawancara Konstitusi (The Forge Interview)** untuk memahami DNA proyek Anda (Frontend/Backend, Tech Stack, Tujuan Bisnis), lalu secara cerdas mencetak file yang relevan menggunakan sistem *Generation Directive*.

Forge mengatasi 3 masalah utama dalam kolaborasi AI-Developer:
1. **Yes-Man Syndrome:** Mencegah AI mengiyakan instruksi developer yang destruktif (Anti-Pattern, N+1 Query).
2. **Auto-Proceed Hijack:** Mencegah sistem AI melompat dari perencanaan ke eksekusi otomatis tanpa persetujuan eksplisit.
3. **Halusinasi Kode:** Memaksa AI menggunakan Panca Indera (MCP Database & Agent-LSP) sebelum menulis/menganalisis masalah.

## 🚀 Fitur & Senjata (The Two-Gateway Pipeline)
Setelah Forge diinjeksikan ke sebuah proyek, proyek tersebut akan memiliki 7 *Slash Commands* absolut:

**Gateway 1: Hulu (Ideasi)**
- `/edeate` → Merumuskan ide mentah menjadi Spesifikasi Arsitektur (Tiket Level 3).

**Gateway 2: Hilir (Eksekusi)**
- `/grill-me` → Interogasi arsitektur 1-lawan-1 untuk mencari solusi *trade-off* terbaik dari tiket eksisting.
- `/plan` → Merumuskan urutan eksekusi *bottom-up* yang murni.
- `/tdd` → Menulis skenario gagal (Strict Red Phase).
- `/execute` → Mengeksekusi kode produksi dengan *Blast-Radius Assessment*.
- `/audit` → Evaluasi statis dengan LSP dan pembuatan Pull Request via MCP GitHub.
- `/debug` → Investigasi anomali/akar masalah berbasis AST dan bukti sebelum penulisan patch.

## 💻 Instalasi & Konfigurasi

Forge didukung secara penuh untuk pengguna **Antigravity IDE** (berbasis editor) maupun **Hermes Agent** (berbasis terminal). Silakan pilih lingkungan kerja yang Anda gunakan:

### Opsi A: Instalasi untuk Hermes Agent (Native CLI)

Hermes Agent adalah platform *command-line* paling optimal untuk menjalankan Forge karena dukungannya yang kuat terhadap *persistent memory* dan *prompt caching*.

1. Buka **PowerShell** di Windows Anda.
2. Jalankan perintah satu baris ini untuk mengunduh Forge dan mengaktifkannya sebagai *Global Skill* di Hermes:
   ```powershell
   git clone https://github.com/Protic-PNC/forge.git "$env:LOCALAPPDATA\hermes\forge"; New-Item -ItemType Junction -Path "$env:LOCALAPPDATA\hermes\skills\forge-constitution" -Value "$env:LOCALAPPDATA\hermes\forge\skills\forge-constitution"; New-Item -ItemType Junction -Path "$env:LOCALAPPDATA\hermes\skills\forge-update" -Value "$env:LOCALAPPDATA\hermes\forge\skills\forge-update"
   ```
3. Selesai! Anda bisa langsung membuka terminal di folder proyek mana pun, ketik `hermes`, lalu jalankan `/forge-constitution` atau `/forge-update`.

### Opsi B: Instalasi untuk Antigravity IDE

1. Buka **PowerShell** atau Terminal di dalam VS Code Anda.
2. Jalankan perintah di bawah ini untuk mengkloning repositori Forge ke dalam direktori *plugin* internal Antigravity:
   ```powershell
   New-Item -ItemType Directory -Force -Path "$HOME\.gemini\config\plugins"; git clone https://github.com/Protic-PNC/forge.git "$HOME\.gemini\config\plugins\forge"
   ```
3. **PENTING:** Tutup (Close) aplikasi IDE Anda sepenuhnya, lalu buka kembali agar sistem membaca "kekuatan" baru yang baru saja Anda pasang.

## 🔄 Pembaruan (Update) Plugin

Jika ada versi terbaru dari Forge dan Anda ingin memperbaruinya, cukup buka PowerShell dan jalankan perintah *pull* sesuai lingkungan yang Anda instal:

* **Pengguna Hermes Agent:**
  ```powershell
  Set-Location "$env:LOCALAPPDATA\hermes\forge"; git pull
  ```

* **Pengguna Antigravity IDE:**
  ```powershell
  Set-Location "$HOME\.gemini\config\plugins\forge"; git pull
  ```

*(Catatan untuk pengguna Antigravity: Jangan lupa *restart* IDE Anda setelah melakukan pembaruan).*

### Sinkronisasi Konstitusi Lokal (`/forge-update`)

Setelah melakukan `git pull` pada plugin Forge global, proyek-proyek Anda yang sudah di-forge sebelumnya **TIDAK** otomatis ter-update. Untuk menyinkronkan konstitusi lokal proyek dengan versi Forge terbaru:

1. Buka repositori proyek yang ingin diperbarui.
2. Panggil *slash command* berikut di chat agen AI:
   > `/forge-update`
3. AI akan menjalankan **Declarative Re-render**:
   - Membaca target pembaruan dari `plugin.json` rilis terbaru (hanya memproses berkas yang berubah, hemat 70%+ token).
   - Mengambil data keputusan DNA proyek secara deterministik dari `.agents/forge_manifest.json`.
   - Menampilkan rangkuman rilis dan meminta checkpoint git.
   - Merender ulang berkas blueprint yang terdampak secara terisolasi satu per satu.
   - Memberikan kendali penuh kepada Git (`git diff`) untuk meninjau perubahan teks nyata.

## ⚙️ Cara Penggunaan (The Injection)

1. Buka proyek/repositori baru Anda (yang masih kosong atau butuh regulasi).
2. Panggil agen AI (Hermes / Antigravity) dan langsung panggil *slash command* berikut di chat:
   > `/forge-constitution`
3. AI akan bertransformasi menjadi **The Forge Master**. Cukup ikuti wawancara 5 tahap yang ia berikan:
   - Tahap 1: Penggalian DNA Proyek
   - Tahap 2: Pembentukan Visi Jangka Panjang
   - Tahap 3: Pembuatan Hukum & Aturan Bermain
   - Tahap 4: Konfigurasi Panca Indera (MCP)
   - Tahap 5: Injeksi Fisik (Pencetakan Brankas DNA `.agents/forge_manifest.json` dan seluruh file konstitusi ke dalam folder `.agents/` proyek Anda)

---

*Ditempa dengan kedisiplinan tingkat tinggi untuk melahirkan kode skala Enterprise.*