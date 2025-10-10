class A():
    name = "A"
    
    def __init__(self):
        self.age = 20
        
class B(A):
    name = "B"
    
    def __init__(self):
        self.age = 100
        super().__init__()
    
# print(A.name)
# print(B.name)

obj = B()

print(obj.age)
