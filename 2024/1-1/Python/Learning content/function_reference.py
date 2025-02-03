bar = [2, 3, 5]

def foo(arg_list):   # 메모리 주소 값
    arg_list[1] = 100
    
foo(bar)

print(bar)   # 2, 100, 5