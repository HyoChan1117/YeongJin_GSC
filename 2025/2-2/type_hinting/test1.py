def test():
    return 1, "2", True

a, b, c = test()

x = test()

print(x)  # (1, "2", True)

print(type(x))  # tuple

print(a, b, c)