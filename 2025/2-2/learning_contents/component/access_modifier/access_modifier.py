class A:
    def __init__(self):  # -> private X
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"
        
obj = A()

print(obj.public)  # 누구나 접근 가능
print(obj._protected)  # 내부 전용으로 사용할거야
# print(obj.__private)  # 접근 불가 (AttributeError)

print(obj._A__private)  # 접근 가능 (name mangling)
# _A__private = A 클래스의 __private 멤버에 접근하는 방법