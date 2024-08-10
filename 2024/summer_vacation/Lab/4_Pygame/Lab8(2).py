import pygame
import random

pygame.init()

#=======================================================================

# <<-- 환경 변수 설정
# 화면 사이즈
screen_width = 800
screen_height = 600

# 장애물 사이즈
obs_width = 120
obs_height = 100

# 장애물 개수
obs_num = 5

# 아이템 사이즈
item_width = 20
item_height = 20

# 아이템 개수
item_num = 10

# 움직이는 사각형 사이즈
moving_rect_width = 50
moving_rect_height = 50

# 스피드
speed = 300

#=======================================================================

# 기본 설정 및 객체 생성
# 화면, FPS 설정
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

#=======================================================================
obs_list = []
# 장애물 랜덤하게 생성
for _ in range(obs_num):
    while True:
        rect_x = random.randint(0, screen_width - obs_width)
        rect_y = random.randint(0, screen_height - obs_height)
        rect = pygame.Rect(rect_x, rect_y, obs_width, obs_height)
        
        if rect.collidelist(obs_list) == -1:
            obs_list.append(rect)
            break
        
item_list = []
# 아이템 랜덤하게 생성
for _ in range(item_num):
    while True:
        rect_x = random.randint(0, screen_width - item_width)
        rect_y = random.randint(0, screen_height - item_height)
        rect = pygame.Rect(rect_x, rect_y, item_width, item_height)

        if rect.collidelist(item_list) == -1 and rect.collidelist(obs_list) == -1:
            item_list.append(rect)
            break
        
# 움직이는 사각형 랜덤하게 생성
while True:
    rect_x = random.randint(0, screen_width - moving_rect_width)
    rect_y = random.randint(0, screen_height - moving_rect_height)
    moving_rect = pygame.Rect(rect_x, rect_y, moving_rect_width, moving_rect_height)
    
    if moving_rect.collidelist(obs_list) == -1 and moving_rect.collidelist(item_list) == -1:
        break

#=======================================================================

running = True
while running:
    # << -- 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Delta time 설정
    dt = clock.tick(60) / 1000
    
    # 움직이는 사각형의 이전 좌표를 저장
    prev_pos = moving_rect.topleft
    
    # key 입력
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        moving_rect.x -= speed * dt
    
    if keys[pygame.K_RIGHT]:
        moving_rect.x += speed * dt
        
    if keys[pygame.K_UP]:
        moving_rect.y -= speed * dt
        
    if keys[pygame.K_DOWN]:
        moving_rect.y += speed * dt
        
    # 화면 경계 설정
    moving_rect.x = max(0, min(moving_rect.x, screen_width - moving_rect_width))
    moving_rect.y = max(0, min(moving_rect.y, screen_height - moving_rect_height))
    
    # 장애물과 부딪힐 경우
    if moving_rect.collidelist(obs_list) != -1:
        moving_rect.topleft = prev_pos
    
    # 움직이는 사각형이 아이템과 부딪힐 경우
    col_index = moving_rect.collidelist(item_list)
    if col_index != -1:
        del item_list[col_index]
        
    # 아이템를 다 먹었을 경우
    if len(item_list) == 0:
        running = False
    
    # <<-- 화면 그리기
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))
    
    # 장애물 그리기
    for rect in obs_list:
        pygame.draw.rect(screen, (255, 0, 0), rect)
    
    # 아이템 그리기
    for rect in item_list:
        pygame.draw.rect(screen, (0, 0, 255), rect)
        
    # 사각형 그리기
    pygame.draw.rect(screen, (0, 255, 0), moving_rect)
    
    # 메모리에 그려진 그림을 한번에 출력
    pygame.display.flip()
    
#=======================================================================

pygame.quit()