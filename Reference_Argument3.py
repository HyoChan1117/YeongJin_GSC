# Argument(인자값)

# 3) default argument
# 함수를 정의할 때 매개변수에 초기값을 지정해 줌
def kin(arg_a = 1, arg_b = 2, arg_c = 3, arg_d = 4):
    print(arg_a, arg_b, arg_c, arg_d)


# 특정 매개변수에 대한 값을 다르게 주고 싶을 때
# default argument를 사용함

# 매개변수에 초기값을 지정해줬다면 인자값과 개수와 무조건
# 동일하게 할 필요는 없음

# 함수를 호출할 때 인자값을 넣어주면 매개변수에서 지정했던
# 초기값을 무시함

# 인자값을 넣어주지 않으면 매개변수에서 지정했던 초기값이
# 출력됨

# default argument를 사용할 때는 2가지 조건이 있음
# 1. 모든 매개변수에 초기값을 설정
# 2. 초기 값을 가지는 매개변수는 제일 뒤 쪽에 위치
# ex) def pos(arg_a, arg_b, arg_d = 9, arg_c = 8) -> O
# ex) def pos(arg_a, arg_c = 8, arg_b, arg_d = 9) -> X

kin()  # 1, 2, 3, 4
kin(6, 7, 8, 9)  # 6, 7, 8, 9
kin(6)  # 6, 2, 3, 4
kin(6, 7)  # 6, 7, 3, 4
kin(6, 7, arg_d = 10)  # 6, 7, 3, 10

print("hello", end = "")  # hello