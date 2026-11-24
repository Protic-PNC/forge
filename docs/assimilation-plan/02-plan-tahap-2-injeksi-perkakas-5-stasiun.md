# Rencana Eksekusi: TAHAP 2 — Injeksi Perkakas Spesifik ke 5 Stasiun Gerbang
**Dokumen Diskusi & Persetujuan:** Tahap 2 dari 4 (Antrean setelah Tahap 1 Selesai)  
**Target:** Mempersenjatai 5 stasiun gerbang FORGE dengan perkakas teknis presisi standar enterprise.  
**Lokasi Berkas Sasaran:** `blueprints/` (`edeate`, `plan`, `execute`, `audit`, `debug`) dan `skills/forge-constitution/scripts/`

---

## 1. Rincian 5 Injeksi Stasiun

### Item 2.1: Stasiun `/edeate` ──► Injeksi Context-First Auto-Check
* **Target Berkas:** `blueprints/edeate.template.md`
* **Sebelum:** AI mewawancarai ideasi bisnis tanpa membaca file konteks arsitektur yang sudah ada.
* **Sesudah:** AI membaca `project-context.md` dan `ARCHITECTURE.md` secara diam-diam sebelum membuka pembicaraan, memangkas pertanyaan basi.
* **Mekanisme AI:** Pengecekan pra-syarat (*Pre-Flight Context Subtraction*).
* **Keuntungan:** Wawancara ideasi menjadi tajam dan langsung menyasar kebutuhan fitur baru.

---

### Item 2.2: Stasiun `/plan` ──► Injeksi Database Checklist (RLS, Partial Index, Expand-Contract)
* **Target Berkas:** `blueprints/plan.template.md`
* **Sebelum:** Perencanaan database hanya berfokus pada nama tabel dan kolom standar.
* **Sesudah:** AI mewajibkan checklist arsitektur data:
  1. *Row-Level Security (RLS)* untuk tabel multi-tenant.
  2. *Partial Indexing* pada tabel ber-soft delete (`WHERE deleted_at IS NULL`).
  3. *Expand & Contract Pattern* untuk migrasi skema tabel besar tanpa downtime.
* **Mekanisme AI:** Validasi kepatuhan skema (*Schema Completeness Guard*).
* **Keuntungan:** Mahasiswa terbiasa merancang database aman sejak hari pertama.

---

### Item 2.3: Stasiun `/execute` ──► Injeksi Proactive Triggers di Header
* **Target Berkas:** `blueprints/execute.template.md`
* **Sebelum:** Aturan proteksi UI terkubur dalam teks undang-undang 16KB.
* **Sesudah:** Header `/execute` memuat 4–6 trigger otomatis: Unmounted Guard `if (!isOpen) return null;`, Sticky Collision Scroll Margin, dan Adaptive Bounds.
* **Mekanisme AI:** *Pattern Recognition Active Guard* saat koding berlangsung.
* **Keuntungan:** Bug visual & memory leak tertangkap sebelum masuk ke fase audit.

---

### Item 2.4: Stasiun `/audit` ──► Injeksi API Tools & Tier 0 Transkrip Forensics
* **Target Berkas:** `blueprints/audit.template.md`, `skills/forge-constitution/scripts/` (`api_scorecard.py`, `breaking_change_detector.py`, `api_linter.py`)
* **Sebelum:** Audit API mengandalkan pembacaan teks LLM; audit tes hanya percaya klaim teks chat.
* **Sesudah:** 
  1. Skrip menghitung mutu API secara kuantitatif (Grade A–F) dan mendeteksi *breaking changes*.
  2. Tier 0 memeriksa transkrip asli (`transcript.jsonl`) untuk mendeteksi *STALE test* (tes lulus tapi kodenya dirusak setelahnya).
* **Mekanisme AI:** Evaluasi deterministik ber-exit code (Exit 0 / Exit 1).
* **Keuntungan:** Melenyapkan penipuan terminal (*Green Terminal Fallacy*) dan melindungi kompatibilitas klien.

---

### Item 2.5: Stasiun `/debug` ──► Injeksi *The Iron Law of Diagnosis*
* **Target Berkas:** `blueprints/debug.template.md`
* **Sebelum:** Belum ada pembatasan graf dependensi 2 arah yang ketat.
* **Sesudah:** Menerapkan hukum besi dari `focused-fix`: **Dilarang keras mengedit kode sebelum Fase Scope ──► Trace ──► Diagnose selesai**.
* **Mekanisme AI:** Penguncian fase kognitif berurutan (*Strict Sequential Phasing*).
* **Keuntungan:** Melenyapkan kebiasaan buruk AI yang suka menambal kode acak (*Shotgun Debugging*).
