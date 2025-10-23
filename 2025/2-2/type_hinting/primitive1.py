# Type hinting을 함수에 적용한 예제
# 함수에서 매개변수와 반환값에 타입 힌트를 추가
# 반환값이 있으면 반환값의 자료형도 명시
def sum(x: int, y: int) -> int:
    return x + y

print(sum(1, 2))

# 반환값이 없는 함수의 예제
def greet() -> None:
    print("Hello, World!")

# 클래스에서 타입 힌트를 사용하는 예제
class Bar:
    # 생성자에서 멤버 변수의 타입 힌트를 지정
    # 반환 값이 없는 생성자이므로 반환값 타입은 None
    def __init__(self, x: int, y: str) -> None:
        self.x: int = x
        self.y: str = y
        
