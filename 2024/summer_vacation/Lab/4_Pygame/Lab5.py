import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

# 무작위 색상 생성
rand_color = random.randint(0, 255)
# 시작점 (화면 중앙)
center_x, center_y = screen.get_width() / 2, screen.get_height() / 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        