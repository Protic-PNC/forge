#!/usr/bin/env python3
"""
check_upstream.py
Deterministik Upstream Drift Detector & Lossless Updater untuk Maintainer FORGE.
Pure Python Standard Library (0 pip install).

Fitur:
- Membandingkan seluruh aset lossless di upstream_lock.json terhadap raw.githubusercontent.com
  tanpa terkena batas GitHub JSON API rate limit (60 req/jam).
- Cerdas menghadapi perbedaan line-ending Windows (CRLF) vs GitHub (LF) agar tidak false alarm.
- Otomatis menjalankan 2 Safety Gate untuk calon pembaruan skrip Python:
  1. AST Stdlib Guard: memblokir import non-stdlib demi menjaga prinsip 0 pip install.
  2. CLI Smoke & Flag Regression Check: menguji --help di file temp & memastikan required_flags utuh.
- Menulis pembaruan 100% byte-for-byte lossless saat --apply dijalankan dengan verifikasi SHA-256.

Contoh Pemakaian:
  python .agents/skills/upstream-sync/scripts/check_upstream.py --check
  python .agents/skills/upstream-sync/scripts/check_upstream.py --diff blader_humanizer
  python .agents/skills/upstream-sync/scripts/check_upstream.py --apply blader_humanizer
"""

import argparse
import ast
import datetime
import difflib
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_LOCKFILE = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "upstream_lock.json"))
DEFAULT_FORGE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "..", ".."))


def raw_github_url(asset):
    return (
        f"https://raw.githubusercontent.com/"
        f"{asset['repo']}/{asset['branch']}/{asset['upstream_path']}"
    )


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def normalize_eol(data):
    return data.replace(b"\r\n", b"\n")


def fetch_upstream_bytes(url, timeout=15):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "FORGE-Upstream-Sync/1.0",
            "Cache-Control": "no-cache",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read(), None
    except urllib.error.HTTPError as e:
        return None, f"HTTP_{e.code}"
    except urllib.error.URLError as e:
        return None, f"NETWORK_ERROR: {e.reason}"
    except Exception as e:
        return None, f"FETCH_ERROR: {e}"


def get_stdlib_names():
    if hasattr(sys, "stdlib_module_names"):
        return set(sys.stdlib_module_names) | set(sys.builtin_module_names) | {"__future__"}
    # Fallback untuk Python 3.8/3.9
    return set(sys.builtin_module_names) | {
        "__future__", "abc", "argparse", "ast", "base64", "collections", "contextlib",
        "copy", "csv", "dataclasses", "datetime", "difflib", "enum", "fnmatch",
        "functools", "glob", "hashlib", "http", "importlib", "inspect", "io",
        "itertools", "json", "logging", "math", "os", "pathlib", "re", "shutil",
        "signal", "socket", "statistics", "string", "subprocess", "sys", "tempfile",
        "textwrap", "threading", "time", "typing", "unicodedata", "urllib", "uuid",
        "warnings", "xml", "zipfile",
    }


def run_python_safety_gates(raw_bytes, required_flags):
    """Jalankan AST Stdlib Guard + CLI --help & required_flags Regression Check."""
    report = {
        "syntax_ok": False,
        "stdlib_ok": False,
        "non_stdlib_imports": [],
        "cli_help_ok": False,
        "missing_flags": [],
        "errors": [],
    }
    try:
        source = raw_bytes.decode("utf-8")
    except UnicodeDecodeError as e:
        report["errors"].append(f"UTF8_DECODE_ERROR: {e}")
        return report

    try:
        tree = ast.parse(source)
        report["syntax_ok"] = True
    except SyntaxError as e:
        report["errors"].append(f"SYNTAX_ERROR: {e}")
        return report

    stdlib = get_stdlib_names()
    non_stdlib = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root_mod = alias.name.split(".")[0]
                if root_mod not in stdlib:
                    non_stdlib.add(root_mod)
        elif isinstance(node, ast.ImportFrom):
            if node.level == 0 and node.module:
                root_mod = node.module.split(".")[0]
                if root_mod not in stdlib:
                    non_stdlib.add(root_mod)

    report["non_stdlib_imports"] = sorted(non_stdlib)
    report["stdlib_ok"] = len(non_stdlib) == 0
    if not report["stdlib_ok"]:
        report["errors"].append(f"NON_STDLIB_IMPORTS: {', '.join(report['non_stdlib_imports'])}")

    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(mode="wb", suffix=".py", delete=False) as tf:
            tf.write(raw_bytes)
            tmp_path = tf.name
        proc = subprocess.run(
            [sys.executable, tmp_path, "--help"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
        )
        help_text = (proc.stdout or "") + "\n" + (proc.stderr or "")
        report["cli_help_ok"] = proc.returncode == 0
        if not report["cli_help_ok"]:
            report["errors"].append(f"CLI_HELP_FAILED (exit={proc.returncode})")
        missing = [flag for flag in required_flags if flag not in help_text]
        report["missing_flags"] = missing
        if missing:
            report["errors"].append(f"MISSING_REQUIRED_FLAGS: {', '.join(missing)}")
    except subprocess.TimeoutExpired:
        report["errors"].append("CLI_HELP_TIMEOUT (>10s)")
    except Exception as e:
        report["errors"].append(f"CLI_SMOKE_ERROR: {e}")
    finally:
        if tmp_path and os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except OSError:
                pass

    return report


def compute_diff_stats(local_bytes, upstream_bytes, local_label, upstream_label):
    local_lines = normalize_eol(local_bytes).decode("utf-8", errors="replace").splitlines(keepends=True)
    up_lines = normalize_eol(upstream_bytes).decode("utf-8", errors="replace").splitlines(keepends=True)
    diff_lines = list(
        difflib.unified_diff(local_lines, up_lines, fromfile=local_label, tofile=upstream_label, n=3)
    )
    added = sum(1 for ln in diff_lines if ln.startswith("+") and not ln.startswith("+++"))
    removed = sum(1 for ln in diff_lines if ln.startswith("-") and not ln.startswith("---"))
    return added, removed, "".join(diff_lines)


def inspect_asset(asset, forge_root, include_diff=False):
    local_abs = os.path.join(forge_root, asset["local_path"])
    url = raw_github_url(asset)
    res = {
        "id": asset["id"],
        "asset_type": asset["asset_type"],
        "local_path": asset["local_path"],
        "url": url,
        "status": "UNKNOWN",
        "local_sha256": None,
        "upstream_sha256": None,
        "lock_sha256": asset.get("local_sha256"),
        "local_drift": False,
        "added_lines": 0,
        "removed_lines": 0,
        "safety_gates": None,
        "error": None,
    }

    if not os.path.isfile(local_abs):
        res["status"] = "LOCAL_MISSING"
        res["error"] = f"Local file not found: {local_abs}"
        return res, None

    with open(local_abs, "rb") as f:
        local_bytes = f.read()

    local_hash = sha256_bytes(local_bytes)
    local_norm_hash = sha256_bytes(normalize_eol(local_bytes))
    res["local_sha256"] = local_hash

    lock_hash = asset.get("local_sha256")
    if lock_hash and local_hash != lock_hash:
        # Bisa jadi EOL lokal berubah akibat git autocrlf; cek dengan upstream nanti
        res["local_drift"] = True

    up_bytes, err = fetch_upstream_bytes(url)
    if err:
        res["status"] = "UPSTREAM_404" if err == "HTTP_404" else "FETCH_FAILED"
        res["error"] = err
        return res, None

    up_hash = sha256_bytes(up_bytes)
    up_norm_hash = sha256_bytes(normalize_eol(up_bytes))
    res["upstream_sha256"] = up_hash

    if local_hash == up_hash:
        res["status"] = "UP_TO_DATE"
        res["local_drift"] = False
    elif local_norm_hash == up_norm_hash:
        res["status"] = "UP_TO_DATE_EOL_ONLY"
        res["local_drift"] = False
    else:
        res["status"] = "LOCAL_DRIFT_AND_DIFF" if res["local_drift"] else "UPDATE_AVAILABLE"
        added, removed, diff_text = compute_diff_stats(
            local_bytes, up_bytes, f"local/{asset['local_path']}", f"upstream/{asset['repo']}/{asset['upstream_path']}"
        )
        res["added_lines"] = added
        res["removed_lines"] = removed
        if include_diff:
            res["diff"] = diff_text
        if asset["asset_type"] == "python_stdlib_script":
            res["safety_gates"] = run_python_safety_gates(up_bytes, asset.get("required_flags", []))

    return res, up_bytes


def load_lockfile(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_lockfile(path, data):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def cmd_check(lock_data, forge_root, filter_ids, as_json):
    assets = lock_data["assets"]
    if filter_ids:
        assets = [a for a in assets if a["id"] in filter_ids]
        if not assets:
            print(f"❌ Tidak ada asset id cocok: {filter_ids}", file=sys.stderr)
            return 2

    results = []
    for asset in assets:
        res, _ = inspect_asset(asset, forge_root, include_diff=False)
        results.append(res)

    if as_json:
        print(json.dumps({"checked": len(results), "results": results}, indent=2))
        return 0

    up_to_date = sum(1 for r in results if r["status"] in ("UP_TO_DATE", "UP_TO_DATE_EOL_ONLY"))
    updates = [r for r in results if r["status"] in ("UPDATE_AVAILABLE", "LOCAL_DRIFT_AND_DIFF")]
    failures = [r for r in results if r["status"] in ("UPSTREAM_404", "FETCH_FAILED", "LOCAL_MISSING")]

    print(f"## 🔍 Laporan Audit Upstream FORGE ({len(results)} Aset Terpantau)")
    print(f"- ✅ Up-to-Date: **{up_to_date}** | 🔄 Update Tersedia: **{len(updates)}** | ❌ Error/404: **{len(failures)}**\n")
    print("| Asset ID | Jenis | Status | Delta | Safety Gate (Python) |")
    print("| :--- | :--- | :--- | :---: | :--- |")

    icons = {
        "UP_TO_DATE": "✅ UP-TO-DATE",
        "UP_TO_DATE_EOL_ONLY": "✅ UP-TO-DATE (EOL)",
        "UPDATE_AVAILABLE": "🔄 UPDATE AVAILABLE",
        "LOCAL_DRIFT_AND_DIFF": "⚠️ LOCAL DRIFT + DIFF",
        "UPSTREAM_404": "❌ UPSTREAM 404",
        "FETCH_FAILED": "❌ FETCH FAILED",
        "LOCAL_MISSING": "❌ LOCAL MISSING",
    }

    for r in results:
        status_str = icons.get(r["status"], r["status"])
        delta = f"`+{r['added_lines']}/-{r['removed_lines']}`" if r["status"] in ("UPDATE_AVAILABLE", "LOCAL_DRIFT_AND_DIFF") else "—"
        if r["error"]:
            gate_str = f"`{r['error']}`"
        elif r["safety_gates"]:
            sg = r["safety_gates"]
            if sg["errors"]:
                gate_str = "🚨 " + "; ".join(sg["errors"])
            else:
                gate_str = "✅ Stdlib + `--help` + Flags OK"
        elif r["asset_type"] == "markdown_reference" and r["status"] in ("UPDATE_AVAILABLE", "LOCAL_DRIFT_AND_DIFF"):
            gate_str = "🔎 Wajib Review Diff Prompt"
        else:
            gate_str = "—"
        print(f"| `{r['id']}` | `{r['asset_type']}` | {status_str} | {delta} | {gate_str} |")

    if updates:
        print("\n💡 Jalankan `--diff <asset_id>` untuk mengaudit perubahan sebelum menyetujui `--apply <asset_id>`.")
    return 1 if failures else 0


def cmd_diff(lock_data, forge_root, asset_id):
    matches = [a for a in lock_data["assets"] if a["id"] == asset_id]
    if not matches:
        print(f"❌ Asset ID tidak ditemukan di upstream_lock.json: {asset_id}", file=sys.stderr)
        return 2
    res, _ = inspect_asset(matches[0], forge_root, include_diff=True)
    if res["status"] in ("UP_TO_DATE", "UP_TO_DATE_EOL_ONLY"):
        print(f"✅ `{asset_id}` sudah 100% identik dengan upstream ({res['url']}). Tidak ada diff.")
        return 0
    if res["error"]:
        print(f"❌ Gagal mengambil upstream untuk `{asset_id}`: {res['error']}", file=sys.stderr)
        return 1

    print(f"### 🔎 Unified Diff: `{asset_id}` (`+{res['added_lines']}/-{res['removed_lines']}`)")
    print(f"- Sumber: {res['url']}")
    print(f"- Digunakan di: {', '.join(matches[0].get('used_by_blueprints', []))}")
    if res["safety_gates"]:
        sg = res["safety_gates"]
        verdict = "✅ LOLOS" if not sg["errors"] else "🚨 DIBLOKIR: " + "; ".join(sg["errors"])
        print(f"- Safety Gate Python: {verdict}")
    print("\n```diff")
    print(res.get("diff", "").rstrip())
    print("```")
    return 0


def cmd_apply(lock_data, lock_path, forge_root, target_ids, allow_non_stdlib, force_local_drift):
    if target_ids == ["all"]:
        targets = lock_data["assets"]
    else:
        id_set = set(target_ids)
        targets = [a for a in lock_data["assets"] if a["id"] in id_set]
        missing = id_set - {a["id"] for a in targets}
        if missing:
            print(f"❌ Asset ID tidak dikenal: {sorted(missing)}", file=sys.stderr)
            return 2

    applied_count = 0
    blocked_count = 0
    today = datetime.date.today().isoformat()

    for asset in targets:
        res, up_bytes = inspect_asset(asset, forge_root, include_diff=False)
        aid = asset["id"]

        if res["status"] in ("UP_TO_DATE", "UP_TO_DATE_EOL_ONLY"):
            print(f"⏭️  [{aid}] Sudah up-to-date, dilewati.")
            continue
        if res["error"] or up_bytes is None:
            print(f"❌ [{aid}] Gagal fetch upstream ({res['error']}).")
            blocked_count += 1
            continue
        if res["status"] == "LOCAL_DRIFT_AND_DIFF" and not force_local_drift:
            print(f"🚨 [{aid}] DIBLOKIR: File lokal memiliki perubahan lokal di luar lockfile. Gunakan --force-local-drift jika yakin ingin menimpa.")
            blocked_count += 1
            continue

        if asset["asset_type"] == "python_stdlib_script" and res["safety_gates"]:
            sg = res["safety_gates"]
            if not sg["syntax_ok"] or not sg["cli_help_ok"] or sg["missing_flags"]:
                print(f"🚨 [{aid}] DIBLOKIR oleh Safety Gate: {'; '.join(sg['errors'])}")
                blocked_count += 1
                continue
            if not sg["stdlib_ok"] and not allow_non_stdlib:
                print(f"🚨 [{aid}] DIBLOKIR oleh AST Stdlib Guard (import eksternal: {sg['non_stdlib_imports']}).")
                blocked_count += 1
                continue

        dst = os.path.join(forge_root, asset["local_path"])
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "wb") as f:
            f.write(up_bytes)

        written_hash = sha256_bytes(open(dst, "rb").read())
        if written_hash != res["upstream_sha256"]:
            print(f"❌ [{aid}] SHA-256 MISMATCH pasca tulis!")
            blocked_count += 1
            continue

        asset["local_sha256"] = written_hash
        asset["last_synced_at"] = today
        applied_count += 1
        print(f"✅ [{aid}] 100% LOSSLESS UPDATED -> `{asset['local_path']}` (sha256: `{written_hash[:16]}...`, `+{res['added_lines']}/-{res['removed_lines']}`)")

    if applied_count > 0:
        save_lockfile(lock_path, lock_data)
        print(f"\n📦 `upstream_lock.json` diperbarui ({applied_count} aset disinkronkan).")
    return 1 if blocked_count > 0 else 0


def main():
    parser = argparse.ArgumentParser(
        description="FORGE Maintainer Tool: Cek & sinkronisasi lossless aset upstream GitHub."
    )
    parser.add_argument("--lockfile", default=DEFAULT_LOCKFILE, help="Path ke upstream_lock.json")
    parser.add_argument("--forge-root", default=DEFAULT_FORGE_ROOT, help="Path ke root repo FORGE")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Mode Read-Only: cek seluruh aset upstream (default)")
    mode.add_argument("--diff", metavar="ASSET_ID", help="Mode Read-Only: tampilkan unified diff untuk 1 aset")
    mode.add_argument("--apply", nargs="+", metavar="ASSET_ID", help="Terapkan update lossless untuk ID tertentu atau 'all'")
    parser.add_argument("--id", nargs="+", help="Filter asset ID tertentu pada mode --check")
    parser.add_argument("--json", action="store_true", help="Output JSON pada mode --check")
    parser.add_argument("--allow-non-stdlib", action="store_true", help="Override AST Stdlib Guard saat --apply (TIDAK DISARANKAN)")
    parser.add_argument("--force-local-drift", action="store_true", help="Izinkan menimpa file lokal yang punya local drift")
    args = parser.parse_args()

    if not os.path.isfile(args.lockfile):
        print(f"❌ Lockfile tidak ditemukan: {args.lockfile}", file=sys.stderr)
        sys.exit(2)

    lock_data = load_lockfile(args.lockfile)

    if args.diff:
        sys.exit(cmd_diff(lock_data, args.forge_root, args.diff))
    elif args.apply:
        sys.exit(
            cmd_apply(
                lock_data,
                args.lockfile,
                args.forge_root,
                args.apply,
                args.allow_non_stdlib,
                args.force_local_drift,
            )
        )
    else:
        sys.exit(cmd_check(lock_data, args.forge_root, args.id, args.json))


if __name__ == "__main__":
    main()
