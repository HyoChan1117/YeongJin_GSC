# NamedTuple
# 함수나 메서드의 반환값에 대해 많이 사용 됨
from typing import NamedTuple

class User(NamedTuple):
    name: str
    age: int
    gender: str
    
u1 = User("hyochan", 2, "M")

def create_user(name:str, age:int, gender:str)-> tuple:
    return User(name, age, gender)

name, age, gender = create_user("hyochan", 2, "M")
