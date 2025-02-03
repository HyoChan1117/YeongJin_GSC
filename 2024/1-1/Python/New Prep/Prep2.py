# 정수를 입력 받아서, 짝수이면 "짝수"를 출력. "짝수가 아니면 아무것도 출력하지 않는다."

num = int(input("정수를 입력하세요: "))

if num % 2 == 0:
    print("짝수")
elif num % 2 == 1:
    print("홀수")

if num % 2 == 0:
    print("짝수")
if num % 2 == 0:
    print("홀수)")

# 둘 중에 하나는 무조건 선택해야 하는 경우(정답)
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")