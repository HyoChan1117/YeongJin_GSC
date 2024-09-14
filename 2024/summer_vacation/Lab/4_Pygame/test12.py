import pygame
import random
import sys
import math

# 파이게임 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 1500, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("미로 충돌 감지")

# 시간
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load('44.png')

# 플레이어 사각형 설정
rect = pygame.Rect(95, 880, 20, 20)
rect_speed = 300  # 픽셀/초 단위

# 움직이는 원 리스트 생성
circles = [{'position': [random.randint(5, screen_width - 5), random.randint(5, screen_height - 5)],
            'velocity': [random.choice([-1, 1]) * 100, random.choice([-1, 1]) * 100]} for _ in range(100)]

# 색깔에 따른 충돌 확인 함수
def is_colliding_with_color(x, y, color):
    return background.get_at((int(x), int(y)))[:3] == color[:3]

# 게임 루프
running = True
mouse_held_down = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_held_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_held_down = False

    dt = clock.tick(60) / 1000

    if mouse_held_down:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        distance = math.sqrt((mouse_x - rect.x) ** 2 + (mouse_y - rect.y) ** 2)
        
        if distance > 0:
            move_x = ((mouse_x - rect.x) / distance) * rect_speed * dt
            move_y = ((mouse_y - rect.y) / distance) * rect_speed * dt

            new_x = rect.x + move_x
            new_y = rect.y + move_y

            # 충돌 감지: 특정 색깔과 충돌하지 않도록 이동
            if not (is_colliding_with_color(new_x, new_y, (127, 206, 244)) or
                    is_colliding_with_color(new_x + rect.width, new_y, (127, 206, 244)) or
                    is_colliding_with_color(new_x, new_y + rect.height, (127, 206, 244)) or
                    is_colliding_with_color(new_x + rect.width, new_y + rect.height, (127, 206, 244))):
                rect.x = new_x
                rect.y = new_y

    # 움직이는 원들 이동 및 경계 반사
    for circle in circles:
        circle['position'][0] += circle['velocity'][0] * dt
        circle['position'][1] += circle['velocity'][1] * dt

        # 경계에서 튕기기
        for i in [0, 1]:
            if circle['position'][i] <= 5 or circle['position'][i] >= (screen_width if i == 0 else screen_height) - 5:
                circle['velocity'][i] = -circle['velocity'][i]

        # 플레이어와 충돌 체크 (안전 구역에서는 제외)
        if rect.collidepoint(circle['position']) and not is_colliding_with_color(rect.x, rect.y, (137, 171, 218)):
            print("충돌! 게임 종료")
            running = False

    # 마지막 지점 도달 시 게임 종료
    if rect.y <= 0:
        print("목표 지점 도착! 게임 종료")
        running = False

    # 화면 그리기
    screen.blit(background, (0, 0))
    for circle in circles:
        pygame.draw.circle(screen, (0, 0, 255), (int(circle['position'][0]), int(circle['position'][1])), 5)
    pygame.draw.rect(screen, (255, 0, 0), rect)
    pygame.display.flip()

pygame.quit()
sys.exit()
