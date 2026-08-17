name = "Nick"
age = 55

print("Your age will be:", age + 10, "next text", name, "...")
print("Your age will be:", age + 10, "next text", name, "...", sep="")
print("Hello", "world", end=" ")
print("I am ...")
print()
print("next line")

f = open("test.txt", "w")
print("Your age will be:", age + 10, "next text", name, "...", file=f, end="")
f.close()

print("Your age will be:", " ", age + 10, " ", "next text", name, "...", sep="")
print("I am ...", sep="!!!")
