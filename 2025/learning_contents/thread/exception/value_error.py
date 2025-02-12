# 1. 사용자 입력 오류
# 숫자를 입력 받아야 하지만, 문자를 입력할 경우 발생하는 오류
num = input("숫자를 입력하세요: ")

try :
    raise ValueError
# result = int(num) * 2
except ValueError:
    print("ValueError 예외 발생")
    
print("결과: 0")