import re
from pathlib import Path

# 지역 치환 규칙
rules = {
    "changwon": "안양",
    "seongsan": "안양",
    "masan": "안양",
    "gimhae": "안양",
}

files = [
    "changwon-drain.html",
    "changwon-sink.html",
    "changwon-toilet.html",
    "gimhae-drain.html",
    "gimhae-sink.html",
    "gimhae-toilet.html",
    "masan-drain.html",
    "masan-sink.html",
    "masan-toilet.html",
    "seongsan-drain.html",
    "seongsan-sink.html",
    "seongsan-toilet.html",
]

for file in files:
    path = Path(file)

    if not path.exists():
        continue

    text = path.read_text(encoding="utf-8")

    for eng, kor in rules.items():

        # 파일 링크명 제거
        text = text.replace(f"{eng}-sink.html", "anyang-sink.html")
        text = text.replace(f"{eng}-drain.html", "anyang-drain.html")
        text = text.replace(f"{eng}-toilet.html", "anyang-toilet.html")

        # 지역명 변경
        text = text.replace(
            {
                "changwon": "창원",
                "seongsan": "성산구",
                "masan": "마산",
                "gimhae": "김해"
            }[eng] + "하수구막힘",
            "안양하수구막힘"
        )

        text = text.replace(
            {
                "changwon": "창원",
                "seongsan": "성산구",
                "masan": "마산",
                "gimhae": "김해"
            }[eng] + "싱크대막힘",
            "안양싱크대막힘"
        )

        text = text.replace(
            {
                "changwon": "창원",
                "seongsan": "성산구",
                "masan": "마산",
                "gimhae": "김해"
            }[eng] + "변기막힘",
            "안양변기막힘"
        )


    # canonical 수정
    text = re.sub(
        r'https://www\.surinamcare\.kr/[^"]+',
        "https://www.surinamcare.kr/anyang-drain.html",
        text
    )

    path.write_text(text, encoding="utf-8")

    print(f"{file} 수정 완료")

print("전체 수정 완료")