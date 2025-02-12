# 1. 사용자 입력 오류
# 숫자를 입력 받아야 하지만, 문자를 입력할 경우 발생하는 오류
num = input("숫자를 입력하세요: ")
try:
    result = int(num) * 2 # valueError 발생 가능
    print(f"결과: {result}")
except ValueError:
    print("정수를 입력하세요")