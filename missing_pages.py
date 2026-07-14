import os

BASE = os.getcwd()

html_files = {
    f.replace(".html", "")
    for f in os.listdir(BASE)
    if f.endswith(".html")
}

services = [
    "drain",
    "sink",
    "toilet"
]

print("=" * 50)
print("수리남 지역 페이지 누락 검사")
print("=" * 50)

missing = []

# 지역명 추출
regions = set()

for file in html_files:
    for service in services:
        suffix = "-" + service
        if file.endswith(suffix):
            region = file.replace(suffix, "")
            regions.add(region)


for region in sorted(regions):

    for service in services:

        filename = f"{region}-{service}"

        if filename not in html_files:
            missing.append(filename + ".html")


print()
print("검사 결과")
print("=" * 50)

if missing:

    for item in missing:
        print("❌ 없음 :", item)

    print()
    print(f"총 누락 파일 : {len(missing)}개")

else:

    print("✅ 모든 지역 페이지 정상")


print()
print("검사 완료")
