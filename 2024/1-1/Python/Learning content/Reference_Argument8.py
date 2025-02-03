# variable parameter : 가변 파라메터
# 1) *
# 2) **
        # ** -> 가변 : Dictionary로 받겠다.
        #                 Key : value
        #                 1개
# 매개변수 앞에 "*"을 하나 붙이면 입력값을 tuple로 받는다.

def foo(arg_a, arg_b, arg_c, arg_d, arg_e):
    print(arg_a, arg_b, arg_c, arg_d, arg_e)
        
# foo(1, 2, 3, 4, 5)

arg_list = [ value for value in range(1, 6)]

foo(*arg_list)