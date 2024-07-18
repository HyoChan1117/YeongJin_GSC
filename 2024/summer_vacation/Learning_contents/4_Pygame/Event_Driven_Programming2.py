
import pygame

# 초기화
pygame.init()
screen = pygame.display.set_mode((640, 480))
running = True

# 색깔 정의
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 이벤트 처리
while running:
    # 이벤트 큐에서 이벤트를 가져옴
    # 이벤트가 종료될 때까지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((255, 255, 255)) # 이벤트가 발생할 때
    
    pygame.draw.circle(screen, GREEN, (100, 200), 40)
    pygame.draw.circle(screen, RED, (300, 500), 40)
    
    pygame.display.flip() # 메모리를 읽고 쓰는데에 시간이 걸리는데 flip을 사용함으로써 한번에
                            # 그림을 그릴 수 있음
        
# 종료
pygame.quit()