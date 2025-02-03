bar = [10, 20, 30]
foo = [1, 2, 3]
pos = [-1, -2, -3]

kin = pos

pos = bar

pos[-1] = 100

pos = kin
print(bar[-1], pos[-1])