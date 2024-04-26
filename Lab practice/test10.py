# 사용자로부터 세 개의 정수를 입력받고, 이 중 가장 큰 숫자를 찾아 출력하는 프로그램 작성

# 첫 번째 정수를 입력 받는다.
inputValue1 = int(input("첫 번째 숫자를 입력하세요: "))

# 두 번째 정수를 입력 받는다.
inputValue2 = int(input("두 번째 숫자를 입력하세요: "))

# 세 번째 정수를 입력 받는다.
inputValue3 = int(input("세 번째 숫자를 입력하세요: "))

# 입력 받은 정수들 중 최대값을 구하는 식을 작성한다.
maxNum = max(inputValue1, inputValue2, inputValue3)

# 결과를 출력한다.
print("가장 큰 숫자는", maxNum, end="입니다.")

