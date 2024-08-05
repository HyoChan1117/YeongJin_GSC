white = input().split()

black = [1, 1, 2, 2, 2, 8]

need_white = []

for index in range(6):
    need_white.append(black[index] - int(white[index]))
    
for value in need_white:
    print(value, end=" ")