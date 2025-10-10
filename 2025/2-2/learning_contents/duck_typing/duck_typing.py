class Duck:
    def quack(self):
        print("꽥꽥!")

class Person:
    def quack(self):
        print("저도 오리 흉내 낼 수 있어요: 꽥꽥!")

def make_it_quack(obj):
    obj.quack()  # obj가 quack 메서드만 있으면 실행 가능

duck = Duck()
person = Person()

make_it_quack(duck)    # 꽥꽥!
make_it_quack(person)  # 저도 오리 흉내 낼 수 있어요: 꽥꽥!