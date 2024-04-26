# 사용자로부터 자연수 N을 입력 받아, 첫째 줄부터 N번째 줄까지 차례대로 별을 출력하는
# 프로그램 작성

n = int(input())

A = ""

for _ in range(1, n+1):
    A = A + "*"
    print(A)