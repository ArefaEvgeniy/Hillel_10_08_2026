def func(a, b, c, **kwargs):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("kwargs:", kwargs)
    print("---")


a, b, c = 1, 2, 3
func(c=a, b=b, a=100, f=33, g=44, h=55)
