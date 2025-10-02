# 변수의 동작모드
# Getter / Setter -> Method
# Setter: 유효하지 않은 범위의 값을 변수에 들어가는 것을 막을 수 있음
# Getter: 
class A:
    def __init__(self):
        self.__age = None
    
    # getter method
    @property
    def age(self):
        return f"나이는 : {self.__age}"
    
    # setter method
    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("음수 값 오류")
        self.__age = age
            
obj = A()
obj.age = 30
print(obj.age)
obj.age = -100