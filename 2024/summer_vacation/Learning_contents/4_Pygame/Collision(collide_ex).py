import pygame

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Collidelist Example')

# 색상 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Rect 리스트 생성
obstacles = [
    pygame.Rect(150, 100, 100, 100),  # 첫 번째 장애물: 위치 (150, 100), 크기 100x100
    pygame.Rect(300, 300, 150, 50),  # 두 번째 장애물: 위치 (300, 300), 크기 150x50
    pygame.Rect(500, 200, 50, 150),  # 세 번째 장애물: 위치 (500, 200), 크기 50x150
    pygame.Rect(400, 400, 200, 50),  # 네 번째 장애물: 위치 (400, 400), 크기 200x50
]

# 이동하는 Rect 생성
moving_rect = pygame.Rect(50, 50, 50, 50)  # 이동 가능한 사각형: 위치 (50, 50), 크기 50x50

# 이동 속도 설정
velocity = 300  # 초당 300 픽셀 이동

# FPS 제어를 위한 Clock 객체 생성
clock = pygame.time.Clock()

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # 이전 위치 저장
    previous_position = moving_rect.topleft
    
    # 델타 타임 계산
    dt = clock.tick(60) / 1000.0  # 프레임당 시간(초) 계산
    
    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moving_rect.x -= velocity * dt
    if keys[pygame.K_RIGHT]:
        moving_rect.x += velocity * dt
    if keys[pygame.K_UP]:
        moving_rect.y -= velocity * dt
    if keys[pygame.K_DOWN]:
        moving_rect.y += velocity * dt
        
    # 충돌 감지
    collision_index = moving_rect.collidelist(obstacles)
    if collision_index != -1:
        print(f"Collision with obstacle {collision_index}")
        # 충돌이 발생한 경우 이전 위치로 되돌리기
        moving_rect.topleft = previous_position
        
    # 화면 초기화
    screen.fill(WHITE)
    
    # 장애물 그리기
    for obs in obstacles:
        pygame.draw.rect(screen, BLUE, obs)
    
    # 이동하는 Rect 그리기
    pygame.draw.rect(screen, RED, moving_rect)
    
    # 화면 경계에 충돌 처리 (moving_rect)
    if moving_rect.left < 0:
        moving_rect.left = 0
    if moving_rect.right > screen_width: 
        moving_rect.right = screen_width
    if moving_rect.top < 0:
        moving_rect.top = 0
    if moving_rect.bottom > screen_height:
        moving_rect.bottom = screen_height
    
    # 화면 업데이트
    pygame.display.flip()
    
# Pygame 종료
pygame.quit()