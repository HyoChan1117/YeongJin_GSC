# 사용자로부터 테스트 케이스의 개수 T와 두 정수 A, B를 입력 받아, A+B를 출력하는 프로그램 작성

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(A + B)