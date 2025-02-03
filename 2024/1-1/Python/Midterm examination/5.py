# 별(*)을 반복하여 줄이 내려가면서 별(*)이 하나씩 없어지면서 출력하는 프로그램 작성

N = int(input())

count = 0
for count in range(N, 0, -1):
    A = (" " * (N - count)) + ("*" * count)
    print(A)