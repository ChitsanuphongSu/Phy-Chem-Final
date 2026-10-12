from __future__ import annotations

import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"D:\Luna\Phy-Chem\physical-chemistry-study-hub")
BASE = ROOT / "backups" / "phase-7a"
FILES = [
    "data/exam_priority.json",
    "data/formulas.json",
    "data/problems.json",
    "data/topics.json",
    "README.md",
    "PROJECT_REPORT.md",
    "tests/validate_project.py",
]


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def unique_target() -> Path:
    if not BASE.exists():
        return BASE
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    candidate = ROOT / "backups" / f"phase-7a-{stamp}"
    index = 1
    while candidate.exists():
        candidate = ROOT / "backups" / f"phase-7a-{stamp}-{index}"
        index += 1
    return candidate


target = unique_target()
target.mkdir(parents=True)
records = []
for relative in FILES:
    source = ROOT / relative
    backup = target / relative
    backup.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, backup)
    original_hash = digest(source)
    backup_hash = digest(backup)
    if original_hash != backup_hash or source.stat().st_size != backup.stat().st_size:
        raise RuntimeError(f"Backup verification failed: {relative}")
    records.append({
        "original_file_path": relative.replace("\\", "/"),
        "backup_file_path": str(backup.relative_to(ROOT)).replace("\\", "/"),
        "sha256": original_hash,
        "file_size_bytes": source.stat().st_size,
        "backup_verified": True,
    })

manifest = {
    "phase": "7A",
    "created_at_utc": datetime.now(timezone.utc).isoformat(),
    "backup_directory": str(target.relative_to(ROOT)).replace("\\", "/"),
    "files": records,
}
(target / "backup_manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
)
print(target)
