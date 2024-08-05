N, M = map(int, input().split())

basket = [ value for value in range(1, N+1) ]

for _ in range(M):
    start, stop = map(int, input().split())
    basket[start-1 : stop] = basket[start-1 : stop][::-1]
    
for value in basket:
    print(value, end=" ")