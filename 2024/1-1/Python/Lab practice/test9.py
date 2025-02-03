# 사용자로부터 방향 명령어를 입력받아 출력하는 프로그램 작성

# 방향 명령어를 입력 받는다.
direction = input("방향을 입력하세요(left, right, up, down): ")

# 입력 받은 방향 명령어에 따라 "~로 이동합니다." 문구를 출력한다.
if direction == "left" :
    print("왼쪽으로 이동합니다.")

elif direction == "right" :
    print("오른쪽으로 이동합니다.")

elif direction == "up" :
    print("위로 이동합니다.")

elif direction == "down" :
    print("아래로 이동합니다.")

# 입력 받은 명령어에 다른 단어가 입력되면 "알 수 없는 명령입니다." 문구를 출력한다.
else :
    print("알 수 없는 명령입니다.")

