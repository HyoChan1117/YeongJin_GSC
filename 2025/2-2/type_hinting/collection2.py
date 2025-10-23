# collection -> 표현식, 콜렉션 요소의 자료형
# list, tuple, set, dict

# Generic type: 자료형을 미리 정하지 않고, 나중에 사용할 때 정하는 타입
# 타입이 변할 수 있는 재사용 가능한 코드 틀

# List
x: list[int] = [1, 2, 3, 4]
x = [2.0]
# x = (1, 2)  # Type checker가 잡아냄 -> 에러는 아님

# Tuple
y: tuple[int, int, int] = (1, 2, 3)
y = (1, 3)

# Dictionary
z: dict[str, str] = {"name" : "hyochan"}

# NamedDict