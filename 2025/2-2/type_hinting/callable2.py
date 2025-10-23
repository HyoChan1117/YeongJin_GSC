from typing import Optional, Union, NoReturn, Callable

# 일급 시민: 프로그램을 구성하는 요소들이 
# 1. 변수에 저장될 수 있고,
# 2. 변수로부터 읽을 수 있으며,
# 3. 함수의 인자나 반환값으로 사용될 수 있는 것

def test():
    ...
    
# 1. test 함수의 주소값이 x 변수에 저장됨
x = test

# 2. x 변수로부터 함수를 읽음
x()

# 3. 함수의 인자나 반환 값으로 사용될 수 있는 것
def run(func):
    return func

run(test)


