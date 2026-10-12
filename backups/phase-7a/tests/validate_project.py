import json
from pathlib import Path

ROOT=Path(r"D:\Luna\Phy-Chem\physical-chemistry-study-hub")
data={name:json.loads((ROOT/'data'/name).read_text(encoding='utf-8')) for name in ['document_inventory.json','topics.json','formulas.json','problems.json','exam_priority.json']}
assert len(data['document_inventory.json']['documents'])==6
primary=[d for d in data['document_inventory.json']['documents'] if d['role']=='primary_instructor']
assert sum(d['page_count'] for d in primary)==300
assert all(p.get('star_detection',{}).get('status') in {'CONFIRMED','NOT_FOUND'} for d in primary for p in d['pages'])
assert len(data['exam_priority.json']['items'])==20
assert all(x['priority']=='P1' and x['evidence_classification']=='CONFIRMED' for x in data['exam_priority.json']['items'])
formula_ids={f['id'] for f in data['formulas.json']['formulas']}
assert all(fid in formula_ids for t in data['topics.json']['topics'] for fid in t['formula_ids'])
assert all(fid in formula_ids for p in data['problems.json']['problems'] for fid in p['related_formula_ids'])
for name in ['01_Complete_Revision','02_Exam_Focus','03_Formula_and_Problems']:
    assert (ROOT/'outputs/slides'/f'{name}.pptx').stat().st_size>10000
    assert (ROOT/'outputs/slides'/f'{name}.pdf').stat().st_size>10000
assert (ROOT/'web/dist/index.html').exists()
print('Project integrity checks passed')
