foo = []

foo.append(10)
foo.append(20)
foo.append(30)
foo.append(5)

for index in range(0, 4):
    print(foo[index])
    # 1) foo[0] -> 10
    # 2) foo[1] -> 20
    # 3) foo[2] -> 30
    # 4) foo[3] -> 5

print("foo list의 사이즈: ", len(foo))  # 4