#!/usr/bin/env python3
"""
copy_static_assets.py
Deterministik Lossless Asset Copier dengan Verifikasi SHA-256 (Stdlib Only)
Bagian dari FORGE Constitution Engine - Standard Library murni (sys, os, shutil, hashlib, json, argparse).

Kegunaan:
Menyalin berkas statis murni (`blueprints/references/*.md` dan `skills/forge-constitution/scripts/*.py`)
dari repositori global FORGE ke proyek target secara 100% bit-for-bit lossless (menggunakan OS filesystem copy
`shutil.copy2` + verifikasi hash `SHA-256`) agar AI TIDAK PERNAH mengetik ulang file statis via `write_file`
yang rawan terkena LLM summarization bias.

Contoh Pemakaian:
  python copy_static_assets.py --forge-root "/path/to/FORGE" --target-root "." --profile fullstack
  python copy_static_assets.py --forge-root "/path/to/FORGE" --target-root "." --profile fe
  python copy_static_assets.py --forge-root "/path/to/FORGE" --target-root "." --profile be
"""

import argparse
import hashlib
import json
import os
import shutil
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Pemetaan aset statis: (relatif terhadap FORGE root, relatif terhadap proyek target, kondisi profil)
# Profil yang didukung: "all", "fe", "be", "db"
ASSET_MANIFEST = [
    # /edeate references (Wajib semua proyek)
    ("blueprints/references/dual_track_protocol.md", ".agents/skills/project-edeate/references/dual_track_protocol.md", "all"),
    ("blueprints/references/ticket_variants.md", ".agents/skills/project-edeate/references/ticket_variants.md", "all"),
    ("blueprints/references/anti_patterns.md", ".agents/skills/project-edeate/references/anti_patterns.md", "all"),

    # /plan references (Khusus proyek dengan DB)
    ("blueprints/references/database_design_checklist.md", ".agents/skills/project-plan/references/database_design_checklist.md", "db"),

    # /audit references & scripts (Wajib semua proyek)
    ("blueprints/references/audit_handoff_package.md", ".agents/skills/project-audit/references/audit_handoff_package.md", "all"),
    ("skills/forge-constitution/scripts/classify_blast_radius.py", ".agents/skills/project-audit/scripts/classify_blast_radius.py", "all"),

    # /audit FE/Fullstack assets
    ("blueprints/references/audit_visual_gate.md", ".agents/skills/project-audit/references/audit_visual_gate.md", "fe"),
    ("skills/forge-constitution/scripts/finish_lint.py", ".agents/skills/project-audit/scripts/finish_lint.py", "fe"),
    ("skills/forge-constitution/scripts/state_matrix_checker.py", ".agents/skills/project-audit/scripts/state_matrix_checker.py", "fe"),

    # /audit BE/Fullstack assets (OpenAPI Gate)
    ("blueprints/references/audit_api_checklist.md", ".agents/skills/project-audit/references/audit_api_checklist.md", "be"),
    ("skills/forge-constitution/scripts/api_linter.py", ".agents/skills/project-audit/scripts/api_linter.py", "be"),
    ("skills/forge-constitution/scripts/breaking_change_detector.py", ".agents/skills/project-audit/scripts/breaking_change_detector.py", "be"),
    ("skills/forge-constitution/scripts/api_scorecard.py", ".agents/skills/project-audit/scripts/api_scorecard.py", "be"),

    # /ship scripts (Wajib semua proyek)
    ("skills/forge-constitution/scripts/changelog_generator.py", ".agents/skills/project-ship/scripts/changelog_generator.py", "all"),

    # /prototype FE/Fullstack assets
    ("blueprints/references/anti_slop_design_guide.md", ".agents/skills/project-prototype/references/anti_slop_design_guide.md", "fe"),
    ("skills/forge-constitution/scripts/design_token_generator.py", ".agents/skills/project-prototype/scripts/design_token_generator.py", "fe"),
    ("skills/forge-constitution/scripts/finish_lint.py", ".agents/skills/project-prototype/scripts/finish_lint.py", "fe"),
    ("skills/forge-constitution/scripts/state_matrix_checker.py", ".agents/skills/project-prototype/scripts/state_matrix_checker.py", "fe"),
]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def active_tags(profile, has_db):
    tags = {"all"}
    if profile == "fe":
        tags.add("fe")
    elif profile == "be":
        tags.add("be")
        tags.add("db")
    elif profile == "fullstack":
        tags.update({"fe", "be", "db"})
    if has_db:
        tags.add("db")
    return tags


def copy_assets(forge_root, target_root, profile, has_db, dry_run=False):
    tags = active_tags(profile, has_db)
    results = []
    errors = []

    for src_rel, dst_rel, tag in ASSET_MANIFEST:
        if tag not in tags:
            continue
        src = os.path.join(forge_root, src_rel)
        dst = os.path.join(target_root, dst_rel)

        if not os.path.isfile(src):
            errors.append(f"SOURCE_NOT_FOUND: {src}")
            continue

        src_hash = sha256_file(src)
        if dry_run:
            results.append({"file": dst_rel, "status": "DRY_RUN", "sha256": src_hash[:16]})
            continue

        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        dst_hash = sha256_file(dst)

        if src_hash != dst_hash:
            errors.append(f"SHA256_MISMATCH: {dst_rel}")
        else:
            results.append({"file": dst_rel, "status": "SHA256_VERIFIED", "bytes": os.path.getsize(dst), "sha256": dst_hash[:16]})

    # Salin juga folder opsional blueprints/references/upstream/ ke /prototype jika ada (profil FE/Fullstack)
    upstream_dir = os.path.join(forge_root, "blueprints", "references", "upstream")
    if "fe" in tags and os.path.isdir(upstream_dir):
        for fname in sorted(os.listdir(upstream_dir)):
            src = os.path.join(upstream_dir, fname)
            if not os.path.isfile(src):
                continue
            dst_rel = f".agents/skills/project-prototype/references/upstream/{fname}"
            dst = os.path.join(target_root, dst_rel)
            src_hash = sha256_file(src)
            if dry_run:
                results.append({"file": dst_rel, "status": "DRY_RUN", "sha256": src_hash[:16]})
                continue
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            dst_hash = sha256_file(dst)
            if src_hash != dst_hash:
                errors.append(f"SHA256_MISMATCH: {dst_rel}")
            else:
                results.append({"file": dst_rel, "status": "SHA256_VERIFIED", "bytes": os.path.getsize(dst), "sha256": dst_hash[:16]})

    return {"ok": len(errors) == 0, "profile": profile, "copied": len(results), "results": results, "errors": errors}


def main():
    parser = argparse.ArgumentParser(description="Lossless SHA-256 verified copier for FORGE static references & scripts.")
    parser.add_argument("--forge-root", default=os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")),
                        help="Path ke root direktori repositori FORGE global")
    parser.add_argument("--target-root", required=True, help="Path ke root direktori proyek target")
    parser.add_argument("--profile", choices=["fe", "be", "fullstack", "minimal"], required=True,
                        help="Profil stack proyek: fe (Frontend statis), be (Pure Backend), fullstack, atau minimal")
    parser.add_argument("--has-db", action="store_true", help="Paksa salin checklist DB (otomatis aktif pada be/fullstack)")
    parser.add_argument("--dry-run", action="store_true", help="Pratinjau daftar file yang akan disalin tanpa menulis ke disk")
    parser.add_argument("--json", action="store_true", help="Output dalam format JSON")
    args = parser.parse_args()

    report = copy_assets(args.forge_root, args.target_root, args.profile, args.has_db, args.dry_run)

    if args.json:
        print(json.dumps(report, indent=2))
        sys.exit(0 if report["ok"] else 1)

    status_label = "✅ 100% LOSSLESS SHA-256 VERIFIED" if report["ok"] else "❌ GAGAL / MISMATCH"
    print(f"**Vonis Penyalinan Aset Statis ({args.profile.upper()}): {status_label}**")
    print(f"- Total Berkas Diproses: {report['copied']}\n")
    for item in report["results"]:
        print(f"  - [{item['status']}] `{item['file']}` (sha256: `{item['sha256']}...`)")
    if report["errors"]:
        print("\n🚨 **Errors:**")
        for err in report["errors"]:
            print(f"  - {err}")
    sys.exit(0 if report["ok"] else 1)


if __name__ == "__main__":
    main()
