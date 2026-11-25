# PANDUAN REFERENSI: ADVERSARIAL REVIEW 3-LENSA & TRANSLASI MENTOR (`/plan` & `/audit`)
**Direktori Rujukan On-Demand untuk Memecah *Self-Confirmation Bias* — Ramah Mahasiswa & IDE-Agnostic**

> 🎯 **Tujuan:** Ketika agen AI yang sama merancang rencana (`/plan`) atau menulis kode (`/execute`) lalu langsung mengevaluasinya sendiri, LLM berbagi *mental model* dan *blind spot* yang sama (*Self-Review Trap*). Panduan ini memecah bias tersebut melalui **3 Lensa Peninjau Independen** di konteks terisolasi, lalu menerjemahkan hasilnya melalui **Filter Mentor Kakak Tingkat** agar mahasiswa tetap merasa didukung, bukan dihakimi.

---

## 🚦 1. Kriteria Pemicu Selektif (*Zero Token Waste*)

Agar tidak memboroskan kuota token dan waktu mahasiswa pada tiket ringan, gerbang ini bersifat **SELEKTIF**:

- **✅ WAJIB AKTIF OTOMATIS** jika tiket menyentuh salah satu zona risiko **Medium/High** berikut:
  1. Autentikasi, Otorisasi, RBAC, atau sesi pengguna.
  2. Migrasi skema database, transaksi atomik, atau mutasi data inti.
  3. Integrasi API eksternal, webhook, pembayaran, atau perubahan kontrak `docs/api/openapi.json`.
  4. Manajemen state kompleks / sinkronisasi *concurrency*.
  5. *Blast Radius* $\ge 4$ berkas eksisting (terdeteksi dari rencana `/plan` atau `classify_blast_radius.py` di `/audit`).
- **✅ AKTIF MANUAL** kapan saja developer menyertakan flag `--adversarial` (misal: `/plan --adversarial` atau `/audit --adversarial`).
- **⏭️ OTOMATIS BYPASS** untuk tiket kosmetik ringan (ubah teks/copy, penyesuaian padding/warna minor, dokumentasi) tanpa menyentuh logika/data.

---

## ⚙️ 2. Protokol Eksekusi 2-Jalur (Native Sub-Agent + Graceful Fallback)

### Jalur A: Native Sub-Agent Isolation *(Default di Antigravity / Claude Code — 0 Instalasi)*
Jika IDE menyediakan tool sub-agent read-only (misal `invoke_subagent` dengan `TypeName="research"` di Antigravity):
1. Panggil sub-agent dengan **konteks 100% segar** (JANGAN kirim riwayat chat penyusunan rencana/kode agar bebas bias).
2. Berikan pada `Prompt` sub-agent **HANYA**:
   - Path berkas panduan ini (`references/adversarial_review_lens.md`).
   - Target audit fisik:
     - *Saat `/plan`:* Path `.docs/plan/issue-<nomor>-...md` + `.agents/rules/ARCHITECTURE.md`.
     - *Saat `/audit`:* Daftar berkas berubah + ringkasan `git diff` (minta sub-agent membaca **berkas utuh**, bukan hanya baris diff).
   - Instruksi menjalankan **3 Lensa + Aturan *Severity Promotion*** dan mengembalikan laporan objektif (`BLOCK` / `CONCERNS` / `CLEAN`) ke agen utama.
3. Karena sandbox `research` bersifat **read-only**, sub-agent mustahil mengubah atau merusak kode proyek.

### Jalur B: *Graceful Fallback* *(Otomatis di IDE Tanpa Sub-Agent)*
Jika tool sub-agent tidak tersedia di IDE mahasiswa, agen utama **TIDAK BOLEH error atau membatalkan alur**. Jalankan 3 lensa di bawah secara sekuensial dengan menerapkan **Teknik Pemecah *Self-Review Trap***:
1. Baca berkas rencana/kode secara **terbalik (*bottom-up*)** dari langkah/fungsi terakhir ke awal.
2. Nyatakan kontrak tiap fungsi/langkah sebelum memeriksa detail implementasinya.
3. Asumsikan setiap input pengguna bisa bernilai `null`/kosong/ekstrem dan setiap panggilan eksternal (DB/API) bisa gagal atau *timeout*.

---

## 🔎 3. Tiga Lensa Peninjau Independen (Dual-Target: `/plan` & `/audit`)

Setiap lensa **WAJIB** menghasilkan minimal 1 temuan nyata **ATAU** mencatat 1 asumsi paling rapuh yang menjadi titik tumpu sistem (*Anti-Rubber-Stamp*: dilarang vonis malas *"LGTM, aman semua"* tanpa analisis).

### Lensa 1 — *The Saboteur* (Skenario Kegagalan Ekstrem)
* **Saat `/plan`:** Apakah urutan langkah *Bottom-Up* berisiko meninggalkan state setengah jadi jika gagal di tengah? Apakah skenario *race condition*, double-submit, *empty/error state*, atau kegagalan panggilan eksternal sudah terakomodasi di rencana?
* **Saat `/audit`:** Input tanpa validasi, potensi `null`/`undefined` dereference, *swallowed exception* (`catch` kosong), *off-by-one*, atau kebocoran *listener*/koneksi/memori.

### Lensa 2 — *The New Hire* (Keterbacaan & Pemeliharaan Anggota Tim Baru)
* **Saat `/plan`:** Apakah ada *implicit knowledge* (langkah yang hanya dimengerti penyusun rencana, bukan anggota tim lain)? Apakah lingkup berkas terdampak (*Blast Radius*) terlalu melebar untuk 1 tiket atomik?
* **Saat `/audit`:** Nama variabel/fungsi ambigu (`data`, `process()`), fungsi mengerjakan terlalu banyak tugas, *magic string/number*, inkonsistensi pola modul saudara, atau test yang menguji detail internal alih-alih perilaku.

### Lensa 3 — *The Security Auditor* (Batas Kepercayaan & OWASP)
* **Saat `/plan` & `/audit`:** Periksa setiap *trust boundary* (input form/API, DB query, file upload, env vars):
  - *Injection* (query non-parameterized, unsanitized HTML/DOM).
  - *Broken Auth & IDOR* (apakah User A bisa membaca/mengubah data milik User B? Apakah pengecekan role/Policy ada di server, bukan hanya disembunyikan di UI?).
  - *Data Exposure & Secrets* (stack trace, password, token, atau field sensitif bocor ke respons API/log/kode).
  - *Insecure Defaults* (CORS wildcard, mode debug aktif, izin terlalu longgar).

---

## 📊 4. Klasifikasi Keparahan & Aturan *Severity Promotion*

| Level | Definisi | Dampak ke Vonis |
| :--- | :--- | :--- |
| **CRITICAL** | Berpotensi memicu kehilangan data, celah keamanan fatal, atau crash produksi/fitur inti. | **`BLOCK`** ($\ge 1$ Critical $\rightarrow$ Wajib revisi sebelum lanjut) |
| **WARNING** | Berisiko bug *edge-case*, performa menurun, atau menyulitkan pemeliharaan tim. | **`CONCERNS`** (0 Critical, $\ge 2$ Warning $\rightarrow$ Perbaiki atau terima risiko sadar) |
| **NOTE** | Perapian minor, dokumentasi, atau peluang peningkatan kecil. | **`CLEAN`** (Hanya Note $\rightarrow$ Aman lanjut) |

- **⚖️ Aturan Promosi Otomatis (*Severity Promotion*):** Jika isu yang sama tertangkap oleh **$\ge 2$ lensa berbeda**, tingkat keparahannya otomatis **naik 1 tingkat** (`NOTE` $\rightarrow$ `WARNING`, `WARNING` $\rightarrow$ `CRITICAL`).

---

## 🎓 5. FILTER TRANSLASI MENTOR (WAJIB SEBELUM TAMPIL KE MAHASISWA)

Agen utama (**Kakak Tingkat Senior** sesuai `.agents/rules/PERSONA_MENTOR.md`) **DILARANG KERAS** melemparkan laporan mentah sub-agent dengan nada keras, sinis, atau seperti dosen penguji sidang. Agen utama **WAJIB** mengemas ulang hasilnya dengan format:

1. **Baris 1 (*Bottom Line First*):**
   `🛡️ Adversarial Review [Mode: Sub-Agent Terisolasi / Fallback Sekuensial]: [🟢 CLEAN / 🟡 CONCERNS / 🔴 BLOCK]`
2. **Daftar Temuan Terkurasi dengan Tag Bukti (`🟢 Verified` / `🟡 Medium` / `🔴 Assumed`):**
   - Kelompokkan tegas: **Wajib Dibereskan Dulu** (`CRITICAL`), **Perlu Dipertimbangkan** (`WARNING`), dan **Catatan Ringan** (`NOTE`).
   - Cantumkan lokasi berkas/langkah nyata dan 1 saran perbaikan konkret per temuan.
3. **Nada Suportif & *Hard Stop* Pemberdayaan:**
   > *"Kabar baiknya celah ini ketangkap lebih awal sebelum kita koding/merge, jadi tim nggak bakal buang waktu bongkar ulang belakangan! Menurutmu poin mana yang mau kita rapikan sekarang, atau ada catatan `WARNING` yang mau kita sepakati sebagai risiko yang diterima (*accepted risk*) dulu?"*
