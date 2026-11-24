# Fase 1: Standar Penulisan & Komparasi 10 Pola vs Skill Hasil FORGE (`eco-enzyme-landing/.agents`)
**Sumber Referensi:** `alirezarezvani/claude-skills` (`SKILL-AUTHORING-STANDARD.md` & `CONVENTIONS.md`)  
**Objek Komparasi Nyata:** Seluruh file Konstitusi & Skill hasil scaffolding dapur FORGE pada proyek nyata:  
`C:\Users\sofya\Documents\JS\eco-enzyme-landing\.agents\`

---

## 1. Peta Anatomi Skill di Proyek `eco-enzyme-landing/.agents`

Di proyek `eco-enzyme-landing`, FORGE telah menghasilkan arsitektur AI yang terdiri dari:
1. **Folder `rules/` (Hukum Permanen Proyek):**
   * `00-router.md` (Router Konstitusi & Anti Yes-Man)
   * `MASTER_RULES.md` (Hukum Arsitektur, Unmounted Guard, Blast-Radius, Gating System - 16.8 KB)
   * `ARCHITECTURE.md` (Fakta DNA & Keputusan Kunci)
   * `GIT_WORKFLOW.md` (Hukum Branch & PR)
   * `META_RULES.md` (State-Machine & Tool-First Audit)
2. **Folder `skills/` (SOP Alur Kerja Operasional):**
   * `project-edeate` (`SKILL.md`: **49.5 KB** - Gerbang Hulu / Ideasi & PRD)
   * `project-audit` (`SKILL.md`: **17.6 KB** - Gerbang Hilir / Four-Tier Quality Gate)
   * `project-grill-me` (`SKILL.md`: **15.6 KB** - Interogasi Rencana)
   * `project-debug` (`SKILL.md`: 8.7 KB)
   * `project-execute` (`SKILL.md`: 7.2 KB)
   * `project-plan` (`SKILL.md`: 5.5 KB)
   * `project-tdd` (`SKILL.md`: 3.5 KB)
   * `project-epic-persistence` (`SKILL.md`: 3.1 KB)
   * `session-handoff` (`SKILL.md`: 10 KB + `scripts/` + `references/` + `assets/`)

---

## 2. Matriks Komparasi 1-to-1: 10 Pola Enterprise vs Skill FORGE di `eco-enzyme-landing`

Berikut adalah hasil audit komparasi sistematis untuk **seluruh 10 Pola Arsitektur**:

| No | Pola Arsitektur Enterprise | Standar Enterprise (`claude-skills`) | Kondisi Riil di `eco-enzyme-landing/.agents` | Status Komparasi |
| :---: | :--- | :--- | :--- | :---: |
| **1** | **Context-First** | Wajib periksa context sebelum bertanya. Hanya tanyakan yang belum tercatat (*gap only*). | `project-edeate` memiliki **Tahap 0: Pre-Flight Audit** untuk membaca codebase sebelum wawancara. | 🟢 **Sangat Baik** |
| **2** | **Practitioner Voice** | Praktisi senior 100x. Beropini tegas ("Lakukan X, jangan Y"). | **Luar biasa.** `00-router.md` mewajibkan **Anti Yes-Man & Devil's Advocate**, `project-audit` menggunakan filosofi "Kakak Tingkat Senior". | 🏆 **FORGE Unggul** |
| **3** | **Multi-Mode Workflows** | Wajib membagi minimal Mode 1 (Greenfield) vs Mode 2 (Brownfield). | `project-audit` memiliki **Smart Blast-Radius Tri-Track** (Jalur 1 BE, Jalur 2 FE Logic, Jalur 3 Visual UI). `/edeate` memiliki **Dual-Track Routing** (Track A FEAT vs Track B ARCH). | 🏆 **FORGE Unggul** |
| **4** | **Related Skills Disambiguation** | Wajib ada seksi `Related Skills` dengan klausul tegas **WHEN TO USE** dan **NOT FOR**. | Ada `00-router.md`, namun di masing-masing file `SKILL.md` **belum ada klausul `NOT FOR`** untuk mencegah tumpang tindih. | ⚠️ **Celah Kritis** |
| **5** | **Reference Separation (10KB Rule)** | `SKILL.md` ketat $\le$10KB. Pengetahuan tebal dipindah ke `references/` (on-demand). | **Monolitik Raksasa.** `project-edeate` berukuran **49.5 KB** dan `project-audit` **17.6 KB** dalam satu file datar tanpa folder `references/`. | 🔴 **Kelemahan Fatal** |
| **6** | **Proactive Triggers** | 4–6 poin bahaya tersembunyi yang agen **wajib suarakan tanpa diminta**. | FORGE punya hukum proteksi kuat (*Unmounted Guard `if (!isOpen) return null;`*, *Sticky Collision Gate*), tapi terkubur dalam teks panjang. | 🟡 **Parsial** |
| **7** | **Output Artifacts Mapping** | Tabel deliverable: *"Jika minta X $\rightarrow$ kamu dapat artefak Y format Z"*. | Output sudah terstandarisasi (`.docs/plan/`, PR Handoff), namun belum dipetakan dalam tabel ringkas di header skill. | 🟡 **Parsial** |
| **8** | **Quality Loop & Verification** | AI self-verify & tag bukti: 🟢 Verified, 🟡 Medium, 🔴 Assumed. | **Standar Uji Luar Biasa di `/audit`:** *Four-Tier Quality Gate* + *Playwright Visual Smoke* anti-manipulasi. Namun di fase ideasi belum ada tagging keyakinan bukti. | 🟢 **Sangat Kuat (di Audit)** |
| **9** | **Structured Communication** | *Bottom line first* (kesimpulan di baris 1), What-Why-How, tanpa narasi bertele-tele. | Laporan `/audit` sangat rapi terstruktur (4 Bagian). Namun di `/edeate`, percakapan masih sering sangat panjang karena gaya mengajar Socratic. | 🟡 **Parsial** |
| **10** | **Python Tools (Stdlib-Only)** | Skrip Python mandiri di `scripts/` untuk scoring 0–100 dan validasi otomatis. | Seluruh skill asli FORGE **0% memiliki folder `scripts/`** (hanya `session-handoff` yang memilikinya). Bergantung 100% pada LLM. | 🔴 **Kelemahan FORGE** |

---

## 3. Bedah Mendalam Tiap Pola pada Skill `eco-enzyme-landing`

### Pattern 1: Context-First (Nilai: 🟢 Sangat Baik)
* **Kenyataan di Lapangan:**  
  Di `project-edeate/SKILL.md`, FORGE sudah menanamkan **"Tahap 0: Pre-Flight Audit (Codebase Exploration)"**. Agen diperintahkan untuk membaca AST kode, package.json, dan route yang ada *sebelum* mulai mewawancarai developer.
* **Celah yang Perlu Diperbaiki:**  
  Meskipun Tahap 0 ada, agen di `/edeate` kadang tetap menanyakan hal bisnis yang sebenarnya sudah tertulis di `ARCHITECTURE.md` atau `README.md`.
* **Rekomendasi:** Tambahkan instruksi eksplisit di baris paling atas `project-edeate/SKILL.md`:  
  *"BACA `ARCHITECTURE.md` terlebih dahulu. Dilarang menanyakan ulang aktor bisnis atau batasan arsitektur yang sudah didefinisikan di dokumen tersebut."*

---

### Pattern 2: Practitioner Voice (Nilai: 🏆 FORGE Unggul)
* **Kenyataan di Lapangan:**  
  Skill FORGE di `eco-enzyme-landing` memiliki kepribadian paling solid:
  * Di `00-router.md`: *"ANTI YES-MAN & DEVIL'S ADVOCATE: Jangan pernah menyetujui ide yang cacat secara arsitektur hanya demi menyenangkan pengguna."*
  * Di `project-audit`: Menggunakan filosofi *Kakak Tingkat Senior* yang mendidik developer tentang *Zero Test-Tampering Law* dan *Real Inner-Viewport 1280x680*.
* **Kesimpulan:** Gaya bicara FORGE jauh lebih mendalam dan melindungi proyek daripada gaya instruksi repo luar yang sering kali terlalu kering dan kaku.

---

### Pattern 3: Multi-Mode Workflows (Nilai: 🏆 FORGE Unggul)
* **Kenyataan di Lapangan:**  
  FORGE di proyek ini telah menerapkan spesialisasi mode tingkat tinggi:
  * Di `project-audit`: **Smart Blast-Radius Tri-Track Routing** (Jalur 1: Pure BE bypass visual, Jalur 2: Frontend Refactor logic-only + manual smoke checklist, Jalur 3: Active UI wajib Playwright multi-viewport).
  * Di `project-edeate`: **Dual-Track Routing** (Track A: FEAT Socratic Bisnis vs Track B: ARCH/REFACTOR NFR Fast-Track).
* **Kesimpulan:** Pembagian mode berbasis domain dampak (*blast radius*) di FORGE adalah inovasi kelas enterprise yang melampaui rata-rata skill umum di GitHub.

---

### Pattern 4: Related Skills Navigation & Disambiguation (Nilai: ⚠️ Celah Kritis)
* **Kenyataan di Lapangan:**  
  Di proyek `eco-enzyme-landing`, terdapat 9 skill berbeda di `.agents/skills/`.
  * Masalahnya: Di dalam file `project-plan/SKILL.md`, **tidak ada klausul yang melarang agen melakukan ideasi bisnis**. Akibatnya, jika user mengetik *"buatkan rencana fitur donasi"*, agen di `/plan` kadang malah masuk ke diskusi ideasi bisnis yang seharusnya menjadi tugas `/edeate`.
* **Rekomendasi:** Di setiap `SKILL.md`, tambahkan seksi:
  ```markdown
  ## Related Skills
  - **project-edeate**: Untuk menggali kebutuhan bisnis dan PRD. BUKAN untuk breakdown tiket sprint (gunakan project-plan).
  - **project-audit**: Untuk validasi kelayakan PR sebelum merge. BUKAN untuk mencari root-cause bug aktif (gunakan project-debug).
  ```

---

### Pattern 5: Reference Separation / The 10KB Rule (Nilai: 🔴 Kelemahan Fatal)
* **Kenyataan di Lapangan:**  
  Mari kita lihat perbandingan ukuran file di folder `.agents/skills/`:
  * `project-edeate/SKILL.md`: **49.5 KB** (Hampir 5x batas standar enterprise!).
  * `project-audit/SKILL.md`: **17.6 KB**.
  * Bandingkan dengan `session-handoff/SKILL.md` (hanya **10 KB** karena memisahkan panduannya ke folder `references/` dan `scripts/`).
* **Dampak Buruknya:**  
  Saat developer memanggil `/edeate`, memori AI langsung dibanjiri 49KB teks panduan. Ini menyebabkan:
  1. Konsumsi token melonjak drastis.
  2. Terjadinya *Attention Dilution* (AI mulai lupa aturan di tengah file, seperti melewatkan *Hard Stop Macro* atau lupa melakukan Pre-Flight Audit).
* **Rekomendasi:** Pecah `project-edeate` menjadi:
  * `SKILL.md` ($\le$8KB): Alur Gateway Hulu & State Machine.
  * `references/dual_track_protocol.md`: Panduan Track A vs Track B.
  * `references/ticket_templates.md`: Contoh draf Tiket Level 3.

---

### Pattern 6: Proactive Triggers (Nilai: 🟡 Parsial)
* **Kenyataan di Lapangan:**  
  `MASTER_RULES.md` memiliki aturan proaktif yang luar biasa:
  * *Hukum Default Unmounted Guard:* `if (!isOpen) return null;` untuk mencegah memori bocor pada modal.
  * *Hug-Content Adaptive Bounds:* Larangan hardcode tinggi `h-[600px]` pada kartu dinamis.
  * *Real Anchor-Click Sticky Collision Gate:* Mencegah tombol tertutup navbar sticky.
* **Celahnya:**  
  Aturan ini ditulis sebagai pasal undang-undang pasif di dalam file 16KB, bukan disajikan sebagai **4–6 Proactive Triggers di header skill**. Akibatnya, saat agen menulis kode di `/execute`, agen sering baru sadar setelah ditegur di fase `/audit`.
* **Rekomendasi:** Pindahkan aturan-aturan emas ini ke blok `## Proactive Triggers` di `project-execute/SKILL.md`.

---

### Pattern 7: Output Artifacts Mapping (Nilai: 🟡 Parsial)
* **Kenyataan di Lapangan:**  
  FORGE sudah memiliki standar deliverable yang jelas:
  * `/edeate` $\rightarrow$ Issue GitHub Level 3.
  * `/plan` $\rightarrow$ `.docs/plan/issue-<nomor>-<prefix>-<slug>.md`.
  * `/audit` $\rightarrow$ PR Handoff Report lengkap dengan 4-Tier Gate.
* **Rekomendasi:** Rangkum artefak ini dalam tabel `Output Artifacts` di bagian atas masing-masing skill agar developer dan AI memiliki ekspektasi format yang instan.

---

### Pattern 8: Quality Loop & Verification (Nilai: 🟢 Sangat Kuat di Audit)
* **Kenyataan di Lapangan:**  
  Modul `project-audit` di `eco-enzyme-landing` adalah salah satu sistem audit terketat:
  * Menolak *Green Terminal Fallacy*.
  * Menguji responsivitas Playwright pada viewport nyata `1280x680`.
  * Mengharuskan tangkapan layar visual riil dijabarkan di chat.
* **Celahnya:**  
  Di fase perancangan `/edeate` dan `/plan`, AI belum menggunakan **Confidence Tagging** (🟢 Verified / 🟡 Medium / 🔴 Assumed) saat membuat estimasi teknis.

---

### Pattern 9: Structured Communication (Nilai: 🟡 Parsial)
* **Kenyataan di Lapangan:**  
  Laporan audit di `project-audit` sangat rapi dan berstruktur (dibagi menjadi 4 bagian baku).  
  Namun pada saat sesi `/edeate` dan `/grill-me`, AI sering kali memberikan respons yang terlalu panjang (bisa 4–5 layar HP) sebelum memberikan pertanyaan intinya.
* **Rekomendasi:** Terapkan prinsip **Bottom Line First**: Sajikan kesimpulan dan pertanyaan inti di paragraf pertama, baru diikuti dengan penjelasan latar belakang dan timbangan konsekuensi di bawahnya.

---

### Pattern 10: Python Tools / Stdlib-Only Automation (Nilai: 🔴 Kelemahan FORGE)
* **Kenyataan di Lapangan:**  
  Perhatikan fakta menarik di folder `eco-enzyme-landing/.agents/skills/`:
  * Satu-satunya skill yang memiliki folder `scripts/` adalah `session-handoff` (yang memiliki `cleanup.py`, `handoff_self_check.py`, `redaction_linter.py`).
  * Seluruh skill buatan FORGE (`project-edeate`, `project-audit`, `project-plan`, `project-execute`) **sama sekali tidak memiliki skrip pembantu**.
  * Seluruh pengecekan linting, AST diff, dan validasi checklist diserahkan 100% pada pembacaan teks oleh LLM. Ini lambat, boros token, dan rentan salah hitung.
* **Rekomendasi:**  
  Buat script Python stdlib sederhana untuk mendampingi skill FORGE, misalnya:
  * `scripts/blast_radius_checker.py`: Script 30 baris untuk memeriksa `git diff --name-only` dan langsung menentukan secara deterministik apakah tiket masuk Jalur 1, 2, atau 3.

---

## 4. Kesimpulan Evaluasi Dapur FORGE

Dapur FORGE telah menghasilkan konstitusi dan skill dengan **fondasi rekayasa perangkat lunak yang sangat matang (Tier Enterprise untuk filosofi & quality gate)**. 

Namun, ada **2 penyakit arsitektur utama** yang diwariskan dapur FORGE ke proyek `eco-enzyme-landing`:
1. **Penyakit Monolitik (Melanggar Pattern 5):** File `SKILL.md` terlalu gemuk (mencapai 49.5KB), memboroskan token dan memicu kelupaan AI.
2. **Ketergantungan Total pada Prompt Teks (Melanggar Pattern 10):** Tidak ada skrip Python deterministik untuk membantu tugas-tugas kalkulasi/klasifikasi mekanis.

Jika dua hal ini kita benahi dengan mengadopsi standar modular dari repo `claude-skills`, skill hasil dapur FORGE akan menjadi **tak tertandingi**: memiliki filosofi rekayasa yang sangat bijak, namun berjalan dengan performa secepat kilat dan hemat token.

---
*Dokumen ini merupakan audit komparasi resmi berbasis kode nyata di `eco-enzyme-landing/.agents`.*
