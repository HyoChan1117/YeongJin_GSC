
# Call-by-value, Call-by-reference

bar = 3

# 값이 복사가 되어서 가는 것 : Call-by-value
# 복사가 되어서 넘어가기 때문에 원본 값에 영향이 X
def foo(bar):
    bar = bar + 1
    print("1: ", bar)

foo(bar)
print("2: ", bar)

# 이 문제를 이해하기 위해서는
# 변수의 접근 범위를 봐야 함

# Variable
# 1) Primitive : 자연 세계에서 사용하는 원시적인 값을
# 저장하는 변수(number(int, float), string, boolean)
# 2) Reference : 메모리 주소 값을 저장하는 변수


# 메모리 주소 값이 넘어가는 것 : Call-by-reference
# 메모리 주소 값이 넘어가기 때문에 원본 값에 영향을 줌
bar = [20, 30, 40]  #  -> bar : reference variable

def foo(argList):
    argList[2] = 100
    argList[0] = 300
    
foo(bar)

print(bar)