"""Phase 7C preservation and implementation invariants."""
from pathlib import Path
import hashlib, json

ROOT=Path(__file__).resolve().parents[1]
EXPECTED={
 'data/topics.json':'e331cf2db49785e6a0627a6a34908da7c5d5e69e5ba90fc41b89018421239363',
 'data/formulas.json':'bbe8de88ae0b2d7d3b157707a6e0945ebceca70a235d8403d9ca66abb4169b19',
 'data/problems.json':'ec8ac8dfcc3f251c68ef36b4e8f87f19189c43122b25466cac7719005c82ade4',
 'data/exam_priority.json':'aa012056441d6b63d749e968956fa9d3606fd84659eb71395e6c76b7f2026b76',
 'data/p1_traceability.json':'46b2709f48789346bae05e0d3e4038accfe85fef7264cd4bc55c6f5b4b672226',
}
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
for rel,digest in EXPECTED.items():
 path=ROOT/rel
 assert path.exists(),rel
 assert sha(path)==digest,f'Phase 7C changed protected educational data: {rel}'
topics=json.loads((ROOT/'data/topics.json').read_text(encoding='utf-8'))['topics']
formulas=json.loads((ROOT/'data/formulas.json').read_text(encoding='utf-8'))['formulas']
problems=json.loads((ROOT/'data/problems.json').read_text(encoding='utf-8'))['problems']
priority=json.loads((ROOT/'data/exam_priority.json').read_text(encoding='utf-8'))['items']
trace=json.loads((ROOT/'data/p1_traceability.json').read_text(encoding='utf-8'))['items']
assert (len(topics),len(formulas),len(problems),len(priority),len(trace))==(18,23,65,20,20)
assert sum(p['difficulty']=='easy' for p in problems)==20
assert sum(p['difficulty']=='medium' for p in problems)==29
assert sum(p['difficulty']=='hard' for p in problems)==16
manifest=json.loads((ROOT/'backups/phase-7c/backup_manifest.json').read_text(encoding='utf-8'))
assert manifest['files'] and all(item['backup_verified'] for item in manifest['files'])
for item in manifest['files']:
 backup=ROOT/item['backup_file_path']
 assert backup.exists() and sha(backup)==item['sha256']
storage=(ROOT/'web/src/storage.ts').read_text(encoding='utf-8')
assert "phychem-study-v1" in storage
for rel in ['web/src/analytics/index.ts','web/src/analytics/mastery.ts','web/src/mockEngine.ts','web/src/Phase7C.tsx']:
 assert (ROOT/rel).exists(),rel
print('Phase 7C validation passed: protected content unchanged; counts, backup, storage key and feature modules verified')
