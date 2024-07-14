# 2차원 리스트 조작


# 사용자로부터 행과 열의 수를 입력 받는다.
input_row = int(input("Enter the number of rows: "))
input_col = int(input("Enter the number of columns: "))

# 해당 크기에 맞는 2차원 리스트를 생성한다.
matrix = []
for i in range(input_row):
    rows = []
    for j in range(input_col):
        input_value = int(input(f"Enter value for [{i}][{j}]: "))
        rows.append(input_value)
    # 반복이 끝나면 matrix로 append 한다.
    matrix.append(rows)


# 리스트를 출력한다.
for list in matrix:
    print()
    for element in list:
        print(element, " ", end="")