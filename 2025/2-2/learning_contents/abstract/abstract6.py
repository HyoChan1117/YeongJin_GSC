from abc import ABC, abstractmethod

class Bar(ABC):
    def test_1(self):
        raise NotImplementedError("test_1 must be overridden in subclass")
    
    @abstractmethod
    def test_2(self):
        pass
    
class Foo(Bar):
    # def test_1(self):
    #     print("test_1")
    def test_2(self):
        print("test_2")
        
obj = Foo()
obj.test_1()  # Foo 클래스에서 test_1을 오버라이드하지 않았기 때문에 Bar 클래스의 test_1이 호출됨
obj.test_2()