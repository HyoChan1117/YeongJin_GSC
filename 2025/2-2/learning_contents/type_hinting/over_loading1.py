# 파이썬은 동적 타입 언어이기 때문에 함수 오버로딩을 지원하지 않는다.
# 오버로딩은 기본적으로 매개변수의 개수와 타입을 다르게 하여 동일한 이름의 함수를 여러 개 정의하는 것을 의미한다.
# 파이썬은 오버로딩을 흉내내기 위해 다음과 같은 방법을 사용할 수 있다.
# 1. 매개변수의 개수: 가변 인자를 사용하여 매개변수의 개수를 다르게 할 수 있다.
# 2. 매개변수의 타입: isinstance() 함수를 사용하여 매개변수의 타입을 확인하고, 그에 따라 다른 동작을 수행할 수 있다.

from functools import singledispatch

# 기본 함수 정의 (Dispatcher 객체로 교체됨)
# @singledispatch : 첫 번째 인자의 타입에 따라 다른 구현을 선택하도록 만들어 줌
@singledispatch
def bar(x):
    # 기본 구현 (fallback): 지원되지 않는 타입이면 에러 발생
    raise TypeError("Unsupported type")

@bar.register(float)
def _(x: float):
    print("x is float")
    
@bar.register(int)
def _(x: int):
    print("x is int")
    
# bar("2")  # -> TypeError: Unsupported type