import os
import re

print("수리남 SEO 전체 검사 시작")
print("=" * 50)

files = [f for f in os.listdir() if f.endswith(".html")]

html_files = set(files)

print(f"HTML 파일 개수 : {len(files)}개")
print("=" * 50)


# -------------------------
# 1. 기본 HTML 요소 검사
# -------------------------

print("\n[1] 제목(title) 검사")
print("-" * 50)

no_title = []

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        data = f.read()

    if "<title>" not in data:
        no_title.append(file)

if no_title:
    for x in no_title:
        print("❌ title 없음 :", x)
else:
    print("✅ 모든 페이지 title 존재")


# -------------------------
# 2. meta description 검사
# -------------------------

print("\n[2] description 검사")
print("-" * 50)

no_desc = []

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        data = f.read()

    if 'name="description"' not in data:
        no_desc.append(file)

if no_desc:
    for x in no_desc:
        print("❌ description 없음 :", x)
else:
    print("✅ 모든 페이지 description 존재")


# -------------------------
# 3. canonical 검사
# -------------------------

print("\n[3] canonical 검사")
print("-" * 50)

no_canonical = []

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        data = f.read()

    if "canonical" not in data:
        no_canonical.append(file)

if no_canonical:
    for x in no_canonical:
        print("❌ canonical 없음 :", x)
else:
    print("✅ 모든 페이지 canonical 존재")


# -------------------------
# 4. 내부 링크 검사
# -------------------------

print("\n[4] 내부 링크 검사")
print("-" * 50)

broken = []

for file in files:

    with open(file, "r", encoding="utf-8") as f:
        data = f.read()

    links = re.findall(r'href="([^"]+\.html)"', data)

    for link in links:

        if link not in html_files:
            broken.append(f"{file} → {link}")


if broken:
    for x in broken:
        print("❌", x)
else:
    print("✅ 깨진 내부 링크 없음")


# -------------------------
# 5. sitemap 검사
# -------------------------

print("\n[5] sitemap 검사")
print("-" * 50)

if os.path.exists("sitemap.xml"):

    with open("sitemap.xml", "r", encoding="utf-8") as f:
        sitemap = f.read()

    missing = []

    for file in files:

        if file not in sitemap:
            missing.append(file)

    if missing:
        for x in missing:
            print("❌ sitemap 누락 :", x)
    else:
        print("✅ 모든 HTML sitemap 등록")

else:
    print("❌ sitemap.xml 없음")


print("\n" + "=" * 50)
print("SEO 전체 검사 완료")
print("=" * 50)