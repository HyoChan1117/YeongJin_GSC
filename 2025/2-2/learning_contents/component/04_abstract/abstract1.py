from abc import ABC, abstractmethod

class Bar(ABC):
    @abstractmethod
    def prtmethod(self, age):
        pass
    
    @abstractmethod
    def testmethod(self):
        pass
    
class Foo(Bar):
    def prtmethod(self, age):
        return print(f"나의 나이는 {age}살입니다.")
    
    def testmethod(self):
        return print("안녕하세요!")
    
obj = Foo()
obj.prtmethod(20)
obj.prtmethod(40)
obj.testmethod()