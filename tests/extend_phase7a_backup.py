import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(r"D:\Luna\Phy-Chem\physical-chemistry-study-hub")
BACKUP_ROOT = ROOT / "backups" / "phase-7a"
MANIFEST_PATH = BACKUP_ROOT / "backup_manifest.json"
SOURCE = ROOT / "web" / "src" / "data" / "formulas.json"
TARGET = BACKUP_ROOT / "web" / "src" / "data" / "formulas.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
already_recorded = any(
    item["original_file_path"] == "web/src/data/formulas.json" for item in manifest["files"]
)
if already_recorded:
    raise SystemExit("Backup is already recorded; refusing to duplicate it")
if not TARGET.exists():
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE, TARGET)
if digest(SOURCE) != digest(TARGET):
    raise SystemExit("Backup checksum verification failed")

manifest["files"].append(
    {
        "original_file_path": str(SOURCE.relative_to(ROOT)).replace("\\", "/"),
        "backup_file_path": str(TARGET.relative_to(ROOT)).replace("\\", "/"),
        "sha256": digest(SOURCE),
        "file_size_bytes": SOURCE.stat().st_size,
        "backup_creation_timestamp": datetime.now(timezone.utc).isoformat(),
        "backup_verified": True,
    }
)
MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Backed up and verified: {SOURCE.relative_to(ROOT)}")
