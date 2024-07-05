def print_matrix(arg_list):
    for row in arg_list:
        for col in row:
            print(col, "\t", end="")
        print()
    print("-" * 20)
            
matrix = [ [1, 2], [4, 5, 6], [7, 8, 9, 10] ]

print_matrix(matrix)

# matrix의 원소의 개수
print(len(matrix))

# matrix의 0번째 리스트의 원소의 개수
print(len(matrix[0]))

# matrix의 1번째 리스트의 원소의 개수
print(len(matrix[1]))

# matrix의 2번째 리스트의 원소의 개수
print(len(matrix[2]))