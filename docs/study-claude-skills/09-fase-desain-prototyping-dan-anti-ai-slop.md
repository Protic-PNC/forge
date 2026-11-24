# Fase Desain, UI Prototyping & Pembasmi "AI Slop"
**Fokus Khusus:** Menutup celah terbesar dalam siklus hidup FORGE (Ketiadaan Fase Desain UI, Copywriting, dan Prototyping) serta membedah persenjataan anti-AI Slop.  
**Sumber Referensi:** `scratch/claude-skills/` (`product-team/`, `marketing-skill/`, `markdown-html/`, `engineering/behuman`).

---

## 1. Menemukan Celah Terbesar: Mengapa Fase Desain Hilang di FORGE?

Di alur kerja FORGE saat ini, kita melompat langsung dari:
```
/edeate (Ideasi Bisnis) ──► /plan (Arsitektur Teknis / DDL Database) ──► /execute (Koding Frontend & Backend)
```

### Dampak Bencana bagi Mahasiswa & Produk:
Karena tidak ada **Gerbang Desain & Prototyping**, mahasiswa langsung dipaksa menulis kode UI (React/Astro/Tailwind) di `/execute`. Hasilnya hampir selalu menghasilkan fenomena yang disebut industri sebagai **"AI SLOP" (Sampah Visual AI)**:

1. **AI Visual Slop:** Tampilan klise yang membosankan khas template AI: gradasi warna ungu-biru neon generik, sudut kartu melengkung berlebihan (`rounded-3xl`), kontras warna buruk, dan tidak punya *Design System* yang kohesif.
2. **AI Text Slop:** Teks promosi dan konten tombol yang kaku seperti terjemahan robot: *"Selamat datang di platform revolusioner kami yang mulus dan tak tertandingi"* atau dipenuhi teks palsu *"Lorem Ipsum"*.
3. **Half-Finished Zombie UI:** Tombol yang dipasang handler kosong `onClick={() => {}}`, halaman tanpa kondisi *Loading State*, *Empty State* (jika data kosong), dan *Error State*.

Repositori enterprise memecahkan bencana ini dengan menyusun **Cluster Khusus Desain UI & Humanisasi Konten**.

---

## 2. Bedah 5 Senjata Emas untuk Fase Desain & Prototyping

---

### Senjata 1: `ui-design-system` (Pondasi Token Desain Matematis)
* **Kategori:** Product & Frontend Architecture (`product-team/skills/ui-design-system`)
* **Fungsi:** Menghilangkan kebiasaan mahasiswa yang mengacak-acak warna dan ukuran font di setiap komponen (`text-[15px]`, `bg-[#234123]`).
* **Mekanisme Kerja:**
  * Membangun **Design Tokens** (skala tipografi matematis, skala spacing 4px/8px, dan palet warna harmonis 50–900).
  * Menghasilkan variabel CSS/Tailwind tokens (`design_token_generator.py`) sehingga seluruh halaman memiliki satu DNA visual yang rapi.
* **Deliverable:** `src/styles/design-tokens.css` atau konfigurasi `tailwind.config.mjs` terstandarisasi.

---

### Senjata 2: `copywriting` (Copywriting Konversi & Penguji Headline)
* **Kategori:** Conversion Copywriting (`marketing-skill/skills/copywriting`)
* **Fungsi:** Menggantikan teks klise dengan copywriting yang menjual dan menyentuh masalah nyata manusia.
* **Senjata Deterministik: `headline_scorer.py`:**
  * Alih-alih menebak judul landing page, skrip ini menguji calon headline dan memberi skor matematis 0–100 berdasarkan 4 kriteria:
    1. *Clarity (Kejelasan Masalah)*
    2. *Specificity (Kekonkretan Angka/Hasil)*
    3. *Emotional Resonance (Pemicu Tindakan)*
    4. *Length / Skimmability (Kemudahan Dibaca Cepat)*
* **Dampak:** Judul landing page tugas mahasiswa tidak lagi berbunyi *"Solusi Terbaik untuk Sampah"*, melainkan *"Ubah 10 Kg Sampah Dapur Menjadi Cairan Pembersih Organik dalam 90 Hari"*.

---

### Senjata 3: `content-humanizer` & `behuman` (Penghancur Teks AI Slop)
* **Kategori:** Anti-AI Detection & Voice Authenticity (`marketing-skill/skills/content-humanizer` & `engineering/behuman`)
* **Fungsi:** Menghilangkan "bau robot" pada teks website, email, dan dokumentasi.
* **Mekanisme Kerja: The Self-Mirror Consciousness Loop:**
  * AI biasa langsung memuntahkan teks draf pertama yang penuh klise formal (*"delve"*, *"crucial"*, *"foster"*, *"in summary"*).
  * Skill `behuman` memaksa AI melakukan dialog batin (*Inner Dialogue*) sebelum merespon:
    * **Langkah 1 (Self):** Menghasilkan draf awal.
    * **Langkah 2 (Mirror):** Mengkritik draf sendiri secara kejam: *"Ini terdengar seperti brosur korporat palsu. Hapus daftar bullet points yang membosankan dan bicaralah seperti manusia biasa!"*
    * **Langkah 3 (Humanized Output):** Menulis ulang dengan ritme kalimat manusia (kombinasi kalimat pendek dan panjang yang dinamis).

---

### Senjata 4: `landing-page-generator` (Prototyping Instan Berbasis Komponen)
* **Kategori:** Rapid UI Prototyping (`product-team/skills/landing-page-generator`)
* **Fungsi:** Mengubah deskripsi produk menjadi prototipe Next.js/Astro TSX lengkap dalam hitungan detik menggunakan framework copywriting teruji (**PAS**: *Problem-Agitate-Solution*, atau **AIDA**: *Attention-Interest-Desire-Action*).
* **Standar Mutu:** Menghasilkan 5 varian Hero section, tabel harga komparatif, dan komponen accordion FAQ yang otomatis ramah SEO (*Core Web Vitals LCP < 1s*).

---

### Senjata 5: `design-qa` (Satpam Penjaga Zombie UI)
* **Kategori:** UI Gatekeeper (`product-team/skills/design-qa`)
* **Hukum Utama:** *"Gates the rendered result, not the design file."* (Menguji apa yang benar-benar tampil di browser, bukan sekadar file desain Figma).
* **3 Skrip Pemeriksa Keras (Blocking Exit Codes):**
  1. **`finish_lint.py`:** Memblokir kode jika menemukan tombol yang mengarah ke `() => {}`, link mati `href="#"`, atau teks yang masih berisi *"Lorem Ipsum"*.
  2. **`state_matrix_checker.py`:** Memeriksa apakah komponen memiliki 5 state wajib: **Default, Loading, Empty, Error, dan Focus Ring**.
  3. **`rendered_audit.py`:** Mengaudit tangkapan layar rendered pada viewport sempit (320px) untuk memastikan teks tidak bertabrakan atau terpotong (*broken reflow*).

---

## 3. Integrasi Alur Baru ke FORGE: Gerbang `/prototype` atau `/design`

Dengan mengasimilasikan kelima senjata di atas, kita menyisipkan satu stasiun baru di Two-Gateway Pipeline FORGE:

```
[ GERBANG HULU: BISNIS ]
       /edeate
          │
          ▼
┌────────────────────────────────────────────────────────────────────────┐
│  GERBANG BARU: /prototype (atau /design)                               │
│  Fokus: Membangun Antarmuka, Copywriting Asli, dan Desain Visual       │
├────────────────────────────────────────────────────────────────────────┤
│  1. Token Desain: Buat palet warna & tipografi via `ui-design-system`   │
│  2. Copywriting: Buat headline berbobot via `headline_scorer.py`       │
│  3. Anti-Slop: Bersihkan teks robotik via `content-humanizer`          │
│  4. Scaffolding: Bangun prototipe komponen via `landing-page-generator`│
│  5. Verification: Audit tombol mati & empty-state via `design-qa`      │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
[ GERBANG HILIR: ARSITEKTUR & IMPLEMENTASI ]
        /plan ──► /execute (TDD) ──► /audit (4-Tier Gate) ──► /ship
```

### Mengapa Ini Sangat Menyelamatkan Mahasiswa?
1. **Tidak Ada Lagi "Blank Screen Panic":** Mahasiswa tidak lagi bengong menatap layar kosong saat disuruh bikin UI.
2. **Karya Portofolio Terlihat Mahal:** Mahasiswa semester awal bisa menghasilkan antarmuka web yang estetik, tidak bergaya template murahan, dan memiliki copywriting manusiawi yang siap dipamerkan ke calon klien atau industri.
3. **Bebas Tombol Mati:** Skill `design-qa` mendidik mahasiswa sejak dini bahwa tombol yang tidak ada fungsinya adalah aib rekayasa perangkat lunak!

---
*Dokumen ini merupakan modul analisis khusus untuk integrasi Fase Desain, UI Prototyping, dan Anti-Slop.*
