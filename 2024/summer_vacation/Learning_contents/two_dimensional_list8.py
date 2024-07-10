# 2차원 리스트를 함수
def print_matrix(arg_list):
    for row in arg_list:
        for col in row:
            print(col, "\t", end="")
        print()
    print("-" * 20)

# 특정 열을 del 하는 함수
def del_col(arg_list, col_num):
    for index in range(len(arg_list)):
        del arg_list[index][col_num]

matrix = [ [1, 2, 3], [4, 5], [6, 7] ]

print_matrix(matrix)

# matrix에서 1번째 열(col)을 del 하는 함수를 호출
del_col(matrix, 1)

# 2차원 리스트에서 2번째 원소 안에 100 추가
matrix[2].append(100)

print_matrix(matrix)

# 2차원 리스트에서 마지막 원소에 [8, 9, 10, 11] 추가
matrix.append([8, 9, 10, 11])

print_matrix(matrix)

# 2차원 리스트에서 2번째 원소에 [100, 200, 300] 추가
matrix.insert(2, [100, 200, 300])

print_matrix(matrix)