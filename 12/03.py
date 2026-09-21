with open("example.txt", encoding="utf-8") as f:
    print(f.readline().strip())
    print(f.readline().strip())
    print(f.readline().strip())


with open("example.txt", encoding="utf-8") as f:
    print(f.readlines())
