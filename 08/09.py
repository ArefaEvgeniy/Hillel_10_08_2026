def func(a, b, c):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("---")


func(c=4, b=0, a=100)

a = {"b": 12, "c": 23, "a": 45}
func(**a)  # **{"b": 12, "c": 23, "a": 45} -> func(b=12, c=23, a=45)
