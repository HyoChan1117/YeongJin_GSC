import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("동그라미 이동 및 색상 변경 프로그램")

# 무작위 색상 생성
color = [(255, 0, 0), (0, 0, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)]
current_color = random.choice(color)
radius = 40

# 시작점 (화면 중앙)
x = screen.get_width() / 2
y = screen.get_height() / 2

# 프레임 설정
clock = pygame.time.Clock()
fps = 30

# 이동 속도
speed = 100

running = True
while running:
    dt = clock.tick(fps) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # 왼쪽 버튼 클릭
                new_color = random.choice(color)
                while new_color == current_color:
                    new_color = random.choice(color)
                current_color = new_color
                
    # 키보드 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed * dt
    if keys[pygame.K_RIGHT]:
        x += speed * dt
    if keys[pygame.K_UP]:
        y -= speed * dt
    if keys[pygame.K_DOWN]:
        y += speed * dt
        
    # 화면 경계 체크
    if x - radius < 0:
        x = radius
    if x + radius < screen.get_width():
        x = screen.get_width() - radius
    if y - radius < 0:
        y = radius
    if y - radius < screen.get_height():
        y = screen.get_height() - radius
        
    # 화면 그리기
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (current_color), (x, y), radius)
    
    # 화면 업데이트
    pygame.display.flip()
        
# 파이게임 종료
pygame.quit()
        
        
        
        
        
        
        