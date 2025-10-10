# Python에서는 추상 클래스를 선언할 때, ABC 클래스를 상속 받아서 사용한다.
from abc import ABC, abstractmethod

# ABC 클래스를 상속 받아 추상 클래스 선언
class Bar(ABC):
    # 추상 인스턴스 메서드
    @abstractmethod
    def instance_method(self):
        pass
    
    # 추상 클래스 메서드
    @classmethod
    @abstractmethod
    def class_method(cls):
        pass
    
    # 추상 static 메서드
    @staticmethod
    @abstractmethod
    def static_method():
        pass
    
    # 추상 property (Getter) 메서드
    @property
    @abstractmethod
    def getter(self):
        pass
    
# obj = Bar()   # -> Bar 클래스는 추상 메서드를 구현하지 않았기 때문에 에러 발생