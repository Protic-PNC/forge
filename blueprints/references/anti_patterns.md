# PANDUAN REFERENSI: TABEL PENJAGA KUALITAS (ANTI-PATTERNS)
**Direktori Rujukan On-Demand untuk Gerbang Hulu (`/edeate`)**

---

## ⚠️ PENJAGA KUALITAS (Anti-Pattern yang Harus Ditolak AI)

| Anti-Pattern | Dampak | Tindakan Wajib AI |
|---|---|---|
| **Question Bombing / Dosen Sidang Mode** | Mahasiswa junior terintimidasi, overload kognitif, takut salah | AI WAJIB 1 topik per respons, pakai analogi ramah, dan sajikan Mini Trade-off Box |
| **Blind Choice without Trade-off** | Developer memilih tanpa paham konsekuensi, tidak bertumbuh | AI WAJIB membeberkan untung vs harga yang dibayar sebelum mencatat keputusan |
| **Multi-Ticket Dumping** (Mencetak lebih dari 1 tiket Level 3 dalam 1 sesi) | Fokus buyar, *blast radius* membengkak, pengujian bias dan campur aduk | AI WAJIB membatasi hanya 1 tiket Level 3 yang difinalisasi per sesi. Sisanya dicatat di roadmap backlog. |
| **Premature Ticket Synthesis** (Langsung mencetak tiket tanpa ACC plan) | Resiko rework besar jika asumsi dasar arsitektur atau boundary salah | AI WAJIB menyajikan rangkuman & scope plan di Fase 4 dan menunggu ACC Tech Lead di Fase 5. |
| **Hulu Code Execution / Auto-PR Offer** (Menawarkan eksekusi kode/PR di `/edeate`) | Melanggar batas gerbang, membypass TDD, Plan, dan Code Audit Hilir | AI DIHARAMKAN menulis kode atau menawarkan PR di Hulu. AI WAJIB menyerahkan tiket ke Gateway 2 via `/grill-me`. |
| **Tiket Terlalu Luas** ("Bikin fitur manajemen event lengkap") | Scope tak terbatas, sprint berantakan | AI WAJIB meminta developer memecah menjadi tiket-tiket kecil yang independen |
| **DoD Ambigu** ("Berhasil dijalankan") | Developer dan reviewer punya definisi sukses yang berbeda | AI WAJIB mendesak definisi yang terukur (angka, waktu, kondisi boolean, perintah test) |
| **Triad Dogma / Strawman Bloat** (Memaksakan 3 opsi arsitektur saat problemnya secara alami biner) | Melahirkan opsi ke-3 yang konyol, membingungkan pemula, dan memicu *over-engineering* | AI WAJIB menyajikan spektrum 2–3 opsi sah dan DILARANG mengarang Opsi 3 jika pilihannya biner |
| **Camouflage Trap** (Menyamarkan mekanik runtime/toolchain menjadi dongeng ormawa fiktif) | Diskusi terasa konyol, manipulatif, dan mengaburkan esensi teknis | AI WAJIB menggunakan Track B (NFR Fast-Track 1 ketukan) untuk tiket pondasi/toolchain |
| **Backend-Only Ticket Template Bias** (Memaksakan Policy Matrix & Controller/Service pada tiket Frontend/Toolchain) | Struktur tiket tidak relevan, kolom diisi kosong atau fiktif | AI WAJIB mengadopsi format matriks dan langkah implementasi modular (Varian A, B, atau C) |
| **Tiket Tanpa Blast Radius** | Developer/AI mengedit file liar di luar cakupan tugas | AI WAJIB memetakan daftar berkas entry point, service, schema, dan test |
| **Tiket Tanpa Invariant** | Tidak ada kontrak yang bisa diuji → Feature Test menjadi formalitas dangkal | AI WAJIB menggali minimal 1-2 invariant absolut sebelum draft disahkan |
| **Asumsi Tanpa Audit Kode** | AI berbicara dari imajinasi, bukan realita repositori | AI WAJIB menjalankan Pre-Flight Audit (Fase 0) sebelum sesi dimulai |
| **Langsung Lompat ke Solusi** | Masalah bisnis inti tidak dipahami | AI WAJIB menyelesaikan Pilar Bisnis (Track A) atau Sasaran NFR (Track B) terlebih dahulu |
| **Premature Roadmap Checkmark** (Mencentang `[x]` di `DEVELOPMENT_ROADMAP.md` saat `/edeate`) | Menimbulkan *False Sense of Completion* dan memicu pencemaran branch Git aktif | AI WAJIB mempertahankan kotak centang kosong `- [ ]` dan hanya menyematkan nomor tiket `(Issue #[Nomor])`. Hak centang `[x]` mutlak milik `/audit` di hilir. |
| **Recommendation Anchoring Trap** (Menaruh bintang ⭐ atau label `[Rekomendasi]` di judul kartu opsi) | Memicu *Anchoring Bias* & *Halo Effect*: developer mengabaikan opsi lain dan melewatkan analisis trade-off | AI WAJIB menyajikan seluruh judul kartu secara netral dan menunda deklarasi rekomendasi ke bagian paling bawah |
