N, M = map(int, input().split())

count_list = [ value for value in range(1, N + 1) ]

for _ in range(M):
    i, j = map(int, input().split())
    value = count_list[i-1]
    count_list[i-1] = count_list[j-1]
    count_list[j-1] = value
    
for num in count_list:
    print(num, end=" ")