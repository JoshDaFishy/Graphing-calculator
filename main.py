import pygame, json
from pygame.locals import *

with open("data.json") as f:
    data = json.load(f)

screenx = 800
screeny = 800
running = True
pygame.init()
clock = pygame.time.Clock()
angle = 0
screen = pygame.display.set_mode(size=(screenx,screeny))
original_surf = pygame.Surface((10,10), pygame.SRCALPHA)
original_surf.fill((255,0,0))
coords = []


def drawGrid():
    squarecount = 0
    blockSize = 20 #Set the size of the grid block
    for x in range(0, screenx, blockSize):
        for y in range(0, screeny, blockSize):
            if not (x < blockSize*4 or screeny - y < blockSize*5):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, ((10,10,10)), rect, 1)
                squarecount += 1
    pygame.draw.lines(screen, (0,0,0), False, [(blockSize*4,0),(blockSize*4,(screeny-blockSize*4)),(blockSize*4,screeny-blockSize*4),(screenx,(screeny-blockSize*4))], 1)
    return squarecount,blockSize*4,blockSize*5
    # ((x/blockSize)-3)

outputdata = drawGrid()
squarecounter = outputdata[0]
marginx = outputdata[1]
marginy = outputdata[2]

for i in range(0,len(data["x"])):
    pointx = (((data["x"][i]/squarecounter) * 1000) + marginx)
    pointy = (((data["y"][i]/squarecounter) * 1000) + marginy)
    coords.append((pointx,pointy))


while running:
    screen.fill((255,255,255))
    outputdata = drawGrid()
    squarecounter = outputdata[0]
    marginx = outputdata[1]
    marginy = outputdata[2]
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    for i in range(0,len(data["x"])):
        surf = pygame.transform.rotate(original_surf, angle)   
        surfrect = surf.get_rect()
        surfrect.centerx = (((data["x"][i]/squarecounter) * 1000) + marginx)
        surfrect.centery = (((data["y"][i]/squarecounter) * 1000) + marginy)
        screen.blit(surf,(surfrect))
    pygame.draw.lines(screen,((255,0,0)),False,coords, 1)
    pygame.display.flip()
    # angle += 1
    # print(angle)
    # if angle == 90:
    #     angle = 0 

pygame.quit()
