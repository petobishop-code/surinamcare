from pathlib import Path

files = [
    "seongsan-drain.html",
    "seongsan-sink.html",
    "seongsan-toilet.html"
]

for f in files:
    path = Path(f)

    html = path.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    html = html.replace(
        "seongsan",
        "성산구"
    )

    path.write_text(
        html,
        encoding="utf-8"
    )

print("성산구 페이지 복구 완료")