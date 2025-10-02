class A:
    def __init__(self):
        self._age = 20
        
class B(A):
    def __init__(self):
        super().__init__()
        self.age = 30
        
obj = B()
print(obj.__dict__)