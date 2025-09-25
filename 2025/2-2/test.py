class A:
    def __init__(self):
        self.name = "Class A"
        
    @classmethod
    def prt_something(cls):
        print("Invoked prt_something")
        
class B:
    def __init__(self):
        super().__init__()
        self.age = 20
        
obj = A()
A.prt_something()