# PANDUAN REFERENSI: PAKET PENYERAHAN TIKET & HANDOFF PR (`/audit`)
**Direktori Rujukan On-Demand untuk Bagian 3 Laporan Audit — 100% Lossless Extraction**

---

## 📬 Bagian 3: Action Hook & Paket Penyerahan Tiket (Handoff Package)

DILARANG menutup respons audit dengan salam santai atau kalimat umum seperti "silakan buat PR dan kabari tech lead". AI WAJIB menyajikan seluruh komponen Handoff Package berikut secara utuh:

* *Sinkronisasi Dokumen Roadmap (Roadmap Alignment Gate):* AI **WAJIB** secara otomatis memperbarui file `DEVELOPMENT_ROADMAP.md` di root proyek dengan mencentang item checklist (`- [x]`) yang berhasil diselesaikan oleh tiket ini. Dokumen roadmap adalah *North Star* proyek yang wajib selalu mencerminkan progres nyata di lapangan sebelum penyerahan PR.
* *Langkah Git & Push:* Perintah terminal siap salin yang mencakup keseluruhan alur Git (`git add .`, `git commit -m "..."` sesuai standar Conventional Commits, lalu `git push -u origin <branch>`).
* *Draf Pull Request Siap Salin:* Judul PR & Deskripsi PR lengkap (mengintegrasikan ringkasan fitur, trade-off, dan checklist DoD). AI **WAJIB** mengekstrak nomor issue dari nama branch aktif (`issue-<nomor>`) atau artefak plan dan mencantumkan `Closes #<nomor-issue>` di baris paling atas deskripsi PR untuk menjamin penutupan otomatis tiket di GitHub dan menggerakkan kartu Kanban dari `In Progress` ke `Done` saat PR di-merge. Sertakan juga penetapan label PR resmi: `needs-review` dan label domain/modul terkait. Draf PR ini WAJIB disajikan sepenuhnya di dalam blok kode markdown (` ```markdown `) agar mudah disalin utuh oleh pengguna.
* *Pelayanan Proaktif & Penawaran MCP GitHub PR:* DILARANG melakukan `git merge` lokal ke `main`. Di akhir sesi, AI **WAJIB** mengambil alih beban kognitif pengguna dengan menawarkan secara elegan:
  > *"Audit telah lulus dengan predikat Enterprise. Apakah Anda ingin saya langsung membuatkan Pull Request resminya menggunakan MCP GitHub (`create_pull_request`) ke branch `main` sekarang (lengkap dengan `Closes #<id>` dan label `needs-review`) agar papan Kanban kampus otomatis bergerak dan Anda bisa langsung bersantai?"*
  Jika developer menyetujui, AI memanggil tool MCP GitHub untuk menerbitkan PR secara nyata dan menyematkan label `needs-review`.
* *Peringatan & Penawaran Interaktif Visual Smoke Test (Khusus Fallback):* Jika Tier 4 dialihkan ke fallback statis karena browser Playwright belum terpasang, wajib cetak persis callout penawaran di `references/audit_visual_gate.md` Bagian 4.
* *Action Hook (Pertanyaan Pancingan Aksi Selanjutnya):* AI wajib memancing aksi berikutnya dengan menanyakan apakah developer ingin lanjut mengambil tiket berikutnya atau ada bagian teknis yang ingin didalami.
