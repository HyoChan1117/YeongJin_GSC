# List comprehension

# bar = [1, 2, 3, 4, 5, 6]

# print(bar)


# bar.clear()

# print(bar)

foo = [1, 2, 3, 4, 5, 6]
bar = foo
del foo  # 참조변수 foo는 지우지만 리스트는 지우지 않음
print(bar)