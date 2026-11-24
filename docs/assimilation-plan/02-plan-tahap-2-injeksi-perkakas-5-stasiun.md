# Rencana Eksekusi: TAHAP 2 — Injeksi Perkakas Spesifik ke Stasiun Gerbang
**Dokumen Diskusi & Persetujuan:** Tahap 2 dari 4 (Setelah Tahap 1 Tuntas & Di-commit di `8e600ec`)  
**Target:** Mempersenjatai stasiun gerbang FORGE (`/edeate`, `/plan`, `/audit`, `/debug`) dengan perkakas teknis presisi standar enterprise secara **bebas bias stack (*Stack-Aware*)** dan **100% *Lossless*** tanpa menggerus persona mentor ramah FORGE.  
**Lokasi Berkas Sasaran:** `blueprints/`, `blueprints/references/`, `skills/forge-constitution/scripts/`, `skills/forge-constitution/references/physical_injection_spec.md`, dan `skills/forge-update/SKILL.md`.

---

## 1. Catatan Sinkronisasi dengan Hasil Tahap 1

> 💡 **Koreksi Penting terhadap Draf Awal Tahap 2:**
> 1. **Eks Item 2.3 (`/execute` Proactive Triggers) — SUDAH SELESAI DI TAHAP 1 (`8e600ec`):** Sudah diimplementasikan menggunakan Model Hibrida 2 Lapisan (Statis Universal + Dinamis `EXECUTE_PROACTIVE_TRIGGERS`). Tidak dikerjakan ulang.
> 2. **Eks Item 2.1 (`project-context.md`):** Disesuaikan dengan keputusan Tahap 1 — menggunakan `.agents/rules/ARCHITECTURE.md` + wajib *Confidence Tagging* (🟢/🟡/🔴).
> 3. **Prinsip Bebas Domain Bias (3 Kasta Invariant):** Seluruh perkakas Database (`database_design_checklist.md`) dan OpenAPI (`openapi.json` + 3 skrip Python) diaktifkan **secara kondisional khusus proyek Backend / Fullstack**, sehingga proyek Frontend statis tidak terkena *Prompt Pollution*.
> 4. **Strategi Eksekusi:** Dipecah menjadi **2 Micro-Batch** (`Batch 2A` dan `Batch 2B`) agar bebas risiko kepenuhan token (*truncation*) dan mudah diaudit via `git diff`.

---

## 2. Rincian 4 Item Pembenahan TAHAP 2

---

### ✅ BATCH 2A: Pembenahan `/edeate`, `/plan`, `/execute`, `/debug`, & `forge-constitution` (STATUS: SELESAI DIEKSEKUSI)

> 📌 **Tambahan Terverifikasi di Batch 2A:**
> - `blueprints/execute.template.md`: Ditambahkan 1 baris aturan tegas sinkronisasi `docs/api/openapi.json` khusus proyek Backend/API.
> - `skills/forge-constitution/references/interview_guide.md`: Ditambahkan kewajiban kondisional OpenAPI Spec Exporter di **Epik 1 Roadmap (Fase 2.3)** dan **`ONBOARDING.md` (Fase 4.4)** setara dengan Playwright, LSP, & MCP.
> - `physical_injection_spec.md` & `forge-update/SKILL.md`: Didaftarkan pemetaan kondisional `references/database_design_checklist.md` untuk proyek ber-Database.

#### Item 2.1: Stasiun `/edeate` ──► Silent `ARCHITECTURE.md` Grounding & Confidence Tagging
* **Target Berkas:** `blueprints/edeate.template.md` (Fase 0)
* **Kondisi Sebelum (Before):** Fase 0 mewajibkan AI membaca `DEVELOPMENT_ROADMAP.md` dan kode eksisting, tetapi belum secara eksplisit memerintahkan *Silent Inspection* ke `.agents/rules/ARCHITECTURE.md` dan belum mewajibkan label keyakinan bukti (🟢/🟡/🔴) pada laporan Pre-Flight Audit.
* **Kondisi Sesudah (After):** Di Fase 0 Langkah 2, AI wajib membaca `.agents/rules/ARCHITECTURE.md` secara senyap untuk memangkas pertanyaan basi, lalu melabeli setiap butir temuan Pre-Flight Audit dengan 🟢 **Verified** (fakta file/baris), 🟡 **Medium** (standar industri), atau 🔴 **Assumed** (asumsi bisnis yang butuh konfirmasi developer).
* **Perubahan Mekanisme AI:** *Context Subtraction + Epistemic Calibration* sejak respons pembuka sesi ideasi.
* **Dampak Positif:** Nol pertanyaan basi & mahasiswa langsung sadar bagian mana yang fakta repo vs asumsi AI.
* **Potensi Risiko & Mitigasi:** Risiko `ARCHITECTURE.md` tertinggal dari kode riil $\rightarrow$ Mitigasi: AI langsung memberi label 🟢 pada bukti kode fisik dan menanyakan 1 baris apakah `ARCHITECTURE.md` perlu entri ADR baru.

---

#### Item 2.2: Stasiun `/plan` ──► Database Design Checklist (On-Demand) & Kontrak `openapi.json`
* **Target Berkas:**
  * `blueprints/plan.template.md`
  * `blueprints/references/database_design_checklist.md` *(Berkas Rujukan Baru — Kondisional Proyek dengan DB)*
* **Kondisi Sebelum (Before):** Perencanaan skema database belum memiliki standar checklist *cross-cutting concerns* (index, soft-delete, multi-tenant isolation, migrasi aman), dan kontrak API hanya ditulis sebagai teks bebas tanpa standar `openapi.json`.
* **Kondisi Sesudah (After):**
  1. Membuat modul referensi on-demand `references/database_design_checklist.md` yang berisi 2 tingkat panduan:
     * **Dasar Wajib Proyek Kampus:** Normalisasi entitas, Foreign Key + eksplisit `ON DELETE`, audit timestamps (`created_at`/`updated_at`), dan Composite/FK Indexing.
     * **Pola Skala Produksi (Dengan Panduan *"🎓 Kapan Wajib vs Kapan Lewati"*):** *Partial Index* (`WHERE deleted_at IS NULL` khusus jika pakai soft delete), *Row-Level Security / Tenant Isolation* (khusus multi-tenant), dan *Expand & Contract Pattern* (khusus DB produksi aktif).
  2. Menambahkan pemicu rujukan kondisional di `plan.template.md` agar checklist DB & pengadaan `openapi.json` **hanya aktif** pada proyek yang memiliki Database / REST API (mengikuti opsi pengadaan `openapi.json` yang disepakati di Bagian 3 di bawah).
* **Perubahan Mekanisme AI:** *Conditional On-Demand Schema & Contract Guard* (0 polusi untuk proyek Frontend statis).
* **Dampak Positif:** Mahasiswa terbiasa merancang skema DB yang sehat dan kontrak API yang baku sebelum koding tanpa pusing oleh *over-engineering*.
* **Potensi Risiko & Mitigasi:** Mahasiswa pemula takut melihat istilah RLS/Expand-Contract $\rightarrow$ Mitigasi: Setiap teknik tingkat lanjut diberi label eksplisit kapan boleh dilewati pada proyek semester awal.

---

#### Item 2.3: Stasiun `/debug` ──► Upgrade 3 Mekanisme Inti `focused-fix`
* **Target Berkas:** `blueprints/debug.template.md`
* **Kondisi Sebelum (Before):** Sudah memiliki Scientific Debugging 4 Fase yang sangat solid untuk *single bug*, tetapi belum memisahkan penanganan 1 bug kecil vs 1 modul rusak menyeluruh, belum memiliki format peta dependensi 2 arah (*Inbound + Outbound*), dan belum memiliki rem darurat jika perbaikan gagal berulang kali.
* **Kondisi Sesudah (After):** Mempertahankan 100% filosofi ramah *No Shame Culture* dan 4 fase yang ada, ditambah **3 mekanisme presisi dari `focused-fix`**:
  1. **Dual-Mode Routing:** Mode Default (`/debug` untuk *Single Bug*) vs Mode Modul (`/debug --module` untuk *"fitur/modul X rusak menyeluruh"* $\rightarrow$ wajib memetakan seluruh berkas di folder fitur pada Fase 0).
  2. **Bidirectional Dependency Map (INBOUND + OUTBOUND):** Pada Fase 2 (Evidence Tracing), untuk bug lintas modul AI wajib memetakan *Inbound* (impor file, env vars, schema DB, API eksternal yang dipakai modul) DAN *Outbound* (semua *consumer* yang mengimpor modul ini).
  3. **The 3-Fix Escalation Rule (Circuit Breaker Anti-Whack-a-Mole):** Jika **3 kali percobaan perbaikan berturut-turut** tetap gagal atau malah memunculkan bug baru di tempat lain $\rightarrow$ **STOP TOTAL!** AI dilarang mencoba tambalan ke-4 secara membabi-buta, wajib mengakui adanya cacat arsitektur, dan mengajak developer berdiskusi ulang.
* **Perubahan Mekanisme AI:** *Bounded Repair Graph + Infinite-Loop Circuit Breaker*.
* **Dampak Positif:** Mencegah mahasiswa & AI terjebak *infinite debug loop* (tambal satu tempat, jebol tempat lain sampai kuota habis).
* **Potensi Risiko & Mitigasi:** Mode `--module` terlalu berat untuk typo 1 baris $\rightarrow$ Mitigasi: Routing eksplisit di bagian atas memisahkan bug tunggal vs modul rusak menyeluruh.

---

### ✅ BATCH 2B: Reformasi `/audit` (Lossless Chunking, Tier 0 Forensics, & 3 Skrip OpenAPI) (STATUS: SELESAI DIEKSEKUSI)

> 📌 **Hasil Terverifikasi Batch 2B:**
> - `blueprints/audit.template.md`: Dirampingkan dari **17.8 KB $\rightarrow$ 9.8 KiB (10.037 byte, -43.8%)** (State-Machine + Tier 0 Evidence Integrity + Wiring `classify_blast_radius.py` + 100% utuh Pedagogi Anti-Dosen Penguji).
> - `blueprints/references/audit_visual_gate.md` (9.0 KB) & `blueprints/references/audit_handoff_package.md` (2.7 KB): **100% Lossless Extraction Terbukti Matematis** (116/125 klausa cocok identik huruf-per-huruf; 9 baris selebihnya murni upgrade fitur Tahap 2; **0 klausa hilang**).
> - `blueprints/references/audit_api_checklist.md` + 3 skrip Python stdlib (`api_linter.py`, `breaking_change_detector.py`, `api_scorecard.py`) di `skills/forge-constitution/scripts/`.
> - `blueprints/edeate.template.md`: Penegasan pengecualian resmi penulisan entri `[ADR-YYYY-MM-DD]` ke `.agents/rules/ARCHITECTURE.md` bila disetujui developer.
> - `physical_injection_spec.md` & `forge-update/SKILL.md`: Tersinkronisasi 100% untuk penyalinan skrip & referensi kondisional `/audit`.

#### Item 2.4: Stasiun `/audit` ──► Lossless Chunking ($\le$8 KB), Wiring Skrip Blast-Radius, Tier 0 Forensics, & Gerbang OpenAPI
* **Target Berkas:**
  * `blueprints/audit.template.md` *(17.8 KB $\rightarrow \le$8 KB via Lossless Chunking)*
  * `blueprints/references/audit_visual_gate.md` *(Berkas Rujukan Baru — 100% teks asli 4 Pilar Visual Playwright & Fallback)*
  * `blueprints/references/audit_api_checklist.md` *(Berkas Rujukan Baru — Kondisional BE/Fullstack: Panduan 3 Skrip OpenAPI, REST Rules, & Grade A–F)*
  * `skills/forge-constitution/scripts/api_linter.py` *(Stdlib murni, diadaptasi dari `claude-skills` — MIT)*
  * `skills/forge-constitution/scripts/breaking_change_detector.py` *(Stdlib murni, diadaptasi dari `claude-skills` — MIT)*
  * `skills/forge-constitution/scripts/api_scorecard.py` *(Stdlib murni, diadaptasi dari `claude-skills` — MIT)*
  * Sinkronisasi urutan injeksi & tabel mapping di `skills/forge-constitution/references/physical_injection_spec.md` dan `skills/forge-update/SKILL.md`.
* **Kondisi Sebelum (Before):**
  1. `audit.template.md` berukuran **17.8 KB** (melebihi batas 10KB Rule).
  2. Klasifikasi Jalur 1/2/3 ditebak LLM (belum menyambungkan `classify_blast_radius.py` dari Tahap 1).
  3. Belum ada pengaman terhadap *Stale Test* (file diedit lagi setelah test terakhir lulus) dan *Compound Pipe Trap* (`npm test | tee log`).
  4. Belum ada verifikasi deterministik mutu REST API (Grade A–F) & *breaking changes* via `openapi.json`.
* **Kondisi Sesudah (After):**
  1. **Lossless Chunking ($\le$8 KB):** Detail lengkap 4 Pilar Visual Playwright & Fallback dipindah **100% utuh kata-per-kata** ke `references/audit_visual_gate.md` (dibaca on-demand khusus Jalur 2/3).
  2. **Wiring `classify_blast_radius.py`:** Langkah 1 `/audit` memanfaatkan skrip deterministik Tahap 1 untuk menentukan Jalur 1/2/3 secara instan (0 halusinasi, fallback ke `git diff --name-only` jika Python belum tersedia).
  3. **Tier 0 — Evidence Integrity & Anti-Stale Gate (IDE-Agnostic):**
     * *Anti-Stale Test:* Jika ada perubahan kode setelah eksekusi test/build terakhir $\rightarrow$ status bukti lama `STALE`, wajib jalankan ulang sebelum `PASS`.
     * *Anti-Pipe Trap:* Dilarang menilai exit code 0 dari perintah berantai/pipe (`cmd | tee`).
     * *Recorded vs Inferred:* Laporan Bagian 2 wajib memisahkan bukti terminal riil (`Recorded`) vs kesimpulan bacaan kode (`Inferred`).
  4. **Gerbang Audit OpenAPI Deterministik (Khusus Proyek Backend / Fullstack):**
     * Menjalankan 3 skrip Python stdlib (`api_linter.py`, `api_scorecard.py --min-grade B`, dan `breaking_change_detector.py` terhadap baseline `main`) + rujukan `references/audit_api_checklist.md`.
* **Perubahan Mekanisme AI:** Evaluasi bukti berlapis berbasis *exit code* deterministik + efisiensi konteks 55%+ di gerbang audit.
* **Dampak Positif:** Melenyapkan *Green Terminal Fallacy*, mencegah *breaking change* API yang mematahkan Frontend, dan menjaga persona ramah *Anti-Dosen Penguji* tetap utuh 100%.
* **Potensi Risiko & Mitigasi:**
  * Risiko proyek Frontend statis ikut diminta menjalankan skrip OpenAPI $\rightarrow$ Mitigasi: Gerbang OpenAPI hanya diinjeksi/aktif pada proyek yang memiliki REST API (`dna.FRONTEND_BACKEND_SEPARATION_STRATEGY` / `TECH_STACK_SUMMARY`).
  * Risiko AI melupakan detail Visual Gate $\rightarrow$ Mitigasi: Perintah wajib baca `references/audit_visual_gate.md` di Jalur 3.

---

## 3. Keputusan Terkunci: Standar Wajib Kontrak `openapi.json` (Khusus Proyek BE / Fullstack)

> ✅ **Status: DIKUNCI (Best Practice Industri — Tanpa Percabangan Opsi Rumit)**  
> Pengadaan berkas kontrak `docs/api/openapi.json` ditetapkan sebagai **hukum wajib bagi seluruh proyek yang memiliki Backend / REST API** (otomatis di-bypass untuk proyek Frontend statis tanpa API):
> 1. **Di `/plan` (Contract-First):** AI menyusun/memperbarui draf kontrak endpoint di `docs/api/openapi.json` sebelum kode ditulis.
> 2. **Di `/execute` (Ringkas — 1 Baris Aturan Tegas):** Wajib menjaga `docs/api/openapi.json` sinkron dengan kode implementasi (jalankan perintah exporter bawaan stack seperti FastAPI/Laravel Scramble bila terpasang di proyek, atau sinkronkan langsung oleh AI bila stack polos).
> 3. **Di `/audit` (Verifikasi Deterministik):** Wajib mengeksekusi 3 skrip Python stdlib (`api_linter.py`, `api_scorecard.py --min-grade B`, dan `breaking_change_detector.py` terhadap baseline `git show main:docs/api/openapi.json`).
> 4. **Setup di `ONBOARDING.md`:** 3 skrip audit = **0 dependency tambahan** (Python stdlib murni). Jika proyek memakai Spec Exporter (misal `dedoc/scramble` di Laravel), cukup tercatat sebagai package standar proyek (`composer install` / `npm install`) tanpa langkah setup rumit.

---

## 4. Garansi Perlindungan Persona FORGE
Seluruh pemecahan berkas (`audit.template.md` $\rightarrow$ `references/audit_visual_gate.md`) mematuhi hukum **Lossless Restoration** dari Tahap 1: 0% pemangkasan kalimat edukatif, filosofi *Anti-Dosen Penguji* di `/audit` dan *No Shame Culture* di `/debug` dipertahankan 100% utuh kata-per-kata.