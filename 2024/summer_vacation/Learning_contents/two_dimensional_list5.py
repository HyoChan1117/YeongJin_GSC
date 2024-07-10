def print_matrix(arg_list):
    for row in arg_list:
        for col in row:
            print(col, "\t", end="")
        print()
    print("-" * 20)
            
matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

print_matrix(matrix)

del matrix[1][1]

print_matrix(matrix)