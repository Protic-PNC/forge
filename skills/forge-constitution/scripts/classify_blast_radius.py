#!/usr/bin/env python3
"""
classify_blast_radius.py
Deterministik Blast-Radius & Tri-Track Routing Classifier (Stdlib Only)
Bagian dari FORGE Constitution Engine - Standard Library murni (sys, os, subprocess, json).

Kegunaan:
Menganalisis file yang dimodifikasi (via git diff atau argumen) dan mengklasifikasikan:
1. Dimensi terdampak: Backend, Frontend UI, Database Schema, Config/Deps.
2. Jalur Four-Tier Audit (Jalur 1: Pure BE, Jalur 2: FE Logic-Only, Jalur 3: Active Visual UI).
"""

import sys
import os
import subprocess
import json

# Pola ekstensi & direktori untuk klasifikasi deterministik
UI_EXTENSIONS = {'.jsx', '.tsx', '.vue', '.svelte', '.html', '.css', '.scss', '.sass', '.less'}
UI_DIRS = {'components', 'views', 'pages', 'ui', 'styles', 'layouts'}

BE_EXTENSIONS = {'.py', '.php', '.java', '.go', '.rs', '.rb', '.cs'}
BE_DIRS = {'api', 'controllers', 'services', 'repositories', 'models', 'routes', 'middlewares', 'handlers'}

DB_PATTERNS = {'migration', 'migrations', 'schema.prisma', 'schema.sql', 'schema.ts', 'drizzle', 'typeorm', 'entity', 'entities'}
CONFIG_PATTERNS = {'package.json', 'package-lock.json', 'pnpm-lock.yaml', 'yarn.lock', 'tsconfig.json', 'composer.json', 'requirements.txt', 'cargo.toml', 'go.mod'}


def get_git_diff_files(base_ref=None):
    """Mengambil daftar file yang berubah via git diff atau git status."""
    try:
        if base_ref:
            cmd = ['git', 'diff', '--name-only', base_ref]
        else:
            # Bandingkan HEAD, jika gagal (repo kosong / tanpa commit) cek git status
            cmd = ['git', 'diff', '--name-only', 'HEAD']
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
        files = [line.strip() for line in res.stdout.splitlines() if line.strip()]
        
        # Tambahkan juga untracked files yang relevan
        status_cmd = ['git', 'status', '--porcelain']
        status_res = subprocess.run(status_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
        for line in status_res.stdout.splitlines():
            line = line.strip()
            if line.startswith('??'):
                file_path = line[3:].strip()
                if file_path not in files:
                    files.append(file_path)
        return files
    except Exception as e:
        sys.stderr.write(f"Warning: gagal menjalankan git ({e}). Menggunakan argumen CLI jika ada.\n")
        return []


def classify_files(file_list):
    ui_files = []
    be_files = []
    db_files = []
    config_files = []
    other_files = []

    for f in file_list:
        normalized = f.replace('\\', '/').lower()
        parts = normalized.split('/')
        filename = parts[-1]
        _, ext = os.path.splitext(filename)

        is_categorized = False

        # Cek Database
        if any(db_kw in normalized for db_kw in DB_PATTERNS):
            db_files.append(f)
            is_categorized = True

        # Cek Config
        if filename in CONFIG_PATTERNS or any(normalized.endswith(cfg) for cfg in CONFIG_PATTERNS):
            config_files.append(f)
            is_categorized = True

        # Cek UI
        if ext in UI_EXTENSIONS or any(ui_dir in parts for ui_dir in UI_DIRS):
            ui_files.append(f)
            is_categorized = True

        # Cek Backend
        if ext in BE_EXTENSIONS or any(be_dir in parts for be_dir in BE_DIRS):
            be_files.append(f)
            is_categorized = True

        if not is_categorized:
            # Fallback untuk ts/js
            if ext in {'.ts', '.js'}:
                if any(kw in normalized for kw in ['hook', 'context', 'store', 'view', 'component']):
                    ui_files.append(f)
                else:
                    be_files.append(f)
            else:
                other_files.append(f)

    # Tentukan Jalur Audit Tri-Track
    # Jalur 1: Pure Backend (Zero UI Footprint)
    # Jalur 2: Frontend Logic/Refactor (Zero Visual Delta)
    # Jalur 3: Active Visual & Interactive UI
    if len(ui_files) == 0:
        recommended_track = 1
        track_name = "Jalur 1 (Pure Backend - Zero UI Footprint)"
        track_description = "Bypass Tier 4 Playwright. Cukup Tier 1 (Lint), Tier 2 (Test), dan Tier 3 (Build)."
    else:
        # Cek apakah ada ekstensi visual langsung (jsx, tsx, vue, svelte, css, html)
        has_direct_visual = any(os.path.splitext(f.lower())[1] in UI_EXTENSIONS for f in ui_files)
        if has_direct_visual:
            recommended_track = 3
            track_name = "Jalur 3 (Active Visual & Interactive UI)"
            track_description = "Wajib bukti tangkapan layar Playwright (1280x680 & 375x667), uji tabrakan Navbar, dan cek light/dark mode."
        else:
            recommended_track = 2
            track_name = "Jalur 2 (Frontend Refactor / Logic-Only - Zero Visual Delta)"
            track_description = "Static code verification + Human-in-the-Loop Checklist tanpa wajib Playwright visual screenshot."

    return {
        "total_files": len(file_list),
        "recommended_track": recommended_track,
        "track_name": track_name,
        "track_description": track_description,
        "blast_radius": {
            "ui_count": len(ui_files),
            "be_count": len(be_files),
            "db_count": len(db_files),
            "config_count": len(config_files),
            "other_count": len(other_files)
        },
        "breakdown": {
            "ui_files": ui_files,
            "be_files": be_files,
            "db_files": db_files,
            "config_files": config_files,
            "other_files": other_files
        }
    }


def main():
    # Jika ada argumen path/file yang dioper via CLI
    cli_files = [arg for arg in sys.argv[1:] if not arg.startswith('--')]
    as_json = '--json' in sys.argv

    if cli_files:
        files = cli_files
    else:
        files = get_git_diff_files()

    analysis = classify_files(files)

    if as_json:
        print(json.dumps(analysis, indent=2))
        return

    # Output Markdown Ramah Mentor (Bottom Line First!)
    print(f"**Vonis Jalur Audit: {analysis['track_name']}**")
    print(f"👉 *{analysis['track_description']}*\n")
    print("### 📊 Ringkasan Radius Ledakan (Blast Radius)")
    print(f"- Total Berkas Terdampak: **{analysis['total_files']}**")
    print(f"- Berkas UI: {analysis['blast_radius']['ui_count']}")
    print(f"- Berkas Backend/Logic: {analysis['blast_radius']['be_count']}")
    print(f"- Berkas DB/Migrasi: {analysis['blast_radius']['db_count']}")
    print(f"- Berkas Konfigurasi: {analysis['blast_radius']['config_count']}")
    print()

    if analysis['total_files'] > 0:
        print("### 📁 Rincian Berkas")
        for category, file_items in analysis['breakdown'].items():
            if file_items:
                print(f"**{category.replace('_', ' ').title()}:**")
                for f in file_items:
                    print(f"  - `{f}`")


if __name__ == '__main__':
    main()
