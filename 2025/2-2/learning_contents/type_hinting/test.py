x = 1

if isinstance(x, int):
    print("x는 정수형입니다.")
elif isinstance(x, float):
    print("x는 실수형입니다.")
else:
    raise TypeError("x는 정수형도 실수형도 아닙니다.")