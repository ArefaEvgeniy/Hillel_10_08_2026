a = " HellO, IT's world!   "

print(a.split("l"))

text = "Python    is  a\tprogramming         language. \nPython is        easy to learn. Python is  powerful."

my_list = text.split()
print(my_list)

new_text = " ".join(my_list)
print(new_text)

print(new_text.replace("Python", "Java", 1))
