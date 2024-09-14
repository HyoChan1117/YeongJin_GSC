import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 사각형 속성
rect_width = 50
rect_height = 50
rect_x = 100
rect_y = 100
rect_speed = 5

# 검은색 영역 설정 (이 영역에 충돌하면 게임 종료)
black_zone_x = 300
black_zone_y = 200
black_zone_width = 200
black_zone_height = 150

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    # 화면을 흰색으로 채우기
    screen.fill(WHITE)

    # 검은색 영역 그리기
    pygame.draw.rect(screen, BLACK, (black_zone_x, black_zone_y, black_zone_width, black_zone_height))

    # 사각형 그리기
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    # 충돌 감지 (사각형과 검은색 영역)
    if (rect_x < black_zone_x + black_zone_width and
        rect_x + rect_width > black_zone_x and
        rect_y < black_zone_y + black_zone_height and
        rect_y + rect_height > black_zone_y):
        print("사각형이 검은색 영역에 충돌했습니다! 게임 종료!")
        running = False

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 수 조절
    pygame.time.Clock().tick(30)

# Pygame 종료
pygame.quit()
sys.exit()
