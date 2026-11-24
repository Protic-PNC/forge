# PANDUAN REFERENSI: GERBANG AUDIT OPENAPI & KONTRAK REST API
**Direktori Rujukan On-Demand untuk Gerbang Audit (`/audit`) — KHUSUS PROYEK BACKEND / FULLSTACK**

> 🎯 **Tujuan:** Mengaudit kualitas desain REST API secara deterministik (0 halusinasi) menggunakan 3 skrip Python Stdlib murni (`scripts/api_linter.py`, `scripts/api_scorecard.py`, `scripts/breaking_change_detector.py`) terhadap berkas kontrak `docs/api/openapi.json`.

---

## ⚙️ 1. Alur Eksekusi 3 Skrip Deterministik (WAJIB pada Tiket yang Menyentuh API)

### Langkah A — Periksa Keberadaan `docs/api/openapi.json`
Jika proyek memiliki Backend/REST API, periksa apakah `docs/api/openapi.json` sudah ada dan mutakhir:
- **Jika berkas `docs/api/openapi.json` BELUM ADA (*Graceful Guidance*):**
  AI **DILARANG** sekadar menulis `FAIL` tanpa arahan. Tampilkan callout bimbingan ramah sesuai stack di `ONBOARDING.md`:
  > 💡 **Peringatan Kontrak OpenAPI:** Berkas `docs/api/openapi.json` belum ditemukan di repositori ini.  
  > - **Laravel (`dedoc/scramble`):** `php artisan scramble:export --path=docs/api/openapi.json`  
  > - **FastAPI:** Simpan output endpoint `/openapi.json` ke `docs/api/openapi.json`  
  > - **Express / Next.js polos:** Balas *"buatin draft openapi.json"* agar aku menyusun kontraknya dari route aktualmu sekarang.

### Langkah B — Jalankan 3 Skrip Audit Python (0 `pip install`)
Jalankan perintah berikut dari root proyek (asumsi skrip berada di `.agents/skills/project-audit/scripts/`):

```bash
# 1. Lint konvensi REST (kebab-case resource, camelCase field, HTTP methods, status codes)
python .agents/skills/project-audit/scripts/api_linter.py docs/api/openapi.json

# 2. Penilaian mutu desain API berbobot (Grade A-F, ambang lulus minimal: Grade B)
python .agents/skills/project-audit/scripts/api_scorecard.py docs/api/openapi.json --min-grade B
```

### Langkah C — Deteksi Breaking Change Otomatis Berbasis Git `main`
Bandingkan kontrak `docs/api/openapi.json` di branch fitur saat ini melawan versi produksi di branch `main` (tanpa perlu menyimpan manual file `v1.json` dan `v2.json`!):
1. Periksa apakah `docs/api/openapi.json` sudah ada di `main`:
   ```bash
   git show main:docs/api/openapi.json > .tmp-openapi-main.json
   ```
   - **Jika belum ada di `main`** (ini adalah tiket API pertama yang memperkenalkan `openapi.json`): Catat status `[BASELINE CREATED - Initial OpenAPI Spec]` dan lewati perbandingan diff.
   - **Jika sudah ada di `main`:** Jalankan detektor breaking change lalu hapus file sementara:
     ```bash
     python .agents/skills/project-audit/scripts/breaking_change_detector.py .tmp-openapi-main.json docs/api/openapi.json --exit-on-breaking
     ```
     *(Hapus `.tmp-openapi-main.json` setelah selesai agar tidak ikut ter-commit!).*

---

## 🔍 2. Cross-Check Anti-Spec-Drift (Khusus Stack Tanpa Auto-Exporter)

Jika proyek tidak menggunakan Spec Exporter otomatis (misal Express / Next.js polos), AI **WAJIB** melakukan 1 langkah pemeriksaan silang cepat sebelum meloloskan audit:
- Bandingkan rute, HTTP method, dan field response pada file Controller/Route yang disentuh di `git diff` melawan `docs/api/openapi.json`.
- Jika ada field baru di Controller yang belum tertulis di `openapi.json`, tandai `WARN: Spec Drift Detected` dan bantu perbarui sebelum PR dibuat.

---

## 📊 3. Rubrik Evaluasi Mutu API (5 Dimensi `api_scorecard.py`)

Agar mahasiswa memahami arti nilai A–F dari scorecard:
1. **Consistency (30%):** Konvensi penamaan URL (`/api/v1/user-profiles` bukan `/getUsers`), keseragaman struktur error & respons.
2. **Documentation (20%):** Kelengkapan `summary`, `description`, contoh payload, dan definisi respons.
3. **Security (20%):** Deklarasi skema autentikasi (`bearerAuth` / Sanctum / OAuth), otorisasi endpoint privat, dan zero leak data sensitif.
4. **Usability (15%):** Kemudahan dipahami tim Frontend, parameter filter/sort jelas, dan status code presisi (`201 Created`, `401`, `403`, `422`).
5. **Performance (15%):** Pola paginasi untuk endpoint list/koleksi dan dukungan caching/header bila relevan.

**Aturan Kelulusan:**
- **Grade A / B + 0 Breaking Changes:** ✅ `PASS`
- **Grade C / D / F:** ⚠️ Berikan penjelasan hangat + saran perbaikan konkret pada dimensi dengan skor terendah.
- **Breaking Change Terdeteksi (Exit Code 1):** 🚨 `BLOCK` — Wajib edukasi dampak ke tim Frontend/Consumer; hanya boleh diloloskan jika endpoint di-versioning ulang (`/api/v2/...`) atau disetujui eksplisit oleh Tech Lead (dan wajib sertakan *Notifikasi Lintas Tim* di Bagian 3 laporan audit).
