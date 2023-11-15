import pygame
import sys
from settings import *
from plane import Plane
from planes import Enemies

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Planes!")
mountain = pygame.image.load("assets/images/mountain1.png").convert()
point_mountain = pygame.image.load("assets/images/pointy_mountains.png").convert()
mountain.set_colorkey((0, 0, 0))
point_mountain.set_colorkey((0, 0, 0))
main_plane = Plane(300, 300)

print(point_mountain.get_size())
print(mountain.get_size())

background = screen.copy()
def draw_background():
    background.fill(SKY_COLOR)

    background.blit(point_mountain, (0, 432 ))
    background.blit(mountain, (250, 294))

draw_background()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("no mo play")
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                main_plane.moving_left = True
            if event.key == pygame.K_RIGHT:
                main_plane.moving_right = True
            if event.key == pygame.K_UP:
                main_plane.moving_up = True
            if event.key == pygame.K_DOWN:
                main_plane.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                main_plane.moving_left = False
            if event.key == pygame.K_RIGHT:
                main_plane.moving_right = False
            if event.key == pygame.K_UP:
                main_plane.moving_up = False
            if event.key == pygame.K_DOWN:
                main_plane.moving_down = False

    main_plane.update()

    screen.blit(background, (0, 0))
    main_plane.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
