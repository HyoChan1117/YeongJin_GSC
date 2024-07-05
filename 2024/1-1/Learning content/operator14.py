bar = [2, 3, 4, 5]
foo = (6, 7, 8, 9)
foo = 6, 7, 8, 9

# 2번 코드와 3번 코드는 모두 tuple이지만
# 가독성 측면에서는 2번 코드가 좋음

def getValue():
    return 2, 3, 4, 5

print(getValue())

print(type(getValue()))

# 9번에서 받은 2, 3, 4, 5는 11번에서 출력될 때
# tuple화가 됨

