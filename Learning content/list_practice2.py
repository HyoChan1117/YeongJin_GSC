
bar = [90, 10, 20]

def test(argValue):
    for index in range(0, len(argValue)):
        argValue[index] += 1
        
test(bar)

print(bar)