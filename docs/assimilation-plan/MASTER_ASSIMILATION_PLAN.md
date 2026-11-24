# Master Assimilation Plan: Cetak Biru Perubahan Dapur FORGE
**Status:** Dokumen Rencana Aksi Sebelum Eksekusi (Menunggu Persetujuan Pengguna)  
**Tujuan Dokumen:** Memaparkan secara transparan setiap perubahan berkas, membandingkan kondisi *Sebelum vs Sesudah*, menjelaskan perubahan mekanisme kerja AI, membeberkan keuntungan dan potensi risiko, serta **menjamin 100% perlindungan Persona & Jiwa Mentor FORGE**.  
**Lokasi Berkas Target:** Dapur Scaffolder FORGE (`d:/exe/HERD/SIM/FORGE/`)

---

## 1. Janji Perlindungan Mutlak: DNA & Persona FORGE Tidak Boleh Hilang

Sebelum masuk ke rincian teknis, berikut adalah **Prinsip Garansi Mutlak**:
> **Persona "The Principal Engineer & Mentor (Kakak Tingkat Senior yang Ramah)" adalah aset termahal FORGE.**  
> Perubahan ini **BUKAN** untuk mengubah FORGE menjadi asisten korporat yang kaku dan dingin ala Silicon Valley. Seluruh nilai pedagogi: *Active Mentorship, The Trade-Off Balance Scale, The Safe Harbor (Jaring Pengaman Mahasiswa Baru), dan Anti-Yes Man* **DIJAMIN 100% TETAP HIDUP**.

Tujuan refactoring ini murni membedah **struktur teknis di balik layar**: membuat mesinnya berjalan lebih cepat, lebih hemat token, dan bebas dari kebingungan kognitif (*attention dilution*), sementara suara yang berbicara ke mahasiswa tetaplah suara Kakak Tingkat yang hangat.

---

## 2. Struktur Analisis Perubahan (Format Sebelum vs Sesudah)

Setiap butir perubahan di bawah ini dianalisis menggunakan format evaluasi 6 dimensi:
* **Kondisi Sebelumnya (Before):** Bagaimana file dan prompt bekerja saat ini.
* **Kondisi Sesudah (After):** Bagaimana file dan struktur baru setelah diubah.
* **Mekanisme Kerja AI:** Apa yang terjadi di dalam proses berpikir/eksekusi LLM.
* **Dampak Positif (Keuntungan):** Manfaat nyata bagi performa dan mahasiswa.
* **Potensi Risiko / Dampak Negatif:** Kemungkinan efek samping buruk yang bisa timbul.
* **Langkah Mitigasi Risiko:** Cara kita memastikan risiko tersebut tidak terjadi.

---

## TAHAP 1: PEMBENAHAN 7 PILAR POLA PRIORITAS (Fondasi Wadah)

---

### Item 1.1: Pembuatan `project-context.template.md` & Protokol Gap-Only (Pola 1)
* **Target Berkas:** `blueprints/project-context.template.md` *(Baru)*, `blueprints/00-router.template.md`, `blueprints/edeate.template.md`
* **Kondisi Sebelumnya (Before):**  
  AI memulai sesi `/edeate` atau `/plan` dengan menodong pertanyaan umum (*"Kamu mau bikin apa? Tech stack-nya apa?"*) meskipun informasi tersebut sudah ada di repo.
* **Kondisi Sesudah (After):**  
  Disediakan berkas `.agents/rules/project-context.md`. Di awal sesi, AI membaca berkas ini secara diam-diam (*Silent Inspection*), lalu hanya menanyakan data yang belum ada (*Gap-Only*).
* **Perubahan Mekanisme AI:**  
  AI beralih dari mode *Generatif Tanya-Semua* menjadi mode *Diff-Checking* (membandingkan variabel yang dibutuhkan vs variabel yang sudah tercatat di file).
* **Dampak Positif (Keuntungan):**  
  Mahasiswa tidak jengkel karena ditanyai hal-hal dasar berulang kali. Menghemat 3–5 putaran chat yang tidak perlu.
* **Potensi Risiko / Dampak Negatif:**  
  Jika file `project-context.md` berisi data usang (misal mahasiswa ganti tech stack tapi lupa update file), AI bisa mengambil keputusan berdasarkan data lama.
* **Mitigasi:** Tambahkan aturan konfirmasi ringan di `/explore` atau awal `/edeate`: *"Saya melihat tech stack di project-context adalah Astro+Tailwind, apakah masih sesuai?"*

---

### Item 1.2: Pemisahan Monolitik / The 10KB Rule (Pola 5)
* **Target Berkas:** `skills/forge-constitution/SKILL.md` (31.4KB $\rightarrow \le$8KB), `blueprints/edeate.template.md` (49.5KB $\rightarrow \le$8KB), pembuatan folder `blueprints/references/`
* **Kondisi Sebelumnya (Before):**  
  Semua instruksi panduan (Track A/B, varian tiket, contoh kasus, anti-pattern) ditumpuk jadi satu di dalam satu berkas raksasa 49.5 KB.
* **Kondisi Sesudah (After):**  
  `edeate.template.md` hanya berisi alur kerja 5 tahap dan state machine ($\le$8KB). Rincian format tiket dipindah ke `references/ticket_variants.md`, dan tabel anti-pattern dipindah ke `references/anti_patterns.md`. AI membaca referensi tersebut hanya saat tahap terkait aktif.
* **Perubahan Mekanisme AI:**  
  Menghilangkan fenomena *Lost in the Middle*. Perhatian (*attention score*) AI fokus 100% pada aturan fase yang sedang dikerjakan tanpa terdistraksi oleh teks ratusan baris lain.
* **Dampak Positif (Keuntungan):**  
  Konsumsi token turun drastis (menghemat ~10.000 token per giliran). AI tidak lagi "lupa" aturan *Hard Stop* atau melompati audit.
* **Potensi Risiko / Dampak Negatif:**  
  Jika AI lupa memanggil berkas referensi saat dibutuhkan, AI bisa menghasilkan tiket yang formatnya kurang lengkap.
* **Mitigasi:** Pasang instruksi tegas ber-path eksplisit di `SKILL.md`: *"Saat memasuki Tahap 4, kamu WAJIB membaca file `references/ticket_variants.md` sebelum mencetak draf tiket."*

---

### Item 1.3: Proactive Triggers di Header Skill (Pola 6)
* **Target Berkas:** `blueprints/execute.template.md`, `blueprints/plan.template.md`
* **Kondisi Sebelumnya (Before):**  
  Aturan emas proteksi UI (Unmounted Guard `if (!isOpen) return null;`, Sticky Collision, Adaptive Bounds) terkubur di baris 400-an berkas `MASTER_RULES.md`. Saat koding di `/execute`, AI sering lupa dan baru ditegur saat `/audit`.
* **Kondisi Sesudah (After):**  
  Aturan-aturan tersebut diekstrak menjadi blok `## Proactive Triggers` tepat di bawah header berkas `execute.template.md` (bagian yang paling pertama dibaca AI).
* **Perubahan Mekanisme AI:**  
  AI mengaktifkan "mata elang" (*pattern recognition*). Saat AI mengetik kode komponen Modal, trigger otomatis aktif di otaknya untuk memasang `if (!isOpen) return null;` sejak baris pertama kode ditulis.
* **Dampak Positif (Keuntungan):**  
  Mencegah bug visual dan memory leak sejak fase koding. Waktu audit di hilir menjadi jauh lebih cepat karena kodenya sudah bersih dari awal.
* **Potensi Risiko / Dampak Negatif:**  
  AI bisa menjadi terlalu kaku atau over-protective pada komponen eksperimental yang belum butuh guard.
* **Mitigasi:** Nyatakan secara spesifik kondisi pemicunya (misal: *Hanya aktif jika komponen memiliki state isOpen/modal*).

---

### Item 1.4: Output Artifacts Mapping (Pola 7)
* **Target Berkas:** Seluruh berkas template di `blueprints/*.template.md`
* **Kondisi Sebelumnya (Before):**  
  Bentuk dan lokasi file yang dihasilkan dijelaskan tersebar dalam paragraf narasi panjang.
* **Kondisi Sesudah (After):**  
  Di bagian atas setiap skill dicantumkan tabel kontrak deliverable:
  | Saat Meminta... | Yang Dihasilkan AI... | Lokasi Berkas Fisik |
  | :--- | :--- | :--- |
* **Perubahan Mekanisme AI:**  
  AI memiliki ekspektasi output yang terkunci (*deterministic output path*), tidak lagi mengarang lokasi penyimpanan baru secara acak.
* **Dampak Positif (Keuntungan):**  
  Mahasiswa tahu persis di mana file mereka tersimpan. Struktur proyek selalu rapi.
* **Potensi Risiko:** Hampir nol resiko (murni standarisasi tabel).

---

### Item 1.5: Keyakinan Bukti / Confidence Tagging (Pola 8)
* **Target Berkas:** `blueprints/master_rules.template.md`, `blueprints/grill-me.template.md`
* **Kondisi Sebelumnya (Before):**  
  AI menyampaikan saran teknis tanpa membedakan mana yang merupakan fakta kode di repo vs mana yang hanya asumsi/tebakan AI.
* **Kondisi Sesudah (After):**  
  Setiap rekomendasi wajib diberi tag simbol: 🟢 *Verified* (ada di kode/dokumentasi), 🟡 *Medium* (best practice industri), 🔴 *Assumed* (tebakan AI yang wajib dikonfirmasi mahasiswa).
* **Perubahan Mekanisme AI:**  
  AI dipaksa melakukan *Self-Verification* (audit keyakinan) sebelum mengeluarkan pendapat.
* **Dampak Positif (Keuntungan):**  
  Mendidik mahasiswa agar kritis: mahasiswa tahu mana fakta keras dan mana hal yang masih harus mereka uji. Menghilangkan halusinasi AI yang berkedok percaya diri palsu.
* **Potensi Risiko / Dampak Negatif:**  
  Tampilan chat ada tambahan ikon warna yang mungkin sedikit asing bagi pemula di hari pertama.
* **Mitigasi:** Berikan legenda penjelasan singkat di sesi pertama: *"🟢 artinya sudah pasti ada di kodemu, 🔴 artinya tebakanku yang butuh persetujuanmu"*.

---

### Item 1.6: Kesimpulan di Baris Pertama / Bottom Line First (Pola 9)
* **Target Berkas:** `blueprints/master_rules.template.md`
* **Kondisi Sebelumnya (Before):**  
  AI sering menulis 3–4 paragraf ceramah panjang dan analogi sebelum akhirnya memberikan jawaban intinya di bagian paling bawah (*Verbosity Fatigue*).
* **Kondisi Sesudah (After):**  
  Rumus jawaban diubah: **Vonis/Keputusan langsung di Baris 1**, baru disusul penjelasan **What + Why + How**, dan analogi ramah diletakkan di bawah.
* **Perubahan Mekanisme AI:**  
  AI dipaksa berpikir secara terstruktur (*Inverted Pyramid Structure*).
* **Dampak Positif (Keuntungan):**  
  Mahasiswa yang sedang buru-buru koding langsung mendapatkan inti solusi dalam 3 detik tanpa harus scroll layar berulang kali.
* **Potensi Risiko (PENTING untuk Persona FORGE):**  
  **Risiko:** Jika terlalu ekstrem to-the-point, AI bisa kehilangan kehangatan gaya mengajar Kakak Tingkatnya dan berubah menjadi robot kaku.
* **Mitigasi Mutlak:** Kita TIDAK melarang analogi dan edukasi ramah! Analogi ramah tetap ada, tetapi posisinya ditaruh **setelah** kesimpulan baris pertama disajikan.

---

### Item 1.7: Skrip Otomasi Python Lokal Stdlib-Only (Pola 10)
* **Target Berkas:** `skills/forge-constitution/scripts/` *(Folder Baru)*: `classify_blast_radius.py`, `validate_manifest.py`
* **Kondisi Sebelumnya (Before):**  
  0 file skrip. Tugas mekanis (seperti membaca `git diff --name-only` untuk menentukan Jalur 1, 2, atau 3 di `/audit`) diserahkan 100% pada pembacaan teks oleh LLM.
* **Kondisi Sesudah (After):**  
  Dibuat skrip Python mandiri (menggunakan modul bawaan Python, tanpa `pip install`). AI menjalankan skrip via terminal untuk klasifikasi jalur secara instan.
* **Perubahan Mekanisme AI:**  
  Tugas klasifikasi dialihkan dari *Penalaran Bahasa* ke *Algoritma Deterministik CPU*.
* **Dampak Positif (Keuntungan):**  
  Kecepatan eksekusi di `/audit` naik drastis (selesai dalam 5 milidetik), 0 token prompt terbuang, dan akurasi 100% (tidak ada halusinasi salah jalur).
* **Potensi Risiko / Dampak Negatif:**  
  Lingkungan mahasiswa harus memiliki Python terinstal di laptopnya.
* **Mitigasi:** Skrip dibuat murni menggunakan Python Standard Library (`sys`, `os`, `json`, `subprocess`) tanpa library pihak ketiga agar jalan di instalasi Python versi apa pun (Python 3.8 s.d. 3.13).

---

## TAHAP 2: INJEKSI PERKAKAS SPESIFIK KE 5 STASIUN GERBANG

---

### Item 2.1: Injeksi Skrip API Reviewer ke Stasiun `/audit`
* **Target Berkas:** `blueprints/audit.template.md`, penambahan skrip di `skills/forge-constitution/scripts/`: `api_linter.py`, `breaking_change_detector.py`, `api_scorecard.py`
* **Kondisi Sebelumnya (Before):**  
  Modul `/audit` (v1.3.6) sudah sangat hebat untuk Visual UI Playwright (Tier 4), tetapi untuk endpoint API, AI hanya membaca manual tanpa standarisasi.
* **Kondisi Sesudah (After):**  
  Di Bagian 2 `/audit`, ditambahkan verifikasi otomatis: skrip menghitung mutu API (Grade A–F) dan mendeteksi apakah ada perubahan yang mematikan klien (*breaking changes*).
* **Dampak Positif:** Mahasiswa belajar membuat API REST yang rapi sesuai standar industri (status code benar, penamaan konsisten).
* **Potensi Risiko:** Jika skrip terlalu galak, mahasiswa pemula bisa stres karena nilainya dapat Grade C atau D.
* **Mitigasi:** Skrip diatur dalam mode *Edukasi* di tingkat awal: memberikan peringatan dan petunjuk perbaikan yang jelas, bukan langsung memblokir tugas jika hanya tugas kuliah sederhana.

---

### Item 2.2: Injeksi Tier 0 Transkrip Forensics ke Stasiun `/audit`
* **Target Berkas:** `blueprints/audit.template.md`
* **Kondisi Sebelumnya (Before):**  
  Jika AI mengklaim di chat: *"Semua unit test sudah lolos"*, sistem percaya pada teks tersebut tanpa bukti log harness.
* **Kondisi Sesudah (After):**  
  Sebelum memeriksa kode, AI diwajibkan memeriksa file log transkrip internal Antigravity (`transcript.jsonl`) untuk membuktikan tes benar-benar lulus di terminal dan mendeteksi status **`STALE test`**.
* **Dampak Positif:** Melenyapkan penipuan terminal (*Green Terminal Fallacy*) di level runtime AI.

---

### Item 2.3: Injeksi Checklist RLS & Partial Index ke Stasiun `/plan`
* **Target Berkas:** `blueprints/plan.template.md`
* **Kondisi Sebelumnya (Before):**  
  Perencanaan database di `/plan` fokus pada nama tabel dan kolom DDL standar.
* **Kondisi Sesudah (After):**  
  Ditambahkan checklist arsitektur data: Jika tabel multi-user $\rightarrow$ wajib pertimbangkan Row-Level Security (RLS). Jika ada soft delete $\rightarrow$ wajib partial index `WHERE deleted_at IS NULL`.
* **Dampak Positif:** Mahasiswa sejak semester awal sudah terbiasa dengan konsep keamanan data tingkat tinggi.

---

### Item 2.4: Injeksi *The Iron Law of Diagnosis* ke Stasiun `/debug`
* **Target Berkas:** `blueprints/debug.template.md`
* **Kondisi Sebelumnya (Before):**  
  AI memiliki protokol Deferred Recommendation yang baik, tetapi belum membatasi graf dependensi secara ketat.
* **Kondisi Sesudah (After):**  
  Ditegakkan aturan keras dari `focused-fix`: **AI dilarang mengedit kode sebelum Fase Scope $\rightarrow$ Trace $\rightarrow$ Diagnose selesai**.
* **Dampak Positif:** Menghilangkan kebiasaan buruk AI yang suka menambal-nambal kode acak (*Shotgun Debugging*) yang sering merusak fitur lain.

---

## TAHAP 3: EKSPANSI 3 GERBANG BARU RAMAH MAHASISWA

---

### Item 3.1: Gerbang Awal `/explore` (Tur Kampus Kode)
* **Target Berkas:** `blueprints/explore.template.md` *(Berkas Baru)*
* **Kapan Dipanggil:** Sekali di hari pertama proyek saat baru clone repo.
* **Mekanisme AI:** AI membaca pohon folder, `package.json`, dan file entry point, lalu menerbitkan peta denah visual ke `.agents/rules/PROJECT_DNA.md`.
* **Dampak Positif:** Menghilangkan kepanikan mahasiswa baru (*"Aduh filenya banyak banget, aku harus mulai koding di mana?"*).

---

### Item 3.2: Gerbang Desain `/prototype` (Kanvas Penpot & Visual Contract Gate)
* **Target Berkas:** `blueprints/prototype.template.md` *(Berkas Baru)*
* **Kapan Dipanggil:** Di antara `/plan` dan `/execute` (khusus saat membuat fitur antarmuka visual).
* **Mekanisme AI & Jaring Pengaman:**  
  Mahasiswa mendesain tata letak visual di Penpot (menerapkan materi kuliah Desain Antarmuka). Sebelum koding di `/execute`, **The Visual Contract Gate** memvalidasi apakah elemen Penpot cocok dengan skema di `/plan`. Jika mahasiswa menambahkan input liar di kanvas, AI menolak koding dan meminta rekonsiliasi.
* **Dampak Positif:** Menjembatani mata kuliah Desain Antarmuka dengan Rekayasa Kode tanpa risiko kodingan berantakan.

---

### Item 3.3: Gerbang Akhir `/ship` (Kertas Kado Rilis Portofolio)
* **Target Berkas:** `blueprints/ship.template.md` *(Berkas Baru)*
* **Kapan Dipanggil:** Sekali di akhir semester menjelang demo UAS atau deploy hosting.
* **Mekanisme AI:** Menjalankan pre-flight check hosting gratis, menetapkan versi resmi `v1.0.0`, dan membuat file `CHANGELOG.md` otomatis dari git commit.
* **Dampak Positif:** Tugas mahasiswa terbungkus rapi layaknya software profesional yang siap dipamerkan di portofolio LinkedIn.

---

## TAHAP 4: ASIMILASI MULTI-AGENT & MODULARITAS PERSONA

---

### Item 4.1: Pemisahan Fisik Persona Mentor ke Berkas Independen
* **Target Berkas:** `blueprints/personas/kakak-tingkat-mentor.md` *(Berkas Baru)*
* **Kondisi Sebelumnya (Before):**  
  Instruksi kepribadian "Kakak Tingkat Senior" tertanam menyatu di dalam berkas SOP teknis 49KB.
* **Kondisi Sesudah (After):**  
  Seluruh nilai pedagogi, empati, analogi kampus, dan jaring pengaman mahasiswa pemula dipusatkan di berkas persona khusus `kakak-tingkat-mentor.md`. Berkas `SKILL.md` hanya berisi alur teknis yang ramping.
* **Mekanisme AI:** Agen me-load persona sebagai "Identitas Jiwa" dan me-load skill sebagai "Instruksi Kerja".
* **Dampak Positif & Garansi Perlindungan:**  
  **Persona FORGE 100% terlindungi dan tidak akan pernah terhapus secara tidak sengaja saat blueprint teknis di-update!**

---

### Item 4.2: Injeksi Sub-Agent `adversarial-reviewer` di `/plan` & `/grill-me`
* **Target Berkas:** `blueprints/personas/adversarial-reviewer.md` *(Berkas Baru)*
* **Kondisi Sebelumnya (Before):**  
  Agen yang merancang rencana di `/plan` adalah agen yang sama yang mengevaluasinya (rawan bias konfirmasi sendiri).
* **Kondisi Sesudah (After):**  
  Di akhir `/plan`, sistem memanggil sub-agent penyerang independen yang bertugas mencari skenario terburuk (*worst-case*) sebelum koding dimulai.
* **Dampak Positif:** Mendidik mahasiswa melihat blind spot rencana sistem mereka sebelum buang waktu koding.

---

## 3. Matriks Keputusan: Siap Direview & Disetujui

Berikut ringkasan seluruh berkas yang akan disentuh saat eksekusi:

| Komponen Rencana | Jenis Aksi | Berkas yang Terlibat | Tingkat Resiko |
| :--- | :---: | :--- | :---: |
| **Pilar 1 (Context-First)** | Buat Baru & Update | `blueprints/project-context.template.md`, `00-router.template.md` | Rendah |
| **Pilar 2 (10KB Modular)** | Refactor Pecah File| `skills/forge-constitution/SKILL.md`, `edeate.template.md`, `references/` | Sedang |
| **Pilar 3, 4, 5, 6 (Master Rules)**| Update Aturan | `blueprints/master_rules.template.md`, `execute.template.md` | Rendah |
| **Pilar 7 (Skrip Python Stdlib)**| Buat Baru | `skills/forge-constitution/scripts/*.py` | Rendah |
| **Gerbang `/explore`** | Buat Baru | `blueprints/explore.template.md`, `00-router.template.md` | Rendah |
| **Gerbang `/prototype` (Penpot)** | Buat Baru | `blueprints/prototype.template.md`, `00-router.template.md` | Rendah |
| **Gerbang `/ship`** | Buat Baru | `blueprints/ship.template.md`, `00-router.template.md` | Rendah |
| **Persona Kakak Tingkat** | Buat Berkas Mandiri| `blueprints/personas/kakak-tingkat-mentor.md` | Nol (Proteksi) |
| **Persona Adversarial Reviewer**| Buat Baru | `blueprints/personas/adversarial-reviewer.md` | Rendah |
| **Injeksi Skrip `/audit` & `/debug`**| Update Blueprint | `blueprints/audit.template.md`, `blueprints/debug.template.md` | Rendah |
| **Plugin Version Bump** | Update Metadata | `plugin.json` (Bump versi ke `v1.4.0`) | Rendah |

---

## 4. Alur Langkah Persetujuan (Next Step)

Dokumen ini disimpan secara permanen di:  
👉 **[MASTER_ASSIMILATION_PLAN.md](file:///d:/exe/HERD/SIM/FORGE/docs/assimilation-plan/MASTER_ASSIMILATION_PLAN.md)**

Silakan kamu pelajari dokumen rencana di atas.  
* **Jika ada butir yang tidak kamu sukai atau ingin diubah formulanya**, beri tahu saya di bagian mana.  
* **Jika kamu sudah merasa mantap dan yakin bahwa persona FORGE-mu aman**, kamu cukup katakan:  
  **"Setuju, silakan eksekusi Tahap 1"** (atau tahap mana yang ingin kamu mulai duluan). 

Sesuai instruksimu: **Saya tidak akan menyentuh satu berkas proyek/blueprint pun sebelum ada lampu hijau persetujuan darimu.**
