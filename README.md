# 🛡️ Antigravity Plugin: Forge

**Forge** adalah sebuah meta-plugin (Scaffolder) yang dirancang untuk menginjeksi "Mentalitas Mentor Arsitek Senior" ke dalam AI Antigravity pada proyek baru mana pun. 

Dengan menjalankan *Forge Constitution*, Anda dapat secara otomatis membangun regulasi arsitektur, prosedur, dan rantai komando (Skill & Rules) standar Enterprise tanpa harus menulis ulang protokol dari nol.

## 🌟 Filosofi Inti
Forge tidak hanya menyalin file. Ia melakukan **Wawancara Konstitusi (The Forge Interview)** untuk memahami DNA proyek Anda (Frontend/Backend, Tech Stack, Tujuan Bisnis), lalu secara cerdas mencetak file yang relevan menggunakan sistem *Generation Directive*.

Forge mengatasi 3 masalah utama dalam kolaborasi AI-Developer:
1. **Yes-Man Syndrome:** Mencegah AI mengiyakan instruksi developer yang destruktif (Anti-Pattern, N+1 Query).
2. **Auto-Proceed Hijack:** Mencegah sistem AI melompat dari perencanaan ke eksekusi otomatis tanpa persetujuan eksplisit.
3. **Halusinasi Kode:** Memaksa AI menggunakan Panca Indera (MCP Database & Agent-LSP) sebelum menulis/menganalisis masalah.

## 🚀 Fitur & Senjata (The Two-Gateway Pipeline)
Setelah Forge diinjeksikan ke sebuah proyek, proyek tersebut akan memiliki 6 *Slash Commands* absolut:

**Gateway 1: Hulu (Ideasi)**
- `/edeate` → Merumuskan ide mentah menjadi Spesifikasi Arsitektur (Tiket Level 3).

**Gateway 2: Hilir (Eksekusi)**
- `/grill-me` → Interogasi arsitektur 1-lawan-1 untuk mencari solusi *trade-off* terbaik dari tiket eksisting.
- `/plan` → Merumuskan urutan eksekusi *bottom-up* yang murni.
- `/tdd` → Menulis skenario gagal (Strict Red Phase).
- `/execute` → Mengeksekusi kode produksi dengan *Blast-Radius Assessment*.
- `/audit` → Evaluasi statis dengan LSP dan pembuatan Pull Request via MCP GitHub.

## 💻 Instalasi (Super Mudah untuk Pemula)

Agar AI di komputer Anda mengenali perintah `/forge-constitution`, Anda harus memasang folder ini ke dalam "otak" Antigravity Anda. Pilih salah satu cara di bawah ini:

### Cara 1: Lewat Terminal (Paling Cepat)
Cukup buka **PowerShell** atau Terminal di VSCode Anda, lalu *copy-paste* perintah sakti ini dan tekan Enter:

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.gemini\config\plugins"; git clone https://github.com/Protic-PNC/forge.git "$HOME\.gemini\config\plugins\forge"
```

### Cara 2: Manual (Tanpa Coding/Terminal)
Jika Anda pusing melihat terminal, ikuti langkah *drag-and-drop* ini:
1. Di halaman GitHub ini, klik tombol hijau **Code** lalu pilih **Download ZIP**.
2. Ekstrak (Unzip) file yang baru saja didownload.
3. Ubah nama foldernya menjadi `forge` (huruf kecil semua).
4. Pindahkan folder `forge` tersebut ke dalam direktori tersembunyi ini di komputer Anda:
   👉 `C:\Users\NAMA_USER_KOMPUTER_ANDA\.gemini\config\plugins\`
   *(Jika folder `plugins` belum ada, buat saja foldernya secara manual).*

---
**⚠️ LAKUKAN INI SETELAH SELESAI:**
Tutup (Close) aplikasi IDE Anda sepenuhnya, lalu buka kembali agar sistem membaca "kekuatan" baru yang baru saja Anda pasang.
l
## ⚙️ Cara Penggunaan (The Injection)

1. Buka proyek/repositori baru Anda (yang masih kosong atau butuh regulasi).
2. Panggil agen Antigravity dan langsung panggil *slash command* berikut di chat:
   > `/forge-constitution`
3. AI akan bertransformasi menjadi **The Forge Master**. Cukup ikuti wawancara 5 tahap yang ia berikan:
   - Tahap 1: Penggalian DNA Proyek
   - Tahap 2: Pembentukan Visi Jangka Panjang
   - Tahap 3: Pembuatan Hukum & Aturan Bermain
   - Tahap 4: Konfigurasi Panca Indera (MCP)
   - Tahap 5: Injeksi Fisik (Pencetakan File ke dalam folder `.agents/` proyek Anda)

---
*Ditempa dengan kedisiplinan tingkat tinggi untuk melahirkan kode skala Enterprise.*
