# Rencana Eksekusi: TAHAP 4 — Modularitas Persona, Multi-Agent Adversarial Review, & Rilis FORGE v2.0.0

**Dokumen Diskusi & Persetujuan:** Tahap 4 dari 4 (Setelah Tahap 1 `8e600ec`, Tahap 2 `4028ef6`, Tahap 3 `260b995`, & Mini-Batch 3.5 `7cd2b09` Tuntas)  
**Target:** Menyelesaikan pemisahan persona *WHO vs HOW* yang 100% *Always-On* & *lossless*, menyuntikkan sub-agent `adversarial-reviewer` yang ramah pemula (berfilter Mentor) ke `/plan` & `/audit`, memperkuat ringkasan handoff tanpa *doc sprawl*, dan mengesahkan **Rilis Mayor FORGE `v2.0.0`**.  
**Status Eksekusi:** ✅ **SELESAI DIEKSEKUSI (Batch 4A + 4B + 4C — FORGE v2.0.0 Siap Commit Lokal)**

---

## 1. Keputusan yang Sudah DIKUNCI (Hasil Diskusi & Audit Fisik)

1. **Keputusan 1A — Pemisahan Persona *WHO vs HOW* di `.agents/rules/` + Lossless Chunking `grill-me` (DIKUNCI):**
   - Pindahkan Pasal 6 (`Protokol Pedagogi & Kode Etik Mentor Arsitek`, baris 88–142, ~6.5 KB) dari `blueprints/master_rules.template.md` secara **100% verbatim lossless** ke berkas rule mandiri baru: **`blueprints/persona_mentor.template.md`** $\rightarrow$ `.agents/rules/PERSONA_MENTOR.md`.
   - *Alasan Teknis Transparan:* Diletakkan di `.agents/rules/` (bukan `.agents/personas/`) agar **100% Always-On** di IDE Antigravity (0% risiko persona terlupakan). Manfaat utamanya adalah **proteksi `/forge-update`** (pembaruan aturan teknis di `MASTER_RULES.md` tidak akan pernah menyentuh berkas persona) dan **batas semantik** yang bersih — bukan pengurangan total byte *Always-On*.
   - Ekstrak blok template & jaring pengaman repetitif di `blueprints/grill-me.template.md` (baris 84–128, ~6.8 KB) secara **100% verbatim lossless** ke **`blueprints/references/grill_cards_and_guards.md`** (*Progressive Disclosure* on-demand di Langkah 2), menurunkan `grill-me.template.md` dari `15.83 KB` $\rightarrow$ `~9.0 KB`.

2. **Keputusan 2A — Multi-Agent `adversarial-reviewer` Selektif + Translasi Mentor di `/plan` & `/audit` (DIKUNCI):**
   - Membuat referensi statis **`blueprints/references/adversarial_review_lens.md`** (~4–5 KB) berbasis 3 lensa asli `adversarial-reviewer` (*The Saboteur*, *The New Hire*, *The Security Auditor*) + aturan *Severity Promotion* (temuan dari $\ge 2$ lensa naik 1 tingkat), mendukung **Dual-Target** (*Plan Review* di akhir `/plan` & *Code Diff Review* di `/audit`).
   - **Pemicu Selektif (Hemat Token & Kuota):** Otomatis aktif hanya untuk tiket **Risiko Medium/High** (*Auth/Otorisasi, Migrasi/Mutasi DB, Integrasi API/Payment, State Kompleks, atau Blast Radius $\ge 4$ berkas*), atau saat dipicu manual dengan flag `--adversarial`. Tiket kosmetik/ringan langsung *bypass*.
   - **Mekanisme Sub-Agent Native + Graceful Fallback:** Menggunakan fitur bawaan IDE `invoke_subagent(TypeName="research")` (*sandbox read-only*, konteks 100% segar tanpa bias penyusunan rencana/kode). Jika IDE pengguna tidak mendukung sub-agent, otomatis beralih menjalankan 3 lensa secara sekuensial tanpa error.
   - **Filter Translasi Mentor (Anti-Intimidasi):** Vonis mentah sub-agent (`BLOCK` / `CONCERNS` / `CLEAN`) **wajib diterjemahkan ulang** oleh Agen Utama (*Kakak Tingkat Mentor*) dengan bahasa suportif, *Bottom Line First*, dan tag bukti `🟢/🟡/🔴`, lalu **Hard Stop** menyerahkan keputusan ke mahasiswa.
   - **Zero Instalasi di `ONBOARDING.md`:** Cukup tambahkan 1 blok catatan literasi singkat (tanpa instalasi *tool*/plugin eksternal apa pun).

3. **Keputusan 3.1 — Handoff Padat Tanpa *Doc Sprawl* (DIKUNCI):**
   - Tidak menambah berkas/skill `session-handoff` baru. Cukup memperkaya `blueprints/references/audit_handoff_package.md` dengan 1 sub-poin **Ringkasan Handoff Sesi Padat** (*Keputusan Terkunci $\rightarrow$ Path Artefak Fisik $\rightarrow$ Celah Terbuka untuk Tiket Berikutnya*).

4. **Keputusan 3.2 — Finalisasi Rilis Mayor `v2.0.0` (DIKUNCI):**
   - Naikkan `version` di `plugin.json` dari `1.3.6` $\rightarrow$ **`2.0.0`** dengan entri `releases["2.0.0"]` yang memuat daftar lengkap seluruh blueprint, referensi, dan skrip hasil Tahap 1–4 agar proyek mahasiswa lama dapat naik versi secara deterministik melalui `/forge-update`.

---

## 2. Peta Eksekusi 3 Micro-Batch

### 🧩 BATCH 4A: Pemisahan Persona *WHO vs HOW* & Lossless Chunking `/grill-me`
| Aksi | Berkas Sasaran | Dampak & Target Ukuran |
| :--- | :--- | :--- |
| **Buat Baru** | `blueprints/persona_mentor.template.md` | Menampung 100% verbatim Pasal 6 `master_rules.template.md` (~6.5 KB) $\rightarrow$ `.agents/rules/PERSONA_MENTOR.md`. |
| **Edit** | `blueprints/master_rules.template.md` | Turun dari `16.87 KB` $\rightarrow$ `~10.3 KB`; Pasal 6 menjadi penunjuk resmi ke `.agents/rules/PERSONA_MENTOR.md`. |
| **Buat Baru** | `blueprints/references/grill_cards_and_guards.md` | Menampung 100% verbatim baris 84–128 `grill-me.template.md` (~6.8 KB, on-demand Langkah 2). |
| **Edit** | `blueprints/grill-me.template.md` | Turun dari `15.83 KB` $\rightarrow$ `~9.0 KB`; menunjuk on-demand ke `references/grill_cards_and_guards.md`. |
| **Edit** | `blueprints/00-router.template.md` | Mendaftarkan `.agents/rules/PERSONA_MENTOR.md` di daftar Dokumen Konstitusi Resmi. |

**Bukti Verifikasi Wajib Batch 4A:**
- Skrip audit Python matematis membandingkan `git show HEAD:blueprints/master_rules.template.md` vs gabungan (`master_rules.template.md` + `persona_mentor.template.md`) serta `git show HEAD:blueprints/grill-me.template.md` vs gabungan (`grill-me.template.md` + `references/grill_cards_and_guards.md`) $\rightarrow$ **Wajib 0 klausa terhapus / diringkas.**

---

### 🧩 BATCH 4B: Multi-Agent `adversarial-reviewer`, Penguatan Handoff, & Copier Update
| Aksi | Berkas Sasaran | Dampak & Mekanisme |
| :--- | :--- | :--- |
| **Buat Baru** | `blueprints/references/adversarial_review_lens.md` | Panduan 3 Lensa (*Saboteur*, *New Hire*, *Security Auditor*), *Severity Promotion*, Dual-Target (*Plan* & *Code Diff*), protokol `invoke_subagent(research)` + *Graceful Fallback*, & *Filter Translasi Mentor*. |
| **Edit** | `blueprints/plan.template.md` | Menambahkan gerbang opsional/selektif *Adversarial Plan Review* di akhir penyusunan `.docs/plan/` (risiko Medium/High atau `--adversarial`), tetap tunduk pada *Anti-Auto-Proceed*. |
| **Edit** | `blueprints/audit.template.md` | Menambahkan rujukan `references/adversarial_review_lens.md` & pemicu selektif *Self-Review Trap Breaker* (saat Blast Radius tinggi / perubahan sensitif / `--adversarial`). |
| **Edit** | `blueprints/references/audit_handoff_package.md` | Menambahkan 1 butir **Ringkasan Handoff Sesi Padat** (*Keputusan $\rightarrow$ Path Artefak $\rightarrow$ Celah Terbuka*) di Bagian 3 tanpa menambah berkas baru. |
| **Edit** | `skills/forge-constitution/references/interview_guide.md` | Menambahkan 1 blok catatan literasi singkat (*0 instalasi*) di template `ONBOARDING.md` Fase 4.4 mengenai fitur *Adversarial Reviewer Sub-Agent* bawaan IDE. |
| **Edit** | `skills/forge-constitution/scripts/copy_static_assets.py` | Mendaftarkan `grill_cards_and_guards.md` (`/grill-me`) & `adversarial_review_lens.md` (`/plan` & `/audit`) untuk profil `all` agar 100% disalin bit-for-bit + verifikasi SHA-256. |

---

### 🧩 BATCH 4C: Sinkronisasi Installer/Updater, Bump `plugin.json` v2.0.0, & Uji Integritas Akhir
| Aksi | Berkas Sasaran | Dampak & Mekanisme |
| :--- | :--- | :--- |
| **Edit** | `skills/forge-constitution/references/physical_injection_spec.md` | Menambahkan Langkah `3b` (`.agents/rules/PERSONA_MENTOR.md`), melengkapi daftar salinan aset baru di Langkah 10/11/14, dan menyelaraskan contoh `"forge_version": "2.0.0"`. |
| **Edit** | `skills/forge-update/SKILL.md` | Menambahkan `persona_mentor.template.md`, `references/grill_cards_and_guards.md`, dan `references/adversarial_review_lens.md` ke Tabel Mapping. |
| **Edit** | `plugin.json` | Bump `"version": "1.3.6"` $\rightarrow$ **`"2.0.0"`** + menambahkan objek `releases["2.0.0"]` berisi seluruh daftar `updated_blueprints` dan ringkasan utuh evolusi v2.0.0. |

**Gerbang Verifikasi Akhir v2.0.0 (Sebelum Commit Lokal):**
1. **Audit Lossless Matematis:** `0` klausa hilang pada `master_rules` & `grill-me`.
2. **Audit Copier SHA-256 (4 Profil):** `copy_static_assets.py --dry-run` lolos Exit 0 untuk `fullstack`, `fe`, `be`, dan `minimal` dengan isolasi stack 100% bersih.
3. **Audit Manifest Validator:** `validate_manifest.py` lolos terhadap manifest proyek nyata (`eco-enzyme-landing`).
4. **Audit Upstream Drift:** `check_upstream.py --check` tetap 10/10 `✅ UP-TO-DATE`.
5. **Audit Kebersihan Path & Ukuran Blueprint:** `0` path absolut lokal (`d:/exe/HERD`) di seluruh `blueprints/`, `skills/`, dan `.agents/skills/`, serta tabel ukuran akhir seluruh 18 blueprint.
6. **Commit Lokal Rilis `v2.0.0`** di branch `main` (tanpa `git push` sampai diminta).

---

## 3. Gerbang Persetujuan Eksekusi

Silakan tinjau rencana 3 Micro-Batch di atas. Jika tidak ada revisi, cukup balas **"gas 4A"** (atau **"gas Tahap 4"**) untuk memulai eksekusi secara bertahap dengan laporan bukti lengkap di setiap batch.
