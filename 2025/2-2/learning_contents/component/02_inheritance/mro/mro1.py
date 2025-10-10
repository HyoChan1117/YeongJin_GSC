# D.mro = D -> B -> C -> A -> Object
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()  # C class object 이동
        
    def prt(self):
        print("B - prt")

class C(A):
    def __init__(self):
        print("C")
        super().__init__()  # A class object 이동
        
    def prt(self):
        print("C - prt")

class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()  # B class object 이동
        
    def prt(self):
        print("D - prt")
    
print(C.__mro__)
obj = D()
obj.prt()