---
name: project-explore
description: >-
  SOP Eksplorasi Codebase (/explore). Tur Kampus Kode Interaktif 4 Lapisan dengan Active Recall untuk membangun pemahaman mendalam tentang bisnis, alur data, dan struktur proyek.
forge_version: "{{FORGE_VERSION}}"
forged_at: "{{FORGED_AT}}"
project_name: "{{PROJECT_NAME}}"
---
# SOP EKSPLORASI CODEBASE (`/explore`)
# DOMAIN: {{PROJECT_NAME}}

## 📦 OUTPUT ARTIFACTS MAPPING
| Aksi / Permintaan | Artefak Hasil Kerja | Lokasi Penyimpanan Fisik |
| :--- | :--- | :--- |
| Tur Kampus Kode (`/explore`) | Tur Pedagogi Interaktif 4 Lapisan + Diagram Mermaid & *Active Recall* | In-Chat Markdown Response *(0 file ekstra agar bebas stale doc)* |

## ⚡ PROACTIVE TRIGGERS (EVENT-DRIVEN INVARIANTS)
### Lapisan 1: Universal Process Triggers (Statis — Berlaku untuk 100% Tech Stack)
* **WHEN pengguna memanggil `/explore`:**  
  $\implies$ **ALWAYS** jalankan inspeksi fisik (`view_file`, `list_dir`, atau `agent-lsp`) terhadap manifest proyek (`package.json`/`composer.json`), titik masuk (*entry point*), rute, dan `.agents/rules/ARCHITECTURE.md` secara senyap  
  $\implies$ **BEFORE** mencetak satu kata pun ke chat (Anti-Halusinasi & Tool-First Law).
* **WHEN membuka Lapisan 1 Orientasi:**  
  $\implies$ **ALWAYS** sajikan tujuan bisnis + 1 diagram Mermaid makro dalam 1 layar bersih  
  $\implies$ **BEFORE** menumpahkan daftar folder mentah (**DILARANG KERAS** memuntahkan ratusan baris *folder tree*!).
* **WHEN berada di dalam sesi `/explore`:**  
  $\implies$ **ALWAYS** jaga mode **100% Read-Only** — **DILARANG KERAS** memodifikasi file kode, membuat file dokumen baru, atau menjalankan perintah mutasi Git  
  $\implies$ **BEFORE** sesi berakhir (Eksplorasi adalah ruang aman untuk belajar).

---

> 🗺️ **FILOSOFI "GOOGLE MAPS KAMPUS" (BUKAN CETAK POHON FOLDER):**
> Bayangkan mahasiswa baru pertama kali masuk kampus. Memuntahkan daftar 100 nama ruangan tidak akan membuatnya paham — ia butuh dituntun berjalan pelan melewati 1 jalur nyata: *"Ini pintu gerbangnya, ini ruang administrasinya, dan ini ruang kelasnya."* Tujuan `/explore` adalah membangun **pemahaman mental model bisnis & alur data yang menempel di kepala**, bukan sekadar memamerkan daftar folder.

---

## 🎓 ALUR TUR PEDAGOGI INTERAKTIF 4 LAPISAN (GUIDED ACTIVE-RECALL TOUR)

AI **WAJIB** memandu developer melalui 4 lapisan berikut secara bertahap (1 lapisan per giliran respons):

### LAPISAN 1: ORIENTASI BISNIS & PETA 10.000 KAKI (*The "Why" First*)
Setelah membaca repo secara senyap (*Silent Inspection*), awali di **Baris 1 (Bottom Line First)** dengan 1 kalimat ringkas identitas proyek, lalu sajikan 3 blok ringkas dalam 1 layar:
1. **🎯 Tujuan Bisnis & Aktor:** Masalah nyata apa yang diselesaikan aplikasi ini dan siapa penggunanya (merujuk `.agents/rules/ARCHITECTURE.md` — 🟢 Verified).
2. **🗺️ Peta Makro Alur Sistem (1 Diagram Mermaid Sederhana):** Gambarkan hubungan antara **Pintu Masuk (*Entry Point*)**, **Etalase UI** *(jika ada)*, dan **Dapur Logika/Data** *(jika ada)* dengan menyebut nama folder induk utamanya saja (maksimal 5–7 kotak, BUKAN *folder tree* lengkap!).
3. **🔍 Status Keselarasan *Drift* (Confidence Tagging 🟢/🟡/🔴):** Laporkan singkat apakah struktur kode aktual cocok 100% dengan `.agents/rules/ARCHITECTURE.md` (🟢 Verified) atau ada pergeseran teknologi/folder yang perlu dicatat sebagai ADR (🔴 Assumed / Drift).

---

### LAPISAN 2: MENU PILIHAN JALUR FITUR (*Student Agency + Hard Stop*)
Tepat di bawah Lapisan 1, tawarkan **3 hingga 4 alur fitur nyata** yang hidup di repositori ini agar mahasiswa memilih sendiri rute belajarnya:
```markdown
### 🚶 Mau Mulai Jalan-Jalan dari Alur yang Mana?
1. **Alur A — [Nama Alur Nyata 1, misal: Bagaimana Produk Diambil & Tampil di Layar]**
2. **Alur B — [Nama Alur Nyata 2, misal: Bagaimana Form/Checkout Dikirim ke Server/WA]**
3. **Alur C — [Nama Alur Nyata 3, misal: Bagaimana Autentikasi Menjaga Area Admin]**

Pilih nomor alur yang paling bikin kamu penasaran (atau ketik nama fitur lain yang ingin kamu bedah)!
```
> 🛑 **HARD STOP LAPISAN 2:** AI **WAJIB BERHENTI TOTAL** di sini! Dilarang langsung membedah kode sebelum mahasiswa memilih alur yang ingin ditelusuri.

---

### LAPISAN 3: BEDAH 1 ALUR *END-TO-END* (*Request-to-Screen Trace*, Protokol 2-Ketukan)
Begitu mahasiswa memilih 1 alur, lacak alur tersebut dari ujung ke ujung dengan bukti fisik kode nyata:
1. **Jejak Langkah Konkret (Maksimal 4–5 Titik Kunci):** Tunjukkan rantai panggilan nyata lengkap dengan path & nomor baris (`path/to/file:L10-L25`), misal: *Interaksi User / Route $\rightarrow$ Controller / Handler $\rightarrow$ Service / Data Layer $\rightarrow$ Render Tampilan*.
2. **Analogi Eksistensial (*Makna Daun & Batang*):** Jelaskan *mengapa* berkas-berkas itu dipisah demikian dengan bahasa santai Kakak Tingkat (bukan sekadar membaca sintaks baris per baris!).
3. **Patuhi Protokol 2-Ketukan:** Maksimal ~200–250 kata per ketukan; jangan melempar ratusan baris kode utuh tanpa diminta.

---

### LAPISAN 4: *ACTIVE RECALL CHECK* (Kuis Santai Tanpa Menghakimi)
Di akhir penelusuran 1 alur pada Lapisan 3, tutup dengan **1 skenario ringan *Active Recall*** untuk mengunci pemahaman mental mahasiswa:
> *"🎯 **Tebak Santai (Biar Makin Nempel):** Misalnya besok dosen atau Tech Lead minta kita [skenario perubahan kecil yang realistis pada alur barusan, misal: mengganti teks tombol CTA / menambah 1 kolom validasi], kira-kira file mana dulu nih yang pertama kali bakal kamu buka? Santai aja, nggak ada nilai salah-benar di sini — kalau mau tebak silakan, atau ketik **'Lanjut alur lain'** / **'Sudah paham, lanjut `/edeate`'**!"*

* **Jika mahasiswa menebak:** Apresiasi usahanya dengan hangat (*No Shame Culture*), konfirmasi jawaban benarnya beserta alasan singkatnya, lalu tawarkan apakah ingin menelusuri 1 alur lain dari Menu Lapisan 2 atau sudah siap masuk ke siklus kerja (`/edeate` / `/grill-me`).

---

## 🎓 PEDAGOGI & PENJAGA KUALITAS (`/explore`)
* **Kapan Dipanggil:** 1 kali di hari pertama saat baru `git clone` repo, saat mahasiswa baru bergabung ke tim, atau kapan pun merasa tersesat di dalam kode. Tidak perlu dipanggil berulang pada setiap tiket mingguan.
* **No Shame Culture:** Jika mahasiswa mengaku bingung bahkan dengan istilah dasar (*route*, *component*, *controller*), AI wajib mundur 1 langkah dan menjelaskannya dengan analogi dunia kampus sebelum melanjutkan tur.
