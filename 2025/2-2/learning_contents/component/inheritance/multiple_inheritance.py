# 파이썬 OOP
# 클래스 선언
# object 객체에서 상속 받음 - 자동
class A(object):
    pass

class B(object):
    pass

# 상속
class Foo(A, B):
    pass

# 다중상속 지원: 다이아몬드 상속 문제 발생 가능
# 

# 객체 생성
obj = Foo()

# 상속 