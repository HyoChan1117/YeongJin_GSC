import pygame
import sys

pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Rectangle Shooting")

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 사각형 초기 위치 및 크기
rect_width = 50
rect_height = 50
rect_x = screen_width // 2
rect_y = screen_height // 2
rect_speed = 5

# 총알 리스트
bullets = []

# 총알 속도
bullet_speed = 7

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 키 입력 받기
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed
    
    # 스페이스바를 눌러 총알 발사
    if keys[pygame.K_SPACE]:
        bullet_rect = pygame.Rect(rect_x + rect_width // 2 - 5, rect_y, 10, 20)
        bullets.append(bullet_rect)

    # 총알 움직임
    for bullet in bullets:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # 화면 그리기
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

    pygame.display.flip()
    clock.tick(60)
