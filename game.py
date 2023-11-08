import pygame
import sys
from settings import *


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Planes!")
house = pygame.image.load("assets/images/house_front_tall.png").convert()
big_house = pygame.image.load("assets/images/house_side_tall.png").convert()
mountain = pygame.image.load("assets/images/mountain1.png").convert()
point_mountain = pygame.image.load("assets/images/pointy_mountains.png").convert()
house.set_colorkey((0, 0, 0))
big_house.set_colorkey((0, 0, 0))
mountain.set_colorkey((0, 0, 0))
point_mountain.set_colorkey((0, 0, 0))

print(point_mountain.get_size())
print(mountain.get_size())
house = pygame.transform.scale(house, (50,50 ))

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

    pygame.display.flip()
    pygame.time.Clock().tick(60)
    screen.blit(background, (0, 0))
