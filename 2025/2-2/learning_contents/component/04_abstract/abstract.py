from abc import ABC, abstractmethod  # abc: abstract base class

# 추상클래스를 정의
# Java -> abstract class Bar {}

# Bar를 추상클래스로 정의
# 파이썬에서는 ABC 클래스를 상속받아 추상클래스를 정의

class Bar(ABC):
    
    # 추상메서드를 정의하려면 @abstractmethod 데코레이터를 사용
    @abstractmethod
    def instance_method(self):
        pass
    
# obj = Bar()  # Error: 추상 클래스 내부에 추상 메서드가 있기 때문에 인스턴스를 생성할 수 없음
    
class MyClass(Bar):
    def instance_method(self):
        print("MyClass : instance_method")
        
obj = MyClass()
obj.instance_method()