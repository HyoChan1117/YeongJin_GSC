def bar(a, b, *args, c=100):
    print(a, b, args, c)
    
bar(1, 2, 3, 4, 5, 6)  # -> 1, 2, (3, 4, 5, 6)