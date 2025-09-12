class Foo:
    univ = "YJU"
    dept = "GSC"
    
    def __init__(self, name):
        self.name = name
        
    def prt_info(self, age):
        self.age = age
        print(self.name, self.age)
        
obj1 = Foo("Kim")
obj1.prt_info(20)
obj2 = Foo("Hong")
obj2.prt_info(30)