from pathlib import Path
import re

root = Path(".")

for file in root.glob("*.html"):

    filename = file.stem.lower()

    # 지역-서비스 형태 파일만 처리
    if "-" not in filename:
        continue

    area, service = filename.rsplit("-", 1)

    html = file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    # ==========================
    # canonical 수정
    # ==========================

    html = re.sub(
        r'<link rel="canonical" href="[^"]+">',
        f'<link rel="canonical" href="https://surinamcare.kr/{filename}.html">',
        html
    )


    # ==========================
    # 지역 링크 수정
    # ==========================

    # 모든 지역 서비스 링크 찾기
    pattern = r'href="([a-z0-9-]+)-(sink|drain|toilet)\.html"'

    def replace_link(match):

        old_area = match.group(1)
        service_type = match.group(2)

        # 자기 지역 링크로 변경
        return f'href="{area}-{service_type}.html"'


    html = re.sub(
        pattern,
        replace_link,
        html
    )


    # ==========================
    # 잘못된 지역명 텍스트 수정
    # ==========================

    # 제목, 본문 등에 들어간 영문 지역명 제거
    html = re.sub(
        r'(?i)\b[a-z]+(?=(하수구막힘|싱크대막힘|변기막힘))',
        area,
        html
    )


    file.write_text(
        html,
        encoding="utf-8"
    )


print("전체 HTML 지역 링크 및 canonical 수정 완료")