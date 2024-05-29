# Membership operator
# in, not in
# A in B
# A 값, B sequential Object
# 결과 값은 Boolean

# print("a" in "abc")

# bar = [3, 4, 5, 6]

# print(4 in bar)
# print(4 not in bar)

# in, not in은 출력값이 boolean
# in은 좌항에 있는 값이 우항에 있으면 True
# in not은 좌항에 있는 값이 우항에 없으면 True

# argSeqObj가 argValue 안에 들어가는지 확인하는 코드
# in 구현하기
def myInOperator(argValue, argSeqObj):
    for value in argSeqObj:
        if value == argValue:
            return True
        
    return False

# not in 구현하기
def myNotInOperator(argValue, argSeqObj):
    for value in argSeqObj:
        if value == argValue:
            return False
        
    return True