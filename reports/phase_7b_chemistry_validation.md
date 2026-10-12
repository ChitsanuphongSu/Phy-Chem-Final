# Phase 7B — Chemistry Validation

## Method

Numerical questions were independently recalculated from machine-readable `validation_spec` by `tests/validate_phase7b.py`; tolerance was checked against the recalculated value. Conceptual/MCQ items were checked for source relevance, unambiguous answer, distractor validity, and explicit assumptions.

## Per-question audit

| ID | Type | Validation evidence | Source | Status |
|---|---|---|---|---|
| P-K-006 | numerical-calculation | op=div; expected=0.01 M s^-1; tolerance=1e-05 | PhCh-SC202301 Physical Chemistry Part1.pdf p.94 | VALIDATED |
| P-K-007 | multiple-choice | correct option=B; 4 unique options; distractor explanations verified | PhCh-SC202301 Physical Chemistry Part1.pdf p.94 | VALIDATED |
| P-K-008 | numerical-calculation | op=mul_div; expected=0.004 M s^-1; tolerance=4e-06 | PhCh-SC202301 Physical Chemistry Part1.pdf p.94 | VALIDATED |
| P-K-009 | multiple-choice | correct option=C; 4 unique options; distractor explanations verified | PhCh-SC202301 Physical Chemistry Part1.pdf p.21 | VALIDATED |
| P-K-010 | numerical-calculation | op=product; expected=0.01 M s^-1; tolerance=1e-05 | PhCh-SC202301 Physical Chemistry Part1.pdf p.21 | VALIDATED |
| P-K-011 | numerical-calculation | op=div_square; expected=0.4 M^-1 s^-1; tolerance=0.0004 | PhCh-SC202301 Physical Chemistry Part1.pdf p.26 | VALIDATED |
| P-K-012 | data-table-interpretation | op=div_square; expected=0.45 M^-1 s^-1; tolerance=0.00045 | PhCh-SC202301 Physical Chemistry Part1.pdf p.26 | VALIDATED |
| P-K-013 | multiple-choice | correct option=B; 4 unique options; distractor explanations verified | PhCh-SC202301 Physical Chemistry Part1.pdf p.35 | VALIDATED |
| P-K-014 | numerical-calculation | op=subtract_product; expected=0.5 M; tolerance=0.0005 | PhCh-SC202301 Physical Chemistry Part1.pdf p.31 | VALIDATED |
| P-K-015 | numerical-calculation | op=first_order_conc; expected=0.2744 M; tolerance=0.0003 | PhCh-SC202301 Physical Chemistry Part1.pdf p.42 | VALIDATED |
| P-K-016 | numerical-calculation | op=second_order_conc; expected=0.05 M; tolerance=5e-05 | PhCh-SC202301 Physical Chemistry Part1.pdf p.49 | VALIDATED |
| P-K-017 | data-table-interpretation | op=inverse_linear; expected=0.1111 M; tolerance=0.0002 | PhCh-SC202301 Physical Chemistry Part1.pdf p.49 | VALIDATED |
| P-K-018 | numerical-calculation | op=div; expected=231.0 s; tolerance=0.3 | PhCh-SC202301 Physical Chemistry Part1.pdf p.40 | VALIDATED |
| P-K-019 | numerical-calculation | op=div; expected=15.0 min; tolerance=0.02 | PhCh-SC202301 Physical Chemistry Part1.pdf p.40 | VALIDATED |
| P-K-020 | numerical-calculation | op=div; expected=0.5 ; tolerance=0.001 | PhCh-SC202301 Physical Chemistry Part1.pdf p.40 | VALIDATED |
| P-K-021 | energy-diagram-interpretation | correct option=D; 4 unique options; distractor explanations verified | PhCh-SC202301 Physical Chemistry Part1.pdf p.61 | VALIDATED |
| P-K-022 | energy-diagram-interpretation | op=subtract; expected=50.0 kJ mol^-1; tolerance=0.05 | PhCh-SC202301 Physical Chemistry Part1.pdf p.61 | VALIDATED |
| P-K-023 | energy-diagram-interpretation | principle=อธิบายผลของ catalyst ต่อ energy profile; controlled accepted answers=3 | PhCh-SC202301 Physical Chemistry Part1.pdf p.61 | VALIDATED |
| P-K-024 | energy-diagram-interpretation | op=subtract; expected=90.0 kJ mol^-1; tolerance=0.09 | PhCh-SC202301 Physical Chemistry Part1.pdf p.61 | VALIDATED |
| P-K-025 | multiple-choice | correct option=C; 4 unique options; distractor explanations verified | PhCh-SC202301 Physical Chemistry Part1.pdf p.91 | VALIDATED |
| P-K-026 | numerical-calculation | op=arrhenius; expected=1737.0 s^-1; tolerance=2.0 | PhCh-SC202301 Physical Chemistry Part1.pdf p.91 | VALIDATED |
| P-K-027 | numerical-calculation | op=arrhenius_two_temp; expected=38021.0 J mol^-1; tolerance=60.0 | PhCh-SC202301 Physical Chemistry Part1.pdf p.91 | VALIDATED |
| P-K-028 | reaction-mechanism-analysis | correct option=C; 4 unique options; distractor explanations verified | PhCh-SC202301 Physical Chemistry Part1.pdf p.74 | VALIDATED |
| P-K-029 | reaction-mechanism-analysis | principle=อธิบายข้อจำกัดของการอนุมาน rate law จาก overall reaction; controlled accepted answers=3 | PhCh-SC202301 Physical Chemistry Part1.pdf p.77 | VALIDATED |
| P-K-030 | reaction-mechanism-analysis | correct option=B; 4 unique options; distractor explanations verified | PhCh-SC202301 Physical Chemistry Part1.pdf p.77 | VALIDATED |
| P-K-031 | collision-theory | correct option=D; 4 unique options; distractor explanations verified | PhCh-SC202301 Physical Chemistry Part1.pdf p.162 | VALIDATED |
| P-K-032 | collision-encounter-comparison | principle=อธิบายผลของ physical environment ต่อการชน; controlled accepted answers=3 | PhCh-SC202301 Physical Chemistry Part1.pdf p.162 | VALIDATED |
| P-E-007 | conceptual-graph-interpretation | correct option=B; 4 unique options; distractor explanations verified | PhCh-SC202301 Physical Chemistry Part2.pdf p.18 | VALIDATED |
| P-E-008 | conceptual-graph-interpretation | principle=ตีความกราฟ dielectric constant ภายในช่วงที่ให้; controlled accepted answers=3 | PhCh-SC202301 Physical Chemistry Part2.pdf p.18 | VALIDATED |
| P-E-009 | multiple-choice | correct option=A; 4 unique options; distractor explanations verified | PhCh-SC202301 Physical Chemistry Part2.pdf p.13 | VALIDATED |
| P-E-010 | numerical-calculation | op=reciprocal; expected=0.004 S; tolerance=4e-06 | PhCh-SC202301 Physical Chemistry Part2.pdf p.31 | VALIDATED |
| P-E-011 | numerical-calculation | op=mul_div; expected=75.0 S cm2 mol^-1; tolerance=0.08 | PhCh-SC202301 Physical Chemistry Part2.pdf p.48 | VALIDATED |
| P-E-012 | numerical-calculation | op=product; expected=0.00025 S cm^-1; tolerance=2.5e-07 | PhCh-SC202301 Physical Chemistry Part2.pdf p.34 | VALIDATED |
| P-E-013 | multi-step-calculation | op=agbr_ksp; expected=2.5e-13 ; tolerance=3e-15 | PhCh-SC202301 Physical Chemistry Part2.pdf p.66 | VALIDATED |
| P-E-014 | numerical-calculation | op=div; expected=0.0625 ; tolerance=0.0001 | PhCh-SC202301 Physical Chemistry Part2.pdf p.48 | VALIDATED |
| P-E-015 | multiple-choice | correct option=C; 4 unique options; distractor explanations verified | PhCh-SC202301 Physical Chemistry Part2.pdf p.48 | VALIDATED |
| P-E-016 | numerical-calculation | op=ostwald; expected=1.667e-05 ; tolerance=2e-08 | PhCh-SC202301 Physical Chemistry Part2.pdf p.48 | VALIDATED |
| P-E-017 | multi-step-calculation | op=conductivity_ka; expected=3.205e-05 ; tolerance=4e-08 | PhCh-SC202301 Physical Chemistry Part2.pdf p.48 | VALIDATED |
| P-E-018 | numerical-calculation | op=ionic_strength; expected=0.01 mol L^-1; tolerance=1e-05 | PhCh-SC202301 Physical Chemistry Part2.pdf p.83 | VALIDATED |
| P-E-019 | numerical-calculation | op=ionic_strength; expected=0.06 mol L^-1; tolerance=6e-05 | PhCh-SC202301 Physical Chemistry Part2.pdf p.83 | VALIDATED |
| P-E-020 | multiple-choice | correct option=B; 4 unique options; distractor explanations verified | PhCh-SC202301 Physical Chemistry Part2.pdf p.83 | VALIDATED |
| P-E-021 | numerical-calculation | op=dhll; expected=0.6664 ; tolerance=0.001 | PhCh-SC202301 Physical Chemistry Part2.pdf p.83 | VALIDATED |
| P-E-022 | multi-step-calculation | op=mean_activity_12; expected=0.005953 mol L^-1; tolerance=7e-06 | PhCh-SC202301 Physical Chemistry Part2.pdf p.83 | VALIDATED |
| P-E-023 | multiple-choice | correct option=A; 4 unique options; distractor explanations verified | PhCh-SC202301 Physical Chemistry Part2.pdf p.89 | VALIDATED |
| P-E-024 | multiple-choice | correct option=C; 4 unique options; distractor explanations verified | PhCh-SC202301 Physical Chemistry Part2.pdf p.89 | VALIDATED |
| P-E-025 | conceptual-short-answer | principle=อธิบาย salting effects โดยไม่ overgeneralize; controlled accepted answers=3 | PhCh-SC202301 Physical Chemistry Part2.pdf p.89 | VALIDATED |
| P-E-026 | multiple-choice | correct option=B; 4 unique options; distractor explanations verified | PhCh-SC202301 Physical Chemistry Part2.pdf p.95 | VALIDATED |
| P-E-027 | electrochemical-cell-notation | correct option=A; 4 unique options; distractor explanations verified | PhCh-SC202301 Physical Chemistry Part2.pdf p.95 | VALIDATED |
| P-E-028 | numerical-calculation | op=subtract; expected=1.103 V; tolerance=0.002 | PhCh-SC202301 Physical Chemistry Part2.pdf p.108 | VALIDATED |
| P-E-029 | numerical-calculation | op=subtract; expected=1.0 V; tolerance=0.001 | PhCh-SC202301 Physical Chemistry Part2.pdf p.108 | VALIDATED |
| P-E-030 | multiple-choice | correct option=A; 4 unique options; distractor explanations verified | PhCh-SC202301 Physical Chemistry Part2.pdf p.108 | VALIDATED |
| P-E-031 | numerical-calculation | op=neg_product; expected=-48242.5 J mol^-1; tolerance=50 | PhCh-SC202301 Physical Chemistry Part2.pdf p.108 | VALIDATED |
| P-E-032 | numerical-calculation | op=equilibrium_k; expected=100.0 ; tolerance=0.2 | PhCh-SC202301 Physical Chemistry Part2.pdf p.108 | VALIDATED |
| P-E-033 | multi-step-calculation | op=nernst_298; expected=0.24084 V; tolerance=0.0003 | PhCh-SC202301 Physical Chemistry Part2.pdf p.119 | VALIDATED |

## Special validation notes

- P-K-026 corrected during independent validation to 1737 s^-1 for A=1.00×10^12 s^-1, Ea=50.0 kJ mol^-1, T=298.15 K.
- P-E-022 corrected during independent validation to 0.005953 mol L^-1 for the explicitly stated concentration-scale definition.
- P-E-013 is an adapted AgBr problem with κblank-corrected=6.50×10^-8 S cm^-1, S=5.00×10^-7 M, Ksp=2.50×10^-13; it does not reuse the original erroneous subtraction.
- Existing P-E-002 remains unchanged with the documented source correction.
