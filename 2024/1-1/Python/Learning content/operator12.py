# multiple assignment : 다중 대입

bar, foo, kin = 10, 20, 30

print(f"{bar}, {foo}, {kin}")


def getValue():
    return 2, 3, 4, 5

print(getValue())

print(type(getValue()))  # tuple은 immutable
# list는 mutable