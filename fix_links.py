from pathlib import Path
import re

root = Path(".")

for file in root.glob("*.html"):

    name = file.stem.lower()

    if "-" not in name:
        continue

    area = name.rsplit("-",1)[0]

    html = file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    # 링크 주소 전체 변경
    html = html.replace(
        "seongsan-sink.html",
        f"{area}-sink.html"
    )

    html = html.replace(
        "seongsan-drain.html",
        f"{area}-drain.html"
    )

    html = html.replace(
        "seongsan-toilet.html",
        f"{area}-toilet.html"
    )

    # canonical
    html = re.sub(
        r"https://surinamcare\.kr/seongsan-[^\"']+\.html",
        f"https://surinamcare.kr/{name}.html",
        html
    )

    html = re.sub(
        r"https://www\.surinamcare\.kr/seongsan-[^\"']+\.html",
        f"https://www.surinamcare.kr/{name}.html",
        html
    )

    file.write_text(
        html,
        encoding="utf-8"
    )

print("완료")