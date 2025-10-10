# 추상화 (Abstract) -> OOP
# 미완성 + 강제성
# getter, setter도 추상 메서드로 구현할 수 있음

from abc import ABC, abstractmethod

class Bar(ABC):
    @classmethod
    @abstractmethod
    def test(cls):
        pass
    
class Foo(Bar):
    @classmethod
    def test(cls):
        print("추상")
    
obj = Foo()
obj.test()