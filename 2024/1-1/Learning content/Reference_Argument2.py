# Argument(인자값)

# 2) keyword argument
# 매개변수의 이름을 이용해서 값을 지정함
# 매개변수 이름을 이용해서 지정해 주기 때문에 순서가 의미 없음
def pos(arg_a, arg_b, arg_c):
    print(arg_a, arg_b, arg_c)
    
pos(arg_c = 1, arg_a = 2, arg_b = 3)
