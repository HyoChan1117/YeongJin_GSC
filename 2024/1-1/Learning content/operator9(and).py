
value = int(input("정수 입력: "))

# if value > 1 and value <= 3:
#     print("참")

# else:
#     print("거짓")


# Chained comparison  ->  파이썬에서의 특징
# 특정 구간을 선택할 때 사용
# False가 나와버리면 바로 종료
# and 연산자가 사이사이에 들어가 있기 때문에
# False가 나오는 순간 연산이 종료됨
if 1 < value <= 3:
    print("참")
else:
    print("거짓")