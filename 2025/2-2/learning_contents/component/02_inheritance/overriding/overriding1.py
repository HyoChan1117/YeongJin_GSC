class A:
    def __init__(self):
        print("A")
        
class B(A):
    pass
        
class C(B):
    pass

obj = C()  # A