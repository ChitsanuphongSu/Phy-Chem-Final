import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
manifest_path=ROOT/"backups/phase-7b/backup_manifest.json"
manifest=json.loads(manifest_path.read_text(encoding="utf-8"))
relative="web/vite.config.ts"
source=ROOT/relative
target=ROOT/"backups/phase-7b"/relative
if any(x["original_file_path"]==relative for x in manifest["files"]):
    raise SystemExit("Already backed up")
if target.exists():
    raise SystemExit("Refusing to overwrite backup")
target.parent.mkdir(parents=True,exist_ok=True)
shutil.copy2(source,target)
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert digest(source)==digest(target)
manifest["files"].append({"original_file_path":relative,"backup_file_path":target.relative_to(ROOT).as_posix(),"sha256":digest(source),"file_size_bytes":source.stat().st_size,"backup_creation_timestamp":datetime.now(timezone.utc).isoformat(),"backup_verified":True})
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("Backed up web/vite.config.ts")
