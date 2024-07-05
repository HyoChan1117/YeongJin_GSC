# turtle을 이용해서 삼각형 그리기

import turtle

# 화면을 생성하여 거북이가 그릴 수 있는 캔버스를 만든다.
screen = turtle.Screen()

# 그림을 그릴 거북이 객체를 생성한다.
t = turtle.Turtle()

# 세 번 반복하여 삼각형을 그림
for _ in range(3):
    # 거북이를 앞으로 100만큼 이동시킴
    t.forward(100)
    # 거북이를 왼쪽으로 120도 회전시킴
    t.left(120)
    
# 터틀 그래픽 창이 닫히지 않고 유지되도록 함
turtle.done()