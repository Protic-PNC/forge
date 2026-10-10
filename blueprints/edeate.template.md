# SOP IDEASI & PENEMUAN TIKET (`/edeate`)
# DOMAIN: {{PROJECT_NAME}}

> **Dokumen ini adalah hukum domain Hulu (Ideasi).**
> Ia berpasangan dengan `MASTER_RULES.md` (domain Hilir/Implementasi) dan `GIT_WORKFLOW.md` (domain Version Control). Ketiganya membentuk **Two-Gateway Pipeline** lengkap dari ide mentah hingga kode produksi.

---

## 🗺️ GAMBARAN BESAR: TWO-GATEWAY PIPELINE

```
IDE MENTAH
    │
    ▼
┌──────────────────────────────────────┐
│  GATEWAY 1 — HULU (Dokumen Ini)      │
│  Slash Command: /edeate              │
│                                      │
│  0. Pre-Flight Audit (Codebase)      │
│  1. Pilar Bisnis                     │
│  2. Pilar Integrasi                  │
│  3. Pilar Keamanan & Concurrency     │
│  4. Draft Tiket Level 3              │
│  5. Verifikasi & Pengesahan          │
└──────────────────┬───────────────────┘
                   │   GitHub Issue dibuat (dapat nomor Issue)
                   ▼
┌──────────────────────────────────────┐
│  GATEWAY 2 — HILIR (MASTER_RULES)    │
│  /grill-me → /plan → /tdd →          │
│  /execute → /audit → PR              │
└──────────────────────────────────────┘
                   │
                   ▼
            KODE PRODUKSI
```

> **Aturan Fundamental:** Sebuah ide **DILARANG** masuk ke Gateway 2 sebelum lulus Gateway 1.
> Ini mencegah "tiket mentah Level 1" yang memaksa developer menebak-nebak konteks di tengah eksekusi.

---

## 🚦 SLASH COMMAND: `/edeate`

**Definisi:** `/edeate` (singkatan dari **Ideate**) adalah perintah yang memulai sesi penemuan dan pembentukan ide secara terstruktur sebelum sebuah tiket ditulis.

**Kapan Digunakan:**
- Developer atau Tech Lead punya gambaran kasar tentang sebuah fitur/perbaikan.
- Ide belum cukup konkret untuk ditulis sebagai GitHub Issue yang bisa langsung dikerjakan.
- Perlu konfirmasi apakah ide tersebut *feasible* secara arsitektur dan tidak memiliki risiko tersembunyi.

**Kapan TIDAK Digunakan:**
- Tiket sudah ada di GitHub dan nomor Issue sudah ditetapkan → langsung `/grill-me #<nomor>`.
- Hanya ada pertanyaan teknis singkat tanpa pembentukan fitur baru.

---

## 📐 TINGKAT KEMATANGAN TIKET (Ticket Maturity Levels)

Sebelum menjalankan `/edeate`, AI dan developer harus memahami target kematangan yang ingin dicapai:

| Level | Nama | Karakteristik | Boleh ke Gateway 2? |
|-------|------|---------------|---------------------|
| **1** | **Mentah (Idea Dump)** | "Bikin sync CSV untuk event committee." Tidak ada konteks, tidak ada DoD. | ❌ TOLAK |
| **2** | **Setengah Matang (Story)** | Ada use case dan kriteria penerimaan umum, tapi DoD masih ambigu ("berhasil sync"). | ⚠️ Revisi dulu |
| **3** | **Matang — Sweet Spot** | Ada **invariant** yang terukur, DoD berbasis uji (testable), dan kontrak API terdefinisi. | ✅ IZINKAN |

> **Target `/edeate`:** Selalu menghasilkan tiket **Level 3**.

---

## 🔬 PROTOKOL `/edeate` — ALUR IDE DARI HULU KE TIKET

> 🚨 **PROTOKOL ITERASI WAJIB:** 
> - AI **DILARANG KERAS** memborong seluruh Fase atau semua pertanyaan sekaligus dalam satu respons. 
> - AI **WAJIB** membahas HANYA 1 Fase/Pilar per giliran. 
> - AI **DILARANG** pindah ke pertanyaan/Fase berikutnya sebelum mendapat persetujuan, keputusan, atau jawaban eksplisit dari Tech Lead di tahap sebelumnya.
> - Tiket Final hanya boleh dicetak setelah Fase 1-3 tuntas didiskusikan satu per satu.

### FASE 0 — Penerimaan & Klasifikasi Awal (AI)

Ketika developer mengetik `/edeate [deskripsi ide]`, AI **WAJIB** melakukan hal berikut **sebelum** mengajukan pertanyaan apa pun:

**Langkah 0.1 — Klasifikasi Tiket Otomatis:**
AI mengidentifikasi tipe tiket berdasarkan kata kunci ide:
- *"sync", "CSV", "import", "sinkronisasi"* → Tipe: **[FEAT] External I/O**
- *"bug", "error", "gagal", "salah"* → Tipe: **[FIX]**
- *"refactor", "standarisasi", "pisah", "bersihkan"* → Tipe: **[REFACTOR]**
- *"test", "coverage", "uji"* → Tipe: **[TEST]**

**Langkah 0.2 — Pre-Flight Codebase Audit (WAJIB, Sebelum Giliran Pertanyaan):**
AI **WAJIB** memanggil tool `grep_search` atau `view_file` ke modul yang relevan terlebih dahulu. Tujuannya adalah memastikan AI berbicara dari fakta repositori, bukan asumsi.

Pola audit berdasarkan tipe tiket:
- **External I/O / Sync:** Baca controller saudara yang sudah punya `sync` (misal `UserController`, `AgendaController`) untuk memetakan pola `Cache::lock` + `DB::transaction` yang berlaku.
- **Fitur Baru pada Entitas Existing:** Baca model terkait + migration terakhir untuk memahami skema data saat ini.
- **Otorisasi / Policy:** Baca `routes/api.php` dan `Policy` yang relevan.
- **Pengujian:** Baca `tests/Feature/` terkait untuk menghindari duplikasi skenario.

**Output Langkah 0.2 — Blok Bukti Fisik Audit Wajib:**

```markdown
### 🔍 Konteks Repositori Aktual (Pre-Flight Audit)
- **Modul Referensi:** [`app/Http/Controllers/XyzController.php`](file:///...) (baris A–B):
  Pola `Cache::lock` + `upsert()` sudah ada. Fitur baru harus mengikuti pola ini.
- **Kontrak Data Existing:** Tabel `xyz_table` memiliki kolom `[...]`.
  Kolom baru apa pun harus dibuatkan migrasinya.
- **Celah yang Terdeteksi:** [Ada/Tidak ada] potensi konflik atau duplikasi dengan kode existing.
```

---

### FASE 1 — PILAR BISNIS (The Business Grill)

> *Tujuan: Memahami "MENGAPA" fitur ini ada dan "SIAPA" yang terdampak.*

AI mengajukan pertanyaan berikut, **satu per giliran**, menunggu jawaban sebelum lanjut:

**1. Pemantik Konteks:**
> *"Apa kejadian spesifik yang membuatmu menyadari fitur ini perlu ada? (misal: ada data yang salah, ada proses manual yang melelahkan, ada laporan yang tidak akurat)"*

**2. Identifikasi Aktor:**
> *"Siapa yang akan menjalankan fitur ini? (Admin, Tech Lead, Anggota Biasa, Sistem Otomatis?) Dan dari 'pintu' mana mereka masuk? (Dashboard, API, Cron Job?)"*

**3. Definisi Sukses yang Terukur:**
> *"Bagaimana kamu tahu fitur ini 'berhasil'? Bukan dalam arti 'tidak error', tapi dalam arti bisnis. Misal: 'Data 50 anggota committee ter-sync dalam 5 detik' atau 'Laporan keuangan menampilkan angka yang sama dengan Google Sheet.'"*

**4. Kasus Tepi Bisnis:**
> *"Apa yang seharusnya terjadi kalau: (a) file CSV-nya kosong? (b) ada data duplikat di CSV? (c) koneksi terputus di tengah proses?"*

---

### FASE 2 — PILAR INTEGRASI (The Integration Grill)

> *Tujuan: Memetakan "APA" yang akan berubah di sistem dan dampaknya ke modul lain.*

**5. Pemetaan Entitas & Relasi:**
> *"Entitas (tabel database) apa saja yang terlibat? Apakah ada relasi pivot (many-to-many) yang perlu diubah? Misal: apakah `event_committees` perlu kolom baru, atau hanya mengisi data yang sudah ada?"*

**6. Kontrak API:**
> *"Endpoint HTTP apa yang akan menjadi pintu masuk? Apakah ada endpoint existing yang harus dimodifikasi, atau kita butuh endpoint baru sama sekali? Format request-nya seperti apa? (multipart/form-data untuk upload file, JSON untuk data biasa)"*

**7. Dampak ke Modul Lain:**
> *"Setelah fitur ini berjalan, modul lain mana yang bisa terdampak? Misalnya: apakah sync committee ini akan mempengaruhi perhitungan iuran bulanan, laporan kehadiran, atau sistem otorisasi BPH?"*

---

### FASE 3 — PILAR KEAMANAN & CONCURRENCY (The Security Grill)

> *Tujuan: Mendeteksi risiko tersembunyi yang tidak terlihat dari permukaan ide.*

**8. Otorisasi:**
> *"Siapa saja yang TIDAK BOLEH mengakses atau menjalankan fitur ini? Apakah hanya Admin/Tech Lead? Apakah ada kondisi di mana anggota biasa bisa memicu ini secara tidak sengaja?"*

**9. Proteksi Konkurensi:**
> *"Bisakah dua orang Admin menjalankan fitur ini pada saat yang bersamaan? Kalau iya, apa yang terjadi pada data? Apakah kita butuh mekanisme pengunci (locking)?"*

**10. Invariant — Pertanyaan Kunci Level 3:**
> *"Properti data apa yang harus SELALU BENAR, bahkan kalau terjadi error di tengah proses? Misal: 'Tidak boleh ada committee yang terdaftar dua kali di event yang sama' atau 'Jika sync gagal di baris ke-30, data 1-29 harus di-rollback.'"*

---

### FASE 4 — SINTESIS & PEMBUATAN DRAFT TIKET LEVEL 3

Setelah ketiga pilar terjawab, AI **WAJIB** menyusun Draft Tiket Level 3 menggunakan format berikut:

```markdown
## 🎫 DRAFT TIKET LEVEL 3

**Prefix & Judul:** `[FEAT/FIX/REFACTOR] Nama Fitur yang Jelas`
**Estimasi Kompleksitas:** S / M / L / XL

---

### Latar Belakang (The "Why")
[1-2 kalimat tentang masalah bisnis nyata yang diselesaikan, bukan deskripsi teknis]

### Scope & Definisi of Done (DoD)

**✅ Yang HARUS dikerjakan:**
- [ ] [Aksi konkret 1, misal: "Tambahkan endpoint `POST /api/events/{id}/committees/sync`"]
- [ ] [Aksi konkret 2, misal: "Buat FormRequest `SyncEventCommitteeRequest` dengan validasi file CSV"]
- [ ] [Aksi konkret 3, misal: "Implement `EventCommitteeService::syncFromCsv()` dengan `Cache::lock` + `DB::transaction`"]

**❌ Yang TIDAK termasuk scope (Out of Scope):**
- [Hal yang dengan sengaja dikecualikan agar scope tidak melebar]

### Invariant yang Harus Dijaga (Contract)
> *Ini adalah kondisi yang harus selalu BENAR, dibuktikan oleh Feature Test.*

1. `INVARIANT-1:` [misal: "Tidak boleh ada duplikasi NIM dalam satu event committee"]
2. `INVARIANT-2:` [misal: "Jika proses sync gagal di baris mana pun, TIDAK ADA data yang berubah (full rollback)"]
3. `INVARIANT-3:` [misal: "Hanya user dengan role `admin` yang dapat memicu endpoint ini"]

### Kriteria Penolakan (Rejection Criteria)
> *Kondisi yang menyebabkan PR WAJIB ditolak saat review.*

- PR ditolak jika: tidak ada Feature Test yang membuktikan semua INVARIANT di atas.
- PR ditolak jika: ada query Eloquent di dalam loop (N+1).
- PR ditolak jika: tidak ada `Cache::lock` pada operasi write data massal.

### Referensi Pola Arsitektur
- Ikuti pola: [`XyzController@syncFromCsv`](file:///...) (baris A–B) sebagai referensi implementasi.
```

---

### FASE 5 — VERIFIKASI & PENGESAHAN DRAFT

Setelah draft disajikan, AI mengajukan satu pertanyaan penutup:

> *"Draft tiket di atas sudah merangkum semua yang kita diskusikan. Ada poin yang perlu direvisi, ditambahkan, atau dihapus sebelum kita buat sebagai GitHub Issue resmi?"*

Jika developer menyetujui → **Draft Tiket dinyatakan SAH**. Developer membuat GitHub Issue menggunakan draft tersebut, mendapatkan nomor Issue, lalu memulai Gateway 2 dengan `/grill-me #<nomor>`.

---

## ⚠️ PENJAGA KUALITAS (Anti-Pattern yang Harus Ditolak AI)

| Anti-Pattern | Dampak | Tindakan AI |
|---|---|---|
| **Tiket Terlalu Luas** ("Bikin fitur manajemen event lengkap") | Scope tak terbatas, sprint berantakan | AI WAJIB meminta developer memecah menjadi tiket-tiket kecil yang independen |
| **DoD Ambigu** ("Berhasil dijalankan") | Developer dan reviewer punya definisi sukses yang berbeda | AI WAJIB mendesak definisi yang terukur (angka, waktu, kondisi boolean) |
| **Tiket Tanpa Invariant** | Tidak ada kontrak yang bisa diuji → Feature Test menjadi formalitas dangkal | AI WAJIB menggali minimal 2-3 invariant sebelum draft disahkan |
| **Asumsi Tanpa Audit Kode** | AI berbicara dari imaginasi, bukan realita repositori | AI WAJIB menjalankan Pre-Flight Audit (Fase 0) sebelum sesi dimulai |
| **Langsung Lompat ke Solusi** | Masalah bisnis inti tidak dipahami | AI WAJIB menyelesaikan Pilar Bisnis (Fase 1) terlebih dahulu |
