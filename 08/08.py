def func(b, a=0, c=0):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("---")


func(44, 64, 23)
a = [45, 76, 23]
func(*a)  #  *[45, 76, 23] -> func(45, 76, 23)
