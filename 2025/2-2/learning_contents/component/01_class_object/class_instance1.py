class Bar:
    cValue = 100
    
    # instance method
    def i_method(self):
        self.iValue = 20
    
    # class method
    @classmethod
    def c_method(cls):
        cls.cValue = 30
    
obj = Bar()
obj.i_method()
Bar.c_method()
del obj.iValue
del Bar.cValue
del Bar.i_method
Bar.cValue = 1000