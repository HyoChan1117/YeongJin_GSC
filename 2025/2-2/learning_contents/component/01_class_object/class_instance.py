class Bar:
    # instance method
    def i_method(self):
        self.iValue = 20
    
    # class method
    @classmethod
    def c_method(cls):
        cls.cValue = 30
        
obj = Bar()
obj.i_method()   # == Bar.i_method(obj)
obj.c_method()   # == Bar.c_method()
print(obj.iValue)
print(obj.cValue)