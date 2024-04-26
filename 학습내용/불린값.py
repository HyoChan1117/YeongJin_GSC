# =(대입연산자)을 기준으로 우측에 있는 것을 먼저 실행한 후 좌측으로 대입
# <, >와 같은 연산자는 비교할 때 사용되기 때문에 불린값이 출력됨
bar = 3 > 3 # <- 수식(Expression)
print(bar) # 결과값은 불린값으로 나옴


bar = 3 >= 3
print(bar)

# !=는 같지 않음
bar = 3 != 4
print(bar)


bar = 3 == 3
print(bar)


bar = True and False
print(bar)


bar = True or False
print(bar)