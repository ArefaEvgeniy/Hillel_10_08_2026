my_str = "Привіт, світ!"

bytes_str = my_str.encode()

print(bytes_str)
print(bytes_str.decode('Latin-1'))
print(bytes_str.decode('Windows-1251'))
print(bytes_str.decode('utf-8'))
