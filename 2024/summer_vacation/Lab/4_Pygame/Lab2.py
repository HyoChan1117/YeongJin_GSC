
import pygame
import random

# 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))

# 화면 초기화
screen.fill((255, 255, 255))
pygame.display.flip()

# 원 그리기
rand_num = random.randint(5, 20)
for _ in range(rand_num):
    rand_r = random.randint(0, 255)
    rand_g = random.randint(0, 255)
    rand_b = random.randint(0, 255)
    rand_x = random.randint(0, 799)
    rand_y = random.randint(0, 599)
    rand_size = random.randint(10, 100)
    pygame.draw.circle(screen, (rand_r, rand_g, rand_b), (rand_x, rand_y), rand_size)
    

pygame.display.flip() # 화면 업데이트

# 이벤트 처리
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
# 종료
pygame.quit()