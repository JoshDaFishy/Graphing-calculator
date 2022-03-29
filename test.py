import pygame
from pygame.locals import *

running = True
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size=(800,600))

while running:
    screen.fill((0,0,0))
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    
    pygame.display.flip()


pygame.quit()
