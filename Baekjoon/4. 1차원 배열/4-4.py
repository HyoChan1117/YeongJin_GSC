list_num = []
for _ in range(9):
    num = int(input())
    list_num.append(num)
    
print(max(list_num))

count = 0
for value in list_num:
    if max(list_num) == value:
        count += 1
        break
    else:
        count += 1
print(count)