import math

import pygame
import pygame.math
from settings import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/tile_0000.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.y_speed = 0
        self.x_speed = 0

    def shoot(self, start_position, target_position):
        self.rect.center = start_position
        x = target_position[0] - start_position[0]
        y = target_position[1] - start_position[1]
        theta = math.atan2(y, x)
        self.y_speed = 7*math.sin(theta)
        self.x_speed = 7*math.cos(theta)

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
