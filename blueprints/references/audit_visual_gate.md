# PANDUAN REFERENSI: VISUAL SMOKE GATE, TRI-TRACK ROUTING, & FALLBACK PLAYWRIGHT
**Direktori Rujukan On-Demand untuk Gerbang Audit (`/audit`) — 100% Lossless Extraction**

---

## 🔀 1. Rincian Klasifikasi Domain Tri-Track Routing (Jalur 1, 2, 3, & Campuran)

- **Jalur 1: Pure Backend / Headless (Zero UI Footprint):**
  * *Kriteria:* Hanya menyentuh berkas Controller, Service, Repository, Model, Migration, FormRequest, Policy, Seeder, Route API, atau skrip backend.
  * *Kebijakan Pengujian:* AI **DILARANG KERAS** memanggil Playwright atau menuntut visual testing pada tiket ini. Fokus murni pada pencegahan N+1 Query, transaksi atomik database, sanitasi OWASP, otorisasi Policy, dan Feature Test HTTP.
  * *Pelaporan di Bagian 2:* Status Tier 4 ditulis: `Tier 4 (Visual Smoke): [BYPASS - Pure Backend / Non-Visual]`.
- **Jalur 2: Frontend Refactor / Logic-Only (Zero Visual Delta):**
  * *Kriteria:* Menyentuh berkas di layer frontend (utility function, custom hook, types/interfaces, state store, konfigurasi build, konstanta data, atau refactor logika kalkulasi), TETAPI hasil inspeksi AST/diff membuktikan **tidak ada perubahan tag JSX/HTML, kelas CSS/Tailwind, atau geometri antarmuka pengguna**.
  * *Kebijakan Pengujian:* AI **TIDAK PERLU** memaksakan tangkapan layar Playwright karena tidak terdapat delta visual (pixel identik 100%).
  * *Pelaporan di Bagian 2:* Status Tier 4 ditulis: `Tier 4 (Visual Smoke): [STATIC VERIFIED - Zero Visual Delta]`.
  * *Mandat Panduan Uji Manual Manusia (Human-in-the-Loop Smoke Checklist):* AI **WAJIB** menyajikan checklist langkah verifikasi fungsional konkret agar pengembang/reviewer manusia dapat melakukan uji asap (smoke check) manual di browser:
    ```markdown
    #### 📋 Panduan Verifikasi Manual Pengembang (Logic-Only Smoke Checklist):
    * [ ] Buka rute/halaman target di browser lokal.
    * [ ] Lakukan interaksi uji fungsional (misal: klik aksi, pengiriman data, manipulasi filter).
    * [ ] Periksa DevTools Console ➔ pastikan tidak ada warning re-render liar atau error runtime.
    ```
- **Jalur 3: Active Visual & Interactive UI (Active Visual Delta):**
  * *Kriteria:* Menyentuh komponen antarmuka pengguna, layout halaman (Astro/React/Vue/Blade), styling Tailwind/CSS, responsive breakpoints (`sm:`, `md:`, `lg:`), modal/drawer, form interaktif, atau animasi visual.
  * *Kebijakan Pengujian:* AI **WAJIB** mengeksekusi standar **Four-Tier Quality Gate** secara lengkap (termasuk Tier 4: Visual Smoke & Runtime Actionability Gate).
  * *Mandat Penjabaran Bukti Visual Fisik (In-Chat Visual Evidence):* DILARANG KERAS hanya melaporkan status teks "Pass 0 errors". AI **WAJIB MENAMPILKAN DAN MENJABARKAN BUKTI TANGKAPAN LAYAR RIIL** di dalam Bagian 2 laporan audit:
    1. **Tautan / Render Gambar Lokal:** Menyertakan format tautan media yang dapat dirender/diakses langsung di jendela chat (`[Image: nama-tangkapan-layar.png](#media:<path-lengkap>)` atau sintaks media viewer).
    2. **Multi-Viewport Real-World Coverage (Viewport-First, Bukan Element-Isolated):** Minimal menyajikan bukti `page.screenshot({ fullPage: false })` pada:
       - **Desktop Real Inner-Viewport (`1280 × 680` atau `1366 × 680`):** Merepresentasikan tinggi ruang baca bersih laptop nyata setelah dipotong Chrome Tab/Address/Bookmarks Bar (~110px) dan Taskbar, pada State Normal & State Alternatif.
       - **Mobile Real Viewport (`375 × 667`):** Memvalidasi aliran responsif 1-kolom dan ketiadaan horizontal overflow.
       - **Light Mode dan Dark Mode** (jika aplikasi mendukung dual-theme).
    3. **Observasi Geometri & Aksi:** Penjelasan eksplisit 1–2 kalimat mengenai apa yang dibuktikan oleh tangkapan layar tersebut (misal: tombol CTA utuh di dalam fold `680px`, tidak ada tabrakan dengan sticky navbar, rasio grid 12 proporsional, dan ketiadaan phantom overlay).
- **Jalur Campuran / Fullstack:** Mengombinasikan Jalur 1 untuk layer backend, serta Jalur 2 atau Jalur 3 untuk layer frontend sesuai dengan ada atau tidaknya delta visual.

---

## 🖼️ 2. Tier 4: Visual Smoke & Runtime Actionability Gate via Playwright MCP

* **Pilar 1 — Hukum Viewport-First Screenshot (Haram `element.screenshot()` sebagai Bukti Utama):**
  AI **DILARANG KERAS** mengisolasi tangkapan layar hanya pada node DOM tunggal (`await section.screenshot()`) untuk membuktikan kelayakan tata letak, karena membutakan pengujian terhadap terpotongnya elemen oleh tepi bawah layar atau bocornya seksi bawah ke atas. Bukti utama **WAJIB** menggunakan `await page.screenshot({ fullPage: false })` (potret satu jendela browser utuh). `element.screenshot()` hanya boleh dipakai sebagai lampiran sekunder untuk mikro-komponen (ikon/badge).
* **Pilar 2 — Standar Real-World Laptop Inner-Viewport (`1280 × 680`) & Above-the-Fold Math:**
  Pengujian desktop wajib menggunakan ukuran ruang baca bersih laptop nyata (`width: 1280, height: 680` atau `1366 × 680`, BUKAN `800px/900px` yang mengabaikan tinggi Address/Bookmarks Bar browser). Untuk seksi pembuka (*Hero*), skrip tes wajib memvalidasi secara matematis bahwa elemen aksi utama (*CTA Button*) tidak terpotong tepi bawah layar (`ctaBox.bottom <= window.innerHeight`) dan proporsi seksi mengisi *first fold* secara harmonis.
* **Pilar 3 — Zero Test-Tampering Law (Haram Manipulasi CSS/DOM di Dalam Skrip Tes):**
  AI **DILARANG KERAS** menyuntikkan manipulasi DOM/CSS produksi di dalam skrip pengujian (seperti `header.style.position = 'static'`, `display = 'none'`, atau mengubah `padding/overflow` via `page.evaluate()`) demi mempercantik tangkapan layar. Tes wajib memotret kondisi 100% murni sebagaimana dilihat manusia di browser.
* **Pilar 4 — Real Anchor-Click & Sticky Header Collision Gate:**
  Jika halaman memiliki *Sticky/Fixed Navbar*, skrip tes **WAJIB** menyimulasikan klik nyata pada tautan navigasi (`await page.click('header a[href^="#"]')`) dan memverifikasi secara matematis bahwa judul/konten atas seksi target tidak tertelan di balik *Sticky Navbar* (`sectionBox.top >= headerBox.bottom` atau memiliki *scroll-margin / padding* yang presisi).
* **Deteksi Intercept, Rasio Aspek & Dual-Theme Bleed:** Uji interaksi klik riil pada tombol/input (memastikan tidak terhalang *phantom backdrop* `fixed inset-0`), validasi kontainer gambar adaptif *Hug-Content*, serta verifikasi Light Mode dan Dark Mode.

---

## 🛡️ 3. Protokol Graceful Degradation (Laptop Fresh Clone / Low-End Safe)

Jika lingkungan lokal belum menginstal Playwright MCP atau belum mengunduh browser Chromium (misal developer junior baru melakukan clone di laptop baru):
- AI **DILARANG KERAS** membatalkan audit atau menandai status `FAIL`.
- AI otomatis mengalihkan Tier 4 ke **Static Code Inspection (Fallback Audit)**:
  (a) Memvalidasi bahwa komponen overlay/modal menerapkan pola *Conditional Unmount* (`if (!isOpen) return null;` atau `pointer-events-none` saat state tertutup).
  (b) Memvalidasi bahwa kontainer gambar menggunakan pola adaptif *Hug-Content*.
- AI **WAJIB MENYEBUTKAN PERINTAH LENGKAP & VALID** (bukan perintah tunggal yang memicu warning dependency):
  `npm install -D @playwright/test && npx playwright install chromium`
  *(Jelaskan alasannya: pasang driver ke devDependencies proyek terlebih dahulu agar npx tidak melempar peringatan dependensi hilang, lalu unduh biner peramban Chromium).*

## 📋 4. Format Pelaporan Status Tier 4 di Bagian 2 Laporan Audit

* *Tier 4 (Visual Smoke & Actionability):*
  - Jika **Jalur 1 (Pure Backend):** `[BYPASS - Pure Backend / Non-Visual]` *(Catatan: Tiket murni layer data/API tanpa antarmuka).*
  - Jika **Jalur 2 (Frontend Logic-Only):** `[STATIC VERIFIED - Zero Visual Delta]` disertai **📋 Panduan Verifikasi Manual Pengembang (Human-in-the-Loop Smoke Checklist)**.
  - Jika **Jalur 3 (Active Visual UI):** `[PASS]` disertai **🖼️ Galeri Bukti Visual & Observasi Runtime (Visual Smoke Evidence)** yang memuat tautan gambar lokal, tangkapan layar multi-viewport (Desktop, Mobile, Light/Dark mode), serta analisis ketiadaan layout shift / phantom overlay.
  - Jika **Fallback Terjadi:** `[FALLBACK - Static Inspection]` dengan ringkasan inspeksi conditional unmount dan adaptive bounds.

### Callout Wajib di Bagian 3 Laporan Audit (Khusus Jika Fallback Terjadi):
* *Peringatan & Penawaran Interaktif Visual Smoke Test (Khusus Fallback):* Jika Tier 4 dialihkan ke fallback statis karena browser Playwright belum terpasang, AI **WAJIB MENEKANKANNYA SECARA JELAS DI AKHIR LAPORAN (BAGIAN 3)** dalam blok callout khusus, dan secara eksplisit menawarkan:
  > 💡 **Peringatan Pengujian Visual:** Pengujian Tier 4 Visual Smoke dialihkan ke audit statis karena browser Playwright belum terpasang di perangkat ini.  
  > Untuk mengaktifkannya secara resmi dan bebas error/warning, jalankan:  
  > ```bash
  > npm install -D @playwright/test && npx playwright install chromium
  > ```  
  > **👉 Apakah kamu sudah install Playwright dan mau test visual sekarang?**  
  > *(Jika sudah, balas 'ya jalankan test visual' dan saya akan langsung menguji interaktivitas serta mengambil tangkapan layar Light & Dark mode).*
