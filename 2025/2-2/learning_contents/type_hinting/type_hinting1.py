# Type hinting: 변수, 매개변수, 반환값에 타입을 명시
# -> 부가적인 정보일 뿐이지 타입을 강제하지는 않음

x : int = 3

def div(a : int, b : int) -> float:
    return (a / b)

print(4 / 2)
print(4.0 / 2.0)

print(div(2.0, 3.0))  # -> Error는 아님. 타입 힌팅은 강제가 아니기 때문
print(div(2, 3))      # -> OK
print(div(2, 3.0))    # -> Error는 아님. 타입 힌팅은 강제가 아니기 때문