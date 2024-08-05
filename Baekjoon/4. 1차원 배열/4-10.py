N = int(input())

input_value = input().split()

list_score = [ int(value) for value in input_value ]

max_num = max(list_score)

sum = 0
for num in list_score:
    score = num / max_num * 100
    sum += score
    avg = sum / N

print(avg)