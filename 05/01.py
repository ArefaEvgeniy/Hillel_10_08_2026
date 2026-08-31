a = "Hello, It's World!"
b = 'Hello, "World!'
c_1 = "Hello, It's "
c_2 = '"World"'
d = '''Hello, It's "World"'''
e = "Hello,\tIt'\ns \"World\""
f = """Hello, It's World
this is a multi-line string
    next line
            end...
"""
j = r"\n - this is a new line, \t - this is a tab"

print(a)
print(b)

print(id(a))
print(id(b))

print(c_1 + c_2)
print(d)
print(e)
print(f)
print(j)
