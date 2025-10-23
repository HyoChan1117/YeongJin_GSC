# 자료구조란?
# 데이터를 효율적으로 저장하고 관리하는 방법을 제공하는 체계

# collection framework: 자료 구조
# abstract data type(ADT)을 구현해 놓은 것
# abstract data type(ADT): 자료구조의 논리적 모델
# ex) List, Set, Map, Stack, Queue


# Python Type Hint의 종류
# 기본 데이터 타입(Primitive Data Type)\
# 컬렉션 타입(Collection Type)

# list는 type hint 작성 시 요소의 타입을 지정
x_list_int: list[int | float] = [1, 2, 3]
x_list_int = ["2", 3, 4.0]

# tuple은 type hint 작성 시 요소의 개수와 타입을 명확히 지정
# 요소의 개수를 따지는 것은 tuple만 해당
x_tuple_int: tuple[int] = (2, 3)   # 지정하지 않을 시 오류 발생
x_tuple_int: tuple[int, str, float] = (2, "3", 2.0)

# tuple은 가변 길이도 가능
y: tuple[int, ...]
y = (1, 2, 3, 4, 5)
y = (2, 3, 4, 5, 6)

# dict는 type hint 작성 시 키와 값의 타입을 지정
x_dic_str_float: dict[str, float] = {"k1": 1.0, "k2": 2.0}
x_dic_str_float = {1: 2.0}
x_dic_str_float = {"k1": 2}

# set은 type hint 작성 시 요소의 타입을 지정
x_set_bool: set[bool] = {True, False}