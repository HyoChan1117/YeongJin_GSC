try:
    print("pos")
    
    print(1/0)  # 주석 처리 on/off에 따른 결과 값 확인
    # 주석 처리를 했을 경우: NameError 발생
    # 주석 처리를 안했을 경우: ZeroDivisionError 발생 후 "bar", Kin() 출력 X
    
    print("bar")
    
    kin()
    
except ValueError:
    print("ValueError 예외 발생")
except NameError as e:
    print(f"예외 발생: {e}")
except ZeroDivisionError:
    print("ZeroDivisionError 예외 발생")
    
print(f"결과: 0")