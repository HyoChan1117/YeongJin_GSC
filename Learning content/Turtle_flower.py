# turtle을 이용해서 꽃 그리기

import turtle

# 화면을 생성하여 거북이가 그릴 수 있는 캔버스를 만든다.
screen = turtle.Screen()

# 그림을 그릴 거북이 객체를 생성한다.
t = turtle.Turtle()

# 반지름이 50인 원을 그림
t.circle(50)

# 왼쪽으로 180도 회전
t.left(180)

# 반지름이 50인 원을 그림
t.circle(50)

# 오른쪽으로 90도 회전
t.right(90)

# 반지름이 50인 원을 그림
t.circle(50)

# 왼쪽으로 180도 회전
t.left(180)

# 반지름이 50인 원을 그림
t.circle(50)

# 펜을 듦
t.penup()

# 거북이를 앞으로 20만큼 직진
t.forward(20)

# 펜을 내려놓음
t.pendown()

# 왼쪽으로 90도 회전
t.left(90)

# 반지름이 20인 원을 그림
t.circle(20)

# 터틀 그래픽 창이 닫히지 않고 유지되도록 함
turtle.done()