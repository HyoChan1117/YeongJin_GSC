from typing import overload, Union

@overload
def prt(x: Union[int, float]) -> str:
    # 실제 동작: int/float에 따라 다른 문자열을 반환
    if isinstance(x, int):
        return "x is int"
    elif isinstance(x, float):
        return "x is float"
    
    # int, float 이외 타입이 들어오면 런타임 오류 발생
    raise TypeError("x is not int or float")

print(prt(10))    # "int": 10
print(prt(3.14))  # "float": 3.14