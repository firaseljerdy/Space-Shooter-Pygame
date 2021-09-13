import pygame
from os import path

width, height = 500, 500

def setWidthHeight(w, h):
    width, height = w, h

screen = pygame.display.set_mode((width, height))

img_dir = path.join(path.dirname(__file__), 'Images')
bullet_sprite = pygame.image.load(path.join(img_dir, 'laserBlue16.png' )).convert_alpha()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_sprite

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -12

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
