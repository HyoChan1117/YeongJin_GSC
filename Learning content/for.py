# loop
# 3개 : Legacy - IT에서 이전에 있던 시스템을 Legacy라고 부름
# Legacy C언어, JAVA언어
# 1) for
# 2) while
# 3) do-while

# for 아이템 in 반복 아이템 리스트:
#     실행 문장


# 화면에 1을 10번 출력한다. -> 반복 10번
# 반복의 횟수만 10번이면 되기 때문에 range(10)만 쓰면 됨
# "_"를 사용함으로써 변수가 코드에 쓰이지 않는다고 생각할 수 있게 됨
# "value"나 다른 변수 이름을 사용하게 된다면 변수가
# 코드에 쓰일 것 같다는 생각이 되기 때문에 그냥 "_" 사용
for _ in range(10):
    print("1")
# range(반복 회수)
# range(시작값, 종료값) : 시작 값은 첫 번째 증감값에 대한 적용이 가능할 때 선택
# range(시작값, 종료값, 증감값)

# 증감값이 기본적으로 1이기 때문에 출력이 안됨
for value in range(7, -8):
    print(value)
    
# range를 쓸 때 반복의 횟수가 0번이 될 수도 있음
# 1번째 반복은 다음으로 넘어갈 수 있을 때 사용 가능

for value in range(5, 1, -2):
    print(value)  # 5, 3
# for value in range(5, 1, 1):
#    print(value)

# range의 종료값은 포함하지 않는다.
for value in range(5, -20, -5):
    print(value)  # 5, 0, -5, -10, -15


# range 함수에서 반복의 횟수만 사용할 때
# for _ in range(9):

# range 함수에서 시작값, 종료값을 사용할 때
# 공통 : 아이템을 코드상에서 사용함
# 증감값이 1일 때는 시작값, 종료값만 사용하면 됨
# 증감값이 1을 제외하고 나머지 값을 사용해야 하는 경우 사용하면 됨

for _ in range(8):
    print(_, end="")

print("*" * 20)

for dan in range(2, 10):
    print(dan, end="")
    
    