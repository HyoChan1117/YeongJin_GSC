# 사용자로부터 두 정수 A와 B를 입력 받아, A+B를 출력하는 프로그램 작성

T = int(input())

for _ in range(1, T+1):
    A, B = map(int, input().split())
    print(f"Case #{_}: {A} + {B} = {A+B}")