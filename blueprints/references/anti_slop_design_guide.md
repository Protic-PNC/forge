# INDEX REFERENSI ANTI-AI SLOP, UPSTREAM LOSSLESS, & QA UI
**Direktori Rujukan On-Demand untuk `/prototype` & `/execute` (Khusus Proyek Frontend / Fullstack)**

> 🔒 **Prinsip 100% Lossless Upstream (Bahasa Inggris Asli):**
> Untuk menjaga kepresisian maksimum LLM dan efisiensi token, 3 referensi standar industri di bawah ini disimpan **100% utuh dalam Bahasa Inggris aslinya** di folder `references/upstream/` (disalin bit-for-bit via `copy_static_assets.py` dengan verifikasi SHA-256). Berkas ini berfungsi sebagai **Index Pemanggilan On-Demand + Suplemen Bahasa Indonesia + Perintah 3 Skrip Python**.

---

## 📚 1. Peta Pemanggilan 3 Berkas Upstream Asli (WAJIB BACA ON-DEMAND)

| Kebutuhan Saat Fase `/prototype` / `/execute` | Berkas Asli yang WAJIB Dibaca (Bahasa Inggris Utuh) | Sumber & Lisensi |
| :--- | :--- | :--- |
| **Arah Estetika, Tipografi, & Anti-Visual Slop** *(sebelum menyusun tata letak)* | `references/upstream/anthropic_frontend_design.md` | `anthropics/skills` (`frontend-design`, Apache-2.0) |
| **Humanisasi Copywriting UI** *(sebelum menulis teks judul, subjudul, & deskripsi)* | `references/upstream/blader_humanizer.md` | `blader/humanizer` v4.0 (Wikipedia *Signs of AI Writing*, MIT) |
| **Audit Kepatuhan Antarmuka Web & A11y** *(sebelum koding & saat review komponen)* | `references/upstream/vercel_web_design_guidelines.md` | `vercel-labs/agent-skills` (`web-design-guidelines`) |

---

## 🇮🇩 2. Suplemen Daftar Hitam *AI Text Slop* Bahasa Indonesia
*(Melengkapi `references/upstream/blader_humanizer.md` khusus untuk proyek mahasiswa berbahasa Indonesia)*

* ❌ **DILARANG — Pembuka & Klaim Brosur Kosong:** *"Di era digital yang berkembang pesat..."*, *"Selamat datang di platform revolusioner..."*, *"Solusi mulus, inovatif, dan tak tertandingi"*, *"Menjadi bukti nyata komitmen kami"*, *"Bukan sekadar X, melainkan ekosistem Y"*.
* ❌ **DILARANG — Teks Palsu & CTA Malas:** `Lorem Ipsum`, `Contoh Judul`, `John Doe`, atau label tombol generik seperti `Submit` / `Klik di Sini` / `Click Here`.
* ✅ **WAJIB — Konkret, Membumi, & CTA Aksi Spesifik:** Sebutkan manfaat/angka/konteks nyata pengguna (misal: *"Pesan via WhatsApp"*, *"Simpan Perubahan Jadwal"*, *"Cairan fermentasi kulit jeruk warga Jeruklegi — aman untuk lantai tempat bayi merangkak"*).

---

## 🛠️ 3. Tiga Skrip Deterministik UI (Pure Python Stdlib — 0 `pip install`)

1. **Generator Token Desain Matematis (Saat Kalibrasi `DESIGN.md` di Epik 0):**
   ```bash
   python .agents/skills/project-prototype/scripts/design_token_generator.py "#2E6F40" --style modern --format css
   ```
2. **Satpam Anti-Zombie UI (`finish_lint.py` — Memblokir `onClick={() => {}}`, `href="#"`, `Lorem Ipsum`, `outline-none`, & *Token Drift*):**
   ```bash
   python .agents/skills/project-prototype/scripts/finish_lint.py src/
   ```
3. **Pemeriksa Matriks 5 State Wajib (`state_matrix_checker.py` — Default, Loading, Empty, Error, Focus):**
   ```bash
   python .agents/skills/project-prototype/scripts/state_matrix_checker.py --matrix .docs/plan/ui-states.csv
   ```
