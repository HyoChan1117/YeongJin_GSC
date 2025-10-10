# 변수의 동작모드
# Getter / Setter -> Method
# Setter: 유효하지 않은 범위의 값을 변수에 들어가는 것을 막을 수 있음
# Getter: 변수의 값을 읽어오는 용도
class A:
    def __init__(self):
        self.__age = None
    
    # 변수의 이름과 동일한 함수를 사용하여 getter, setter 구현
    # getter method: 값을 읽어오는 용도
    @property
    def age(self):
        return f"나이는 : {self.__age}"
    
    # setter method: 유효하지 않은 값이 들어가는 것을 막음
    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("음수 값 오류")
        self.__age = age
            
obj = A()
obj.age = 30
print(obj.age)
obj.age = -100