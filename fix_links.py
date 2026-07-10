from pathlib import Path
import re

root = Path(".")

for file in root.glob("*.html"):

    html = file.read_text(encoding="utf-8", errors="ignore")

    filename = file.stem.lower()

    # 자기 파일 이름에서 지역 추출
    if filename.endswith("-drain"):
        area = filename[:-6]
    elif filename.endswith("-sink"):
        area = filename[:-5]
    elif filename.endswith("-toilet"):
        area = filename[:-7]
    else:
        continue

    # 예전 지역 링크 자동 교체
    html = re.sub(r'seongsan-drain\.html', f'{area}-drain.html', html)
    html = re.sub(r'seongsan-sink\.html', f'{area}-sink.html', html)
    html = re.sub(r'seongsan-toilet\.html', f'{area}-toilet.html', html)

    html = re.sub(r'changwon-drain\.html', f'{area}-drain.html', html)
    html = re.sub(r'changwon-sink\.html', f'{area}-sink.html', html)
    html = re.sub(r'changwon-toilet\.html', f'{area}-toilet.html', html)

    file.write_text(html, encoding="utf-8")

print("완료!")