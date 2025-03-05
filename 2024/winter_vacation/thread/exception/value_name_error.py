# 1. 사용자 입력 오류
# 숫자를 입력 받아야 하지만, 문자를 입력할 경우 발생하는 오류
num = int(input("1 또는 2를 입력하세요: "))

try :  # try 안에는 예외가 발생되지 않는다는 전제 하에 코드를 작성
    if num == 1:
        raise ValueError  # raise의 역할 -> 예외를 발생
    else:
        raise NameError
except ValueError:  # except의 역할 -> 발생한 예외를 해결하기 위한 코드가 들어가야 함
    print("ValueError 예외 발생")
except NameError:
    print("NameError 예외 발생")
    
# try 안에는 여러 예외가 발생할 수 있기 때문에 예외마다 구분이 필요하고,
# 이것 때문에 이름을 구분하여 사용
    
print("결과: 0")