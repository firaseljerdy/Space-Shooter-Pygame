import pygame

WIDTH, HEIGHT = 480, 600

# Group of sprites
sprites     =     pygame.sprite.Group()
enemies     =     pygame.sprite.Group()
bullets     =     pygame.sprite.Group()
powerups    =     pygame.sprite.Group()

playerInvincible = False

#Colors
BLACK   =       (0, 0, 0)
WHITE   =       (255, 255, 255)
RED     =       (255, 0, 0)
BLUE    =       (0, 0, 255)
GREEN   =       (0, 255, 0)
YELLOW  =       (255, 255, 0)
