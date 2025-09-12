class Foo:
    # Member method
    # instance와 class 기본적으로 구분
    
    # instance member method
    # self -> this  => 참조변수
    # 매개변수 0개
    def x(self):
        pass
    
    # class member method
    # cls -> class  => 참조변수
    @classmethod   # decorator: 메서드 위에 @붙임
    def y(cls):
        pass
    
    # static member method
    # 참조변수가 필요없음
    @staticmethod
    def z():
        pass

    # 1. class Member Method
    # 2. instance Member Method
    # 3. static Member Method