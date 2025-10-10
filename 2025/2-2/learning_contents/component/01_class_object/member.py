# Member -> variable, method

# Member
# 1) class member:
# 2) instance member

# class member variable: 객체들 간에 데이터가 공유되어 있어야 함
# class member method: 클래스 멤버 변수를 가공할 때


class Foo:
    # class Member Variable
    age = 20
    name = "Kim"
    
    # Constructor
    # self: 특정 객체를 가리키는 참조변수
    def __init__(self):
        # instance Member Variable
        self.university = "YJU"
    
    # Member variable
    # 1) instance MV
    # 2) class MV
    
    # Member method
    # 1) instance MM
    # 2) class MM
    
obj = Foo()
    
print(Foo.age)
print(Foo.name)
print(obj.university)