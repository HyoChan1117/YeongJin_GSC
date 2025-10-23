# Callable -> 함수, 메서드

from typing import Callable

def sum(x: str, y: float) -> float:
    return x + y 

sum_2 = sum  # 함수 자체를 변수에 할당
print(sum_2(2, 3))  # 할당된 변수를 통해 함수 호출

# Callable 타입 힌트 예제
# Callable[[매개변수], 반환값]
def do_something(x: float, y: float, op: Callable[[float, float], float]) -> float:
    return op(x, y)

# do_something 함수에 sum 함수를 전달
# 매개변수의 개수와 반환값의 타입이 일치해야 함
do_something(1, 2, sum)