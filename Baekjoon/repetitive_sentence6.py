# 사용자로부터 테스트 케이스의 개수 T를 입력 받아, 각 테스트 케이스마다 A+B를 한 줄에
# 한 줄에 하나씩 순서대로 출력하는 프로그램 작성

T = int(input())

for _ in range(1, T+1):
    A, B = map(int, input().split())
    print(A + B)