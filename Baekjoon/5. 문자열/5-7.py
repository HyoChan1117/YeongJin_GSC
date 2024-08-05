T = int(input())

for _ in range(T):
    R, S = input().split()
    for value in S:
        print(value * int(R), end="")
    print()