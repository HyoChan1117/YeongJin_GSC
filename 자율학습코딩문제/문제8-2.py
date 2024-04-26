# 사용자로부터 초기값을 입력 받아 사칙연산 계산을 해서 결과를 출력하는 프로그램 작성

# 전역 변수 선언 및 사용자로부터 입력 받기
baseValue = float(input("기본값을 입력하세요: "))

# 더하기, 빼기, 곱하기, 나누기를 출력한다.
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")

select = int(input("선택: "))
num_input = int(input("숫자 입력: "))

def selectOperation():
    global baseValue
    if select == 1 :
        baseValue = baseValue + num_input
    elif select == 2 :
        baseValue = baseValue - num_input
    elif select == 3 :
        baseValue = baseValue * num_input
    elif select == 4 :
        baseValue = baseValue / num_input
    
    print("연산 결과: ", baseValue)
    
selectOperation()