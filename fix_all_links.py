import glob
import re

files = glob.glob("*.html")

regions = {
    "seongsan": "anyang",
    "성산구": "안양",
    "changwon": "anyang",
    "창원": "안양",
    "masan": "anyang",
    "마산": "안양",
    "gimhae": "anyang",
    "김해": "안양",
}

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    original = text

    for old, new in regions.items():
        text = text.replace(old, new)

    # 파일명 링크 수정
    text = text.replace("anyang-drain.html", "anyang-drain.html")
    text = text.replace("anyang-sink.html", "anyang-sink.html")
    text = text.replace("anyang-toilet.html", "anyang-toilet.html")

    # 잘못된 canonical 자동 수정
    text = re.sub(
        r'<link rel="canonical" href="[^"]+">',
        lambda m: f'<link rel="canonical" href="https://www.surinamcare.kr/{file}">',
        text
    )

    if text != original:
        with open(file, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"수정 완료 : {file}")

print("전체 검사 완료")