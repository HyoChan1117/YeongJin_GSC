# 사용자로부터 정수 N을 입력 받아, 혜아가 N바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름을 출력하는 프로그램 작성

N = int(input())

A = ""
for _ in range(0, N // 4):
    A = A + "long "
        
print(f"{A}int")