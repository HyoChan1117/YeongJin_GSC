try:
    print("1")
    
    result = 1 / 0 
    
    print("2")
    
    print("3")
except Exception:
    print("3.5")
except ZeroDivisionError:
    print("4")
except NameError:
    print("5")
except OSError:
    print("6")
    
print("7")