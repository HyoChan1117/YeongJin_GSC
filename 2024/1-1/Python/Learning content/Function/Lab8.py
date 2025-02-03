def calculate_average(*args):
    sum = 0
    for value in args:
        sum += value
        avg = sum / len(args)
    
    return avg

print(calculate_average(1, 2, 3, 4, 5))
print(calculate_average(6, 7, 8))
print(calculate_average(10, 20))