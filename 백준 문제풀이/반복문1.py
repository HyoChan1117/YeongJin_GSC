# 사용자로부터 자연수 N을 입력 받아, 구구단 N단을 출려하는 프로그램 작성

N = int(input())

for _ in range(1, 10):
    print(f"{N} * {_} = {N * _}")