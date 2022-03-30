import pygame
from pygame.locals import *

screenx = 800
screeny = 600
running = True
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size=(screenx,screeny))


def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, screenx, blockSize):
        for y in range(0, screeny, blockSize):
            if not (x < blockSize*4 or screeny - y < blockSize*4):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, ((10,10,10)), rect, 1)
    pygame.draw.lines(screen, (0,0,0), False, [(blockSize*4,0),(blockSize*4,(screeny-blockSize*4)),(blockSize*4,screeny-blockSize*4),(screenx,(screeny-blockSize*4))], 1)

while running:
    screen.fill((255,255,255))
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    drawGrid()


    pygame.display.flip()


pygame.quit()
