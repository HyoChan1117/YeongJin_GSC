class A:
    pass
class B1(A):
    pass
class B2(A):
    pass
class C1(B1, B2):
    pass
class C2:
    pass
class D(C1, C2):
    pass

print(D.__mro__)