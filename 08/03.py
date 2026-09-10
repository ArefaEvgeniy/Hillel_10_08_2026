def func(a, b, c):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("---")


a, b, c = 1, 2, 3
func(c=a, b=b, a=100)
