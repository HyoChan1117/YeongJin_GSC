import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# 사각형 정의
rect1 = pygame.Rect(screen.get_width(), 40, 80, 40)

# 객체 이동 속도
speed = 100 # 100 pixel / 1 sec
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000  # dt이 second 단위이기 때문에 1000을 나눠줌

    # <-, -> Key를 누를 때 사각형을 좌우로 이동
    
    
    
    # rect1.x += speed * dt
    # rect1.y += speed * dt
    
    # if rect1.x + rect1.width 값이 > screen.width
    #    rect1.x = screen.width - rect1.width
    
    # if rect1.x + rect1.width > screen.get_width():
    #     rect1.x = screen.get_width() - rect1.width
    #     speed = -speed  # 방향 반대로 ( + -> - )
    # if rect1.x < 0:
    #     rect1.x = 0
    #     speed = -speed  # 방향
    
    # if rect1.bottom > screen.get_height():
    #     rect1.bottom = screen.get_height()
    #     speed = -speed  # 방향 반대로 ( + -> - )
    # if rect1.top < 0:
    #     rect1.top = 0
    #     speed = -speed  # 방향
    
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 255), rect1) # Rect 객체 이용
    
    
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    
    
pygame.quit()