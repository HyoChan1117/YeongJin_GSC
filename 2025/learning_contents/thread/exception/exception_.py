num = 2

try:
    print("10")
    
    if num == 1:
        raise ValueError
    else:
        raise ZeroDivisionError  # ZeroDivisionError을 처리하기 위한 예외 처리를 못해서 에러

    print("20")
    
except ValueError:
    print("30")
# except ZeroDivisionError:
#     print("50")
    
print("40")

# 10만 찍히고 ZeroDivisionError 발생