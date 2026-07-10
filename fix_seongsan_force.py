import glob
import os
import re

files = glob.glob("*.html")

for file in files:

    if file.startswith("seongsan-"):
        continue

    filename = os.path.splitext(file)[0]

    if "-" not in filename:
        continue

    region = filename.rsplit("-",1)[0]

    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    original = text

    text = text.replace("seongsan-sink.html", f"{region}-sink.html")
    text = text.replace("seongsan-drain.html", f"{region}-drain.html")
    text = text.replace("seongsan-toilet.html", f"{region}-toilet.html")

    if text != original:
        with open(file, "w", encoding="utf-8") as f:
            f.write(text)

        print("수정:", file)

print("완료")