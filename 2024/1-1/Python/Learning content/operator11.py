def bar(argValue):
    print("Bar is invoked")
    return argValue

if True and bar(2) == 2:
    print("참")
else:
    print("거짓")
    
if False and bar(2) == 2:
    print("참")
else:
    print("거짓")
    
if True or bar(2) == 2:
    print("참")
else:
    print("거짓")