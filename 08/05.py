def func(a, *args):
    print("a:", a)
    # print("b:", b)
    # print("c:", c)
    print("args:", args)
    print("---")


a, b, c = 1, 2, 3
func(77, 99, a, 6, 77, 8889, 45, 33, 22, 1)
func(77)
