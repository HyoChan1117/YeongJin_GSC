# variable parameter : 가변 파라메터
# 1) *
# 2) **
        # ** -> 가변 : Dictionary로 받겠다.
        #                 Key : value
        #                 1개
# 매개변수 앞에 "*"을 하나 붙이면 입력값을 tuple로 받는다.
def foo(**args):
    print(len(args))
    
    for key, value in args.items():
        print(f"key: {key}, value : {value}")

foo(test = 2, king = 3)
foo(test = 2, king = 3, lion = 4)