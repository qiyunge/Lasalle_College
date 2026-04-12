from PIL import Image
from pathlib import Path

# 打开你刚生成的图片
BASE_DIR = Path(__file__).resolve().parent

img = Image.open(BASE_DIR / "favicon.png").convert("RGBA")
data = img.get_flattened_data()
# 替换纯白色为透明
new_data = []   
for item in data:
    if item[0] >= 200 and item[1] >= 200 and item[2] >= 200:
        new_data.append((255, 255, 255, 0))  # 设置为透明
    else:
        new_data.append(item)
# 转换为 ICO（多尺寸更好）
img.putdata(new_data)
img.save(
    BASE_DIR / "favicon.ico",
    format="ICO",
    sizes=[(16, 16), (32, 32), (48, 48), (64, 64)]
)