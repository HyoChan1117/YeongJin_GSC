class A:
    def __init__(self):
        self.name = "Class A"
        
    @classmethod
    def prt_something(cls):
        print("Invoked prt_something")
        
class B(A):
    def __init__(self):
        super().__init__()
        self.name = "Class B"
        
obj = B()
print(obj.name)
B.prt_something()