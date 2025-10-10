# 작성하지 않아도 기본으로 있는 것 (object 클래스)
class object:
    def __init__(self):
        pass

class A:
    pass
        
class B(A):
    pass
        
class C(B):
    pass

obj = C()  # A