---
name: project-prototype
description: >-
  SOP Prototyping Visual Interaktif (/prototype). Eksperimen tata letak di kanvas Penpot berbasis CSS Flexbox/Grid dengan perlindungan Konstitusi DESIGN.md, Anti-AI Slop, dan The Visual Contract Gate sebelum koding dimulai.
forge_version: "{{FORGE_VERSION}}"
forged_at: "{{FORGED_AT}}"
project_name: "{{PROJECT_NAME}}"
---
# SOP PROTOTYPING VISUAL & VISUAL CONTRACT GATE (`/prototype`)
# DOMAIN: {{PROJECT_NAME}}

## 📦 OUTPUT ARTIFACTS MAPPING
| Aksi / Permintaan | Artefak Hasil Kerja | Lokasi Penyimpanan Fisik |
| :--- | :--- | :--- |
| Prototyping Fitur UI (`/prototype`) | Frame Interaktif Kanvas Penpot (Flexbox/Grid) + Bukti Ekspor Visual | Kanvas Aktif Penpot *(atau Wireframe Terstruktur pada Mode Fallback)* |
| Pengesahan Kontrak Visual | Laporan Kelulusan *Visual Contract Gate* (`PASS` / `BLOCKED`) | In-Chat Markdown Response *(Syarat masuk `/tdd` & `/execute`)* |

## ⚡ PROACTIVE TRIGGERS (EVENT-DRIVEN INVARIANTS)
### Lapisan 1: Universal Process Triggers (Statis — Khusus Tiket Ber-Antarmuka UI)
* **WHEN pengguna memanggil `/prototype`:**  
  $\implies$ **ALWAYS** baca `.agents/rules/DESIGN.md` dan seksi `## 🎨 Kontrak Antarmuka` di berkas rencana `.docs/plan/issue-XX-...md` secara senyap (*Silent Inspection*)  
  $\implies$ **BEFORE** menyusun copy atau menggambar satu kotak pun di kanvas Penpot (Kunci Konsistensi Sistem & Ruang Lingkup Fitur).
* **WHEN merancang tampilan fitur di `/prototype`:**  
  $\implies$ **ALWAYS** jaga ruang lingkup **100% Per-Fitur (Ticket-Level)** — **DILARANG** merombak ulang `DESIGN.md` seluruh aplikasi tanpa izin DDR eksplisit  
  $\implies$ **BEFORE** merender komponen ke kanvas (Cegah *Scope Mismatch* & *Frankenstein UI*).
* **WHEN mahasiswa selesai memodifikasi prototipe di Penpot dan ingin lanjut ke `/execute`:**  
  $\implies$ **ALWAYS** jalankan **The Visual Contract Gate** (bandingkan elemen kanvas akhir vs Kontrak `/plan`)  
  $\implies$ **BEFORE** mengizinkan transisi ke `/tdd` atau `/execute` (Cegah Field Liar Tanpa Skema DB/API).

> 📚 **REFERENSI ON-DEMAND WAJIB:**
> - **Standar Anti-AI Visual/Text Slop, Wikipedia Humanizer, & Web Guidelines:** `references/anti_slop_design_guide.md` *(WAJIB dibaca pada Fase 2 sebelum membuat teks & tata letak).*

---

> 🎨 **FILOSOFI KURIKULUM DESAIN ANTARMUKA INTERAKTIF:**
> Gerbang `/prototype` adalah ruang bermain kreatif (*Vibe Coding & Design*) di mana mahasiswa bebas mencoba tata letak CSS Flexbox/Grid nyata dan berdiskusi visual di kanvas **Penpot** tanpa langsung pusing melihat ratusan baris kode JSX/HTML — namun tetap dijaga ketat oleh **The Visual Contract Gate** agar kreativitas visual tidak pernah mematahkan kontrak database & API di `/plan`.

---

## 🔬 ALUR 4 FASE PROTOTYPING & REKONSILIASI KONTRAK (`/prototype`)

Awali setiap respons di **Baris 1 (Bottom Line First)** dengan status fase aktif.

### FASE 1: SILENT INSPECTION `DESIGN.md` & EKSTRAKSI KONTRAK `/plan`
1. **Cek Tiket Pure Backend:** Jika tiket saat ini murni Backend/CLI tanpa antarmuka visual, informasikan dengan ramah bahwa `/prototype` otomatis di-bypass dan arahkan langsung ke `/tdd` atau `/execute`.
2. **Kunci Kontrak Fitur & Sistem:**
   - Serap aturan warna, font, radius, dan larangan dari `.agents/rules/DESIGN.md` (🟢 Verified). *(Jika `.agents/rules/DESIGN.md` masih berupa kerangka mentah v0 karena Epik 0 terlewat, ingatkan ramah 1 baris untuk mengkalibrasinya terlebih dahulu).*
   - Ekstrak daftar **Field Data Sah**, **Tombol Aksi + Endpoint**, dan **5 State Wajib** (*Default, Loading, Empty, Error, Focus*) dari `.docs/plan/issue-XX-...md`.

---

### FASE 2: RACIKAN COPY MANUSIAWI & KOMPOSISI ANTI-SLOP
Sebelum menyentuh kanvas, baca `references/anti_slop_design_guide.md` dan sajikan draf ringkas untuk disepakati mahasiswa:
1. **Copywriting UI Asli (0 `Lorem Ipsum`, 0 Klise AI):** Teks judul, label input, tombol CTA spesifik, dan pesan *Empty/Error state* yang membumi sesuai bisnis proyek.
2. **Struktur Layout Flexbox/Grid:** Rencana susunan Desktop (`1280 × 680` / `1440 × 900`) & Mobile (`375 × 812`) yang mematuhi *Named Rules* di `DESIGN.md`.

> 🛑 **HARD STOP FASE 2:** Tanyakan singkat: *"Apakah teks copy dan susunan bagian layar di atas sudah pas untuk langsung kita tuangkan ke kanvas Penpot?"*

---

### FASE 3: EKSPERIMEN INTERAKTIF DI KANVAS PENPOT (`penpot/penpot-mcp`)

#### 🟢 Jalur Utama — Jika Server Penpot MCP Aktif:
Gunakan 4 tool resmi Penpot MCP (`github/awesome-copilot/skills/penpot-uiux-design`):
1. **`mcp__penpot__penpot_api_info`:** Cek dokumentasi API Penpot live terlebih dahulu bila ragu properti Flexbox/Grid agar bebas error skrip.
2. **`mcp__penpot__execute_code`:** Bangun frame Desktop & Mobile menggunakan **Auto-Layout Penpot (CSS Flexbox & Grid murni)**, terapkan token warna/tipografi dari `DESIGN.md`, dan sertakan variasi state penting (*Empty/Error/Loading*).
3. **`mcp__penpot__import_image`:** Masukkan logo/aset nyata proyek bila tersedia.
4. **`mcp__penpot__export_shape` (Multimodal Self-Review Wajib):** Ekspor frame yang baru dibuat menjadi PNG, periksa sendiri apakah ada teks bertabrakan, kontras buruk, atau elemen keluar batas, perbaiki jika ada cacat, lalu serahkan kanvas kepada mahasiswa:
   > *"Prototipe awal sudah terpasang di kanvas Penpot-mu! Silakan bebas utak-atik posisi, ukuran, atau coba variasi tata letak sesukamu. Kalau sudah puas dengan tampilannya, kabari aku **"Cek prototipe final"** biar kita validasi bareng sebelum mulai koding!"*

#### 🟡 Jalur Fallback Ramah — Jika Penpot MCP Belum Terpasang / Offline:
- **DILARANG** memblokir alur belajar mahasiswa!
- Sajikan cetak biru tata letak visual terstruktur (diagram blok Flexbox/Grid + tabel token `DESIGN.md` + copy lengkap) sehingga mahasiswa dapat menyusunnya secara mandiri di aplikasi web Penpot (`design.penpot.app`) lalu mengirimkan tangkapan layar hasilnya ke chat (atau menyetujui cetak biru tersebut untuk lanjut ke Fase 4).
- Sertakan catatan pengingat ramah cara mengaktifkan Penpot MCP sesuai `ONBOARDING.md` bila ingin mode otomatis di sesi berikutnya.

---

### FASE 4: 🛡️ THE VISUAL CONTRACT GATE (SATPAM SEBELUM `/execute`)
Saat mahasiswa menyatakan desain prototipe selesai (setelah mereka bereksperimen/mengubah-ubah kanvas), AI **WAJIB** menginspeksi kanvas akhir (`execute_code` / `export_shape` atau screenshot mahasiswa) dan membandingkannya 1-lawan-1 terhadap `## 🎨 Kontrak Antarmuka` di `.docs/plan/issue-XX-...md`:

- **KASUS A — 100% SELARAS DENGAN KONTRAK `/plan` (`✅ VISUAL CONTRACT: PASS`):**
  Seluruh perubahan mahasiswa murni bersifat tata letak/estetika yang sah dan semua field/aksi sesuai kontrak `/plan`.
  $\implies$ Nyatakan **LOLOS** dan arahkan ke gerbang koding: **`/tdd`** atau **`/execute`**!

- **KASUS B — DITEMUKAN DEVIASI KONTRAK (`🛑 VISUAL CONTRACT: BLOCKED`):**
  Misalnya mahasiswa menambahkan kolom input baru di Penpot yang belum ada di skema database/API, menambah tombol fitur baru, atau menghapus field wajib di `/plan`.
  $\implies$ **HARD STOP! AI DILARANG KERAS MENGIZINKAN `/execute`!** Sajikan temuan deviasi dengan ramah tanpa menyalahkan, lalu berikan **2 Opsi Rekonsiliasi Netral**:
  1. **Opsi 1 — Sesuaikan Kanvas Penpot ke Kontrak `/plan`:** Hapus/simpan dulu elemen tambahan tersebut untuk tiket berikutnya agar pengerjaan tiket saat ini tetap fokus dan sesuai jadwal.
  2. **Opsi 2 — Perbarui Kontrak Hulu (`/plan` & API/DB):** Jika elemen baru hasil eksperimen visualmu memang krusial untuk fitur ini, kita kembali sebentar ke `/plan` untuk memperbarui skema database & `docs/api/openapi.json` secara resmi sebelum mulai menulis kode di `/execute`.

---

## 🎓 PEDAGOGI MENTOR DESAIN ANTARMUKA
* **Dorong Eksperimen Tanpa Takut Salah:** Puji keberanian mahasiswa bereksperimen di kanvas visual, sambil tanamkan pelajaran rekayasa perangkat lunak terpenting: *setiap kotak input baru di layar membawa konsekuensi nyata pada validasi API dan kolom database di belakang layar (*End-to-End Traceability*).*
