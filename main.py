import pygame, json
from pygame.locals import *

with open("data.json") as f:
    data = json.load(f)

coords = []

for i in range(0,len(data["x"])):
    pointx = data["x"][i]
    pointy = data["y"][i]
    coords.append((pointx,pointy))


running = True
pygame.init()
clock = pygame.time.Clock()
angle = 0
screen = pygame.display.set_mode(size=(800,600))
original_surf = pygame.Surface((50,50), pygame.SRCALPHA)
original_surf.fill((255,0,0))

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
        surf = pygame.transform.rotate(original_surf, angle)
        surfrect = surf.get_rect()
        surfrect.centerx = (data["x"][i])
        surfrect.centery = (data["y"][i])
        screen.blit(surf,(surfrect))
    pygame.draw.lines(screen,((255,0,0)),False,coords, 1)
    pygame.display.flip()
    angle += 1
    print(angle)
    if angle == 90:
        angle = 0 

pygame.quit()
