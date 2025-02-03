def contains(arg1, arg):
    for value in arg1:
        if value == arg:
            return True
    return False
        
print(contains([1, 2, 3, 4], 3))
print(contains([1, 2, 3, 4], 8))