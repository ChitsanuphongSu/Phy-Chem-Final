from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

PROJECT = Path(r"D:\Luna\Phy-Chem\physical-chemistry-study-hub")


def make(folder: str) -> None:
    images = sorted((PROJECT / "evidence" / "renders" / folder).glob("*.jpg"))
    out_dir = PROJECT / "evidence" / "contact_sheets" / folder
    out_dir.mkdir(parents=True, exist_ok=True)
    thumb_w, thumb_h, label_h = 360, 270, 24
    cols, rows = 4, 4
    for start in range(0, len(images), cols * rows):
        batch = images[start : start + cols * rows]
        canvas = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), "white")
        draw = ImageDraw.Draw(canvas)
        for idx, image_path in enumerate(batch):
            image = Image.open(image_path).convert("RGB")
            image.thumbnail((thumb_w, thumb_h))
            x = (idx % cols) * thumb_w + (thumb_w - image.width) // 2
            y0 = (idx // cols) * (thumb_h + label_h)
            y = y0 + (thumb_h - image.height) // 2
            canvas.paste(image, (x, y))
            page_number = start + idx + 1
            draw.rectangle((idx % cols * thumb_w, y0 + thumb_h, (idx % cols + 1) * thumb_w, y0 + thumb_h + label_h), fill="#24202a")
            draw.text((idx % cols * thumb_w + 8, y0 + thumb_h + 4), f"PDF page {page_number}", fill="white")
        end = start + len(batch)
        canvas.save(out_dir / f"pages_{start + 1:03d}_{end:03d}.jpg", quality=90)


for name in ("part1", "part2", "chemical_kinetic", "electrochemistry", "final_phychem", "final"):
    make(name)
