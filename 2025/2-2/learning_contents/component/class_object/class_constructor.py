class Foo(object):  # ()는 상속 관계를 정의하기 위해 사용
    # callback 함수 -> 내가 만든 함수를 다른 사람이 호출
    
    # Constructor  
    def __init__(self, name, age):   # __init__(self) -> 생성자
        self.name = name
        self.age = age
        
        # __는 매직 메서드 -> callback 함수
    
    # Member Method

obj = Foo("Kim", 20)  # ()에서 생성자 호출

print(type(obj))