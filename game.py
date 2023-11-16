import pygame
import sys
import random
from settings import *
from plane import Plane
from planes import Enemies, planes
from bullet import Bullet

pygame.init()

#background
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Planes!")
mountain = pygame.image.load("assets/images/mountain1.png").convert()
point_mountain = pygame.image.load("assets/images/pointy_mountains.png").convert()
mountain.set_colorkey((0, 0, 0))
point_mountain.set_colorkey((0, 0, 0))

# moving objects
main_plane = Plane(300, 300)
shot = Bullet(300, 300)
for _ in range(NUM_PLANES):
    planes.add(Enemies(random.randint(0, SCREEN_WIDTH),
                      random.randint(0, SCREEN_HEIGHT)))

# drawing background
background = screen.copy()
def draw_background():
    background.fill(SKY_COLOR)

    background.blit(point_mountain, (0, 432 ))
    background.blit(mountain, (250, 294))

draw_background()

# looking for events
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("no mo play")
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                main_plane.moving_left = True
            if event.key == pygame.K_d:
                main_plane.moving_right = True
            if event.key == pygame.K_w:
                main_plane.moving_up = True
            if event.key == pygame.K_s:
                main_plane.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                main_plane.moving_left = False
            if event.key == pygame.K_d:
                main_plane.moving_right = False
            if event.key == pygame.K_w:
                main_plane.moving_up = False
            if event.key == pygame.K_s:
                main_plane.moving_down = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            shot.shoot(main_plane.rect.center, pygame.mouse.get_pos())


    main_plane.update()
    planes.update()
    shot.update()

    screen.blit(background, (0, 0))
    main_plane.draw(screen)
    planes.draw(screen)
    shot.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
