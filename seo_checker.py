import os
import re

BASE = os.getcwd()

html_files = {
    f for f in os.listdir(BASE)
    if f.endswith(".html")
}

print("=" * 50)
print("수리남 HTML 검사 시작")
print("=" * 50)

print(f"HTML 파일 개수 : {len(html_files)}개")

broken_links = []

for file in html_files:

    path = os.path.join(BASE, file)

    try:
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()

    except:
        continue

    links = re.findall(
        r'href=["\']([^"\']+\.html)["\']',
        html
    )

    for link in links:

        target = link.split("/")[-1]

        if target not in html_files:

            broken_links.append(
                {
                    "file": file,
                    "link": target
                }
            )


print()
print("=" * 50)
print("깨진 링크 검사 결과")
print("=" * 50)


if broken_links:

    for item in broken_links:
        print(
            f"❌ {item['file']} → {item['link']}"
        )

else:

    print("✅ 깨진 HTML 링크 없음")


print()
print("검사 완료")
