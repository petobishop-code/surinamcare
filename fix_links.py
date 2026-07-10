from pathlib import Path
import re

root = Path(".")

for file in root.glob("*.html"):

    filename = file.stem.lower()

    if "-" not in filename:
        continue

    area, category = filename.rsplit("-", 1)

    html = file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    # 모든 seongsan 링크 제거 후 현재 지역으로 변경
    html = html.replace("seongsan-sink.html", f"{area}-sink.html")
    html = html.replace("seongsan-drain.html", f"{area}-drain.html")
    html = html.replace("seongsan-toilet.html", f"{area}-toilet.html")


    # canonical 전체 강제 수정
    html = re.sub(
        r'<link rel="canonical" href="[^"]+">',
        f'<link rel="canonical" href="https://www.surinamcare.kr/{filename}.html">',
        html
    )


    file.write_text(
        html,
        encoding="utf-8"
    )

print("전체 HTML 링크 및 canonical 수정 완료")