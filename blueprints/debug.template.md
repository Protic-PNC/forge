# SOP DEBUGGING KODE (`/debug`)
# DOMAIN: {{PROJECT_NAME}}

## 🐞 PROTOKOL DEBUGGING (`/debug`)
Ketika developer memicu perintah `/debug` atau melaporkan *bug* spesifik, AI **DILARANG KERAS** menyajikan kode perbaikan (Patch) secara prematur. AI WAJIB melalui 3 fase ketat berikut secara berurutan:

1. **Fase 1 (Hipotesis):** AI merumuskan 2-3 dugaan sementara penyebab *bug* berdasarkan *Stack Trace*, pesan error, atau deskripsi masalah.
2. **Fase 2 (Investigasi Bukti):** AI **WAJIB** memvalidasi hipotesis dengan melakukan pencarian fisik ke *codebase*. AI **WAJIB MEMPRIORITASKAN** penggunaan integrasi MCP `agent-lsp` seperti `find_references`, `callers`, atau `go_to_definition` untuk menyusuri jejak (*tracing*) alur logika secara absolut berbasis *AST* (Abstract Syntax Tree). `grep_search`/`view_file` hanya digunakan untuk *fallback* atau membaca *log*.
3. **Fase 3 (Proposisi Bedah Kode):** Hanya setelah menemukan "Jejak Berdarah" (*Smoking Gun*) di kode asli, AI menyajikan penjelasan akar masalah dan strategi perbaikan (*bukan langsung menulis kode perbaikan*). AI harus meminta izin developer sebelum mengeksekusi perubahan.
