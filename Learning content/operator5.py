# 산술연산자
# +, -, *, /

print(type(2 + 3.0))  # float

# 2 + 3.0
# int + float -> float # 이항 연산할 때 문제가 나타남
# float ? (int -> float) 형을 변환한다. Type conversion(형변환)

input_str = int(input("정수를 입력하세요"))
input_int = int(input_str)  # input_str : str -> integer by using int() function

# 4번과 10번, 11번에서 Type conversion이 발생
# 4번은 묵시적 형변환(Implicit type conversion), 10번과 11번은 명시적 형변환(Explicit type conversion)

# 언어를 배울 때 이항 연산을 하게 되면, 이때 좌항과 우항의 자료형이 같지 않을 때
# 묵시적으로 형변환을 무조건 해줘야 함
# -> 각 언어마다 묵시적으로 형변환 하는 규칙이 다름
# 그래서 언어마다 묵시적으로 형변환 하는 규칙을 연산자에 따라 어떻게 되는지 알아야 함
# 묵시적 형변환 규칙에 없으면 에러(error)가 뜸