import pygame

pygame.init()

# 화면 설정
screen = pygame.display.set_mode((640, 480))  # 640x480 크기의 창을 생성
pygame.display.set_caption("Rectangle Collision Example")  # 창의 제목 설정

# 색상 정의
black = (0, 0 ,0)  # 검정색
blue = (0, 0 , 255)  # 파란색
red = (255, 0, 0)  # 빨간색
white = (255, 255, 255)  # 흰색
yellow = (255, 255, 0)  # 노란색

# 3개의 Rect 객체를 생성
# (x, y, width, height)
obstacles = [
    pygame.Rect(20, 20, 40, 40),  # 첫 번째 Rect: (20, 20) 위치, 40x40 크기
    pygame.Rect(100, 100, 50, 50),  # 두 번째 Rect: (100, 100) 위치, 50x50 크기
    pygame.Rect(200, 200, 60, 60),  # 세 번째 Rect: (200, 200) 위치, 60x60 크기
]
obstacles1_speed = [10, 10]  # rect1의 속도 (x 방향, y 방향)
obstacles2_speed = [5, 5]  # rect2의 속도 (x 방향, y 방향)
obstacles3_speed = [3, 3]  # rect3의 속도 (x 방향, y 방향)

# FPS 설정
fps = 60
clock = pygame.time.Clock()

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    clock.tick(fps)
    
    # 사각형 움직임
    obstacles[0] = obstacles[0].move(obstacles1_speed)  # rect1을 속도만큼 이동
    obstacles[1] = obstacles[1].move(obstacles2_speed)  # rect2을 속도만큼 이동
    obstacles[2] = obstacles[2].move(obstacles3_speed)  # rect1을 속도만큼 이동
    
    # 화면 경계에 충돌 처리 (rect1)
    if obstacles[0].left < 0 or obstacles[0].right > 640:  # 화면 좌우 경계에 충돌하면
        obstacles1_speed[0] = -obstacles1_speed[0]  # x 방향 속도 반전
    if obstacles[0].top < 0 or obstacles[0].bottom > 480:  # 화면 상하 경계에 충돌하면
        obstacles1_speed[1] = -obstacles1_speed[1]  # y 방향 속도 반전
        
    # 화면 경계에 충돌 처리 (rect2)
    if obstacles[1].left < 0 or obstacles[1].right > 640:  # 화면 좌우 경계에 충돌하면
        obstacles2_speed[0] = -obstacles2_speed[0]  # x 방향 속도 반전
    if obstacles[1].top < 0 or obstacles[1].bottom > 480:  # 화면 상하 경계에 충돌하면
        obstacles2_speed[1] = -obstacles2_speed[1]  # y 방향 속도 반전
        
    # 화면 경계에 충돌 처리 (rect3)
    if obstacles[2].left < 0 or obstacles[2].right > 640:  # 화면 좌우 경계에 충돌하면
        obstacles3_speed[0] = -obstacles3_speed[0]  # x 방향 속도 반전
    if obstacles[2].top < 0 or obstacles[2].bottom > 480:  # 화면 상하 경계에 충돌하면
        obstacles3_speed[1] = -obstacles3_speed[1]  # y 방향 속도 반전

    # 충돌 감지를 수행할 대상 Rect 객체 생성: 파란색 사각형
    moving_rect = pygame.Rect(120, 130, 100, 100)  # (120, 130) 위치, 100x100 크기

    # moving_rect가 obstacles 리스트의 어떤 Rect와 충돌하는지 확인
    # collidelist 메서드는 충돌한 Rect의 인덱스를 반환. 충돌이 없으면 -1을 반환한다.
    index = moving_rect.collidelist(obstacles)

    if index != -1:
        # 충돌이 발생한 경우, 충돌한 Rect의 인덱스를 출력
        print(f"moving_rect가 obstacles[{index}]와 충돌했습니다.")
    else:
        # 충돌이 발생하지 않은 경우, 해당 메시지를 출력
        print("충돌이 없습니다.")
        
    # 화면 그리기
    screen.fill(white)  # 화면을 검정색으로 채움
    pygame.draw.rect(screen, yellow, obstacles[0])  # rect1을 노란색으로 그리기
    pygame.draw.rect(screen, red, obstacles[1])  # rect2을 빨간색으로 그리기
    pygame.draw.rect(screen, black, obstacles[2])  # rect3을 검은색으로 그리기
    pygame.draw.rect(screen, blue, moving_rect)  # moving_rect을 파란색으로 그리기
    pygame.display.flip()  # 화면 업데이트
    
pygame.quit()  # Pygame 종료