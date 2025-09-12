class Foo:
    def __init__(self):
        self.name = ""
        self.age = ""
    
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age
    
obj = Foo()

# 객체 안에 멤버들을 동적으로 추가, 삭제 가능
obj.set_name("Hong")   # -> Foo.set_name(obj, "Hong")
print(obj.name)

del obj.name    # 동적으로 멤버 삭제


# 동적으로 멤버 추가
obj.address = "Seoul"
print(obj.address)


obj.set_age(14)
print(obj.age)
del obj.age