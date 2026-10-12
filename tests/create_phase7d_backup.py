from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[1];base=ROOT/'backups/phase-7d';dest=base
if dest.exists():dest=base.parent/f"phase-7d-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
files=['web/src/analytics/mastery.ts','web/src/analytics/index.ts','web/src/analytics/types.ts','web/src/analytics/analytics.test.ts','web/src/storage.ts','web/src/storage.test.ts','web/src/App.tsx','web/src/Phase7C.tsx','web/src/styles.css','README.md','PROJECT_REPORT.md']
items=[];now=datetime.now(timezone.utc).isoformat()
for rel in files:
 src=ROOT/rel;out=dest/rel;out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,out);digest=hashlib.sha256(src.read_bytes()).hexdigest();assert hashlib.sha256(out.read_bytes()).hexdigest()==digest
 items.append({'original_file_path':rel,'backup_file_path':out.relative_to(ROOT).as_posix(),'sha256':digest,'file_size_bytes':src.stat().st_size,'backup_creation_timestamp':now,'backup_verified':True})
manifest={'phase':'7D','created_at_utc':now,'backup_directory':dest.relative_to(ROOT).as_posix(),'files':items};(dest/'backup_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8');print(dest)
