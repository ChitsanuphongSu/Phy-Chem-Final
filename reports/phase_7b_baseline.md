# Phase 7B Baseline

วันที่ตรวจ: 12 ตุลาคม 2026

## Current authoritative counts

| Entity | Count |
|---|---:|
| Topics/lessons | 18 |
| Formulas | 23 |
| Problems | 11 |
| Confirmed P1 records | 20 |

## Existing problem distribution

| Dimension | Distribution |
|---|---|
| Difficulty | Easy 3, Medium 6, Hard 2 |
| Grading type | Numerical 10, Conceptual 1, Multiple-choice 0 |

Existing IDs preserved: `P-K-001`–`P-K-005` and `P-E-001`–`P-E-006`.

## Architecture observations

- Canonical content is in project-level `data/*.json` and copied to `web/src/data/` for bundling.
- `Problem.type` currently controls deterministic grading; richer pedagogical formats are not represented separately.
- Practice and Mock Exam originally implement numeric tolerance and exact string comparison inline in `App.tsx`.
- Progress is stored under LocalStorage key `phychem-study-v1`; attempts reference stable Problem IDs.
- Phase 7B will preserve legacy records and IDs, add optional metadata, and centralize grading without changing the storage key.

## Backup

Pre-change copies and SHA-256 checksums are recorded in `backups/phase-7b/backup_manifest.json`.
