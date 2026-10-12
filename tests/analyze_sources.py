from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from PIL import Image
from pypdf import PdfReader
import numpy as np


ROOT = Path(r"D:\Luna\Phy-Chem")
PROJECT = ROOT / "physical-chemistry-study-hub"
PDF_NAMES = [
    "PhCh-SC202301 Physical Chemistry Part1.pdf",
    "PhCh-SC202301 Physical Chemistry Part2.pdf",
    "Chemical Kinetic.pdf",
    "Electrochemistry.pdf",
    "Final Phychem.pdf",
    "Final.pdf",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def compact(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def page_record(page, page_number: int) -> dict:
    text = page.extract_text() or ""
    resources = page.get("/Resources") or {}
    xobjects = resources.get("/XObject") or {}
    annotations = page.get("/Annots") or []
    return {
        "pdf_page": page_number,
        "text": text,
        "text_preview": compact(text)[:500],
        "character_count": len(text),
        "image_object_count": len(xobjects),
        "annotation_count": len(annotations),
        "printed_slide_number": None,
        "manual_review": len(compact(text)) < 20,
    }


def magenta_metrics(image_path: Path) -> dict:
    array = np.asarray(Image.open(image_path).convert("RGB"), dtype=np.int16)
    height, width, _ = array.shape
    r, g, b = array[:, :, 0], array[:, :, 1], array[:, :, 2]
    # Broad magenta detector. Visual inspection determines final status.
    mask = (r >= 160) & (b >= 120) & ((r - g) >= 45) & ((b - g) >= 35)
    ys, xs = np.nonzero(mask)
    count = int(mask.sum())
    fraction = count / (width * height)
    bbox = None if count == 0 else [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())]
    return {
        "magenta_pixel_count": count,
        "magenta_fraction": round(fraction, 8),
        "magenta_bbox": bbox,
        "candidate": count >= 120 and fraction >= 0.00008,
    }


def main() -> None:
    inventory = []
    full_text_dir = PROJECT / "tmp" / "pdfs"
    full_text_dir.mkdir(parents=True, exist_ok=True)
    for name in PDF_NAMES:
        path = ROOT / name
        reader = PdfReader(str(path))
        pages = [page_record(page, i) for i, page in enumerate(reader.pages, 1)]
        safe = re.sub(r"[^A-Za-z0-9_-]", "_", path.stem)
        (full_text_dir / f"{safe}.txt").write_text(
            "\n\n".join(f"===== PDF PAGE {p['pdf_page']} =====\n{p['text']}" for p in pages),
            encoding="utf-8",
        )
        inventory.append(
            {
                "document_id": safe,
                "file_name": name,
                "role": "primary_instructor" if "Part" in name else "supplementary",
                "page_count": len(reader.pages),
                "file_size_bytes": path.stat().st_size,
                "sha256": sha256(path),
                "encrypted": bool(reader.is_encrypted),
                "pages": pages,
            }
        )

    for folder in ("part1", "part2"):
        document = inventory[0 if folder == "part1" else 1]
        images = sorted((PROJECT / "evidence" / "renders" / folder).glob("*.jpg"))
        if len(images) != document["page_count"]:
            raise RuntimeError(f"Render count mismatch for {folder}: {len(images)}")
        for record, image_path in zip(document["pages"], images):
            record["render_path"] = str(image_path.relative_to(PROJECT)).replace("\\", "/")
            record["star_color_screen"] = magenta_metrics(image_path)

    out = PROJECT / "data" / "document_inventory.json"
    out.write_text(json.dumps({"schema_version": 1, "documents": inventory}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {out}")
    for document in inventory:
        candidates = sum(1 for p in document["pages"] if p.get("star_color_screen", {}).get("candidate"))
        print(document["file_name"], document["page_count"], "candidate_pages", candidates)


if __name__ == "__main__":
    main()
