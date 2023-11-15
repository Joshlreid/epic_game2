import pygame
from settings import *

class Plane(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.up_image = pygame.image.load("assets/images/ship_0000.png").convert()
        self.up_image.set_colorkey((0, 0, 0))
        self.down_image = pygame.transform.flip(self.up_image, True, False)
        self.image = self.up_image
        self.rect = pygame.rect.Rect(x,y,self.image.get_width(), self.image.get_height())
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_left:
            self.rect.x -= 2
            self.image = self.down_image
        elif self.moving_right:
            self.rect.x += 2
            self.image = self.up_image
        if self.moving_up:
            self.rect.y -= 2
        elif self.moving_down:
            self.rect.y += 2

        if self.rect.left < 0:
            self.rect.left = 0
            self.moving_left = False
            self.moving_right = False
        if self.rect.top < 0:
            self.rect.top = 0
            self.moving_down = False
            self.moving_up = False
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.moving_left = False
            self.moving_right = False
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.moving_up = False
            self.moving_down = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)



