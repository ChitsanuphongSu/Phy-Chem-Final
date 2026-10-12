from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
protected = {
    'data/topics.json':'e331cf2db49785e6a0627a6a34908da7c5d5e69e5ba90fc41b89018421239363',
    'data/formulas.json':'bbe8de88ae0b2d7d3b157707a6e0945ebceca70a235d8403d9ca66abb4169b19',
    'data/problems.json':'ec8ac8dfcc3f251c68ef36b4e8f87f19189c43122b25466cac7719005c82ade4',
    'data/exam_priority.json':'aa012056441d6b63d749e968956fa9d3606fd84659eb71395e6c76b7f2026b76',
    'data/p1_traceability.json':'46b2709f48789346bae05e0d3e4038accfe85fef7264cd4bc55c6f5b4b672226',
}
for rel, digest in protected.items():
    assert sha(ROOT / rel) == digest, f'protected content changed: {rel}'

inventory = json.loads((ROOT / 'data/document_inventory.json').read_text(encoding='utf-8'))
topics = json.loads((ROOT / 'data/topics.json').read_text(encoding='utf-8'))['topics']
formulas = json.loads((ROOT / 'data/formulas.json').read_text(encoding='utf-8'))['formulas']
problems = json.loads((ROOT / 'data/problems.json').read_text(encoding='utf-8'))['problems']
p1 = json.loads((ROOT / 'data/exam_priority.json').read_text(encoding='utf-8'))['items']
assert len(inventory['documents']) == 6
assert (len(topics), len(formulas), len(problems), len(p1)) == (18, 23, 65, 20)
assert sum(x['content_id'].startswith('K-') for x in p1) == 12
assert sum(x['content_id'].startswith('E-') for x in p1) == 8

manifests = sorted((ROOT / 'backups').glob('phase-7e*/backup_manifest.json'))
assert manifests, 'Phase 7E backup manifest missing'
assert any(len(json.loads(p.read_text(encoding='utf-8'))['files']) >= 10 for p in manifests)
for manifest_path in manifests:
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    for item in manifest['files']:
        backup = ROOT / item['backup_file_path']
        assert backup.exists() and sha(backup) == item['sha256'] and item['backup_verified']

assert "phychem-study-v1" in (ROOT / 'web/src/storage.ts').read_text(encoding='utf-8')
required = [
    'web/playwright.config.ts','web/playwright.preview.config.ts','web/e2e/offline.spec.ts',
    'web/public/favicon.svg','reports/phase_7e_baseline.md','reports/phase_7e_environment.md',
    'reports/phase_7e_browser_e2e.md','reports/phase_7e_accessibility.md',
    'reports/phase_7e_responsive.md','reports/phase_7e_dependency_audit.md',
    'reports/phase_7e_offline_behavior.md','reports/phase_7e_data_integrity.md',
    'reports/phase_7e_release_readiness.md','reports/phase_7e_final_report.md',
]
for rel in required:
    assert (ROOT / rel).exists(), rel
print('Phase 7E validation passed: protected data, counts, backups, storage key and release artifacts verified')
