num = 1

try:
    print("1")

    if num == 2:
        raise KeyboardInterrupt

    print("2")
    
except KeyboardInterrupt:
    print("4")
else:  # 예외가 발생되지 않았을 때 실행
    print("5")
finally:  # 예외와 상관없이 실행 -> 꼭 필요해야 하는 코드
    print("6")

print("7")