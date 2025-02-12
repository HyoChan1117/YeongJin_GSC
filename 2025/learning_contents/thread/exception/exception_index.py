try:
    print("pos")
    
    print(1/0)  
    
    print("bar")
    
    kin()
    
    raise IndexError("인덱스 예외 발생")

# try문에서 발생한 예외를 찾기 위해 except는 위에서부터 순차적으로 해당 예외를 찾아감
# 현재 발생한 예외가 except에 없으면 프로그램이 죽음
except ValueError:
    print("ValueError 예외 발생")
except IndexError as e:
    print(f"예외 발생: {e}")
except NameError as e:
    print(f"예외 발생: {e}")
except ZeroDivisionError:
    print("ZeroDivisionError 예외 발생")
    
print(f"결과: 0")