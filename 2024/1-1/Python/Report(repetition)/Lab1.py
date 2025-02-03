# 삼각형 출력
# While문을 사용하여 아래와 같이 출력하는 프로그램 작성
count = 1

# 한 번의 반복마다 "*"을 하나씩 추가한다.
while True:
    # 6번째에 반복 종료
    if count == 6:
        break
    star = "*" * count
    count += 1
    print(star)