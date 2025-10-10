class Bar:
    # 멤버 변수(속성) -> 1. 인스턴스 멤버 변수   2. 클래스 멤버 변수
    
    # 클래스 멤버 변수
    # 실무 -> 여기!
    cls_test = 100
    
    def __init__(self):
        # 초기화 작업
        # 인스턴스 멤버 변수
        # 실무 -> 여기!
        self.new_var = 1
        pass
    
    def __del__(self):
        # 객체 소멸 전 자원 정리
        # 자원 정리
        pass
    
    # 멤버 메서드 -> 1. 클래스 메서드   2. 인스턴스 메서드
    # 클래스 멤버 메서드
    # cls - class object에 있는 속성에 접근하기 위해 사용
    # @(데코레이터)를 사용해서 클래스 메서드를 구분
    @classmethod
    def class_method(cls):
        pass
    
    # 인스턴스 멤버 메서드
    # self - 특정 인스턴스에 있는 속성에 접근하기 위해 사용
    def instance_method(self):
        pass
    
    # 스태틱 멤버 메서드
    # 참조변수가 없음
    # @(데코레이터)를 사용해서 스태틱 메서드를 구분
    @staticmethod
    def static_method():
        pass

# 인스턴스 생성
obj1 = Bar()
obj2 = Bar()