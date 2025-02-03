import random
import turtle

# 화면을 설정합니다.
screen = turtle.Screen()
screen.title("Turtle 키보드 이벤트 처리 예제")

width = screen.window_width() // 2
height = screen.window_height() // 2
screen.setup(width*2, height*2)

# 창의 경계 설정
boundary_left = -860
boundary_right = 860
boundary_top = 540
boundary_bottom = -540

print("윈도우 가로 X 세로", width, height)

# 거북이를 생성합니다.
t = turtle.Turtle()

t.speed(0)

# 거북이가 움직이는 함수를 정의합니다.
def move_forward():
    t.forward(100)
    
    # 현재 좌표 출력
    x, y = t.position()
    print(x, y)

    # windows 너비, 높이를 벗어나는 경우 180도 회전
    if x >= width:
        t.left(180)
        t.forward(x - width)
    elif x <= -width:
        t.left(180)
        t.forward(-(x + width))
    elif y >= height:
        t.left(180)
        t.forward(y - height)
    elif y <= -height:
        t.left(180)
        t.forward(-(y + height))

def move_backward():
    t.backward(100)
    
def turn_left():
    t.left(15)
    
def turn_right():
    t.right(15)
    
# 펜 색깔을 검은색으로 변경 -> "b" Key를 누를 때 호출
def change_color_to_black():
    t.pencolor("black")

# 펜 색깔을 빨간색으로 변경 -> "r" Key를 누를 때 호출    
def change_color_to_red():
    t.pencolor("red")
    
# 펜 색깔 변경 함수를 정의
def move_random():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    t.pencolor(random.choice(colors))

# 키보드 이벤트를 설정합니다.
screen.listen()
screen.onkey(move_forward, "Up")     # 위쪽 화살표 키를 누르면 앞으로 이동
screen.onkey(move_backward, "Down")  # 아래쪽 화살표 키를 누르면 뒤로 이동
screen.onkey(turn_left, "Left")      # 왼쪽 화살표 키를 누르면 왼쪽으로 회전
screen.onkey(turn_right, "Right")    # 오른쪽 화살표 키를 누르면 오른쪽으로 회전
screen.onkey(move_random, "c")       # 'c' 키를 누르면 펜 색깔 변화
screen.onkey(change_color_to_black, "b") # 'b' 키를 누르면 펜 색깔 검은색으로 변화
screen.onkey(change_color_to_red, "r")   # 'r' 키를 누르면 펜 색깔 빨간색으로 변화

# i를 누르면 색깔이 빨간색 -> 검은색 또는 검은색 -> 빨간색
# 현재 펜 색깔이 빨간색 또는 검은색일 경우에만 반전


# 현재 펜 색깔이 빨간색 또는 검은색일 경우에만 반전하는 함수
def changed_color_red_black():
    current_color = t.pencolor()

    # 둘 중에 하나를 선택하는데 둘 다 선택되지 않을수도 있음
    if current_color == "black":
        t.pencolor("red")
    elif current_color == "red":
        t.pencolor("black")

screen.onkey(changed_color_red_black, "i")

# 색깔 바꾸기
def change_color():
    while True:
        print("색깔 선택: ")
        print("1. 파란색")
        print("2. 검정색")
        print("3. 노란색")
        # 1 ~ 3 이외 값 입력 시 재입력 -> 언제까지? 1~3 값이 입력될 때 까지
        input_value = int(input("숫자 입력: "))
        
        if 1 <= input_value <= 3:
            if input_value == 1:
                t.pencolor("blue")
            elif input_value == 2:
                t.pencolor("black")
            elif input_value == 3:
                t.pencolor("yellow")
            break

screen.onkey(change_color, "t")

# 이벤트 루프를 시작합니다.
screen.mainloop()