# 사용자로부터 자연수 N 입력 받아, 1부터 N까지 합을 출력하는 프로그램 작성

N = int(input())

A = 0
for _ in range(N+1):
    A = A + _

print(A)