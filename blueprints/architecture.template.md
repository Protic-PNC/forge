---
forge_version: "{{FORGE_VERSION}}"
forged_at: "{{FORGED_AT}}"
project_name: "{{PROJECT_NAME}}"
---
# ARCHITECTURE BLUEPRINT: {{PROJECT_NAME}}

> Dokumen ini memetakan rancangan makro sistem. Seluruh tiket dan fitur yang digarap melalui `/edeate` wajib berkiblat pada fondasi arsitektur di dokumen ini.

## 1. Peta Aktor & Peran (Role-Based Access)
{{ACTORS_AND_ROLES_DESCRIPTION}}

## 2. Desain Sistem & Infrastruktur
- **Pendekatan Arsitektur:** {{SYSTEM_ARCHITECTURE_APPROACH}}
- **Pola Komunikasi (FE/BE):** {{FRONTEND_BACKEND_SEPARATION_STRATEGY}}

## 3. Lapisan Keamanan & Autentikasi
{{SECURITY_AND_AUTHENTICATION_STRATEGY}}

## 4. Penanganan Celah Bisnis & Edge Cases
{{BUSINESS_GAPS_AND_RESOLUTIONS}}

## 5. Integrasi Eksternal & Layanan Pihak Ketiga
{{INFRASTRUCTURE_AND_3RD_PARTY_INTEGRATIONS}}

## 6. Protokol Perubahan Arsitektur (Architecture Decision Records / ADR)
Dokumen ini bukan artefak statis mati. Jika dalam perjalanan pengembangan terjadi perubahan arsitektur fundamental (misal penggantian library/framework, perubahan pola state management, migrasi autentikasi, atau penambahan integrasi infrastruktur baru), tim dan AI **WAJIB** mencatatnya dalam bentuk ADR di bagian bawah dokumen ini.

AI dan Developer **DILARANG KERAS** merombak arsitektur sistem secara diam-diam tanpa mencatat riwayat keputusan ADR!

### Format Entri ADR:
Setiap keputusan arsitektur baru dicatat secara berurutan kronologis menggunakan format baku:

```markdown
### [ADR-YYYY-MM-DD]: <Judul Keputusan Singkat>
- **Status:** [Disahkan / Digantikan]
- **Konteks & Masalah:** <Mengapa perubahan ini diperlukan?>
- **Pilihan yang Dipertimbangkan:** <Daftar opsi yang dievaluasi beserta trade-off-nya>
- **Keputusan:** <Solusi yang dipilih dan disahkan oleh Tech Lead>
- **Konsekuensi & Dampak:** <Dampak positif, harga teknis/trade-off, dan area berkas yang terdampak>
```

<!-- ADR_LOG_START -->
<!-- Catatan: Entri ADR baru ditambahkan tepat di bawah baris ini oleh tim saat evolusi sistem berlangsung. -->
<!-- ADR_LOG_END -->



