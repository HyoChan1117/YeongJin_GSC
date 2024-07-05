def print_matrix(arg_list):
    for row in arg_list:
        for col in row:
            print(col, "\t", end="")
        print()
    print("-" * 20)

def del_col(arg_list, col_num):
    for index in range(len(arg_list)):
        del arg_list[index][col_num]

matrix = [ [1, 2, 3], [4, 5], [6, 7] ]

print_matrix(matrix)

del_col(matrix, 1)

print_matrix(matrix)

matrix[2].append(100)

print_matrix(matrix)