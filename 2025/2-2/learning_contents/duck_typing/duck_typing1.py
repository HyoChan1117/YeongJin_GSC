# 오리 클래스 생생
class Duck:
    # 오리 울음소리 메서드 생성
    def quack(self):
        print("나는 오리입니다. 꽥꽥")
        
# 사람 클래스 생성
class Human:
    # 오리 울음소리 메서드 생성
    def quack(self):
        print("나는 사람이지만 오리 소리를 낼 수 있어요. 꽥꽥")
        
# 매개변수로 인스턴스를 가리키는 참조변수를 사용하는 메서드 생성
def prt_quack(obj):
    return obj.quack()

# 인스턴스 생성
duck = Duck()
human = Human()

# 메서드 사용
prt_quack(duck)
prt_quack(human)