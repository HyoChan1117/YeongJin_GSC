class Parent:
    def __init__(self):
        self.name = "Parent"

class Child(Parent):
    def __init__(self):
        super().__init__()  # Parent의 name 값을 저장
        self.name = "Child" # Child의 name 값으로 덮어씀
        # super().__init__()
        
obj = Child()
print(obj.__dict__)