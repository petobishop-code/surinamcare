from pathlib import Path
import re

root = Path(".")

for file in root.glob("*.html"):

    name = file.stem.lower()

    if "-" not in name:
        continue

    area = name.rsplit("-", 1)[0]

    html = file.read_text(encoding="utf-8", errors="ignore")

    # 잘못 들어간 성산구 링크 제거 → 현재 파일 지역으로 변경
    html = html.replace("seongsan-sink.html", f"{area}-sink.html")
    html = html.replace("seongsan-drain.html", f"{area}-drain.html")
    html = html.replace("seongsan-toilet.html", f"{area}-toilet.html")

    # canonical도 수정
    html = re.sub(
        r"https://(www\.)?surinamcare\.kr/seongsan-(sink|drain|toilet)\.html",
        lambda m: f"https://www.surinamcare.kr/{area}-{m.group(2)}.html",
        html
    )

    file.write_text(html, encoding="utf-8")

print("전체 링크 수정 완료")