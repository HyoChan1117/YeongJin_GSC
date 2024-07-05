bar = [2, 3, 5]

def foo(arg_list):   # 메모리 주소 값
    copied_list = arg_list[:]
    
    copied_list[0] = 100
    
foo(bar)

print(bar)   # 2, 100, 5

def kin(arg_list):
    arg_list[0] = 200
    
kin(bar.copy())
print(bar)

