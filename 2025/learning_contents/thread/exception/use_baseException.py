try:
    print("1")

    raise KeyboardInterrupt

    print("2")
    
    print("3")
except:  # -> 가장 최후의 수단인 BaseException인 경우
    print("3.1")
    
print("7")