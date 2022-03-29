import pygame, json
from pygame.locals import *

with open("data.json") as f:
    data = json.load(f)


running = True
pygame.init()
clock = pygame.time.Clock()
angle = 0
screen = pygame.display.set_mode(size=(800,600))
# testsurf = pygame.image.load("fish.jpg").convert_alpha()
# testsurfrect = testsurf.get_rect()
# testsurf = pygame.transform.rotate(testsurf,96)
while running:
    screen.fill((0,0,0))
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    for i in range(0,len(data["x"])):
        surf = pygame.Surface((50,50))
        surf.fill((255,0,0))
        surfrect = surf.get_rect()
        surfrect.x = (data["x"][i])
        surfrect.y = (data["y"][i])
        surf = pygame.transform.rotate(surf,angle)
        screen.blit(surf,(surfrect))
    # screen.blit(testsurf,(testsurfrect))
    # testsurf = pygame.transform.rotate(testsurf,96)
    pygame.display.flip()
    angle += 1
    print(angle)
    if angle == 90:
        angle = 0 

pygame.quit()
