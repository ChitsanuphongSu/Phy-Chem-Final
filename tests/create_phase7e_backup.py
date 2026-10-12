from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[1];base=ROOT/'backups/phase-7e';dest=base
if dest.exists():dest=base.parent/f"phase-7e-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
files=['web/package.json','web/pnpm-lock.yaml','web/vite.config.ts','web/index.html','web/src/App.tsx','web/src/Phase7C.tsx','web/src/ProgressPortability.tsx','web/src/styles.css','README.md','PROJECT_REPORT.md']
now=datetime.now(timezone.utc).isoformat();items=[]
for rel in files:
 src=ROOT/rel;out=dest/rel;out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,out);digest=hashlib.sha256(src.read_bytes()).hexdigest();assert hashlib.sha256(out.read_bytes()).hexdigest()==digest;items.append({'original_file_path':rel,'backup_file_path':out.relative_to(ROOT).as_posix(),'sha256':digest,'file_size_bytes':src.stat().st_size,'backup_creation_timestamp':now,'backup_verified':True})
(dest/'backup_manifest.json').write_text(json.dumps({'phase':'7E','created_at_utc':now,'backup_directory':dest.relative_to(ROOT).as_posix(),'files':items},ensure_ascii=False,indent=2),encoding='utf-8');print(dest)
