try:
    print("1")
    
    result = 1 / 0 
    
    print("2")
    
    print("3")
    
except ZeroDivisionError:
    print("ZeroDivisionError 예외 발생")
    
print(f"결과: 0")