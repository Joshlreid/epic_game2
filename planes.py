import pygame
from settings import *

class Enemies(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.up_image = pygame.image.load("assets/images/ship_0005.png").convert()
        self.up_image.set_colorkey((0, 0, 0))
        self.down_image = pygame.transform.flip(self.up_image, False, True)
        self.image = self.up_image
        self.rect = pygame.rect.Rect(x,y,self.image.get_width(), self.image.get_height())
        self.moving_left = True
        self.moving_right = True
        self.moving_up = True
        self.moving_down = True

    def update(self):
        if self.moving_left:
            self.rect.x -= 4
        elif self.moving_right:
            self.rect.x += 4
        if self.moving_up:
            self.image = self.up_image
            self.rect.y -= 4
        elif self.moving_down:
            self.image = self.down_image
            self.rect.y += 4

        if self.rect.left < 0:
            self.rect.left = 0
            self.moving_left = False
            self.moving_right = True
        if self.rect.top < 0:
            self.rect.top = 0
            self.moving_down = True
            self.moving_up = False
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.moving_left = True
            self.moving_right = False
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.moving_up = True
            self.moving_down = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

planes = pygame.sprite.Group()