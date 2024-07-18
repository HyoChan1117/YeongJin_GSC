import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))\
                , (random.randint(0, 799), random.randint(0, 599)), random.randint(10, 100))
            pygame.display.flip()

pygame.quit()