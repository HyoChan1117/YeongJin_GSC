# turtle을 이용해서 꽃 그리기

import turtle

# 화면을 생성하여 거북이가 그릴 수 있는 캔버스를 만든다.
screen = turtle.Screen()

# 그림을 그릴 거북이 객체를 생성한다.
t = turtle.Turtle()

# 왼쪽으로 45도 회전
t.left(45)

# 100만큼 직진
t.forward(100)

# 반원의 반지름 
radius = 50

# 반원 그리기
t.circle(radius, 180)

# 오른쪽으로 90도 회전
t.right(90)

# 반원 그리기
t.circle(radius, 180)

# 100만큼 직진
t.forward(100)

# 100만큼 직진
t.forward(100)

# 반원의 반지름 
radius = 50

# 반원 그리기
t.circle(radius, 180)

# 오른쪽으로 90도 회전
t.right(90)

# 반원 그리기
t.circle(radius, 180)

# 100만큼 직진
t.forward(100)

# 100만큼 직진
t.forward(100)

# 반원의 반지름 
radius = 50

# 반원 그리기
t.circle(radius, 180)

# 오른쪽으로 90도 회전
t.right(90)

# 반원 그리기
t.circle(radius, 180)

# 100만큼 직진
t.forward(100)

# 100만큼 직진
t.forward(100)

# 반원의 반지름 
radius = 50

# 반원 그리기
t.circle(radius, 180)

# 오른쪽으로 90도 회전
t.right(90)

# 반원 그리기
t.circle(radius, 180)

# 100만큼 직진
t.forward(100)

# 터틀 그래픽 창이 닫히지 않고 유지되도록 함
turtle.done()

