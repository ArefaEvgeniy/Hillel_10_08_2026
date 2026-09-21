with open("example.txt", encoding="utf-8") as f:   # "rt"
    content = f.read()

print(content)
# print(content.decode(encoding="utf-16", errors="ignore"))


with open("example.txt", encoding="utf-8") as f:
    content_1 = f.read(7)
    content_2 = f.read(17)
    content_3 = f.read(27)

print(content_1)
print("--------------------")
print(content_2)
print("--------------------")
print(content_3)


print("<-------------------->")
with open("example.txt", "rb") as f:
    content_bytes = f.read(28)

print(content_bytes.decode(encoding="utf-8"))
