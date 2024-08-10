import pygame
import random

# 파이게임 초기화
pygame.init()

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
moving_rect_width = 30
moving_rect_height = 30

# 스피드
speed = 300

# 화면 설정
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# 장애물 랜덤하게 생성
obs_list = []
for _ in range(obs_num):
    while True:
        rect_x = random.randint(0, screen_width - obs_width)
        rect_y = random.randint(0, screen_height - obs_height)
        rect = pygame.Rect(rect_x, rect_y, obs_width, obs_height)
        
        if rect.collidelist(obs_list) == -1:
            obs_list.append(rect)
            break
        
# 아이템 랜덤하게 생성
item_list = []
for _ in range(item_num):
    while True:
        rect_x = random.randint(0, screen_width - item_width)
        rect_y = random.randint(0, screen_height - item_height)
        rect = pygame.Rect(rect_x, rect_y, item_width, item_height)
        
        if rect.collidelist(item_list) == -1 and rect.collidelist(obs_list) == -1:
            item_list.append(rect)
            break
        
# 움직이는 사각형 생성
while True:
    rect_x = random.randint(0, screen_width - moving_rect_width)
    rect_y = random.randint(0, screen_height - moving_rect_height)
    moving_rect = pygame.Rect(rect_x, rect_y, moving_rect_width, moving_rect_height)
    
    if moving_rect.collidelist(obs_list) == -1 and moving_rect.collidelist(item_list) == -1:
        break
    
running = True
while running:
    # << -- 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    dt = clock.tick(60) / 1000
    
    prev_pos = moving_rect.topleft
    
    key = pygame.key.get_pressed()
    
    if key[pygame.K_LEFT]:
        moving_rect.x -= speed * dt
    if key[pygame.K_RIGHT]:
        moving_rect.x += speed * dt
    if key[pygame.K_UP]:
        moving_rect.y -= speed * dt
    if key[pygame.K_DOWN]:
        moving_rect.y += speed * dt
        
    moving_rect.x = max(0, min(moving_rect.x, screen_width - moving_rect_width))
    moving_rect.y = max(0, min(moving_rect.y, screen_height - moving_rect_height))
    
    if moving_rect.collidelist(obs_list) != -1:
        moving_rect.topleft = prev_pos
        
    col_index = moving_rect.collidelist(item_list)
    if col_index != -1:
        del item_list[col_index]
        
    if len(item_list) == 0:
        running = False
    
    # 화면 그리기
    screen.fill((255, 255, 255))
    
    # 장애물 그리기
    for rect in obs_list:
        pygame.draw.rect(screen, (0, 0, 255), rect)
    
    # 아이템 그리기
    for rect in item_list:
        pygame.draw.rect(screen, (255, 255, 0), rect)
        
    # 움직이는 사각형 그리기
    pygame.draw.rect(screen, (255, 0, 0), moving_rect)
    
    # 메모리에 그려진 그림을 한번에 화면에 출력
    pygame.display.flip()

# 파이게임 종료
pygame.quit()