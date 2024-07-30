attendence = [ value for value in range(1, 31) ]

for _ in range(28):
    input_value = int(input())
    attendence.remove(input_value)

for num in attendence:
    print(num)