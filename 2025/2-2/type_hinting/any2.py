class Bar:
    # 생성자는 반환형이 없기 때문에 None이 자동 생성
    # 각각의 멤버에 대한 자료형 명시
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

from typing import Any

# Any: 모든 타입을 허용한다.
# 이 변수는 어떤 타입이 와도 괜찮다.

# x: Any = 2  # 어떤 타입도 허용
x: int | float | str = 1  # int or float or str -> 조합