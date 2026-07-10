import os
import re
import shutil
from datetime import datetime

print("지역명 자동 수정 시작")
print("=" * 50)

# 지역 영어명 : 한글명
regions = {
    "anyang": "안양",
    "bucheon": "부천",
    "bupyeong": "부평",
    "changwon": "창원",
    "cheoin": "처인구",
    "cheongwon": "청원구",
    "daedeok": "대덕구",
    "dalseo": "달서구",
    "danwon": "단원구",
    "deogyang": "덕양구",
    "deokjin": "덕진구",
    "dobong": "도봉구",
    "dongan": "동안구",
    "dongdaemun": "동대문구",
    "dongjak": "동작구",
    "dongnae": "동래구",
    "dongnam": "동남구",
    "eunpyeong": "은평구",
    "gangbuk": "강북구",
    "gangdong": "강동구",
    "gangnam": "강남구",
    "gangseo": "강서구",
    "geumcheon": "금천구",
    "geumjeong": "금정구",
    "giheung": "기흥구",
    "gimhae": "김해",
    "guro": "구로구",
    "gwanak": "관악구",
    "gwangjin": "광진구",
    "gwangsan": "광산구",
    "gyeyang": "계양구",
    "haeundae": "해운대구",
    "heungdeok": "흥덕구",
    "jangan": "장안구",
    "jinhae": "진해구",
    "jongno": "종로구",
    "jungnang": "중랑구",
    "jungwon": "중원구",
    "manan": "만안구",
    "mapo": "마포구",
    "masan": "마산",
    "michuhol": "미추홀구",
    "nowon": "노원구",
    "ojeong": "오정구",
    "paldal": "팔달구",
    "pocheon": "포천",
    "saha": "사하구",
    "sangdang": "상당구",
    "sangnok": "상록구",
    "sasang": "사상구",
    "seobuk": "서북구",
    "seocho": "서초구",
    "seodaemun": "서대문구",
    "seongbuk": "성북구",
    "seongdong": "성동구",
    "seongsan": "성산구",
    "seowon": "서원구",
    "songpa": "송파구",
    "sujeong": "수정구",
    "suji": "수지구",
    "suseong": "수성구",
    "uichang": "의창구",
    "wansan": "완산구",
    "yangcheon": "양천구",
    "yangju": "양주",
    "yeongdeungpo": "영등포구",
    "yeongdo": "영도구",
    "yeongtong": "영통구",
    "yeonje": "연제구",
    "yeonsu": "연수구",
    "yongin": "용인",
    "yongsan": "용산구",
    "yuseong": "유성구"
}


backup = "region_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S")
os.makedirs(backup)

files = [f for f in os.listdir() if f.endswith(".html")]

fixed = []

for file in files:

    # 파일명 기준 현재 지역 확인
    current = None

    for eng in regions:
        if file.startswith(eng + "-"):
            current = eng
            break

    if not current:
        continue

    current_eng = current
    current_kor = regions[current]

    print()
    print("검사 :", file)

    with open(file, "r", encoding="utf-8") as f:
        data = f.read()

    original = data


    for eng, kor in regions.items():

        if eng == current_eng:
            continue

        # 영어 지역명 수정
        if eng in data:
            print("수정 영어 :", eng, "→", current_eng)
            data = data.replace(eng, current_eng)


        # 한글 지역명 수정
        if kor in data:
            print("수정 한글 :", kor, "→", current_kor)

            data = data.replace(
                kor,
                current_kor
            )


    if original != data:

        shutil.copy(
            file,
            os.path.join(backup, file)
        )

        with open(file, "w", encoding="utf-8") as f:
            f.write(data)

        fixed.append(file)


print()
print("=" * 50)
print("자동 수정 완료")
print("=" * 50)

print("수정 파일 개수 :", len(fixed))

for f in fixed:
    print("✅", f)

print()
print("백업 위치 :", backup)
print("전체 완료")