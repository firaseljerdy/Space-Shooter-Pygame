# Importing libraries
import pygame
import random

# Defining constants
WIDTH, HEIGHT = 1000, 800
FPS = 30

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


pygame.quit()

# Init all game components
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

#Group of sprites
sprites = pygame.sprite.Group()

# Window creation
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')

# Main loop variable
done = False

# Game loop
while not done:
    clock.tick(FPS)
    #Events (process inputs)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Update the Game
    sprites.update()

    #Render
    sprites.draw(screen)
    screen.fill(BLUE)
    pygame.display.flip()
