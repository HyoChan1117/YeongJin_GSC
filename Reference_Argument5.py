# variable parameter : 가변 파라메터
# 1) *
# 2) **
        # * -> 가변 : tuple로 받겠다.
# 매개변수 앞에 "*"을 하나 붙이면 입력값을 tuple로 받는다.
def foo(*args):
    print(len(args))
    for value in args:
        print(value)

foo(1)
foo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

def bar(*args):
    if len(args) == 1:
        start = end = args[0]
    elif len(args) == 2:
        start, end = args
    
    for dan in range(start, end + 1):
        for num in range(1, 10):
            print(f"{dan} X {num} = {dan * num}")
            
bar(2)
bar(2, 5)