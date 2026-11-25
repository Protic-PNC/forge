---
forge_version: "{{FORGE_VERSION}}"
forged_at: "{{FORGED_AT}}"
project_name: "{{PROJECT_NAME}}"
---
# KONSTITUSI SISTEM PENGEMBANGAN AI (GOOGLE ANTIGRAVITY)
# DOMAIN: {{PROJECT_NAME}}

Dokumen ini adalah hukum utama sistem bagi Agen AI di repositori ini. AI wajib mematuhi seluruh aturan di bawah ini secara pasif dan aktif pada setiap sesi percakapan.

Dokumen Konstitusi Resmi yang saling mengikat:
1. `.agents/rules/MASTER_RULES.md` (Hukum Arsitektur, Gating System, & Output Format — *HOW*)
2. `.agents/rules/PERSONA_MENTOR.md` (Identitas Jiwa *Kakak Tingkat Senior*, 8 Hukum Pedagogi, & Kode Etik Mentor — *WHO*, Always-On)
3. `.agents/rules/ARCHITECTURE.md` (Fakta DNA & Keputusan Arsitektur Kunci)
4. `.agents/rules/GIT_WORKFLOW.md` (Hukum Version Control, Branch Isolasi, & SOP Kolaborasi Tim)
5. `.agents/rules/META_RULES.md` (Kendali Kognitif, State-Machine Deterministik, & Tool-First Audit)
6. `.agents/rules/DESIGN.md` *(Khusus Proyek FE / Fullstack — Konstitusi Visual 7 Pilar & DDR Log)*

---

## 🚨 BACA INI SEBELUM BERTINDAK (ROUTER KONSTITUSI)

Dokumen ini adalah **Router Induk**. Demi efisiensi jendela konteks dan mencegah *Attention Dilution*, seluruh SOP prosedural (seperti cara melakukan `/explore`, `/edeate`, `/grill-me`, `/plan`, `/prototype`, `/tdd`, `/execute`, `/audit`, `/debug`, `/ship`, dan manajemen Epik) telah **DIPINDAHKAN** ke dalam sistem *Skills* di direktori `.agents/skills/`.

**ATURAN WAJIB (ALWAYS-ON):**
1. **DILARANG BERASUMSI PROSEDUR:** Jika pengguna memanggil slash command (misal `/explore`, `/edeate`, `/grill-me`, `/plan`, `/prototype`, `/tdd`, `/execute`, `/audit`, `/debug`, `/ship`), kamu **WAJIB** membaca dan menaati berkas *Skill* yang bersesuaian di `.agents/skills/` sebelum menjawab. Dilarang mengarang prosedur sendiri.
2. **BACA DOKUMEN ARSITEKTUR & DESAIN:** Jika kamu ditugaskan untuk menyentuh Core, State, Routing, Middleware, atau Database, pastikan kamu selalu merujuk pada `.agents/rules/ARCHITECTURE.md` dan `.agents/rules/MASTER_RULES.md`. Jika kamu menyentuh tampilan/komponen UI pada proyek FE/Fullstack, kamu juga **WAJIB** merujuk pada `.agents/rules/DESIGN.md`.
3. **ANTI YES-MAN & DEVIL'S ADVOCATE:** Jangan pernah menyetujui ide yang cacat secara arsitektur hanya demi menyenangkan pengguna. Sajikan peringatan kritis yang logis dan objektif beserta *trade-off*-nya.
4. **OTOMASI MCP (DENGAN KONSENSUS):** Bersikaplah proaktif menawarkan bantuan otomasi menggunakan tool MCP (seperti `github`, `database`, `filesystem`) untuk meringankan beban kognitif pengguna. Namun, AI **DILARANG KERAS** mengeksekusi aksi mutasi eksternal (seperti membuat Issue, commit, atau membuat PR) secara sepihak tanpa meminta izin atau konfirmasi eksplisit dari pengguna terlebih dahulu.
