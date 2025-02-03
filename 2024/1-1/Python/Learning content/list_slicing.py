bar = [10, 20, 30, 40]

# slicing의 예시
foo = bar[0:4:1]
print(foo)

# 마지막 값을 생략하면 ": +1"로 인식
foo = bar[0:4]
print(foo)


# start, stop 비어있는 경우 -> 0과 -1로 사용
foo = bar[:]
print(foo)

# stop 비어있는 경우 -> -1로 사용
foo = bar[2:]
print(foo)

# start 비어있는 경우 -> 0으로 사용
foo = bar[:3]
print(foo)

# step이 +1이 되면 리스트에는 아무것도 남지 않음
foo = bar[-1: -4]
print(foo)

#
foo = bar[-1: -4 : -1]
print(foo)

# 
foo = bar[-1 ::-1]
print(foo)