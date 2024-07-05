# Argument(인자값)

# 1) positional argument
# 위치 기반으로 인자값이 매개변수로 들어감
# 인자값과 매개변수는 순서대로 1:1 매칭이 돼서 들어감
def foo(arg_a, arg_b, arg_c):
    print(arg_a, arg_b, arg_c)
    
foo(1, 2, 3)

# 함수를 정의했을 때
# 매개변수 개수와 인자값을 개수를 동일하게 해줘야 함