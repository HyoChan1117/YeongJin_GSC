import pygame

# 색상 정의
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

x = screen.get_width()/2
y = screen.get_height()/2
radius = 20
speed = 5

running = True
while running:
    for event in pygame.event.get():  # -> 이벤트 리스너 역할
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 200, 200)) 
    
    pygame.draw.circle(screen, (150, 150, 255), (x, y), radius)  
    
    if x + radius >= screen.get_width() or x - radius <= 0:
        speed = -speed
        
    x += speed

    pygame.display.flip() # -> 메모리 저장된 이벤트가 한 번에 그려지는 것
    
    clock.tick(120)


  
        
pygame.quit()


