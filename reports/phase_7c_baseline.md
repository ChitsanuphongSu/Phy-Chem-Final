# Phase 7C Baseline

วันที่ตรวจ: 12 ตุลาคม 2026

## Application and content baseline

- React + TypeScript + Vite, 7 existing routes, pink Light/Dark design
- Topics/lessons 18; formulas 23; active problems 65; confirmed P1 20
- Difficulty: Easy 20, Medium 29, Hard 16
- Central grading supports numeric tolerance, MCQ option IDs and controlled text answers
- Production bundle before Phase 7C: one JS chunk `index-CHNjqpRA.js`, 757,949 bytes (reported 757.94 kB; gzip 199.33 kB), with >500 kB warning

## Existing storage schema

LocalStorage key: `phychem-study-v1`.

Available raw fields:

- theme
- completed lesson IDs
- formula/problem bookmarks
- attempts: `problemId`, `correct`, `at`
- flashcard interval, due date and review count

Missing historical fields: raw submitted answer, hint usage, time spent, attempt ID, difficulty snapshot, topic snapshot, practice/mock source and mock sessions. Phase 7C must not invent these values for old attempts.

## Analytics prerequisites

Problem metadata supplies canonical topic, difficulty, learning objective, P1 relationships and common mistake. Historical analytics can therefore use correctness/timestamp/question ID, but misconception confirmation requires future raw responses. Derived analytics will be recalculated rather than persisted.

## Baseline QA

Phase 7A/7B Python validators and 19 Vitest tests passed before Phase 7C. Original PDF hashes and P1 evidence were verified by the existing validators.
