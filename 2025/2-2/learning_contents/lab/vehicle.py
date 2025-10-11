# Vehicle 클래스 생성
class Vehicle:
    # 인스턴스 멤버 변수
    # name - 교통수단 이름 (문자열)
    # speed - 속도 (정수, km/h)
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        
        print(f"{name} ({speed} km/h)")
    
    # 인스턴스 멤버 메서드
    # move() -> <name> is moving at <speed> km/h 형태의 문자열 반환
    def move(self):
        print(f"{self.name} is moving at {self.speed} km/h")

# Car 클래스 생성 (Vehicle 상속)
class Car(Vehicle):
    # 추가 속성
    # 인스턴스 멤버 변수
    # fuel - 연료 잔량 (리터, 정수)
    def __init__(self, name, speed, fuel):
        super().__init__(name, speed)
        self.fuel = fuel
    
    # move() 메서드 오버라이드
    def move(self):
        # 연료가 0 이하일 경우
        # <name> has no fuel left 반환
        if (self.fuel <= 0):
            print(f"{self.name} has no fuel left")
        # 그렇지 않으면
        # <name> is driving at <speed> km/h with <fuel>L left 반환
        # 호출될 때마다 fuel 1 감소
        else:
            print(f"{self.name} is driving at {self.speed} km/h with {self.fuel}L left")
            self.fuel -= 1

# ElectricCar 클래스 생성 (Car 상속)
class ElectricCar(Car):
    # 인스턴스 멤버 변수
    # battery(%) 사용
    def __init__(self, name, speed, battery):
        super().__init__(name, speed, 0)
        self.battery = battery
    
    # move() 메서드 오버라이드
    def move(self):
        # 배터리가 0%일 경우
        # <name> battery empty
        if (self.battery == 0):
            print(f"{self.name} battery empty")
        # 그렇지 않으면
        # <name> is driving silently at <speed> km/h (battery: <battery>%) 반환
        # 호출될 때마다 battery 10% 감소
        else:
            print(f"{self.name} is driving silently at {self.speed} km/h (battery: {self.battery}%)")
            self.battery -= 10
            
# 객체 생성
v = Vehicle("Bicycle", 15)
c = Car("Sonata", 80, 3)
e = ElectricCar("Model 3", 100, 50)

# 출력
c.move()
c.move()
c.move()
c.move()

e.move()
e.move()
e.move()
e.move()
e.move()
e.move()
