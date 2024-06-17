# Overloading
# 함수와 메서드에 적용이 된다.
# 사용 목적은? 프로그래머에게 코드 작성의 편리성을 제공하기 위해

def bar(a, b):
    return a + b

def foo(a, b, c):
    return a + b + c

def pos(a, b, c, d):
    return a + b + c + d

print(bar(2, 3))  # 5
print(foo(2, 3, 4))   # 9
print(pos(2, 3, 4, 5))   # 14


# 함수를 호출할 때 매개변수의 개수에 따라 호출하는 함수가 달라짐
# 동일한 함수를 정의
# 파이썬에서는 지원 안함
# function overloading(함수 오버로딩)

def bar(a, b):
    return a + b

def bar(a, b, c):
    return a + b + c

def bar(a, b, c, d):
    return a + b + c + d

print(bar(2, 3))  # 5
print(bar(2, 3, 4))   # 9
print(bar(2, 3, 4, 5))   # 14


# 가변 위치 인자를 이용하면 함수 오버로딩 기능을 구현할 수 있다.
def bar(*args):
    return sum(args)

print(bar(2, 3, 4, 5))

print(bar(2, 3, 4))
print(bar(2, 3))