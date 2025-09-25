class A:
    def __init__(self):
        self.name = "Class A"
        
class B(A):
    def __init__(self):
        super().__init__()
        self.age = 20
        
class C(B):
    def __init__(self):
        super().__init__()
        self.nick = "Class C"
        
obj = C()

print(obj.nick)
print(obj.age)
print(obj.name)