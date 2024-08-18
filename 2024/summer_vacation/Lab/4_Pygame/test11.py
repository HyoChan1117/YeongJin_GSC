import pygame
import random
import sys

# 파이게임 초기화
pygame.init()

# 화면 크기 설정
screen_width = 1500
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("미로 충돌 감지")

# 사용자 정의 이벤트 설정
SPAWN_SQUARE = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_SQUARE, 1000)  # 1초마다 사각형 생성 이벤트 발생

# 시간
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load('44.png')
background_rect = background.get_rect()

# 사각형 설정
rect_color = (255, 0, 0)
rect_width, rect_height = 20, 20
rect_x, rect_y = 95, 880
rect_speed = 300  # 픽셀/초 단위로 변경

# 떨어지는 사각형 설정
falling_squares = []  # 떨어지는 사각형 리스트
falling_speed = 200  # 떨어지는 사각형 속도 (초당 200 픽셀)

# 쉬는 곳 색상
safe_zone_color = (137, 171, 218, 255)

# 충돌 여부를 확인하는 함수
def check_collision(x, y):
    # 위치를 정수로 변환하여 픽셀 색상 가져오기
    pixel_color = background.get_at((int(x), int(y)))
    # 충돌 색상 비교 (미로의 벽 색상)
    if pixel_color == (127, 206, 244, 255):
        return True
    return False

def is_in_safe_zone(x, y):
    # 위치를 정수로 변환하여 픽셀 색상 가져오기
    pixel_color = background.get_at((int(x), int(y)))
    # 쉬는 곳 체크 (쉬는 곳 색상)
    if pixel_color == safe_zone_color:
        return True
    return False

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_SQUARE:  # 사각형 생성 이벤트 발생 시
            # 여러 개의 새로운 사각형을 랜덤 위치에 추가
            for _ in range(random.randint(10, 20)):  # 10~20개의 사각형 생성
                x_position = random.randint(0, screen_width - rect_width)  # 화면 내 랜덤 X 위치
                new_square = pygame.Rect(x_position, 0, rect_width, rect_height)
                falling_squares.append(new_square)  # 새로운 사각형 리스트에 추가

    # delta time
    dt = clock.tick(60) / 1000
    
    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed * dt
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed * dt
    if keys[pygame.K_UP]:
        rect_y -= rect_speed * dt
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed * dt
        
    rect = pygame.Rect(int(rect_x), int(rect_y), rect_width, rect_height)

    # 사각형이 안전 구역에 있는지 확인
    in_safe_zone = (is_in_safe_zone(rect_x, rect_y) or
                    is_in_safe_zone(rect_x + rect_width, rect_y) or
                    is_in_safe_zone(rect_x, rect_y + rect_height) or
                    is_in_safe_zone(rect_x + rect_width, rect_y + rect_height))

    # 떨어지는 사각형 이동 및 충돌 체크
    for square in falling_squares[:]:  # 리스트 복사본을 사용하여 반복
        square.y += falling_speed * dt  # 델타 타임을 사용한 이동
        if square.colliderect(rect) and not in_safe_zone:  # 플레이어와 충돌 시 (안전 구역이 아닐 때만)
            print("충돌! 게임 종료")
            running = False  # 게임 종료
        if square.top > screen_height:  # 화면을 벗어난 사각형 제거
            falling_squares.remove(square)
    
    # 충돌 감지 (사각형 네 모서리 점을 체크)
    if (check_collision(rect_x, rect_y) or
        check_collision(rect_x + rect_width, rect_y) or
        check_collision(rect_x, rect_y + rect_height) or
        check_collision(rect_x + rect_width, rect_y + rect_height)):
        # 충돌 시 위치 초기화
        rect_x = 95
        rect_y = 880
    
    # 화면 그리기
    screen.blit(background, background_rect)
    
    # 떨어지는 사각형 그리기
    for square in falling_squares:
        pygame.draw.rect(screen, (0, 0, 255), square)

    pygame.draw.rect(screen, rect_color, rect)    
    pygame.display.flip()

pygame.quit()
sys.exit()
