# Pylance의 Type Checking 모드를 켠 상태에서 이 코드를 실행
x: int = 2

# x = "3"   # Pylance의 Type Checker가 오류를 잡는다.

y : float = 3.0

y = "2"

z: str = "hello"
z = 10

a: bool = True
a = "False"
a = False

b: bytes = b"test"
