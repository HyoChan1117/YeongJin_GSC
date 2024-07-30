N = int(input())

list_num = input().split()

v = int(input())

count = 0
for index in range(N):
    if int(list_num[index]) == v:
        count += 1
        
print(count)