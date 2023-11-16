import pygame
from settings import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/tile_0000.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.rect.Rect(x,y,self.image.get_width(), self.image.get_height())
        self.y_speed = 0
        self.x_speed = 0

    def shoot(self, start_position, target_position):
        self.rect.center = start_position
        self.y_speed = 5
        self.x_speed = 5

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

