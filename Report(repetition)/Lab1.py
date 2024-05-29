# 삼각형 출력
# While문을 사용하여 아래와 같이 출력하는 프로그램 작성
count = 1

while True:
    if count == 6:
        break
    star = "*" * count
    count += 1
    print(star)