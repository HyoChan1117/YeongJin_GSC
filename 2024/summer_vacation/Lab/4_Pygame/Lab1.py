import pygame

# 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 화면 지우기
screen.fill(WHITE)

# 점 그리기
pygame.draw.circle(screen, RED, (0, 0), 5)
pygame.draw.circle(screen, RED, (799, 0), 5)
pygame.draw.circle(screen, RED, (0, 599), 5)
pygame.draw.circle(screen, RED, (799, 599), 5)

# 대각선 그리기
pygame.draw.line(screen, RED, (0, 0), (799, 599))
pygame.draw.line(screen, RED, (799, 0), (0, 599))

# 작업된 내용을 화면에 그림 그리기
pygame.display.flip()

running = True
# 이벤트 처리
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
# 종료
pygame.quit()