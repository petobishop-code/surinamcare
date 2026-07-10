import glob

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        data = f.read()

    old = data

    data = data.replace("seongsan-drain.html", "suji-drain.html")
    data = data.replace("seongsan-sink.html", "suji-sink.html")
    data = data.replace("seongsan-toilet.html", "suji-toilet.html")
    data = data.replace("성산구", "수지구")
    data = data.replace("seongsan", "suji")

    if old != data:
        with open(file, "w", encoding="utf-8") as f:
            f.write(data)
        print("수정:", file)

print("완료")