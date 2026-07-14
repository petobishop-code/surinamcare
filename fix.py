from pathlib import Path
import re

folder = Path(".")

count = 0

for file in folder.glob("*.html"):

    text = file.read_text(encoding="utf-8", errors="ignore")

    # www 추가
    text = text.replace(
        "https://surinamcare.kr",
        "https://www.surinamcare.kr"
    )

    # canonical 수정
    canonical = f"https://www.surinamcare.kr/{file.name}"

    if '<link rel="canonical"' in text:

        text = re.sub(
            r'<link\s+rel="canonical"\s+href="[^"]*"\s*/?>',
            f'<link rel="canonical" href="{canonical}">',
            text,
            flags=re.I
        )

    file.write_text(text, encoding="utf-8")

    print("수정 :", file.name)

    count += 1

print("="*40)
print(f"{count}개 html 수정 완료")