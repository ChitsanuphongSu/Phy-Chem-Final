from __future__ import annotations
import hashlib,json,shutil
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/'backups/phase-7c'
FILES=['web/src/App.tsx','web/src/main.tsx','web/src/storage.ts','web/src/grading.ts','web/src/types.ts','web/vite.config.ts','web/src/storage.test.ts','web/src/grading.test.ts','web/src/phase7b.test.ts','README.md','PROJECT_REPORT.md']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
target=BASE if not BASE.exists() else ROOT/'backups'/f"phase-7c-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
target.mkdir(parents=True); records=[]
for rel in FILES:
 s=ROOT/rel; d=target/rel; d.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(s,d); assert sha(s)==sha(d)
 records.append({'original_file_path':rel,'backup_file_path':d.relative_to(ROOT).as_posix(),'sha256':sha(s),'file_size_bytes':s.stat().st_size,'backup_creation_timestamp':datetime.now(timezone.utc).isoformat(),'backup_verified':True})
manifest={'phase':'7C','created_at_utc':datetime.now(timezone.utc).isoformat(),'backup_directory':target.relative_to(ROOT).as_posix(),'files':records}
(target/'backup_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(target.relative_to(ROOT).as_posix())
