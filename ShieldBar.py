import pygame
from os import path
from Globals import *

img_dir = path.join(path.dirname(__file__), 'Images')
shieldBar_graphic = pygame.image.load(path.join(img_dir, 'ShieldBar.png'))

class ShieldBar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.defineSelf()

    def defineSelf(self):
        self.image = pygame.transform.scale(shieldBar_graphic, (50, 5))
        self.rect = self.image.get_rect()
        self.BAR_WIDTH = 100

    def placeShieldBar(self, x, y):
        self.rect.centerx = x + 30
        self.rect.centery = y - 10

    def alterShieldBar(self, remaining_shield):
        fill = (remaining_shield / 100) * self.BAR_WIDTH

        if fill <= 0:
            fill = 0
            self.kill()
        else:
            self.image = pygame.transform.scale(shieldBar_graphic, (round(50 * fill / self.BAR_WIDTH), 5))

        print(fill)
