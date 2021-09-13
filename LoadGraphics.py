import pygame
from os import path

img_dir       =      path.join(path.dirname(__file__), 'Images')
explosion_dir =      path.join(img_dir, 'Explosion')

ship_explosion_dir = path.join(img_dir, 'Ship Explosion')


# Dictionary to store frames
explosion_animation = {}
explosion_animation['explosion'] = []
explosion_animation['ship_explosion'] = []

powerup_images = {}
powerup_images['shield_powerup'] =      pygame.image.load(path.join(img_dir, 'shield_gold.png')).convert_alpha()
powerup_images['gun_powerup']    =      pygame.image.load(path.join(img_dir, 'bolt_gold.png')).convert_alpha()


def getPowerupGraphic():
    return powerup_images


# Loading all frames and images
def loadExplosionGraphics():
    for i in range(41):
        frames = 'tile0({}).png'.format(i)                                          # Looping and collecting all frames in my directory
        image = pygame.image.load(path.join(explosion_dir, frames)).convert_alpha() # Loading all these frames so i can use them
        image_explosion = image                                                     # Making a copy of the original images
        explosion_animation['explosion'].append(image_explosion)                    # Adding them to my dictionary for later use

    for i in range(9):
        frames = 'sonicExplosion0{}.png'.format(i)
        image = pygame.image.load(path.join(ship_explosion_dir, frames)).convert_alpha()
        ship_explosion = image
        explosion_animation['ship_explosion'].append(ship_explosion)

    return explosion_animation

# Returning all explosion images
def getExplosionAnim():
    return explosion_animation
