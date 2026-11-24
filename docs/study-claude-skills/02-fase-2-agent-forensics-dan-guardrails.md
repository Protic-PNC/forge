# Fase 2 (Revisi): Agent Forensics, Deterministic Gates & Analisis Komparasi FORGE
**Sumber Referensi:** `alirezarezvani/claude-skills/engineering/` (`agent-run-forensics`, `human-gate`, `skill-retro`)  
**Studi Kasus Nyata:** Komparasi dengan modul `/audit` dan kontrol alur pada **FORGE**.

---

## 1. Pertanyaan Mendasar: Kapan Skill-Skill Ini Dipanggil?

Skill forensik dan guardrails tidak bekerja seperti generator kode biasa. Mereka dipanggil pada momen-momen kritis berikut:

```
[ Siklus Tugas Agen ]
  1. Perencanaan (Plan/Design) ───► [ DIPANGGIL: human-gate ] ───► (Terkunci sampai manusia approve)
  2. Eksekusi & Coding
  3. Validasi & Audit ────────────► [ DIPANGGIL: agent-run-forensics ] ───► (Cek transkrip: benar lulus atau halusinasi?)
  4. Evaluasi Akhir Sesi ─────────► [ DIPANGGIL: skill-retro ] ───► (Evaluasi kelemahan instruksi)
```

### A. Kapan `agent-run-forensics` Dipanggil?
Skill ini dipanggil pada 3 situasi:
1. **Pertanyaan Penyelidikan Riwayat (History Inquiry):**  
   Ketika user atau reviewer bertanya:  
   > *"Kenapa kamu mengubah file auth.ts?", "Apakah test tadi beneran lolos?", "Tunjukkan perintah apa saja yang kamu jalankan 10 menit lalu."*
2. **Post-Mortem Insiden (Debugging Regresi):**  
   Ketika sistem tiba-tiba rusak setelah sesi coding selesai, dan kita butuh tahu langkah mana yang menjadi biang kerok perubahan file diam-diam (*silent edit*).
3. **Verifikasi Otomatis Sebelum PR (Pull Request Gate):**  
   Sistem memanggil tool ini untuk memvalidasi bahwa klaim agen (*"Semua 42 unit test lulus"*) benar-benar tercatat di terminal dengan exit code 0 dan tidak ada status `STALE`.

### B. Kapan `human-gate` Dipanggil?
Skill ini dipanggil **tepat di perbatasan antara fase perencanaan dan fase eksekusi destruktif**:
* Setelah agen selesai menyusun rencana migrasi arsitektur / DDL database / PRD fitur besar.
* Agen **membuka gate** (`human_gate.py open`), menyajikan link review, lalu **wajib menghentikan giliran (Stop Turn)**. Agen dilarang menulis satu baris kode pun sebelum file persetujuan ditandatangani oleh manusia.

### C. Kapan `skill-retro` Dipanggil?
Dipanggil secara periodik (misal: akhir pekan atau setelah 20 sesi interaksi) ketika tim merasa:
> *"Kenapa agen kita sering mengulang-ulang perintah yang sama?", "Kenapa agen sering salah paham saat disuruh TDD?"*

---

## 2. Bedah 3 Mekanisme Kritis Level Enterprise

1. **`agent-run-forensics` (Audit Transkrip Nyata vs Ingatan Halusinasi):**
   * Tidak percaya pada ingatan AI. Selalu membaca rekaman transkrip mentah sistem (`transcript.jsonl`).
   * **Deteksi STALE Test:** Menandai peringatan bahaya jika ada tes unit yang lulus, namun setelah itu AI mengedit kode lagi tanpa menjalankan tes ulang.
   * **Pemisahan `recorded` vs `inferred`:** Membedakan antara fakta tercatat sistem (command asli & exit code) vs asumsi logika AI.
2. **`human-gate` (Palang Pintu Deterministik):**
   * Menggunakan file sidecar persetujuan (`<nama-file>.review.md`).
   * Menggunakan exit code terminal (Exit code 2 = BLOCKED). Jika gate masih blocked karena ada `BLOCKER` atau `MAJOR` yang belum tuntas, agen secara sistemik **tidak bisa melaporkan tugas selesai**.
3. **`skill-retro` (Evaluasi Diri Berbasis Bukti Transkrip):**
   * Menilai efektivitas instruksi prompt bukan dari perasaan developer, melainkan dari data transkrip: berapa kali command gagal, di mana AI stuck looping, dan instruksi mana yang membingungkan.

---

## 3. Komparasi Nyata: Modul `/audit` & Guardrails FORGE vs Standar Enterprise

Plugin FORGE kita memiliki modul `/audit` yang sangat canggih dan protokol kontrol `HARD STOP MACRO`. Namun, mari kita bandingkan secara objektif dengan mekanisme enterprise:

| Parameter | Modul `/audit` & Kontrol FORGE Saat Ini | Standar Enterprise (`agent-run-forensics` & `human-gate`) | Status Evaluasi |
| :--- | :--- | :--- | :--- |
| **Objek yang Diaudit** | **Kode Aplikasi & Hasil Smoke.** Memeriksa git status, static lint, unit test, dan Playwright Visual Smoke (Tri-Track Routing). | **Tindakan & Transkrip AI Itu Sendiri.** Memeriksa apakah agen berhalusinasi, apakah tes kadaluwarsa (*stale*), dan file apa yang diedit diam-diam tanpa lapor. | 🤝 **Saling Melengkapi.** FORGE mengaudit hasil aplikasi, sedangkan Enterprise mengaudit perilaku runtime agen. |
| **Mekanisme Palang Pintu (Guardrails)** | **Himbauan Teks Moral (Prompt-Based Guard):**  
Menggunakan teks kapital di prompt:  
`[TUGAS AI BERHENTI DI SINI. DILARANG MERENDER FASE SELANJUTNYA...]`. | **Deterministik Berbasis Status File & Skrip:**  
Menggunakan skrip Python (`human_gate.py`) yang menghasilkan file review kontrak fisik (`.review.md`) dan Exit Code terminal (Exit 2 = BLOCKED). | ⚠️ **Kelemahan FORGE.** Himbauan moral teks rentan diterobos AI jika pengguna membalas dengan kalimat yang sedikit ambigu. |
| **Deteksi Hasil Tes Palsu / Kadaluwarsa** | Belum ada deteksi `STALE test`. Jika agen mengklaim terminal hijau, FORGE percaya pada laporan teks tersebut. | Memiliki `claim_checker.py`. Mengecek apakah tes dijalankan sebelum atau sesudah file terakhir diedit. | ⚠️ **Celah FORGE.** Masih rawan tertipu fenomena *Green Terminal Fallacy* pada level internal agen. |
| **Tingkatan Umpan Balik Review** | Bersifat naratif umum di chat (percakapan teks bebas). | Terstruktur baku dengan severitas industri: `BLOCKER`, `MAJOR`, `MINOR`, `NIT`. | ⚠️ **Peluang FORGE.** Mengadopsi severitas standar membuat review arsitektur jauh lebih terukur. |

---

## 4. Poin Rekomendasi & Saran Optimasi untuk FORGE

Berikut adalah 4 langkah konkret yang bisa kita adopsi ke dalam FORGE untuk mencapai level reliabilitas enterprise:

### Poin 1: Upgrade Modul `/audit` dengan "Harness Transcript Forensics"
* **Kondisi FORGE Saat Ini:** Modul `/audit` (v1.3.6) sudah memiliki *Four-Tier Quality Gate* dan *Playwright Visual Smoke*. Ini sangat bagus untuk mengaudit UI.
* **Saran Optimasi:** Tambahkan Tier baru di `/audit`: **Tier 0 (Agent Execution Verification)**.
  * Ketika `/audit` dijalankan, suruh agen memeriksa file log transkrip internal Antigravity (`<appDataDir>\brain\<conversation-id>\.system_generated\logs\transcript.jsonl`).
  * Periksa apakah perintah `npm test` atau `pytest` benar-benar dijalankan di command line dan menghasilkan exit code 0.
  * Pastikan tidak ada file kode sumber yang dimodifikasi *setelah* waktu pengujian unit selesai (*Anti-Stale Guard*).

### Poin 2: Ubah Himbauan Moral Menjadi "Sidecar Review Gate" untuk `/plan` & `/edeate`
* **Kondisi FORGE Saat Ini:** AI sering tergesa-gesa merender langkah implementasi karena hanya ditahan oleh kalimat teks `[TUGAS AI BERHENTI DI SINI...]`.
* **Saran Optimasi:** Pada akhir sesi `/edeate` atau `/plan`, buat artefak review fisik:
  `.docs/plan/issue-<nomor>-review.md`.
  * Sebelum agen boleh masuk ke perintah `/execute`, agen wajib memeriksa file `.review.md` tersebut.
  * Jika masih ada tag `## BLOCKER` dari developer yang belum terjawab, agen secara deterministik menolak memulai coding.

### Poin 3: Standardisasi Tingkat Keparahan Review (Severity Taxonomy)
* **Tindakan:** Masukkan taksonomi review resmi ke dalam `master_rules.template.md`:
  * 🛑 **BLOCKER:** Kesalahan logika fatal / risiko data loss $\rightarrow$ Dilarang lanjut.
  * ⚠️ **MAJOR:** Pelanggaran SOP arsitektur / performance bottleneck $\rightarrow$ Wajib revisi rencana.
  * 🟡 **MINOR:** Rekomendasi optimasi kode $\rightarrow$ Boleh dikerjakan menyusul.
  * 🔵 **NIT (Nitpick):** Masalah penamaan variabel atau format $\rightarrow$ Boleh diabaikan jika waktu mepet.

### Poin 4: Self-Evaluation Sesi di `/audit`
* **Tindakan:** Di akhir laporan `/audit`, buat bagian **Agent Efficiency Metrics**:
  * Jumlah tool calls yang terbuang karena error syntax/terminal.
  * Peringatan jika sesi terlalu panjang (>30 percakapan) agar developer diingatkan untuk melakukan compact atau fresh session.

---
*Dokumen ini merupakan pembaruan resmi materi Fase 2 setelah mengintegrasikan analisis langsung terhadap sistem audit FORGE.*
