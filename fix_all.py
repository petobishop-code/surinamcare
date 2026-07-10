from pathlib import Path
import re

root = Path(".")

for file in root.glob("*.html"):

    text = file.read_text(encoding="utf-8", errors="ignore")

    filename = file.name

    # canonical 자동 수정
    canonical = f'https://www.surinamcare.kr/{filename}'

    if '<link rel="canonical"' in text:
        text = re.sub(
            r'<link rel="canonical" href="[^"]*">',
            f'<link rel="canonical" href="{canonical}">',
            text
        )
    else:
        text = text.replace(
            "</head>",
            f'<link rel="canonical" href="{canonical}">\n</head>'
        )

    # 도메인 통일
    text = text.replace("https://surinamcare.kr", "https://www.surinamcare.kr")
    text = text.replace("https://petobishop-code.github.io/surinamcare", "https://www.surinamcare.kr")
    text = text.replace("https://surinamcare.vercel.app", "https://www.surinamcare.kr")

    # 예전 템플릿 흔적 표시
    if "seongsan" in text.lower():
        print(f"⚠ {filename} : seongsan 발견")

    if "changwon" in text.lower():
        print(f"⚠ {filename} : changwon 발견")

    file.write_text(text, encoding="utf-8")

print("\n==========================")
print("모든 HTML 수정 완료")