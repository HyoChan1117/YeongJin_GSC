import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Falling Square Example')

# 색상 정의
WHITE = (255, 255, 255)  # 배경 색상
BLUE = (0, 0, 255)  # 사각형 색상
RED = (255, 0, 0)  # 움직이는 사각형 색상

# 사각형 크기와 속도 설정
square_size = 50
falling_speed = 200  # 초당 200 픽셀

# 사각형 리스트
falling_squares = []

# 움직이는 사각형 사이즈
moving_rect_size = 50

# 스피드
speed = 300  # 초당 300 픽셀

# 사용자 정의 이벤트 설정
SPAWN_SQUARE  = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_SQUARE, 1000)  # 1초마다 사각형 생성

# FPS 제어를 위한 Clock 객체 생성
clock = pygame.time.Clock()

def spawn_square():
    # 랜덤한 x 위치에 새로운 사각형 생성
    x_position = random.randint(0, screen_width - square_size)
    new_square = pygame.Rect(x_position, 0, square_size, square_size)
    falling_squares.append(new_square)
    
# 움직이는 사각형 랜덤하게 생성
moving_rect = pygame.Rect(screen_width / 2 - moving_rect_size / 2,\
                          screen_height - moving_rect_size - 30,\
                          moving_rect_size, moving_rect_size)

    
# 게임 루프
running = True
while running:
    # 델타 타임 계산
    dt = clock.tick(60) / 1000  # 60 fps로 제한
    
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_SQUARE:
            spawn_square()  # 사각형 생성 이벤트 발생 시 사각형 추가
            
    key = pygame.key.get_pressed()
    
    if key[pygame.K_LEFT]:
        moving_rect.x -= speed * dt
    if key[pygame.K_RIGHT]:
        moving_rect.x += speed * dt
        
    # 움직이는 사각형 화면 경계 설정
    moving_rect.x = max(0, min(moving_rect.x, screen_width - moving_rect_size))
        
    # 사각형 이동(slicing을 이용하여 리스트를 복사해서 사용)
    for square in falling_squares[:]:
        square.y += falling_speed * dt  # 델타 타임을 사용한 이동
        if square.top > screen_height:
            falling_squares.remove(square)  # 화면을 벗어나면 제거
            
    # 움직이는 사각형과 사각형이 충돌하면 게임종료
    if moving_rect.collidelist(falling_squares) != -1:
        running = False
            
    # 화면 초기화
    screen.fill(WHITE)
    
    # 사각형 그리기
    for square in falling_squares:
        pygame.draw.rect(screen, BLUE, square)
        
    # 움직이는 사각형 그리기
    pygame.draw.rect(screen, RED, moving_rect)
        
    # 화면 업데이트
    pygame.display.flip()
    
# 게임 종료
pygame.quit()