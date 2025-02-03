# slicing : 하나의 리스트에서 특정 구간에 있는 원소들을 여러 개 지정해서 복사를 해서 가져오는 것
bar = [value for value in range(10, 20)]

# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# slicing
# 참조변수 [start : stop : step]
# start : 0 -> 4 - 1
foo = bar[0:4:1]

print("foo: ", foo)
print("bar: ", bar)

