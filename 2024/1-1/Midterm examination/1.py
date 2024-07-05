# 사용자로부터 두 개의 실수를 입력 받아, 이후 사용할 연산자를 선택하고, 최종적으로 결과를 원하는 자료형으로 출력하는 프로그램을 작성한다.

# 두 개의 실수를 입력 받는다.
num1 = float(input("첫 번째 값을 입력 하세요"))
num2 = float(input("두 번째 값을 입력 하세요"))

# 사용할 연산자를 선택 받는다.
operator = input("연산자를 선택 하세요 (+, -, *, / 중 하나 입력)")

# 원하는 자료형으로 결과를 출력한다.
data_type = input("결과 값 자료형(integer, float, string 중 하나 입력)")

# 입력 받은 두 실수를 계산하는 함수를 정의한다.
def calculate(arg1, arg2):
    sum = arg1 + arg2
    sub = arg1 - arg2
    mul = arg1 * arg2
    div = arg1 / arg2
    return sum, sub, mul, div
    
# 두 실수를 계산하는 함수를 호출하여 선택한 자료형에 따라 결과를 출력한다.
sum, sub, mul, div = calculate(num1, num2)

if data_type == "integer":   # 자료형인 "정수"인 경우
    if operator == "+":   # 연산자가 "+"인 경우
        print(num1, operator, num2, "=", int(sum))
    elif operator == "-":   # 연산자가 "-"인 경우
        print(num1, operator, num2, "=", int(sub))
    elif operator == "*":   # 연산자가 "-"인 경우
        print(num1, operator, num2, "=", int(mul))
    elif operator == "/":   # 연산자가 "-"인 경우
        print(num1, operator, num2, "=", int(div))

if data_type == "float":   # 자료형인 "float"인 경우
    if operator == "+":   # 연산자가 "+"인 경우
        print(num1, operator, num2, "=", float(sum))
    elif operator == "-":   # 연산자가 "-"인 경우
        print(num1, operator, num2, "=", float(sub))
    elif operator == "*":   # 연산자가 "-"인 경우
        print(num1, operator, num2, "=", float(mul))
    elif operator == "/":   # 연산자가 "-"인 경우
        print(num1, operator, num2, "=", float(div))
        
if data_type == "string":   # 자료형인 "string"인 경우
    if operator == "+":   # 연산자가 "+"인 경우
        print(num1, operator, num2, "=", str(sum))
    elif operator == "-":   # 연산자가 "-"인 경우
        print(num1, operator, num2, "=", str(sub))
    elif operator == "*":   # 연산자가 "-"인 경우
        print(num1, operator, num2, "=", str(mul))
    elif operator == "/":   # 연산자가 "-"인 경우
        print(num1, operator, num2, "=", str(div))