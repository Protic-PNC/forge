#!/usr/bin/env python3
"""
validate_manifest.py
Deterministik Manifest & DNA Vault Validator (Stdlib Only)
Bagian dari FORGE Constitution Engine - Standard Library murni (sys, os, json).

Kegunaan:
Memvalidasi integritas brankas fisik `.agents/forge_manifest.json`:
1. Sintaks validitas JSON murni.
2. Keberadaan root keys wajib (`forge_version`, `project_name`, `dna`, `directives`).
3. Kelengkapan variabel DNA kunci proyek.
4. Verifikasi keberadaan file fisik konstitusi di folder `.agents/rules/`.
"""

import sys
import os
import json

REQUIRED_ROOT_KEYS = ['forge_version', 'project_name', 'dna', 'directives']

REQUIRED_DNA_KEYS = [
    'BUSINESS_DOMAIN_SUMMARY',
    'TECH_STACK_SUMMARY',
    'SYSTEM_ARCHITECTURE_APPROACH',
    'TDD_STRICTNESS_DECISION',
    'CODE_AUDIT_STRICTNESS_DECISION'
]

CORE_CONSTITUTION_FILES = [
    'ARCHITECTURE.md',
    'MASTER_RULES.md',
    'META_RULES.md',
    'GIT_WORKFLOW.md'
]


def find_manifest(target_path=None):
    if target_path and os.path.isfile(target_path):
        return os.path.abspath(target_path)
    
    # Lokasi standar
    candidates = [
        os.path.join(os.getcwd(), '.agents', 'forge_manifest.json'),
        os.path.join(os.getcwd(), 'forge_manifest.json')
    ]
    for c in candidates:
        if os.path.isfile(c):
            return c
    return None


def validate_manifest(manifest_path):
    issues = []
    warnings = []

    if not manifest_path or not os.path.isfile(manifest_path):
        return {
            "valid": False,
            "error": "Berkas manifest tidak ditemukan. Jalankan /forge-constitution untuk inisialisasi DNA proyek.",
            "issues": ["MANIFEST_NOT_FOUND"],
            "warnings": []
        }

    # 1. Parse JSON
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return {
            "valid": False,
            "error": f"Sintaks JSON korup: {e}",
            "issues": [f"JSON_SYNTAX_ERROR: {e}"],
            "warnings": []
        }
    except Exception as e:
        return {
            "valid": False,
            "error": f"Gagal membaca file: {e}",
            "issues": [f"IO_ERROR: {e}"],
            "warnings": []
        }

    # 2. Periksa Root Keys
    for key in REQUIRED_ROOT_KEYS:
        if key not in data:
            issues.append(f"Missing root key: '{key}'")

    # 3. Periksa DNA Keys
    dna = data.get('dna', {})
    if not isinstance(dna, dict):
        issues.append("'dna' field harus berupa object/dictionary")
    else:
        for k in REQUIRED_DNA_KEYS:
            val = dna.get(k, '')
            if not val or not str(val).strip():
                issues.append(f"Missing or empty DNA key: '{k}'")

    # 4. Verifikasi Berkas Fisik Konstitusi di Disk
    manifest_dir = os.path.dirname(manifest_path)
    agents_dir = manifest_dir if os.path.basename(manifest_dir) == '.agents' else os.path.join(os.path.dirname(manifest_path), '.agents')
    rules_dir = os.path.join(agents_dir, 'rules')

    existing_rules = []
    missing_rules = []
    if os.path.isdir(rules_dir):
        for rule_file in CORE_CONSTITUTION_FILES:
            full_path = os.path.join(rules_dir, rule_file)
            if os.path.isfile(full_path):
                existing_rules.append(rule_file)
            else:
                missing_rules.append(rule_file)
    else:
        warnings.append(f"Direktori konstitusi fisik belum terdeteksi di '{rules_dir}'.")

    if missing_rules:
        warnings.append(f"Berkas aturan konstitusi belum lengkap di disk: {', '.join(missing_rules)}")

    is_valid = len(issues) == 0

    return {
        "valid": is_valid,
        "manifest_path": manifest_path,
        "forge_version": data.get('forge_version', 'Unknown'),
        "project_name": data.get('project_name', 'Unnamed'),
        "dna_count": len(dna) if isinstance(dna, dict) else 0,
        "directives_count": len(data.get('directives', {})) if isinstance(data.get('directives', dict), dict) else 0,
        "issues": issues,
        "warnings": warnings,
        "existing_rules": existing_rules,
        "missing_rules": missing_rules
    }


def main():
    target_path = None
    as_json = '--json' in sys.argv

    for arg in sys.argv[1:]:
        if not arg.startswith('--'):
            target_path = arg
            break

    manifest_file = find_manifest(target_path)
    result = validate_manifest(manifest_file)

    if as_json:
        print(json.dumps(result, indent=2))
        sys.exit(0 if result['valid'] else 1)

    # Output Bottom Line First!
    if result['valid']:
        print(f"**Vonis Integritas DNA: ✅ VALID (Grade A - Siap Operasional)**")
        print(f"Proyek: **{result['project_name']}** (FORGE v{result['forge_version']})\n")
        print(f"- Path Manifest: `{result['manifest_path']}`")
        print(f"- Total Entri DNA: {result['dna_count']} variabel")
        print(f"- Total Directives: {result['directives_count']} direktif")
        if result['existing_rules']:
            print(f"- Berkas Konstitusi Terverifikasi: {', '.join(result['existing_rules'])}")
        if result['warnings']:
            print("\n⚠️ **Catatan Peringatan:**")
            for w in result['warnings']:
                print(f"  - {w}")
        sys.exit(0)
    else:
        print(f"**Vonis Integritas DNA: ❌ INVALID / INTEGRITAS CACAT**\n")
        if 'error' in result:
            print(f"Error: {result['error']}\n")
        if result['issues']:
            print("🚨 **Daftar Isu yang Wajib Diperbaiki:**")
            for iss in result['issues']:
                print(f"  - {iss}")
        sys.exit(1)


if __name__ == '__main__':
    main()
