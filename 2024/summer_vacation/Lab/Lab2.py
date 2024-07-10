# 2차원 리스트 조작

def print_matrix():
    for i in range(rows):
        bar = []
        for j in range(cols):
            value = int(input(f"Enter value for [{i}][{j}]: "))
            bar.append(value)
        # 반복이 끝나면 리스트 bar를 리스트 matrix에 추가한다.
        matrix.append(bar)
        
# 행과 열 개수를 정수로 입력 받는다.
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# 2차원 리스트를 생성하기 위해 리스트 생성한다.
matrix = []

print_matrix()

# 출력
for list in matrix:
    for num in list:
        print(num, end=" ")
    print()



