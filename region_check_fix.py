import os
import re


print("전체 지역 자동 검사 시작")
print("=" * 50)


# html 파일 가져오기
html_files = [
    f for f in os.listdir()
    if f.endswith(".html")
]


# 파일명에서 지역 영어명 자동 추출
regions = {}

for file in html_files:

    name = file.replace(".html", "")

    if "-" in name:

        area = name.split("-")[0]

        regions[area] = True



print("찾은 지역 개수 :", len(regions))


print("=" * 50)


for file in html_files:

    filename = file.replace(".html", "")


    if "-" not in filename:
        continue


    my_area = filename.split("-")[0]


    with open(
        file,
        "r",
        encoding="utf-8"
    ) as f:
        data = f.read()



    print()
    print("검사 :", file)


    # 다른 영어 지역 검사

    for area in regions:

        if area == my_area:
            continue


        if re.search(
            r"\b" + area + r"\b",
            data,
            re.I
        ):

            print(
                "❌ 다른 영어 지역 발견:",
                area
            )


print()
print("=" * 50)
print("전체 검사 완료")