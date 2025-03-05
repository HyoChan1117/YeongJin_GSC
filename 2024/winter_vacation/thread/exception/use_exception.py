try:
    print("1")
    
    # raise IndexError

    raise KeyError

    print("2")
    
    print("3")
except Exception:  # Exception은 except의 가장 마지막에 있어야 함
                   # 모든 예외처리가 안됐을 경우 사용용
    print("3.1")
except LookupError:
    print("3.5")
    
print("7")