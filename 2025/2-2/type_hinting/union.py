# Union -> 집합의 원소 중 하나이면
# - True 반환
# - 모두 아니면 False 반환

from typing import Union

x: Union[int, float, bool]  # Union 타입 힌트
x_new: int | float | bool   # Python 3.10 이상에서 지원하는 Union 표기법

# Union 타입 힌트는 지정된 자료형 중 하나라도 맞으면 됨
x = 2
x = 3.0
x = False
x = "2"