bar = [2, 3, 4, 5, 6]

foo = bar[:]

print(type(foo))

print(foo)


# 참고사항

bar[0 : 3] = [100, 200, 300]
# [100, 200, 300, 5, 6]