---
name: project-edeate
description: >-
  Alat awal (Gerbang Hulu) untuk memecah ide/Epik di Roadmap menjadi spesifikasi tiket arsitektur Level 3 (GitHub Issue) yang siap dikerjakan di Gerbang Hilir.
forge_version: "{{FORGE_VERSION}}"
forged_at: "{{FORGED_AT}}"
project_name: "{{PROJECT_NAME}}"
---
# SOP IDEASI & PENEMUAN TIKET (`/edeate`)
# DOMAIN: {{PROJECT_NAME}}

## 📦 OUTPUT ARTIFACTS MAPPING
| Aksi / Permintaan | Artefak Hasil Kerja | Lokasi Penyimpanan Fisik |
| :--- | :--- | :--- |
| Sesi Ideasi (`/edeate`) | Spesifikasi Tiket Level 3 | In-Chat Markdown Response / GitHub Issue via MCP |
| Penautan Roadmap Induk | Sub-poin terhubung (`- [ ] (Issue #[Nomor])`) | `DEVELOPMENT_ROADMAP.md` (root proyek) |

---

> **Dokumen ini adalah hukum domain Hulu (Ideasi).**
> Ia berpasangan dengan `MASTER_RULES.md` (Hilir/Implementasi) dan `GIT_WORKFLOW.md` (Version Control). Ketiganya membentuk **Two-Gateway Pipeline** lengkap dari ide mentah hingga kode produksi.

---

## 🗺️ GAMBARAN BESAR: TWO-GATEWAY PIPELINE

```
IDE MENTAH ➔ GATEWAY 1 (Hulu: /edeate) ➔ TIKET LEVEL 3 (GitHub Issue) ➔ GATEWAY 2 (Hilir: /grill-me → /plan → /tdd → /execute → /audit) ➔ KODE PRODUKSI
```

> **Aturan Fundamental:** Sebuah ide **DILARANG** masuk ke Gateway 2 sebelum lulus Gateway 1 (tiket matang Level 3).

### Target Kematangan Tiket:
- **Level 1 (Mentah):** Ide kasar tanpa konteks/DoD ➔ ❌ TOLAK.
- **Level 2 (Story):** Ada use case umum tapi kriteria ambigu ➔ ⚠️ Revisi dulu.
- **Level 3 (Matang - Sweet Spot):** Invariant teruji, DoD berbasis uji otomatis, kontrak API/UI kokoh ➔ ✅ IZINKAN.

---

## 🚨 HUKUM MUTLAK & PEDAGOGI GERBANG HULU

1. **Active Mentorship & Safe Harbor:** AI bertindak sebagai Kakak Senior / Lead Architect yang ramah. Berikan opsi aman: developer boleh menjawab *"Ikut saranmu"*.
2. **Bottom Line First:** Vonis/pertanyaan inti ditaruh di awal, edukasi/analogi di bawahnya.
3. **Pacing 1 Isu Per Giliran & 2-Ketukan:** DILARANG memberondong banyak pertanyaan. Bahas HANYA 1 topik per giliran.
4. **Hukum 1 Sesi = Tepat 1 Atomic Ticket Level 3:** DILARANG mencetak >1 tiket per sesi. Epik besar wajib didekomposisi.
5. **Review Gate Sebelum Cetak:** AI WAJIB menyajikan Scope Plan di Fase 4 dan meminta ACC resmi di Fase 5 sebelum mencetak tiket di Fase 6.
6. **Code-Free & Git-Free Zone:** DIHARAMKAN menulis kode implementasi atau menjalankan perintah git di Hulu.

> 📚 **REFERENSI ON-DEMAND:**
> - Panduan Detail Track A vs B, Formula Wawancara, Kartu Vertikal, & 2-Ketukan: `references/dual_track_protocol.md`
> - Format Lengkap Tiket Level 3 & 3 Varian Matriks (BE / UI / Toolchain): `references/ticket_variants.md`
> - Daftar 16 Anti-Pattern & Penjaga Kualitas: `references/anti_patterns.md`

---

## 🔬 ALUR STATE-MACHINE GERBANG HULU (`/edeate`)

### FASE 0 — Penerimaan, Klasifikasi, & Pre-Flight Audit
1. **Klasifikasi Otomatis & Dual-Track Routing:**
   - Fitur Pengguna / UI / Form / I/O $\rightarrow$ 🟢 **TRACK A ([FEAT])** (Alur Penuh Socratic Bisnis).
   - Fondasi / Toolchain / Config / Refactor / Test $\rightarrow$ ⚡ **TRACK B ([ARCH]/[REFACTOR]/[INFRA])** (NFR Fast-Track 1 Ketukan, No Fictional Persona).
2. **Pre-Flight Codebase & Roadmap Audit:**
   AI WAJIB memeriksa fisik repositori (`view_file` / tool LSP):
   - Baca `DEVELOPMENT_ROADMAP.md`: validasi Epik [X] dan sub-poin `- [ ]` mana yang dibahas.
   - Baca modul/kode eksisting yang bersangkutan.
3. **Orientasi Sesi & Mini-Roadmap:**
   Sajikan temuan audit, klasifikasi tiket, dan agenda sesi.
   - 🛑 **HARD STOP:** Berhenti di respons pertama: *"Apakah kamu siap kita mulai bedah dari Topik 1.1?"* dan tunggu persetujuan.

---

### FASE 1 — Pilar Bisnis / Penguncian Sasaran NFR
- **Jika Track A:** Gali akar masalah, aktor/persona, batasan MVP, dan indikator sukses (Gunakan Formula A di `references/dual_track_protocol.md`). DILARANG membahas struktur folder/kode.
- **Jika Track B:** Kunci target Lighthouse/CWV, batasan kompatibilitas, dan DX dalam 1 ketukan konfirmasi (Gunakan Formula A-NFR di `references/dual_track_protocol.md`).
- 🛑 **HARD STOP:** 1 topik per respons. Tunggu jawaban developer.

---

### FASE 2 — Pilar Integrasi & Arsitektur Teknis
- Bedah segregasi komponen, struktur modul, pemetaan data, dan kontrak komunikasi.
- **Spektrum Opsi Kartu Vertikal:** Sajikan 2–3 opsi arsitektur sah (*Anti-Strawman & Anti-Dogma Angka 3*). Format kartu vertikal, judul netral, rekomendasi diletakkan di dek paling bawah (Gunakan Formula B di `references/dual_track_protocol.md`).
- 🛑 **HARD STOP:** 1 topik per respons. Tunggu keputusan developer.

---

### FASE 3 — Pilar Keamanan, Concurrency, & Invariant
- Deteksi risiko laten: otorisasi akses liar, race condition, data corruption.
- Kunci **Minimal 1–2 Business Invariant Absolut** dan **Rejection Criteria** (kapan PR wajib ditolak).
- *Topic Collapsing:* Pada tiket publik/FE murni, fokuskan ke UI Invariant (Zero Layout Shift, A11y). Pada Track B, fokuskan ke Toolchain Invariant (Build CI green).
- 🛑 **HARD STOP:** 1 topik per respons. Tunggu konfirmasi developer.

---

### FASE 4 — Rangkuman Konsensus Arsitektur & Scope Plan
AI menyajikan ringkasan sebelum tiket difinalisasi:
1. Konsensus Keputusan Arsitektur (Masalah riil, fakta audit, strategi terpilih).
2. Dekomposisi Epik (Daftar tiket; jika >1 tiket buat `.agents/epics/<nama-epik>.md`). Pilih TEPAT 1 TIKET untuk sesi ini.
3. Batasan Cakupan: **Scope IN** (berkas disentuh) vs **Scope OUT** (hal yang ditunda).
4. Rencana Invariant & Rejection Criteria.

---

### FASE 5 — Review Gate & ACC Tech Lead
AI WAJIB BERHENTI TOTAL dan bertanya:
> *"Rangkuman Konsensus Arsitektur dan Scope Plan di atas siap dievaluasi. Apakah batasan ruang lingkup ini disetujui untuk dirumuskan menjadi 1 Tiket Level 3 Sempurna?"*
- 🛑 **HARD STOP MACRO:** AI DILARANG mencetak tiket sebelum ada kata sepakat (**"ACC" / "Setuju" / "Lanjut"**).

---

### FASE 6 — Sintesis 1 Tiket Level 3 & Handover Gateway 2
1. **Cetak Tepat 1 Tiket Level 3:**
   AI WAJIB merujuk template dan memilih varian matriks yang sesuai di `references/ticket_variants.md`:
   - Varian A: Tiket Backend / Data Mutation (Policy Matrix & Service Pattern).
   - Varian B: Tiket Frontend UI / Komponen (UI State Matrix & Hydration Boundary).
   - Varian C: Tiket Track B Toolchain / Runtime (NFR Target Matrix & Auto-Verify).
2. **Penutupan Gerbang Wajib (3 Langkah Berurutan):**
   - **Tawarkan Otomasi GitHub Issue:** Tawarkan pembuatan Issue via MCP GitHub (`create_issue`).
   - **Tautkan Nomor Issue di `DEVELOPMENT_ROADMAP.md`:** 
     Ubah `- [ ] [Nama Fitur]` menjadi `- [ ] [Nama Fitur] (Issue #[Nomor])`.
     ⚠️ **DILARANG MENCENTANG `[x]`!** Hak mencentang selesai adalah milik `/audit` di hilir.
     ⚠️ **DILARANG MANIPULASI GIT!** Sesi `/edeate` adalah Git-Free Zone.
   - **Mandat Handover ke Gateway 2:**
     Arahkan developer untuk membuka branch baru dan memanggil Gateway 2:  
     👉 `/grill-me #[Nomor]`
