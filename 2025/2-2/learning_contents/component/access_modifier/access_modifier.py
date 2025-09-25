class A:
    def __init__(self):  # -> private X
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"
        
obj = A()

print(obj.public)  # 
print(obj._protected)  # 내부 전용으로 사용할거야
print(obj.__private)  # 

print(obj._A__private)