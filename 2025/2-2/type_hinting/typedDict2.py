# TypeDic -> 스키마 정의 -> dictionary -> JSON

from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    gender: str

x1: User = {"name": "hyochan", "age": 20, "gender": "M"}
x2: User = {"name": "hyochan", "age": "30", "gender": "W"}
