# 일급 함수

def test(x: int, y: float, z: str)-> str:
    return f"{x}, {y}, {z}"
    
from typing import Callable
    
# my_func -> argument -> 3개, 반환형은 문자열
# Callable[매개변수 자료형, 반환값 자료형]
# Callable[[매개변수1 자료형, 매개변수2 자료형, ...], 반환값 자료형]
def run(my_func: Callable[[int, float, str], str], a: int, b: float, c: str)-> None:
    print(my_func(a, b, c))
    
# test 함수를 run 함수의 매개변수에 할당
run(test, 1, 2.0, "3")

# def test_2(x, y):
#     ...
    
# run(test_2)