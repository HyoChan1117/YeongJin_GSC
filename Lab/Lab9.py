# 사용자로부터 방향 명령어에 관한 하나의 단어를 입력받는다.
direction = input("방향을 입력하세요(left, right, up, down): ")

# "left"를 입력했을 때의 결과를 출력한다.
if direction == "left" :
    print("왼쪽으로 이동합니다.")

# "right"를 입력했을 때의 결과를 출력한다.
elif direction == "right" :
    print("오른쪽으로 이동합니다.")

# "up"을 입력했을 때의 결과를 출력한다.
elif direction == "up" :
    print("위로 이동합니다.")

# "down"을 입력했을 때의 결과를 출력한다.
elif direction == "down" :
    print("아래로 이동합니다.")

# 이외의 단어를 입력했을 때의 결과를 출력한다.
else :
    print("알 수 없는 명령입니다.")

