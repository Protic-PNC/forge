# Peta Besar & Katalog 126 Skill Engineering (7 Kluster)
**Sumber Referensi:** `scratch/claude-skills/` (`engineering/` dan `engineering-team/`)  
**Tujuan Dokumen:** Memberikan kompas dan *helicopter view* menyeluruh atas 126 skill engineering yang ada di repositori enterprise, dikelompokkan berdasarkan kluster disiplin rekayasa software.

---

## 1. Peta Navigasi 7 Kluster Engineering

```
                               PETA 126 SKILL ENGINEERING
                                           │
  ┌───────────────┬───────────────┬────────┴───────┬───────────────┬───────────────┐
  ▼               ▼               ▼                ▼               ▼               ▼
[Kluster 1]     [Kluster 2]     [Kluster 3]      [Kluster 4]     [Kluster 5]     [Kluster 6]     [Kluster 7]
Arsitektur &    Kualitas,       Keamanan &       Cloud, DevOps,  Debugging,      Spesialisasi    Meta-Agentic &
Desain API      Review, TDD     SecOps           SRE, Infra      Performa        Domain/Role     AI Governance
(15 Skill)      (16 Skill)      (12 Skill)       (19 Skill)      (12 Skill)      (14 Skill)      (22 Skill)
```

---

## 2. Rincian & Anggota Tiap Kluster

---

### Kluster 1: Arsitektur Sistem, Database & Desain API (15 Skill)
*Fokus: Merancang fondasi data dan kontrak antarmuka sebelum satu baris kode pun ditulis.*

| Nama Skill | Deskripsi & Tugas Utama |
| :--- | :--- |
| **`senior-architect`** | Mengevaluasi trade-off arsitektur makro, boundary service, dan System Design. |
| **`tech-stack-evaluator`** | Menilai kelayakan framework/library baru berdasarkan kebutuhan skalabilitas dan tim. |
| **`database-schema-designer`** | Merancang skema relasional 3NF, index komposit, multi-tenancy RLS, dan ERD Mermaid. |
| **`database-designer`** | Spesialis perancangan database terdistribusi dan pemodelan dokumen/NoSQL. |
| **`sql-database-assistant`** | Optimasi sintaks SQL kompleks, query plan analyzer, dan tuning parameter engine. |
| **`migration-architect`** | Merancang skema migrasi database zero-downtime dengan pola *Expand & Contract*. |
| **`api-design-reviewer`** | Linter kontrak REST/OpenAPI, deteksi otomatis *Breaking Changes*, dan grading skor API. |
| **`strict-api`** | Penegakan konvensi penamaan API yang sangat ketat (kebab-case, status code semantics). |
| **`rag-architect`** | Merancang pipeline Retrieval-Augmented Generation (chunking, embedding, vector DB). |
| **`mcp-server-builder`** | Merancang dan memvalidasi server Model Context Protocol (MCP) untuk integrasi AI. |
| **`feature-flags-architect`** | Merancang strategi peluncuran fitur bertahap (canary, dark launch, kill-switch). |
| **`epic-design`** | Memecah inisiatif bisnis besar menjadi milestone arsitektur yang terukur. |
| **`spec-driven-workflow`** | Alur kerja yang mewajibkan spesifikasi fungsional disahkan sebelum coding dimulai. |
| **`interview-system-designer`** | Simulasi wawancara desain sistem skala besar untuk validasi arsitektur. |
| **`game-universe-studio`** | Desain arsitektur state engine dan entitas untuk simulasi/game logic. |

---

### Kluster 2: Kualitas Kode, Review & Testing (16 Skill)
*Fokus: Menjamin kebenaran logika, review kode standar Google/Meta, dan otomasi uji kualitas.*

| Nama Skill | Deskripsi & Tugas Utama |
| :--- | :--- |
| **`code-reviewer`** | Melakukan review kode berbasis best practice industri, efisiensi memori, dan clean code. |
| **`pr-review-expert`** | Reviewer Pull Request formal yang menilai blast-radius, backward compatibility, dan DoD. |
| **`adversarial-reviewer`** | Reviewer "kejam" yang sengaja mencari celah ekstrem (*edge cases*) dan asumsi rapuh tim. |
| **`named-persona-adversarial-review`** | Review kode dari sudut pandang persona tertentu (misal: Security Engineer paranoid). |
| **`tdd-guide`** | Memandu alur kerja Test-Driven Development (Red-Green-Refactor). |
| **`red-green-proof`** | Mewajibkan pembuktian terminal bahwa test benar-benar gagal (*Red*) sebelum kode ditulis. |
| **`api-test-suite-builder`** | Membangun rangkaian integration test otomatis untuk seluruh endpoint HTTP. |
| **`playwright-pro`** | Otomasi pengujian antarmuka browser E2E, multi-viewport, dan interaksi form. |
| **`browser-automation`** | Pengujian fungsionalitas web app dinamis via browser headless. |
| **`full-page-screenshot`** | Tangkapan layar visual beresolusi penuh untuk audit regresi visual. |
| **`a11y-audit`** | Audit aksesibilitas antarmuka pengguna sesuai standar WCAG 2.1 / ARIA. |
| **`i18n-localization`** | Memverifikasi key terjemahan, string placeholder, dan format jam/mata uang multi-negara. |
| **`dependency-auditor`** | Memeriksa versi paket usang dan celah keamanan pada dependensi pihak ketiga. |
| **`data-quality-auditor`** | Memvalidasi integritas data, anomali tipe data, dan sanitasi pipeline data. |
| **`skill-tester`** | Pengujian otomatis apakah suatu instruksi skill AI berjalan sesuai skenario uji. |
| **`changelog-generator`** | Otomasi pembuatan changelog berbasis commit semantik (Conventional Commits). |

---

### Kluster 3: Keamanan, Pentest & SecOps (12 Skill)
*Fokus: Melindungi aplikasi dari serangan siber, kebocoran kunci rahasia, dan kepatuhan OWASP.*

| Nama Skill | Deskripsi & Tugas Utama |
| :--- | :--- |
| **`senior-security`** | Evaluasi postur keamanan aplikasi menyeluruh dan audit arsitektur keamanan. |
| **`security-pen-testing`** | Simulasi pengujian penetrasi untuk menemukan celah SQL injection, XSS, CSRF, dan SSRF. |
| **`red-team`** | Simulasi penyerangan agresif terhadap pertahanan sistem untuk menguji kesiapan tim. |
| **`threat-detection`** | Merancang aturan deteksi ancaman dan anomali akses pada log server. |
| **`ai-security`** | Proteksi dari serangan Prompt Injection, Jailbreak, dan Data Poisoning pada sistem AI. |
| **`security-guidance`** | Panduan kepatuhan standar keamanan (OWASP Top 10, CWE, NIST). |
| **`secrets-vault-manager`** | Pengelolaan kredensial terenkripsi (HashiCorp Vault, AWS Secrets Manager). |
| **`env-secrets-manager`** | Deteksi dini agar tidak ada file `.env`, API key, atau private key yang bocor ke Git. |
| **`mcp-oauth-triage`** | Diagnostik dan perbaikan alur autentikasi OAuth pada tool MCP. |
| **`skill-security-auditor`** | Mengaudit apakah ada instruksi berbahaya di dalam prompt atau kode script skill. |
| **`senior-secops`** | Integrasi keamanan ke dalam siklus hidup software development (DevSecOps). |
| **`cloud-security`** | Pengerasan konfigurasi cloud (IAM least privilege, VPC peering, firewall rules). |

---

### Kluster 4: Cloud, DevOps, Infra & Reliability (19 Skill)
*Fokus: Server, container, pipeline deployment, pemantauan performa sistem, dan penanganan krisis.*

| Nama Skill | Deskripsi & Tugas Utama |
| :--- | :--- |
| **`senior-devops`** | Perancangan arsitektur deployment, automasi infrastruktur, dan rilis software. |
| **`ci-cd-pipeline-builder`** | Membangun pipeline otomatisasi pengujian dan deployment (GitHub Actions, GitLab CI). |
| **`docker-development`** | Optimalisasi Dockerfile (multi-stage build, layer caching, image footprint kecil). |
| **`kubernetes-operator`** | Konfigurasi Deployment, StatefulSet, Ingress, Pod autoscaling (HPA), dan Helm. |
| **`helm-chart-builder`** | Pembuatan dan standarisasi template Helm chart untuk aplikasi cloud-native. |
| **`terraform-patterns`** | Penyusunan Infrastructure-as-Code (IaC) modular dan manajemen state Terraform. |
| **`aws-solution-architect`** | Desain sistem spesifik ekosistem AWS (ECS, Lambda, SQS, RDS, CloudFront). |
| **`gcp-cloud-architect`** | Desain sistem ekosistem Google Cloud (GKE, Cloud Run, BigQuery, Pub/Sub). |
| **`azure-cloud-architect`** | Desain sistem ekosistem Microsoft Azure (AKS, Azure Functions, CosmosDB). |
| **`cloud-finops`** | Audit dan efisiensi biaya infrastruktur cloud (menghilangkan resource zombie). |
| **`slo-architect`** | Perancangan Service Level Objectives (SLO), SLA, dan perhitungan Error Budget. |
| **`chaos-engineering`** | Pengujian ketahanan sistem dengan sengaja menyuntikkan kegagalan jaringan/server. |
| **`observability-designer`** | Konfigurasi metrik, distributed tracing (OpenTelemetry), dan dashboard monitoring. |
| **`runbook-generator`** | Pembuatan SOP teknis langkah-demi-langkah bagi tim on-call saat terjadi alert. |
| **`incident-commander`** | Protokol koordinasi krisis tingkat tinggi saat server produksi down (P1/P2). |
| **`incident-response`** | Mitigasi teknis cepat dan perbaikan darurat saat terjadi downtime. |
| **`snowflake-development`** | Desain arsitektur data warehouse dan query optimization pada Snowflake. |
| **`ms365-tenant-manager`** | Otomasi administrasi dan konfigurasi tenant Microsoft 365. |
| **`google-workspace-cli`** | Integrasi dan otomasi CLI untuk layanan Google Workspace. |

---

### Kluster 5: Debugging, Performa & Refactoring (12 Skill)
*Fokus: Menginvestigasi bug sistemik, menekan latensi, dan merapikan kode berantakan.*

| Nama Skill | Deskripsi & Tugas Utama |
| :--- | :--- |
| **`focused-fix`** | Investigasi dan perbaikan modul rusak end-to-end dengan *The Iron Law of Diagnosis*. |
| **`performance-profiler`** | Melacak memory leak, CPU spikes, dan bottleneck eksekusi kode. |
| **`tech-debt-tracker`** | Menginventarisasi hutang teknis, mengukur bunga resiko, dan membuat roadmap refactoring. |
| **`tc-tracker`** | Pelacakan dan manajemen kasus uji (Test Case management). |
| **`monorepo-navigator`** | Navigasi dan manajemen dependensi antar-paket pada arsitektur monorepo (Turborepo/Nx). |
| **`git-worktree-manager`** | Isolasi pengerjaan multi-branch secara paralel tanpa perlu clone berulang kali. |
| **`commit-craft`** | Penulisan pesan commit semantik yang rapi, informatif, dan terstandarisasi. |
| **`readme-polish`** | Standarisasi dokumentasi proyek agar mudah dipahami developer baru. |
| **`mobile-release`** | SOP persiapan rilis aplikasi mobile ke Google Play Store dan Apple App Store. |
| **`llm-cost-optimizer`** | Strategi pemangkasan biaya token API LLM (prompt compression, caching, model tiering). |
| **`code-tour`** | Pembuatan panduan tur kode interaktif untuk onboarding engineer baru. |
| **`codebase-onboarding`** | Pemetaan instan struktur repository untuk engineer yang baru bergabung. |

---

### Kluster 6: Spesialisasi Rekayasa (Domain & Role Specialists) (14 Skill)
*Fokus: Persona ahli untuk bidang rekayasa tertentu.*

| Nama Skill | Deskripsi & Tugas Utama |
| :--- | :--- |
| **`senior-frontend`** | Spesialis arsitektur UI, state management, render optimization, dan web standards. |
| **`senior-backend`** | Spesialis arsitektur server, concurrency, caching, messaging queue, dan microservices. |
| **`senior-fullstack`** | Penyelarasan integrasi end-to-end antara frontend, backend API, dan database. |
| **`senior-data-engineer`** | Perancangan pipeline data ingestion, ETL/ELT batch & streaming. |
| **`senior-data-scientist`** | Analisis data eksploratif, statistik inferensial, dan evaluasi metrik model. |
| **`senior-ml-engineer`** | MLOps, model deployment, inference optimization, dan monitoring drift. |
| **`senior-computer-vision`** | Pemrosesan citra digital, deteksi objek, dan model vision. |
| **`embedded-iot-mentor`** | Pemrograman mikrokontroler, RTOS, firmware, dan protokol IoT (MQTT/CoAP). |
| **`senior-qa`** | Perancangan strategi Quality Assurance menyeluruh (Piramida Testing). |
| **`stripe-integration-expert`** | Integrasi pembayaran kartu kredit, webhooks, idempotency key, dan refund flow. |
| **`boost-asio-pro`** | Pemrograman jaringan C++ performa tinggi berbasis Boost.Asio. |
| **`universal-scraping-architect`** | Arsitektur web scraping anti-bot, browser stealth, dan proxy rotation. |
| **`spinning-up-deep-rl`** | Panduan algoritma Reinforcement Learning (PPO, DDPG, SAC). |
| **`deep-learning-book`** | Konsultasi konsep dasar matematika dan teori deep learning. |

---

### Kluster 7: Meta-Agentic Engineering & Tata Kelola AI (22 Skill)
*Fokus: Skill yang mengontrol, mengaudit, mengevaluasi, dan mengarahkan agen AI lainnya.*

| Nama Skill | Deskripsi & Tugas Utama |
| :--- | :--- |
| **`agent-run-forensics`** | Membaca log transkrip asli (`transcript.jsonl`) untuk memvalidasi kejujuran tindakan AI. |
| **`human-gate`** | Mengunci aksi berbahaya menggunakan kode keluar terminal (Exit 2) dan file review `.review.md`. |
| **`ship-gate`** | Gerbang verifikasi otomatis sebelum kode dinyatakan layak rilis ke produksi. |
| **`skill-retro`** | Menganalisis 20–50 transkrip masa lalu untuk menemukan kelemahan instruksi prompt. |
| **`agent-harness`** | Kerangka kerja pengujian otomatis untuk memverifikasi perilaku agen AI. |
| **`agent-memory`** | Manajemen memori jangka panjang dan persistensi konteks antar-sesi agen. |
| **`agent-designer`** | Merancang instruksi, batasan peran, dan skema tool untuk agen AI baru. |
| **`agent-workflow-designer`** | Merancang orkestrasi alur kerja multi-step yang melibatkan beberapa agen. |
| **`agent-regression-evals`** | Rangkaian evaluasi benchmark untuk mendeteksi penurunan kecerdasan model. |
| **`self-eval`** | Kemampuan agen mengevaluasi kualitas outputnya sendiri sebelum diserahkan ke pengguna. |
| **`self-improving-agent`** | Pola agen yang mampu memperbarui instruksi kerjanya secara mandiri dari feedback. |
| **`zero-hallucination-coder`** | Membatasi agen agar hanya membuat kode dari file dan fungsi yang terbukti ada di repo. |
| **`prompt-governance`** | Standarisasi aturan penulisan prompt sistem di seluruh organisasi tim. |
| **`senior-prompt-engineer`** | Optimasi teknik prompting (Few-Shot, Chain-of-Thought, ReAct). |
| **`hivemind`** | Pola pertukaran memori dan sinkronisasi pengetahuan antar-banyak agen. |
| **`agenthub`** | Registri sentral untuk mendaftarkan dan memanggil agen spesialis. |
| **`handoff`** | Pembuatan ringkasan konteks padat saat berpindah sesi percakapan. |
| **`collab-proof`** | Melacak kontribusi siapa yang mengarahkan sesi (manusia vs AI). |
| **`autoresearch-agent`** | Agen yang melakukan riset pustaka dan investigasi kode secara otonom. |
| **`workflow-builder`** | Pembangun alur otomasi tugas multi-langkah. |
| **`write-a-skill`** | Skill yang membantu pengguna menyusun berkas `SKILL.md` baru sesuai standar. |
| **`book-to-skill`** | Mengubah buku teks rekayasa menjadi modul skill AI yang bisa dieksekusi. |

---
*Katalog ini disusun resmi untuk memberikan navigasi utuh atas seluruh ekosistem engineering skills.*
