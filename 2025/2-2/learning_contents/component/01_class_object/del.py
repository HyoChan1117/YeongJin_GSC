class Bar:
    
    # Constructor
    def __init__(self):
        # Add instance member variables
        print("Constructor is invoked")
    
    def __del__(self):
        print("Destructor is invoked")
    
obj = Bar()
del obj
print("Program is terminated")