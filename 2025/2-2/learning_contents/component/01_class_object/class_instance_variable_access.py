class Bar:
    name = "Kim"
    
    def __init__(self):
        self.age = 20
        
    def hello(self):
        print(self.name)
        
# 객체 생성 과정 시작
obj = Bar()
obj.hello()