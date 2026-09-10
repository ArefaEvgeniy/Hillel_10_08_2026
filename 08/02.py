def func(b, a=0, c=0):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("---")


a, b, c = 1, 2, 3
func(b, c, a)
func(b, c)
func(12)
# func()
