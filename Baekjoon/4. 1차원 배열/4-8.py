list_num = []

for _ in range(10):
    input_value = int(input())
    if input_value % 42 not in list_num:
        list_num.append(input_value % 42)

print(len(list_num))