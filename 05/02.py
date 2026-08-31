a = "Hello, It's\nWorld!"

print(len(a))
print("hello" in a)

for i in a:
    print(i)

print("-" * 20)
print(a[-1:-4:-1])
print(a[::2])

my_string = "Python" + " is " + "awesome!"
print(my_string)

print("Python" + "Python" + "Python")
print("Python" * 3)
print(3 * "Python")

my_string = "123456789"
# my_string[6] = "N"
my_string = my_string[:6] + "N" + my_string[7:]

print(my_string)
