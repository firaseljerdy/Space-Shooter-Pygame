import pygame
from Bullet import Bullet
from ShieldBar import ShieldBar
from Globals import *


class Player(pygame.sprite.Sprite):
    def __init__(self, player_sprite, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.width, self.height = w, h
        self.defineSelf(player_sprite)
        # Defining object of class shieldBar
        self.shieldBar = ShieldBar()

        # Defining shield for player
        self.shield = 100

        self.lives = 1
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

        self.shieldBar.placeShieldBar(self.rect.x, self.rect.y)
        sprites.add(self.shieldBar)

        self.placeSelf()
        self.speedx = 0

    def update(self):
        self.speedx = 0
        self.keyboardInput()
        self.rect.x += self.speedx
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.alterShieldNumber(25)
            self.hidden = False
            self.placeSelf()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2 + 1200, HEIGHT / 2 + 1200)

    def shoot(self, sprites, bullets):
        print('SHOOT')
        bullet = Bullet(self.rect.centerx, self.rect.top)
        sprites.add(bullet)
        bullets.add(bullet)

    def keyboardInput(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_d]:
            self.speedx = 5
        self.shieldBar.placeShieldBar(self.rect.x, self.rect.y)
        sprites.add(self.shieldBar)

    def defineSelf(self, player_sprite):
        self.image = pygame.transform.scale(player_sprite, (56, 36))
        self.rect = self.image.get_rect()

    def placeSelf(self):
        self.rect.centerx = round(self.width / 2)
        self.rect.bottom = round(self.height)

    def getShield(self):
        return self.shield

    def alterShieldNumber(self, number_shields):
        temp = self.shield + number_shields
        if temp >= 100:
            self.shield = 100
            self.shieldBar.alterShieldBar(self.shield)
        else:
            self.shield += number_shields
            self.shieldBar.alterShieldBar(self.shield)
