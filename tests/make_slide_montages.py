from pathlib import Path
from PIL import Image, ImageDraw

ROOT=Path(r"D:\Luna\Phy-Chem\physical-chemistry-study-hub\tmp\slide-build")
for folder in [p for p in ROOT.iterdir() if p.is_dir()]:
    files=sorted(folder.glob("slide-*.png"))
    if not files: continue
    tw,th=480,270
    canvas=Image.new("RGB",(tw*2,(th+24)*5),"white")
    draw=ImageDraw.Draw(canvas)
    for i,f in enumerate(files[:10]):
        im=Image.open(f).convert("RGB");im.thumbnail((tw,th))
        x=(i%2)*tw;y=(i//2)*(th+24)
        canvas.paste(im,(x,y));draw.text((x+8,y+th+4),f.name,fill="black")
    canvas.save(ROOT/f"{folder.name}-montage.jpg",quality=92)
