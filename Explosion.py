import pygame
from os import path
from LoadGraphics import getExplosionAnim


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, type):
        pygame.sprite.Sprite.__init__(self)
        self.explosion_anim = getExplosionAnim()
        self.type = type
        self.image = self.explosion_anim[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.center = center

        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 22

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_anim[self.type]):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion_anim[self.type][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
