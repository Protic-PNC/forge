---
forge_version: "{{FORGE_VERSION}}"
forged_at: "{{FORGED_AT}}"
project_name: "{{PROJECT_NAME}}"
---
# DESIGN CONSTITUTION: {{PROJECT_NAME}}

> 🎨 **KONSTITUSI VISUAL TUNGGAL PROYEK (KHUSUS FRONTEND / FULLSTACK)**
> Dokumen ini adalah kembaran `.agents/rules/ARCHITECTURE.md` khusus ranah visual & interaksi. Seluruh perancangan di `/prototype`, penulisan komponen di `/execute`, dan verifikasi di `/audit` **WAJIB** tunduk pada 7 pilar di dokumen ini agar seluruh halaman aplikasi memiliki satu jiwa visual yang utuh (*Zero Frankenstein UI & Zero AI Slop*).

---

## 1. Creative North Star & Brand Tone
- **Arah Rasa & Karakter Visual Awal:** {{VISUAL_BRAND_TONE}}

<!-- GENERATION_DIRECTIVE: DESIGN_SYSTEM_FOUNDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INSTRUKSI UNTUK AI TAHAP 5 (INJEKSI FISIK — DRAFT V0) & EPIK 0 (KALIBRASI FINAL):
Sintesis 7 Pilar Konstitusi Visual sesuai domain bisnis (`dna.BUSINESS_DOMAIN_SUMMARY`)
dan arah rasa (`dna.VISUAL_BRAND_TONE`), terinspirasi standar `pbakaus/impeccable` & `anthropics/frontend-design`.
DILARANG menggunakan palet ungu-biru neon generik atau aturan kabur tanpa angka!

WAJIB MEMUAT KE-6 SEKSI BERIKUT SECARA SPESIFIK:

## 2. Named Design Rules (Hukum Visual Bernama)
Rumuskan 3-4 hukum bernama yang tegas (bukan sekadar daftar hex), contoh pola:
- **The Accent Is Jewelry Rule:** Warna aksen primer hanya untuk CTA utama & indikator aktif; DILARANG mengisi latar panel besar.
- **The Contrast Floor Rule:** Seluruh teks fungsional wajib memenuhi rasio kontras WCAG AA (>= 4.5:1 teks normal, >= 3:1 teks besar).
- **The Tabular Data Rule:** Angka harga, kuantitas, timer, dan kolom tabel wajib memakai `tabular-nums` / font monospace agar tidak bergoyang.

## 3. Color Tokens & Peran Semantik
Tetapkan peran permukaan (Surface/Canvas, Surface-Raised), tinta teks (Ink Primary, Muted), Brand Primary/Accent, dan State (Success, Warning, Danger) — gunakan CSS variables / `@theme` Tailwind, bukan hex mentah di komponen.

## 4. Typography Hierarchy & Scale
Tetapkan pasangan font berkarakter (Display/Heading vs Body vs Mono), ukuran lantai minimum fungsional (misal 12px/14px), `line-height`, dan `letter-spacing`.

## 5. Elevation, Depth, & Shapes (Disiplin Border-Radius)
Tetapkan kapan permukaan bersifat flat vs memiliki shadow tipis, serta radius spesifik per komponen (misal: badge/tag, input/button, card, modal) — cegah kebiasaan menaruh `rounded-3xl shadow-2xl` seragam di semua elemen!

## 6. Component Anatomy & 5 Mandatory States
Spesifikasi ringkas Button (Primary vs Secondary, tinggi & tap-target >= 44px), Card, Form Input, Focus Ring (`focus-visible` 2px jelas), serta kewajiban 5 status permukaan: **Default, Loading, Empty, Error, dan Focus/Disabled**.

## 7. Do's & Don'ts + Lokasi Fisik Token
- **Do's:** (3-4 perintah wajib spesifik proyek ini)
- **Don'ts:** (3-4 larangan daftar hitam anti-slop spesifik proyek ini)
- **Single Source of Truth Token CSS:** Sebutkan berkas pastinya (misal `src/styles/design-tokens.css` atau `src/index.css`).
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-->

---

## 8. Protokol Perubahan Desain (Design Decision Records / DDR)
Dokumen ini dikalibrasi tuntas pada **Epik 0 (Pra-Sprint Bootstrap)**. Jika di tengah pengembangan tim menyepakati perubahan besar pada palet warna, pasangan font, atau anatomi komponen inti, AI dan UI Lead **WAJIB** mencatatnya sebagai entri DDR di bawah ini (dilarang mengubah gaya visual secara sepihak di satu halaman saja!):

```markdown
### [DDR-YYYY-MM-DD]: <Judul Perubahan Visual>
- **Status:** [Disahkan / Digantikan]
- **Alasan Perubahan:** <Mengapa penyesuaian visual ini dibutuhkan?>
- **Keputusan Token / Aturan Baru:** <Rincian perubahan palet/font/radius>
- **Komponen Terdampak:** <Daftar berkas/halaman yang diselaraskan>
```

<!-- DDR_LOG_START -->
<!-- Catatan: Entri DDR baru ditambahkan tepat di bawah baris ini dan dilindungi otomatis saat /forge-update. -->
<!-- DDR_LOG_END -->
