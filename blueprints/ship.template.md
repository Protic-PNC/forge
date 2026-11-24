---
name: project-ship
description: >-
  SOP Kesiapan Rilis & Demo (/ship). Membungkus aplikasi mahasiswa menjadi rilis profesional dengan pemeriksaan keamanan .env, SemVer, CHANGELOG.md otomatis, dan Cheat Sheet Demo UAS.
forge_version: "{{FORGE_VERSION}}"
forged_at: "{{FORGED_AT}}"
project_name: "{{PROJECT_NAME}}"
---
# SOP KESIAPAN RILIS & DEMO (`/ship`)
# DOMAIN: {{PROJECT_NAME}}

## 📦 OUTPUT ARTIFACTS MAPPING
| Aksi / Permintaan | Artefak Hasil Kerja | Lokasi Penyimpanan Fisik |
| :--- | :--- | :--- |
| Rilis Milestone / Demo UAS (`/ship`) | Laporan Pre-Flight Release & *Demo Cheat Sheet* | In-Chat Markdown Response |
| Catatan Rilis Resmi | Berkas Changelog Terstruktur (SemVer) | `CHANGELOG.md` (root proyek) |

## ⚡ PROACTIVE TRIGGERS (EVENT-DRIVEN INVARIANTS)
### Lapisan 1: Universal Process Triggers (Statis — Berlaku untuk 100% Tech Stack)
* **WHEN pengguna memanggil `/ship`:**  
  $\implies$ **ALWAYS** jalankan audit kebersihan rahasia (*Secret & `.env` Hygiene*) serta verifikasi `git status` & *production build* Exit Code 0  
  $\implies$ **BEFORE** menyusun `CHANGELOG.md` atau menentukan nomor versi rilis (Cegah Kebocoran Token ke GitHub Publik).
* **WHEN hendak melakukan `git commit` atau menyarankan `git push` rilis:**  
  $\implies$ **ALWAYS** berhenti total (*Hard Stop*) dan minta konfirmasi eksplisit dari developer  
  $\implies$ **BEFORE** mengeksekusi mutasi Git permanen apa pun (Hukum Konsensus Modifikasi Fisik).
* **WHEN menemukan item milestone aktif yang belum lulus `/audit`:**  
  $\implies$ **ALWAYS** peringatkan developer dengan jujur (🟢 Verified dari `git status` & `DEVELOPMENT_ROADMAP.md`) dan tawarkan menjalankan `/audit` terlebih dahulu  
  $\implies$ **BEFORE** menerbitkan stempel versi rilis resmi.

---

> 🎁 **FILOSOFI "KERTAS KADO RILIS":**
> Kalian sudah bekerja keras membangun fitur dan melewati audit satu per satu. Perintah `/ship` memastikan karya kalian tidak diserahkan mentah-mentah — ia mengecek kebocoran rahasia `.env`, merapikan riwayat rilis (`CHANGELOG.md`), memberi stempel versi SemVer (`v1.0.0`), dan menyiapkan materi demo agar layak dipresentasikan di depan dosen maupun dipajang di portofolio industri.

---

## 🚀 ALUR 4 FASE GERBANG RILIS (`/ship`)

Awali setiap respons di **Baris 1 (Bottom Line First)** dengan status kesiapan rilis (**`READY TO SHIP`** / **`NEEDS CLEANUP`**).

### FASE 1: PRE-FLIGHT SECURITY, SECRET HYGIENE, & BUILD SANITY
AI **WAJIB** memverifikasi 4 gerbang keselamatan secara fisik di terminal/tool (berlabel 🟢 Verified):
1. **Audit Kebocoran `.env` & Rahasia:**
   - Periksa apakah berkas `.env` secara tidak sengaja ikut ter-track oleh Git (`git ls-files .env .env.local`). Jika ter-track $\rightarrow$ 🚨 **BLOCKER!**, pandu segera menghapusnya dari index Git (`git rm --cached .env`) dan pastikan `.gitignore` melindunginya.
   - Verifikasi `.env.example` sudah mencantumkan seluruh kunci variabel environment yang dibutuhkan tanpa mengisi nilai rahasianya.
   - Pindai cepat kode sumber terhadap indikasi *hardcoded* API key, password, atau token sensitif.
2. **Kebersihan Working Tree & Sinkronisasi Branch:**
   - Jalankan `git status` untuk memastikan tidak ada perubahan menggantung (*uncommitted changes*) atau berkas sampah sementara (misal `.tmp-openapi-main.json`).
3. **Production Build Sanity:**
   - Jalankan perintah build produksi proyek dan pastikan tuntas dengan **Exit Code 0** (`Recorded` dari terminal nyata — patuhi Tier 0 Anti-Stale!).
4. **Cek Keselarasan `DEVELOPMENT_ROADMAP.md`:**
   - Periksa item yang sudah selesai (`- [x]`) vs yang sengaja ditunda ke versi berikutnya agar jujur dicatat dalam ruang lingkup rilis.

---

### FASE 2: PENENTUAN VERSI SEMVER (EDUKATIF & RINGKAS)
Periksa versi terakhir di `CHANGELOG.md` (atau `package.json` jika ada), lalu pandu developer menentukan nomor versi rilis berikutnya sesuai **Semantic Versioning (`MAJOR.MINOR.PATCH`)**:
- **`v1.0.0` (Major / Rilis Perdana):** Rilis MVP utuh pertama siap demo/produksi, atau ada *breaking change* besar.
- **`v1.X.0` (Minor):** Penambahan fitur baru (`feat`) yang kompatibel dengan versi sebelumnya.
- **`v1.0.X` (Patch):** Murni perbaikan bug (`fix`) dan pemolesan minor.

> 🛑 **HARD STOP FASE 2:** Sajikan hasil Pre-Flight Fase 1 + rekomendasi nomor versi SemVer (beserta alasannya), lalu minta konfirmasi: *"Pre-flight aman. Apakah kita sahkan rilis ini sebagai **`vX.Y.Z`** dan langsung susun `CHANGELOG.md`-nya?"*

---

### FASE 3: GENERASI OTOMATIS `CHANGELOG.md`
Setelah versi disetujui:
1. **Prioritas Skrip Deterministik:** Jalankan skrip bawaan untuk merangkum riwayat Conventional Commits terbaru:
   ```bash
   python .agents/skills/project-ship/scripts/changelog_generator.py
   ```
   *(Fallback: jika Python tidak tersedia, baca `git log --oneline -n 50` secara fisik dan kelompokkan secara rapi ke kategori: **✨ Fitur Baru (`feat`)**, **🐛 Perbaikan Bug (`fix`)**, dan **🔧 Pemeliharaan/Arsitektur (`refactor`/`chore`)**).*
2. Tulis atau perbarui `CHANGELOG.md` di root proyek dengan tanggal rilis hari ini (`YYYY-MM-DD`) dan daftar perubahan yang mudah dibaca manusia (bukan sekadar dump hash commit mentah!).

---

### FASE 4: DEMO UAS / PORTOFOLIO CHEAT SHEET & RELEASE COMMIT HANDOFF
Setelah `CHANGELOG.md` tersimpan, sajikan **Paket Presentasi Rilis**:
1. **🎙️ Elevator Pitch & Cheat Sheet Demo (Siap Baca di Depan Dosen / Penguji):**
   - 3–4 kalimat narasi profesional tentang masalah yang diselesaikan, arsitektur kunci yang dibangun, dan bukti pengujian mutu yang telah dilalui.
   - Urutan skenario demo 3 menit (alur klik yang paling aman & memukau saat presentasi).
2. **📋 Checklist Deployment Cepat (Sesuai Stack di `ARCHITECTURE.md`):**
   - Langkah ringkas deploy (misal Cloudflare Pages / Vercel / VPS) + pengingat menyetel Environment Variables di dashboard hosting.
3. **📦 Perintah Commit & Push Rilis (Hard Stop Konsensus):**
   Sajikan perintah siap salin yang ramah pemula (AI **DILARANG** menjalankan `git push` sepihak tanpa izin eksplisit):
   ```bash
   git add CHANGELOG.md
   git commit -m "chore(release): prepare vX.Y.Z"
   git push origin main
   ```

---

## 🎓 PEDAGOGI & GAYA MENTOR (`/ship`)
* **Rayakan Pencapaian Mahasiswa:** Di akhir sesi `/ship`, berikan apresiasi tulus atas kerja keras mahasiswa menyelesaikan milestone ini. Tekankan bahwa kebiasaan membungkus rilis dengan SemVer, *secret hygiene*, dan `CHANGELOG.md` adalah pembeda utama antara tugas kuliah biasa dengan portofolio *Software Engineer* kelas industri.
