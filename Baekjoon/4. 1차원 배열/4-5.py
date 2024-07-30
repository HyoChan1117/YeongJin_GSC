N, M = map(int, input().split())

count_list = [ value * 0 for value in range(N) ]

for _ in range(M):
    i, j, k = map(int, input().split())
    for num in range(i - 1, j):
        count_list[num] = k
        
for value in count_list:
    print(value, end=" ")