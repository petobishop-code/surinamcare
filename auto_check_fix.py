import os
import re
import shutil
from datetime import datetime

print("수리남 SEO 자동 검사 및 수정 시작")
print("=" * 50)

files = [f for f in os.listdir() if f.endswith(".html")]

html_files = set(files)

print(f"HTML 파일 개수 : {len(files)}개")

backup_folder = "seo_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S")
os.makedirs(backup_folder)

fixed = []
missing = []

for file in files:

    with open(file, "r", encoding="utf-8") as f:
        data = f.read()

    original = data


    # =====================
    # title 검사
    # =====================

    if not re.search(r"<title>.*?</title>", data, re.I):

        name = file.replace(".html","")

        title = name.replace("-", " ")

        data = data.replace(
            "</head>",
            f"<title>{title} | 수리남</title>\n</head>"
        )


    # =====================
    # description 검사
    # =====================

    if not re.search(
        r'<meta name="description"',
        data,
        re.I
    ):

        description = (
            "전국 하수구막힘, 변기막힘, 싱크대막힘 전문 수리남. "
            "빠른 출동과 정확한 배관 점검으로 문제를 해결합니다."
        )

        data = data.replace(
            "</head>",
            f'<meta name="description" content="{description}">\n</head>'
        )


    # =====================
    # canonical 검사
    # =====================

    if not re.search(
        r'<link rel="canonical"',
        data,
        re.I
    ):

        url = "https://www.surinamcare.kr/" + file

        data = data.replace(
            "</head>",
            f'<link rel="canonical" href="{url}">\n</head>'
        )


    # =====================
    # 깨진 링크 검사
    # =====================

    
  links = re.findall(
    r'href="([^"]+\.html)"',
    data
)

for link in links:

    # https://www.surinamcare.kr/ 제거
    clean_link = link.replace(
        "https://www.surinamcare.kr/",
        ""
    )

    if clean_link not in html_files:

            missing.append(
                f"{file} → {link}"
            )


    # 변경사항 저장
    if original != data:links = re.findall(

        shutil.copy(
            file,
            os.path.join(backup_folder,file)
        )

        with open(
            file,
            "w",
            encoding="utf-8"
        ) as f:
            f.write(data)

        fixed.append(file)



print()
print("=" * 50)
print("검사 결과")
print("=" * 50)


if missing:
    print("깨진 링크 발견")
    for m in missing:
        print("❌",m)

else:
    print("깨진 링크 없음")


print()
print("자동 수정된 파일")
print("=" * 50)

for f in fixed:
    print("✅",f)


print()
print("백업 위치:")
print(backup_folder)

print()
print("전체 검사 완료")