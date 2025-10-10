x = 1.0

if isinstance(x, int):
    print("x is int")
elif isinstance(x, float):
    print("x is float")
else:
    raise TypeError("x is not int or float")