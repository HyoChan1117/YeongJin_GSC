# 사용자로부터 두 정수 A와 B를 입력 받은 다음, A+B를 출력하는 프로그램 작성
while True:
    A, B = map(int, input().split())
    sum = A + B
    if A == "":
        break
    print(sum)
