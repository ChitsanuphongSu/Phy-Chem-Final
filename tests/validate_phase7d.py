from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
protected={'data/topics.json':'e331cf2db49785e6a0627a6a34908da7c5d5e69e5ba90fc41b89018421239363','data/formulas.json':'bbe8de88ae0b2d7d3b157707a6e0945ebceca70a235d8403d9ca66abb4169b19','data/problems.json':'ec8ac8dfcc3f251c68ef36b4e8f87f19189c43122b25466cac7719005c82ade4','data/exam_priority.json':'aa012056441d6b63d749e968956fa9d3606fd84659eb71395e6c76b7f2026b76','data/p1_traceability.json':'46b2709f48789346bae05e0d3e4038accfe85fef7264cd4bc55c6f5b4b672226'}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for rel,digest in protected.items():assert sha(ROOT/rel)==digest,f'protected content changed: {rel}'
manifest=json.loads((ROOT/'backups/phase-7d/backup_manifest.json').read_text(encoding='utf-8'));assert len(manifest['files'])==11
for item in manifest['files']:
 p=ROOT/item['backup_file_path'];assert p.exists() and sha(p)==item['sha256'] and item['backup_verified']
storage=(ROOT/'web/src/storage.ts').read_text(encoding='utf-8');assert "phychem-study-v1" in storage
for rel in ['web/src/portability.ts','web/src/ProgressPortability.tsx','web/src/portability.test.ts','reports/phase_7d_release_readiness.md'] :assert (ROOT/rel).exists(),rel
print('Phase 7D validation passed: protected data, backup integrity, storage key and release artifacts verified')
