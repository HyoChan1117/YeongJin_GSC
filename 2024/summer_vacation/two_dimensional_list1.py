# 2차원 리스트 생성
# 1. 직접 선언
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[0] * 3] * 5

# 2. List Comprehension(1)
rows = 3
cols = 3
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

# 3. List Comprehension(2)
# 3x4 행렬 생성, 모든 값은 0
matrix = [[0]*4 for _ in range(3)]