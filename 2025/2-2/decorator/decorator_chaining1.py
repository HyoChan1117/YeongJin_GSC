def strip(func):
    def wrapper(msg:str):
        return func(msg.strip())  # chaining
    
    return wrapper  # chaining
    
def upper(func):
    def wrapper(msg:str):
        return func(msg.upper())  # chaining
    
    return wrapper  # chaining

@upper
def prt_something1(msg:str):
    print(f"prt1: {msg}")
    
@strip
def prt_something2(msg:str):
    print(f"prt2: {msg}")
    
@upper
@strip
def prt_something3(msg:str):
    print(f"prt3: {msg}")
    
prt_something1("  test1  ")
prt_something2("  test2  ")
prt_something3("  test3  ")