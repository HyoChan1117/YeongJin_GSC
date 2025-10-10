# ABC 클래스를 사용하지 않고 강제성을 부여할 수도 있지만 이런 방법도 있다.
# 이 방식은 옛날 방식 -> 요즘은 ABC 클래스를 이용해서 강제성 부여

class Bar:
    # 반드시 자식 클래스에서 구현되기를 희망
    def test(self):
        raise NotImplementedError
    
class Foo(Bar):
    pass

obj = Foo()
obj.test()