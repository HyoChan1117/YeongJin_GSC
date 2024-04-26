# N 값 입력
n = int(input("N 값을 입력하세요: "))

# 1 <= "*" <= N, N번 반복하면 별을 1씩 증가하면서 출력
# 반복 (count)
#   count * "*"
for count in range(1, n + 1):
#    print("*" * count)
    for _ in range(0, count):
        print("*", end="")
    print()
# N -> 1, 1씩 감소.
# 반복 (count)
#   count * "*"
for count in range(n-1, 0, -1):
    print("*" * count)