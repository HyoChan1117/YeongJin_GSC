# variable parameter : 가변 파라메터
# 1) *
# 2) **
        # * -> 가변 : tuple로 받겠다.
# 매개변수 앞에 "*"을 하나 붙이면 입력값을 tuple로 받는다.
def foo(arg_a, arg_b, *args):
    print(arg_a, arg_b)
    print(len(args))
    for value in args:
        print(value)

foo(1)
foo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)