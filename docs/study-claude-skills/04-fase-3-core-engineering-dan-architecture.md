# Fase 3: Core Engineering & Architecture Skills
**Fokus Pembelajaran:** Bagaimana AI Agen mengeksekusi pekerjaan rekayasa software di tingkat Principal/Senior Engineer (Desain API, Skema Database, Bedah Bug Presisi, dan Disiplin Testing).  
**Sumber Referensi:** `scratch/claude-skills/engineering/skills/` (`api-design-reviewer`, `database-schema-designer`, `focused-fix`, `pr-review-expert`, `tdd-guide`)

---

## 1. Konteks Besar: Mengapa Masuk ke Fase 3?

Jika kita melihat peta perjalanan kita sejauh ini:
* **Fase 1 (Format):** Kita belajar bagaimana **mengemas skill** (10 Pola, 10KB Rule, Context-First, Triggers).
* **Fase 2 (Meta/Guardrails):** Kita belajar bagaimana **memasang rem dan polisi** untuk AI (`agent-run-forensics`, `human-gate`, `skill-retro`).
* **Fase 3 (Core Engineering):** Sekarang kita masuk ke **otak teknis eksekusi coding**.

> **Masalah Nyata di Dunia Nyata:**  
> Tanpa skill engineering yang ketat, LLM pada dasarnya adalah *"Junior Developer yang Terlalu Percaya Diri"*. Mereka suka melakukan **Shotgun Debugging** (menebak-nebak bug dan mengubah kode acak), merancang API yang merusak kompatibilitas aplikasi mobile (*breaking change*), dan mendesain database tanpa index yang membuat server ambruk saat data membesar.

Fase 3 membedah bagaimana repositori enterprise memprogram AI agar bekerja dengan disiplin teknis tingkat tinggi.

---

## 2. Bedah 4 Skill Inti Rekayasa Software

---

### Skill 1: `api-design-reviewer` (Pencegah Breaking Change & Standarisasi REST)

Banyak AI asal membuat endpoint: URL pakai kata kerja (`POST /getUserData`), status code selalu 200 OK meskipun error, atau mengubah tipe data JSON tanpa sadar bahwa versi mobile lama akan langsung *crash*.

* **Pola Alur Kerja (Review Flow):**
  Skill ini **menolak me-review API hanya dengan kata-kata narasi**. Ia mewajibkan eksekusi 3 alat verifikasi deterministik:
  ```bash
  # 1. Lint spesifikasi OpenAPI untuk kepatuhan konvensi REST
  python3 scripts/api_linter.py openapi.json -o lint.json

  # 2. Deteksi otomatis Breaking Change antara v1 vs v2 (Gate Exit Non-Zero)
  python3 scripts/breaking_change_detector.py v1.json v2.json --exit-on-breaking

  # 3. Hitung skor mutu desain API (wajib minimal grade B)
  python3 scripts/api_scorecard.py openapi.json --min-grade B
  ```

* **Hukum Besi (The Iron Law):**  
  > *"Never sign off an API review on prose alone — attach the tool outputs."*  
  > (Dilarang menyetujui review API hanya bermodalkan teks pujian AI; wajib melampirkan hasil uji script).

* **Pencegahan Kritis yang Dilakukan:**
  1. *Resource Naming:* Memaksa `kebab-case` untuk resource URL (`/order-items`), bukan `camelCase` atau `snake_case`.
  2. *Status Code Semantics:* Melarang `200 OK` dengan payload `{"error": "not found"}` (wajib `404`).
  3. *Breaking Change Alarm:* Menolak penghapusan field, pengubahan tipe data (misal: `string` jadi `number`), atau penambahan field wajib (*required*) pada request tanpa penomoran versi API baru.

---

### Skill 2: `database-schema-designer` (Arsitektur Data & Zero-Downtime Migration)

AI biasa jika disuruh membuat database hanya mengetik `CREATE TABLE` sederhana. Skill ini mendesain database dengan pola arsitektur enterprise:

* **Kemampuan Kunci:**
  1. **Multi-Tenancy & Row-Level Security (RLS):** Memastikan kolom `tenant_id` terisolasi secara kriptografis dan terindeks dengan benar.
  2. **Index Strategy (Bukan Asal Index):**
     * *Composite Index:* Memahami urutan kolom kiri-ke-kanan (*Leftmost Prefix Rule*) pada query filtering.
     * *Partial / Filtered Index:* Hanya mengindeks baris aktif (`WHERE deleted_at IS NULL`) untuk menghemat disk.
  3. **Zero-Downtime Migration Plan:**  
     Jika mengubah nama kolom atau memecah tabel di tabel dengan jutaan baris, skill ini **melarang langsung `ALTER TABLE DROP COLUMN`**. Ia menerapkan **Pola Expand & Contract**:
     * *Langkah 1 (Expand):* Buat kolom baru, sync data via trigger/dual-write.
     * *Langkah 2 (Transition):* Arahkan aplikasi membaca kolom baru.
     * *Langkah 3 (Contract):* Hapus kolom lama setelah versi stabil.

---

### Skill 3: `focused-fix` (Bedah Mikro Bug & Anti-Shotgun Debugging)

Ketika sistem rusak, penyakit paling berbahaya dari AI adalah **Shotgun Debugging**: AI mengubah 5 baris di file A, gagal, lalu mengubah file B, gagal lagi, dan akhirnya seluruh codebase menjadi berantakan.

* **Pola Desain: The Iron Law of Diagnosis**
  ```
  NO FIXES WITHOUT COMPLETING: SCOPE ──► TRACE ──► DIAGNOSE FIRST
  ```
  AI **DIHARAMKAN menyentuh kode** sebelum menyelesaikan 3 tahap investigasi:
  1. **Scope:** Memetakan seluruh graf ketergantungan berkas (*dependency graph*) yang terhubung dengan modul yang rusak.
  2. **Trace:** Membaca stack trace, log error nyata, dan payload input/output yang menyebabkan crash.
  3. **Diagnose:** Menemukan *Root Cause* (akar masalah sejati), bukan sekadar menambal gejalanya (*symptom patching*).

* **Disambiguasi Penting:**
  * Gunakan `systematic-debugging` untuk 1 bug kecil/lokal.
  * Gunakan `focused-fix` ketika **satu modul atau fitur utuh tidak berfungsi secara end-to-end**.

---

### Skill 4: `tdd-guide` & `red-green-proof` (Disiplin Red-Green-Refactor)

Banyak AI mengaku menerapkan TDD, tetapi sebenarnya mereka menulis kode implementasi terlebih dahulu, baru kemudian menulis unit test formalitas yang diatur agar pasti passing (*palsu*).

* **Protokol Pembuktian Keras (Red-Green Proof):**
  1. **Fase RED (Wajib Gagal):** AI menulis test case spesifikasi. AI **wajib menjalankan test di terminal** dan membuktikan bahwa test tersebut **GAGAL (Exit Code != 0)** dengan alasan assertion yang benar (karena kodenya memang belum ada).
  2. **Fase GREEN (Kode Minimal):** AI hanya diperbolehkan menulis kode minimal yang cukup untuk membuat test yang gagal tadi menjadi hijau. Dilarang menambah logika ekstra di luar cakupan test.
  3. **Fase REFACTOR:** Membersihkan duplikasi kode dengan jaminan bahwa test suite tetap 100% hijau.

---

## 3. Komparasi dengan Blueprint FORGE (`project-plan`, `project-execute`, `project-debug`, `project-tdd`)

Mari kita bandingkan bagaimana FORGE menangani rekayasa kode dibanding skill enterprise di atas:

| Aspek Rekayasa | Standar Enterprise (`claude-skills`) | Kondisi Blueprint FORGE di Proyek Kita | Evaluasi & Peluang Asimilasi |
| :--- | :--- | :--- | :--- |
| **API Review & Breaking Changes** | Menggunakan script otomatis (`breaking_change_detector.py`) untuk membandingkan schema JSON. | Belum ada deteksi breaking change eksplisit. Audit API hanya mengandalkan bacaan mata AI di `/audit`. | ⚠️ **Peluang Besar:** Suntikkan aturan deteksi breaking change ke dalam `/audit` atau `/plan`. |
| **Pencegahan Shotgun Debugging** | Memiliki *The Iron Law of Diagnosis* di `focused-fix` (larangan edit kode sebelum dependency graph tuntas). | FORGE memiliki protokol `/debug` (v1.3.6) yang sangat bagus dengan Deferred Recommendation, namun belum membatasi *dependency blast-radius* sekuat `focused-fix`. | 🟡 **Perkuat `/debug`:** Wajibkan pembuatan diagram alur dependensi sebelum AI boleh mengedit file bug. |
| **Disiplin TDD** | Mewajibkan bukti rekaman terminal saat test gagal (*Red Proof*) sebelum menulis implementasi. | FORGE memiliki `project-tdd` dan aturan *Zero Test-Tampering Law*. Sangat sejalan dan kuat secara filosofis. | 🟢 **FORGE Selaras:** Filosofi TDD FORGE sudah sangat matang, tinggal didukung verifikasi transkrip (Fase 2). |
| **Arsitektur Database** | Fokus pada Expand-Contract migration, indexing partial, dan RLS security. | Diatur dalam `ARCHITECTURE.md` dan `MASTER_RULES.md`, namun belum memiliki checklist strategi index komposit. | 🟡 **Peluang:** Tambahkan checklist migrasi non-blocking di `project-plan`. |

---

## 4. Pelajaran Utama yang Bisa Diasimilasikan ke Dapur FORGE

Dari pembedahan Fase 3 ini, ada **3 Suntikan Kekuatan** yang bisa langsung kita adopsi ke dalam blueprint FORGE:

1. **Adopsi "The Iron Law of Diagnosis" ke `/debug`:**  
   Kunci AI agar tidak boleh melakukan edit kode sebelum membuktikan *Scope $\rightarrow$ Trace $\rightarrow$ Root Cause*. Mencegah AI merusak fitur lain saat memperbaiki 1 bug.
2. **Suntikkan "Breaking Change Checklist" ke `/edeate` dan `/plan`:**  
   Ketika developer merancang endpoint API baru, wajibkan AI mengecek: *"Apakah perubahan skema payload ini akan mematikan client lama?"*
3. **Pola Expand & Contract pada Migrasi Database:**  
   Masukkan larangan `ALTER TABLE DROP COLUMN` langsung pada tabel produksi ke dalam `MASTER_RULES.md`.

---
*Dokumen ini merupakan modul resmi pembelajaran Fase 3. Silakan berdiskusi atau ajukan pertanyaan di jendela percakapan.*
