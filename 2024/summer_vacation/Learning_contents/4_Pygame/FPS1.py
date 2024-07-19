import pygame

## <<--- 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))

## <<-- fps 적용을 위한 시간 객체 생성
clock = pygame.time.Clock()
fps = 30
count = 0
## -->>

x = screen.get_width() / 2
y = screen.get_height() / 2
radius = 40
speed = 10 # pixel/second -> 1초에 10픽셀 움직임

## <<--- 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 40)
    x += 10
    
    if x + radius >= screen.get_width() or x - radius <= 0:
        speed = -speed
    
    pygame.display.flip()
    
    ## <<-- pygame fps 설정
    print(count)
    count += 1
    clock.tick(fps)# -> 30초에 이미지 1장 생성
    ## -->>
## -->> 이미지 생성

## 게임 종료
pygame.quit()
