# Fase 4: Multi-Agent Orchestration & Team Handoff
**Fokus Pembelajaran:** Mengorkestrasi banyak agen, pembagian peran spesialis (Triad: Persona, Skill, Task), mencegah tabrakan konteks (*Context Collision*), dan protokol handoff antar-fase.  
**Sumber Referensi:** `scratch/claude-skills/orchestration/` (`ORCHESTRATION.md`), `agent-launcher/`, dan `engineering-team/` (`adversarial-reviewer`, `senior-architect`, `session-handoff`).

---

## 1. Masalah Fatal pada Sistem Multi-Agent Tanpa Orkestrasi

Banyak developer mencoba membuat sistem "Tim AI" dengan menyuruh 3–5 agen mengobrol bersama dalam satu ruang obrolan (seperti di AutoGen atau ChatDev awal). Hasilnya hampir selalu berujung pada **3 Bencana Klasik**:

1. **Context Collision (Tabrakan Konteks):**  
   Setiap agen men-dump seluruh log pemikirannya ke jendela chat. Dalam 4–5 putaran, context window langsung penuh (80.000+ token) dan agen mulai melupakan tugas utamanya.
2. **The "Yes-Man" Echo Chamber:**  
   Agen Developer menulis kode dengan bug, Agen Reviewer memuji kodenya (*"Bagus sekali!"*), dan Agen QA mengiyakan. Tidak ada ketegangan dialektika kritis yang nyata.
3. **Role Confusion (Krisis Identitas Peran):**  
   Agen yang tadinya bertugas sebagai Arsitek tiba-tiba ikut mengedit CSS, atau agen QA malah sibuk mengubah arsitektur database. Batas wilayah kerja kabur.

Repositori enterprise memecahkan masalah ini dengan **Protokol Orkestrasi Tanpa Framework Rumit (Zero-Dependency Orchestration Protocol)**.

---

## 2. Rumus Inti Orkestrasi: Triad (WHO, HOW, WHAT)

Di level enterprise, orkestrasi agen tidak membutuhkan library Python yang berat. Mereka membedakan agen ke dalam 3 komponen yang saling melengkapi:

```
┌───────────────────────────────────────────────────────────────────────────┐
│                    TRIAD ORKESTRASI MULTI-AGEN                            │
├───────────────────────────────────────────────────────────────────────────┤
│ 1. PERSONA (WHO)  ──► Siapa yang berpikir? (Identitas, gaya komunikasi,   │
│                       standar mutu, dan bias pengambilan keputusan).       │
│                                                                           │
│ 2. SKILL (HOW)    ──► Bagaimana cara mengeksekusi dengan presisi?         │
│                       (SOP, skrip Python, linter, checklist, template).   │
│                                                                           │
│ 3. TASK (WHAT)    ──► Apa tugas spesifik yang harus diselesaikan saat ini?│
│                       (Target artefak fisik, batasan file, deadline).      │
└───────────────────────────────────────────────────────────────────────────┘
```

* **Persona tanpa Skill:** AI hanya banyak bicara gaya konsultan tapi tidak punya alat eksekusi teknis (omong kosong).
* **Skill tanpa Persona:** AI mengeksekusi alat secara kaku tanpa punya kebijaksanaan prioritas bisnis dan trade-off.
* **Kombinasi Keduanya:** Agen yang memiliki *kebijaksanaan arsitek* sekaligus memegang *kunci pas perkakas presisi*.

---

## 3. 4 Pola Orkestrasi Utama di Dunia Industri

Dalam `ORCHESTRATION.md`, ada **4 Pola Desain** yang digunakan sesuai jenis pekerjaan:

```
┌─────────────────────────┬─────────────────────────┬─────────────────────────┬─────────────────────────┐
│  Pola A: Solo Sprint    │ Pola B: Domain Deep     │ Pola C: Multi-Agent     │  Pola D: Skill Chain    │
│  (Ganti Persona Fase)   │ (Skill Stacking)        │ Handoff & Adversarial   │  (Rel Pabrik Prosedural)│
└─────────────────────────┴─────────────────────────┴─────────────────────────┴─────────────────────────┘
```

### Pola A: Solo Sprint (Phase-Switched Persona)
*Cocok untuk: Solo Founder, pengerjaan proyek mandiri dari nol.*
* Agen tunggal yang **berganti persona di setiap pergantian fase waktu**:
  * *Minggu 1:* Load persona `startup-cto` + skill `database-schema-designer` $\rightarrow$ Bangun MVP.
  * *Minggu 2:* Ganti persona `growth-marketer` + skill `copywriting` $\rightarrow$ Rancang landing page.
  * *Minggu 3:* Ganti persona `solo-founder` + skill `analytics-tracking` $\rightarrow$ Peluncuran produk.
* **Aturan Keras:** *Hanya 1 persona aktif dalam 1 waktu.* Dilarang mencampur dua kepribadian dalam satu prompt.

### Pola B: Domain Deep-Dive (Skill Stacking)
*Cocok untuk: Audit sistem kritis, due-diligence arsitektur.*
* Mempertahankan **1 persona tunggal**, tetapi menumpuk (*stack*) beberapa skill spesialis sekaligus:
  * Persona: `startup-cto`
  * Stack Skill yang di-load: `aws-solution-architect` + `senior-security` + `cloud-finops`.
  * Hasil: Analisis arsitektur yang mendalam dari sisi infrastruktur, keamanan data, dan efisiensi biaya server secara serempak.

### Pola C: Multi-Agent Handoff & Adversarial Review (Paling Bernilai!)
*Cocok untuk: Keputusan arsitektur bernilai tinggi dan validasi pra-deploy.*
* Agen-agen dengan persona bertolak belakang diadu untuk saling menguji pekerjaan satu sama lain:
  1. **Langkah 1 (The Creator):** Agen `senior-architect` merancang rencana sistem.
  2. **Langkah 2 (The Attacker):** Agen `adversarial-reviewer` membedah rencana tersebut secara kejam, mencari celah kegagalan ekstrem (*worst-case scenario*), race conditions, dan potensi memory leak.
  3. **Langkah 3 (The Judge):** Agen `startup-cto` membuat keputusan final: risiko mana yang diterima (*accepted risk*) dan mana yang wajib direvisi.

### Pola D: Skill Chain (Alur Pabrik Prosedural)
*Cocok untuk: Pemrosesan berulang (SOP).*
* **Tidak memerlukan Persona.** Skill dirangkai berurutan seperti ban berjalan pabrik:
  `Langkah 1: Scrape Data` $\rightarrow$ `Langkah 2: Format JSON` $\rightarrow$ `Langkah 3: Linter Validator` $\rightarrow$ `Langkah 4: Deploy`.

---

## 4. Protokol Handoff Antar-Sesi: Mencegah Context Drift

Bagaimana cara agen berpindah giliran tanpa men-dump ribuan baris chat yang memboroskan token?  
Enterprise menggunakan **Protokol Handoff Padat (`session-handoff`)**:

### Aturan Emas Handoff (The Handoff Law):
> *"Jangan pernah menyalin ulang isi kode atau dokumen yang sudah ada. Cukup sebutkan PATH filenya, ringkas keputusannya, dan cantumkan pertanyaan yang belum terjawab."*

### Format Baku Dokumen Handoff:
```markdown
# SESSION HANDOFF: [Nama Tiket / Milestone]

## 1. Status Terkini (Current State)
- Tiket: Issue #12 (Integrasi Payment Gateway)
- Git Branch: feat/issue-12-stripe-webhook

## 2. Keputusan yang Telah Dikunci (Decisions Made)
- Menggunakan Stripe Webhook dengan Idempotency Key (bukan polling manual).
- Database migration selesai di berkas: src/db/migrations/003_payments.sql

## 3. Artefak Fisik yang Dihasilkan (Artifacts Created)
- [src/pages/api/webhook.ts](file:///src/pages/api/webhook.ts)
- [src/lib/stripe.ts](file:///src/lib/stripe.ts)

## 4. Celah yang Wajib Diselesaikan Agen Berikutnya (Open Questions & Next Steps)
- Buat integration test untuk menangani error signature verification saat payload dipalsukan.
- Jalankan Playwright visual smoke untuk halaman checkout.

## 5. Rekomendasi Skill untuk Fase Berikutnya (Suggested Skills)
- Load: `engineering-team/skills/stripe-integration-expert`
- Load: `engineering/skills/api-test-suite-builder`
```

Dengan format di atas, agen di sesi baru hanya membaca **~200 token ringkasan** dan bisa langsung melanjutkan pekerjaan tanpa kehilangan arah!

---

## 5. Komparasi dengan FORGE & Peluang Asimilasi

| Dimensi | Standar Enterprise (`ORCHESTRATION.md`) | Kondisi FORGE di Proyek Kita |
| :--- | :--- | :--- |
| **Model Alur Kerja** | Fleksibel: Mendukung 4 Pola (Solo Sprint, Deep-Dive, Adversarial, Skill Chain). | **Terfokus pada Pola D (Pabrik Two-Gateway):** Sangat kuat di alur siklus hidup (`/edeate` $\rightarrow$ `/plan` $\rightarrow$ `/execute` $\rightarrow$ `/audit`). |
| **Pemisahan Persona vs Skill** | Memisahkan secara ketat file persona (`agents/personas/`) dengan file skill (`skills/`). | Menyatu dalam prompt: Persona "Mentor / Kakak Tingkat" tertanam langsung di dalam file `SKILL.md` (30–50KB). |
| **Adversarial Dialectic** | Memiliki skill `adversarial-reviewer` yang sengaja menyerang ide arsitektur secara independen. | FORGE memiliki aturan *Anti Yes-Man* di `00-router.md`, namun masih diperankan oleh agen yang sama. |
| **Protokol Handoff** | Memiliki skill resmi `session-handoff` dengan script pembersih token dan linter privasi. | FORGE mengandalkan penyimpanan file plan `.docs/plan/`, namun ringkasan sesi masih sering bercampur di jendela chat. |

---

## 6. Blueprint Asimilasi: Bagaimana Memperkuat FORGE dengan Pola Orkestrasi?

1. **Suntikkan "Adversarial Review Sub-agent" ke Gerbang `/plan` & `/grill-me`:**  
   Ketika developer selesai membuat rencana di `/plan`, panggil persona **`adversarial-reviewer`** untuk menguji ketahanan rencana tersebut sebelum masuk ke `/execute`.
2. **Pisahkan Persona Mentor dari File `SKILL.md`:**  
   Pindahkan instruksi kepribadian "Kakak Tingkat Senior" ke file persona terpisah, sehingga file `SKILL.md` FORGE bisa mengecil drastis ke batas $\le$10KB.
3. **Standarisasi Dokumen Handoff Antar-Tiket:**  
   Gunakan template handoff padat (Decisions $\rightarrow$ Artifact Paths $\rightarrow$ Next Gaps) setiap kali developer selesai mengerjakan satu tiket Issue di `/audit` sebelum melangkah ke tiket berikutnya.

---
*Dokumen ini merupakan modul resmi pembelajaran Fase 4: Multi-Agent Orchestration.*
