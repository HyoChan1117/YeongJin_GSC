# 별 다이아몬드 출력
# 높이가 5인 다이아몬드 형태의 별을 출력하는 프로그램
count = ""

# 다이아몬드 윗 부분
for i in range(0, 5):
    space = " " * (5 - i)
    count = "*" * (2 * i + 1)
    print(space + count)
    
# 다이아몬드 아랫 부분
for i in range(5, -1, -1):
    space = " " * (5 - i)
    count = "*" * (2 * i + 1)
    print(space + count)
    