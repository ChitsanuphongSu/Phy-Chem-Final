from __future__ import annotations

import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "backups" / "phase-7b"
FILES = [
    "data/problems.json",
    "data/p1_traceability.json",
    "web/src/data/problems.json",
    "web/src/types.ts",
    "web/src/App.tsx",
    "web/src/styles.css",
    "web/src/storage.ts",
    "web/src/storage.test.ts",
    "web/src/dataIntegrity.test.ts",
    "tests/validate_phase7a.py",
    "README.md",
    "PROJECT_REPORT.md",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def choose_target() -> Path:
    if not BASE.exists():
        return BASE
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    candidate = ROOT / "backups" / f"phase-7b-{stamp}"
    suffix = 1
    while candidate.exists():
        candidate = ROOT / "backups" / f"phase-7b-{stamp}-{suffix}"
        suffix += 1
    return candidate


target = choose_target()
target.mkdir(parents=True)
records = []
for relative in FILES:
    source = ROOT / relative
    backup = target / relative
    backup.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, backup)
    if digest(source) != digest(backup) or source.stat().st_size != backup.stat().st_size:
        raise RuntimeError(f"Backup verification failed: {relative}")
    records.append({
        "original_file_path": relative,
        "backup_file_path": backup.relative_to(ROOT).as_posix(),
        "sha256": digest(source),
        "file_size_bytes": source.stat().st_size,
        "backup_creation_timestamp": datetime.now(timezone.utc).isoformat(),
        "backup_verified": True,
    })

manifest = {
    "phase": "7B",
    "created_at_utc": datetime.now(timezone.utc).isoformat(),
    "backup_directory": target.relative_to(ROOT).as_posix(),
    "files": records,
}
(target / "backup_manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(target.relative_to(ROOT).as_posix())
