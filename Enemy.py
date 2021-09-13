import pygame
import random
from Globals import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, meteor_graphic, width, height):
        pygame.sprite.Sprite.__init__(self)
        print('enemy created')
        self.screen_width, self.screen_height = width, height
        self.original_image = meteor_graphic
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        self.random_scalex = random.randint(25, 50)
        self.random_scaley = random.randint(25, 50)

        self.rect.x = random.randrange(self.screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -30)
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(3, 9)

        # Defining rotation
        self.rotation = 0
        self.rotation_speed = random.randrange(-8, 8)
        self.last = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last > 75:
            self.last = now
            self.rotation = self.rotation + self.rotation_speed
            new_image = pygame.transform.rotate(self.original_image, self.rotation)
            previous_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = previous_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > self.screen_height + 20 or self.rect.left < - 100 or self.rect.right > self.screen_width + 100:
            self.rect.x = random.randrange(self.screen_width - self.rect.width)
            self.rect.y = random.randrange(-100, -30)
            self.speedx = random.randrange(-3, 3)
            self.speedy = random.randrange(3, 9)
            print('OOB RECREATED')
