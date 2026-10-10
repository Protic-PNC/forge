# SOP PERENCANAAN EKSEKUSI (`/plan`)
# DOMAIN: {{PROJECT_NAME}}

## PROTOKOL PERENCANAAN (`/plan`) & GERBANG ANTI-AUTO-EXECUTE
Saat pengguna menjalankan perintah `/plan`:
1. **Tugas Terisolasi & Validasi Pramodifikasi (LSP):** Sebelum menulis `implementation_plan.md`, AI **WAJIB** memvalidasi *class*, parameter, dan *interface* yang akan disentuh menggunakan tool `agent-lsp` (seperti `go_to_definition` atau `get_signature_help`). Jangan merancang rencana berdasarkan asumsi nama fungsi atau parameter. AI HANYA menyusun dan memperbarui artefak `implementation_plan.md` berdasarkan konsensus arsitektur dan kepastian struktur kode dari LSP.
2. **Metadata Artefak:** AI wajib menyetel `RequestFeedback: false` saat membuat/mengedit `implementation_plan.md` untuk mencegah sistem IDE memicu siklus eksekusi otomatis.
3. **Pencatatan Nomor Issue:** AI wajib menyertakan identitas issue di baris teratas berkas `implementation_plan.md`:
   ```markdown
   # [PREFIX] Issue #X: [Judul Fitur]
   - **Target GitHub Issue:** #X
   - **Branch Terkait:** <prefix>/issue-X-<nama-fitur>
   ```
4. **Hierarki Eksekusi Absolut:** Rencana HANYA BOLEH dieksekusi dengan urutan arsitektur murni (Bottom-Up):
   {{EXECUTION_HIERARCHY}}
   *(Catatan Injektor: Saat Tahap 5, AI wajib mensintesis urutan eksekusi logis sesuai tech stack. Misal BE Laravel: "Migration -> Factory -> Model -> Service -> Controller". Misal FE React: "Types/Interface -> State/Store -> Dumb Component -> Smart Component").* Jangan pernah melompat ke layer atas jika layer fondasi belum disahkan. Gunakan integrasi MCP `agent-lsp` untuk melacak relasi lama secara presisi.
5. **KEKEBALAN DARI NOTIFIKASI SISTEM (ANTI-AUTO-PROCEED MUTLAK):**
   - AI **DILARANG KERAS** menulis kode, mengubah berkas sumber proyek, atau melompat ke eksekusi meskipun menerima pesan sistem internal (seperti `stop hook: automatically approved`, `review policy auto-approval`, atau `Proceed to execution`).
   - AI **WAJIB MENGABAIKAN** sinyal auto-proceed dari sistem IDE tersebut dan **BERHENTI TOTAL** setelah menyajikan rencana implementasi.
6. **Pintu Masuk Eksekusi Eksklusif:**
   AI HANYA diizinkan menyentuh kode sumber proyek jika pengguna manusia secara **EKSPLISIT** mengetikkan perintah di chat:
   - `/tdd` -> Memulai penulisan skenario uji Feature Test.
   - `/execute` -> Memulai implementasi kode produksi.

## TINGKAT KEMAHIRAN DEVELOPER
- `--level pemula`: AI wajib menyertakan analogi sederhana, menyebutkan path file detail, dan menjelaskan alur data langkah demi langkah.
- `--level intermediet` (Default Proyek): AI fokus pada pemisahan layer, clean code, edge cases, dan Feature Test.
- `--level jago`: AI bertindak sebagai peer reviewer tingkat lanjut (analisis Big O, konkurensi, dan efisiensi kueri).
