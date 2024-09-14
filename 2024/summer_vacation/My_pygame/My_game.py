import pygame

# 초기화
pygame.init()

# 화면 사이즈
screen_width = 1189
screen_height = 841

# 배경 이미지 불러오기
background = pygame.image.load('background.png')
background_rect = background.get_rect()

# 움직이는 사각형 이미지 불러오기
moving_rect_image = pygame.image.load('moving_rect.png')
moving_rect = moving_rect_image.get_rect()

# 아이템 이미지 불러오기 및 여러 아이템 초기화
item_image = pygame.image.load('item.png')

item_list = []
item_positions = [(258, 658), (283, 658), (308, 658), (333, 658),(258, 633), (283, 633), (308, 633), (333, 633),\
(607, 658), (632, 658), (657, 658), (682, 658), (607, 633), (632, 633), (657, 633), (682, 633),\
(507, 308), (532, 308), (557, 308), (582, 308), (507, 283), (532, 283), (557, 283), (582, 283),\
(608, 158), (633, 158), (658, 158), (683, 158), (608, 133), (633, 133), (658, 133), (683, 133),\
(107, 608), (132, 608), (157, 608), (182, 608), (107, 583), (132, 583), (157, 583), (182, 583)]  # 원하는 위치들

for pos in item_positions:
    item_rect = item_image.get_rect()
    item_rect.center = pos
    item_list.append(item_rect)

# 움직이는 사각형 스피드
moving_rect_speed = 200

# 화면 설정
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# 사각형 위치 초기화
rect_x = 135
rect_y = 711
moving_rect.topleft = (rect_x, rect_y)

running = True
# 이벤트 처리
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    
    # 프레임 보정을 위한 Delta time
    dt = clock.tick(60) / 1000
    
    # 사각형의 현재 위치 백업
    original_position = moving_rect.topleft

    # 마우스 좌클릭 이벤트 처리
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 왼쪽 버튼 클릭
        mouse_x, mouse_y = event.pos
        # 클릭한 위치의 색상 가져오기
        clicked_color = screen.get_at((mouse_x, mouse_y))
        print(f"Mouse clicked at ({mouse_x}, {mouse_y}) with color: {clicked_color}")
    
    # 키보드 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moving_rect.x -= moving_rect_speed * dt
    if keys[pygame.K_RIGHT]:
        moving_rect.x += moving_rect_speed * dt
    if keys[pygame.K_UP]:
        moving_rect.y -= moving_rect_speed * dt
    if keys[pygame.K_DOWN]:
        moving_rect.y += moving_rect_speed * dt

    # 화면 그리기
    screen.blit(background, background_rect)
    
    # 경계 색상 확인
    left_color = screen.get_at((moving_rect.left, moving_rect.centery))
    right_color = screen.get_at((moving_rect.right - 1, moving_rect.centery))
    top_color = screen.get_at((moving_rect.centerx, moving_rect.top))
    bottom_color = screen.get_at((moving_rect.centerx, moving_rect.bottom - 1))
    
    target_color = (136, 171, 218, 255)
    
    # 색상에 따라 움직임을 제한
    if left_color == target_color:
        moving_rect.left = original_position[0]
    if right_color == target_color:
        moving_rect.right = original_position[0] + moving_rect.width
    if top_color == target_color:
        moving_rect.top = original_position[1]
    if bottom_color == target_color:
        moving_rect.bottom = original_position[1] + moving_rect.height

    # 움직이는 이미지 그리기
    screen.blit(moving_rect_image, moving_rect)

    # 충돌 감지 및 아이템 그리기
    for item_rect in item_list[:]:  # 리스트 복사본을 사용하여 안전하게 삭제 작업 수행
        if moving_rect.colliderect(item_rect):
            item_list.remove(item_rect)  # 충돌한 아이템을 리스트에서 제거
        else:
            screen.blit(item_image, item_rect)  # 아이템이 충돌하지 않았을 때만 그리기

    # 메모리 상에 그린 그림 한번에 출력
    pygame.display.flip()

# 파이게임 종료
pygame.quit()
