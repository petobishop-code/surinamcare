import glob
import re

regions = {
    "changwon": "창원",
    "gimhae": "김해",
    "masan": "마산",
    "seongsan": "성산",
}

for file in glob.glob("*.html"):

    filename = file.lower()

    target = None

    for eng, kor in regions.items():
        if filename.startswith(eng + "-"):
            target = kor
            break

    if not target:
        continue

    with open(file, "r", encoding="utf-8") as f:
        html = f.read()

    # 안양으로 잘못 들어간 부분 복구
    html = html.replace("안양하수구막힘", target + "하수구막힘")
    html = html.replace("안양싱크대막힘", target + "싱크대막힘")
    html = html.replace("안양변기막힘", target + "변기막힘")

    # canonical 정상화
    base = file.replace("\\", "/")

    html = re.sub(
        r'<link rel="canonical" href=".*?">',
        f'<link rel="canonical" href="https://surinamcare.kr/{base}">',
        html
    )

    with open(file, "w", encoding="utf-8") as f:
        f.write(html)

    print("수정 완료:", file)

print("전체 복구 완료")