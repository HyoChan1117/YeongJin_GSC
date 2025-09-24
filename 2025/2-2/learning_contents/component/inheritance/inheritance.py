class Parent():
    def prt_name(self):
        print(self.name)
    
class Child(Parent):
    def __init__(self):
        self.name = "Child"
        
obj = Child()
obj.prt_name()