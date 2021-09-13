import pygame
import random
from Globals import HEIGHT
from LoadGraphics import getPowerupGraphic

class Powerup(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['gun_powerup', 'shield_powerup'])
        print(self.type)
        powerup_images = getPowerupGraphic()
        self.image = powerup_images[self.type]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = 2

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()
