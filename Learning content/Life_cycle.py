def bar() :
    msg = "안녕하세요"
    foo()
    return msg

def foo():
    print("foo")
    pos()
    print("1")
    kin()
    
def pos():
    print("pos")
    
def kin():
    print("kin")
    
bar()