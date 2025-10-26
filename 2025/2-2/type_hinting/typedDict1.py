from typing import TypedDict

# 1) 필수 키만 있는 TypedDict (기본: total=True)
class Student(TypedDict):
    id: int
    name: str
    gpa: float
    
std1: Student = {"id": 2, "name": "ycjung", "gpa": 4.2}

std2: Student = {"id": 2, "name": "kim", "gpa": 4}

std3: Student = {"id": 3, "gpa": 4.2}