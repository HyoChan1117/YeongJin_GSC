class Foo:
    pass


obj = Foo()

# 파이썬에서는 프로그램이 실행되면서 동적으로 멤버 변수를 추가할 수 있다.
obj.x = 100   # Foo.x(obj) = 100

print(obj.x)  # 100