import pygame

# Pygame 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((640, 480))  # 640x480 크기의 창을 생성
pygame.display.set_caption("Rectangle Collision Example")  # 창의 제목 설정

# 색상 정의
black = (0, 0 ,0)  # 검정색
blue = (0, 0 , 255)  # 파란색
red = (255, 0, 0)  # 빨간색

# 사각형 초기화 (x, y, width, height)
rect1 = pygame.Rect(300, 220, 60, 60)  # (300, 220) 위치에 60x60 크기의 사각형
rect2 = pygame.Rect(100, 100, 60, 60)  # (100, 100) 위치에 60x60 크기의 사각형
rect1_speed = [10, 10]  # rect1의 속도 (x 방향, y 방향)
rect2_speed = [5, 5]  # rect2의 속도 (x 방향, y 방향)

# FPS 설정
fps = 30
clock = pygame.time.Clock()

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    clock.tick(fps)
    
    # 사각형 움직임
    rect1 = rect1.move(rect1_speed)  # rect1을 속도만큼 이동
    rect2 = rect2.move(rect2_speed)  # rect2을 속도만큼 이동
    
    # 화면 경계에 충돌 처리 (rect1)
    if rect1.left < 0 or rect1.right > 640:  # 화면 좌우 경계에 충돌하면
        rect1_speed[0] = -rect1_speed[0]  # x 방향 속도 반전
    if rect1.top < 0 or rect1.bottom > 480:  # 화면 상하 경계에 충돌하면
        rect1_speed[1] = -rect1_speed[1]  # y 방향 속도 반전
        
    # 화면 경계에 충돌 처리 (rect2)
    if rect2.left < 0 or rect2.right > 640:  # 화면 좌우 경계에 충돌하면
        rect2_speed[0] = -rect2_speed[0]  # x 방향 속도 반전
    if rect2.top < 0 or rect2.bottom > 480:  # 화면 상하 경계에 충돌하면
        rect2_speed[1] = -rect2_speed[1]  # y 방향 속도 반전
    
    # 충돌 감지
    if rect1.colliderect(rect2):  # rect1과 rect2가 충돌하면
        print("Collision Detected!")  # 콘솔에 충돌 메시지 출력
        
    # 화면 그리기
    screen.fill(black)  # 화면을 검정색으로 채움
    pygame.draw.rect(screen, blue, rect1)  # rect1을 파란색으로 그리기
    pygame.draw.rect(screen, red, rect2)  # rect2을 파란색으로 그리기
    pygame.display.flip()  # 화면 업데이트
    
pygame.quit()  # Pygame 종료