def func(a_1, a_2, *args, b_1=0, b_2=0, b_3=0, b_4=0, **kwargs):
    # a_1, a_2, b_1=0, b_2=0, b_3=0, b_4=0,
    print("a_1:", a_1)
    print("a_2:", a_2)
    print("b_1:", b_1)
    print("b_2:", b_2)
    print("b_3:", b_3)
    print("b_4:", b_4)
    print("args:", args)
    print("kwargs:", kwargs)
    print("---")


a, b, c = 1, 2, 3
func(55, 66, 88, 345, 234, 990, 55567, b_1=44, c=a, b_2=99, b=b, a=100, f=33, g=44, h=55)
# func(c=a, b=b, a=100, f=33, g=44, h=55)
# func(55, 66, 88, 345, 234, 990, 55567)
# func()
