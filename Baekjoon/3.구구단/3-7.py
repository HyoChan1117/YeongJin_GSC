T = int(input())

for value in range(1, T + 1):
    A, B = map(int, input().split())
    print(f"Case #{value}: {A + B}")