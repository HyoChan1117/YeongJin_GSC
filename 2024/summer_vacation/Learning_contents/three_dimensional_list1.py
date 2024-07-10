# 3차원 리스트
bar = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[11, 12, 13], [14, 15, 16], [17, 18, 19]]]

# [2][3][3]
# 3 X 3 Matrix가 2장


# 첫 번째 : 1번째 Matrix가 반환  -> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 두 번째 : 2번째 Matrix가 반환  -> [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
for matrix in bar:
    print(matrix)

# 첫 번째 : 1번째 Matrix의 1번째 행이 반환
# 두 번째 : 1번째 Matrix의 2번째 행이 반환
# 세 번째 : 1번째 Matrix의 3번째 행이 반환
# 네 번째 : 2번째 Matrix의 1번째 행이 반환
# 다섯번째 : 2번째 Matrix의 2번째 행이 반환
# 여섯번째 : 2번째 Matrix의 3번째 행이 반환
for matrix in bar:
    for row in matrix:
        print(row)


for matrix in bar:
    for row in matrix:
        for col in row:
            print(col, "\t", end= "")
        print()
    print("-" * 20)