
import pygame

# 초기화
pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

# 이벤트 처리
while running: # while이 event를 기다림
    for event in pygame.event.get(): # get이라는 매소드를 호출하면 Queue 안에 쌓여있던 Event들을 호출
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

# 종료
pygame.quit()


# 이벤트를 보관하기 위해서 사용하는 자료구조 : Queue
# Queue : Event -> FIFO(First In Fist Out) : 들어왔는 순서대로 나감
# 데이터가 밀려들어오면 순차적으로 처리해야 함