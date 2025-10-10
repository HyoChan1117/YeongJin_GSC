class Parent:
    def prt(self):
        print("Parent")

class Child(Parent):
    def prt(self):
        print("Child")
        
obj = Child()
obj.prt()  # Child