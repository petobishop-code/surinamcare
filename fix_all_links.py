import glob
import os

files = glob.glob("*.html")

for file in files:

    filename = os.path.splitext(file)[0]

    if "-" not in filename:
        continue

    region = filename.rsplit("-",1)[0]

    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    original = text


    text = text.replace(
        "seongsan-sink.html",
        f"{region}-sink.html"
    )

    text = text.replace(
        "seongsan-drain.html",
        f"{region}-drain.html"
    )

    text = text.replace(
        "seongsan-toilet.html",
        f"{region}-toilet.html"
    )


    text = text.replace(
        "https://surinamcare.kr/seongsan-sink.html",
        f"https://surinamcare.kr/{region}-sink.html"
    )

    text = text.replace(
        "https://surinamcare.kr/seongsan-drain.html",
        f"https://surinamcare.kr/{region}-drain.html"
    )

    text = text.replace(
        "https://surinamcare.kr/seongsan-toilet.html",
        f"https://surinamcare.kr/{region}-toilet.html"
    )


    if text != original:
        with open(file,"w",encoding="utf-8") as f:
            f.write(text)

        print("수정:",file)


print("전체 완료")