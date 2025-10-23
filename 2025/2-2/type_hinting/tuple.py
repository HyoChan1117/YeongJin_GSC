# 자료구조란?
# 데이터를 효율적으로 저장하고 관리하는 방법을 제공하는 체계

# collection framework: 자료 구조
# abstract data type(ADT)을 구현해 놓은 것
# abstract data type(ADT): 자료구조의 논리적 모델
# ex) List, Set, Map, Stack, Queue


# Python Type Hint의 종류
# 기본 데이터 타입(Primitive Data Type)\
# 컬렉션 타입(Collection Type)

def get_total_avg(x: int, y: int) -> tuple:
    sum = x + y
    avg = sum / 2
    return sum, avg

x_tuple: tuple = (1, 2, 3)

x_tuple = [1, 2, 3]

x_dict: dict = {1:2, 3:4, 5:6}

x_set: set = {1, 2, 3, 4}

x_range: range = range(1, 10)