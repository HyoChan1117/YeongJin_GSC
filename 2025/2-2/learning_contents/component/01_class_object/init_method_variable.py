# 클래스 정의
class Foo:
    # 1. 생성자: 객체의 초기화 작업을 하는 메서드
    def __init__(self):
        pass
    
    # 2. 멤버 속성: 데이터
    
    name = "Class Foo"
    # 3. 멤버 메서드: 데이터를 가공하기 위한 알고리즘
    def test(instance_ref):
        instance_ref.name = "Instance member variable: Foo"

obj = Foo()  # 객체 생성
Foo.test(obj)  # 멤버 메서드 호출

# 인스턴스 멤버변수를 선언하는 방법
# 1. 생성자에서 선언
# 2. 멤버 메서드에서 선언
# 3. 소멸자에서 선언

# 왜 보통 생성자에서 선언을 할까?
# 멤버 메서드에서 선언하면 객체를 생성하고
# 멤버 메서드를 호출해야 멤버변수가 생성됨
# 객체가 생성될 때 멤버변수가 자동으로 생성됨

print(obj.name)  # 인스턴스 멤버 변수



# 동적 타입 언어
# 1. 다형성이 희석됨
# 2. 객체 안에 멤버들을 동적으로 추가, 삭제 가능
# 3. 