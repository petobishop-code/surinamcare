import os
import re

print("수리남 전체 HTML 검사 시작")
print("=" * 50)

files = [f for f in os.listdir() if f.endswith(".html")]

html_files = set(files)

print(f"HTML 파일 개수 : {len(files)}개")
print("=" * 50)

missing = []
fixed = []

for file in files:

    with open(file, "r", encoding="utf-8") as f:
        data = f.read()

    original = data

    # href 링크 검사
    links = re.findall(r'href="([^"]+\.html)"', data)

    for link in links:

        # 외부 링크 제외
        if link.startswith("http"):
            continue

        # 존재하지 않는 파일
        if link not in html_files:

            missing.append(f"{file} → {link}")

            # 잘못된 링크 자동 보정
            name = link.replace(".html", "")

            if "-" in name:
                parts = name.split("-")

                if len(parts) == 2:

                    area = parts[0]
                    service = parts[1]

                    possible = f"{area}-{service}.html"

                    if possible in html_files:
                        data = data.replace(link, possible)


    if original != data:

        with open(file, "w", encoding="utf-8") as f:
            f.write(data)

        fixed.append(file)


print()
print("=" * 50)
print("검사 결과")
print("=" * 50)


if missing:
    print("발견된 문제 링크")
    for m in missing:
        print("❌", m)
else:
    print("깨진 링크 없음")


print()
print("자동 수정된 파일")
print("=" * 50)

for f in fixed:
    print("✅", f)


print()
print("전체 검사 완료")