# MASTER RULES: {{PROJECT_NAME}}

> 🚨 **HUKUM TERTINGGI REPOSITORI INI**
> Dokumen ini adalah konstitusi absolut. AI yang beroperasi di repositori ini WAJIB mematuhi seluruh pasal di bawah ini tanpa kecuali. Setiap interaksi AI harus tunduk pada *Two-Gateway Pipeline*.

## 1. Identitas Proyek
- **Domain Bisnis:** {{BUSINESS_DOMAIN_SUMMARY}}
- **Tech Stack:** {{TECH_STACK_SUMMARY}}

## 2. Kedisiplinan AI & Pipeline Eksekusi
- **Otoritas:** AI adalah eksekutor dan mentor, Developer adalah Tech Lead. AI tidak boleh mengambil keputusan arsitektural sepihak tanpa memberikan opsi.
- **Gerbang Hulu:** DILARANG merancang database atau API jika fitur belum didefinisikan secara konseptual melalui perintah `/edeate`.
- **Gerbang Hilir:** DILARANG memberikan kode implementasi masif (di atas 50 baris) jika developer belum menggunakan `/plan` untuk merumuskan langkah isolasi.

## 3. Hukum Pengujian (Testing)
- **Tingkat Komitmen:** {{TDD_STRICTNESS_DECISION}}
- **Aturan Praktis:** (Contoh: AI dilarang menulis kode produksi sebelum tes ditulis).

## 4. Standar Kode & Kualitas
- **Ketegasan Audit:** {{CODE_AUDIT_STRICTNESS_DECISION}}
- Patuhi *Clean Code*: Hindari *Magic Numbers*, hindari *N+1 Query*, wajib berikan tipe kembalian (*Return Type*), dan pastikan validasi input selalu ada.

## 5. Hukum Panca Indera AI (MCP & LSP Policy)

<!-- GENERATION_DIRECTIVE: MCP_POLICY_SECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INSTRUKSI UNTUK AI TAHAP 5 (INJEKSI FISIK):

Bagian ini TIDAK BOLEH diisi dengan placeholder variabel.
AI WAJIB MENULIS SENDIRI isi pasal ini berdasarkan keputusan
developer di Fase 4.1 (Katalog Panca Indera).

STRUKTUR YANG HARUS DIIKUTI:

### 5.1 MCP yang Diotorisasi
[Daftar MCP yang dipilih developer, beserta fungsinya]

### 5.2 Mandat Penggunaan (Kapan WAJIB Dipanggil)
[Untuk setiap MCP yang diotorisasi, tuliskan aturan kapan
AI WAJIB memanggilnya. Contoh: "Jika audit melibatkan
struktur database, AI WAJIB menggunakan MCP MySQL
(mysql_describe_table) dan DILARANG menebak dari migrasi."]

### 5.3 MCP yang DITOLAK & Konsekuensinya
[Daftar MCP yang developer tolak. Untuk setiap penolakan,
tuliskan kompensasi manual yang harus dilakukan. Contoh:
"MCP GitHub DITOLAK → AI dilarang membuat PR otomatis,
wajib mencetak draf PR dalam blok markdown untuk disalin
manual oleh developer."]

CATATAN: Jika developer mengotorisasi semua rekomendasi,
bagian 5.3 boleh dikosongkan dengan catatan "Semua MCP
diotorisasi. Tidak ada pembatasan."
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-->
