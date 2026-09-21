my_str = "Привіт світ!\n Це рядок, який буде записаний у файл.\n"
new_str = "This is a new line added to the string.\n"
new_str_2 = "\nЦе новий рядок, доданий до файлу.\n"

f = open("example.txt", "w", encoding="utf-8")
f.write(my_str)
f.write(new_str)
f.close()


f = open("example.txt", "ab")
try:
    f.write(new_str_2.encode(encoding="utf-8"))
    # f.write(new_str_2.encode(encoding="utf-16"))
finally:
    f.close()
