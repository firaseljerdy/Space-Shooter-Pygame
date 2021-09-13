# Importing libraries
import pygame
import random
from os import path
from Player import Player
from Enemy import Enemy
from Sounds import *
from Globals import *
from LoadGraphics import *
from Explosion import Explosion
from Powerup import Powerup

# Defining constants
FPS = 60
# set up dir
img_dir = path.join(path.dirname(__file__), 'Images')

# Function to handle text output
def draw_text(place, text, size, x, y):
    font_type = pygame.font.match_font('arial')
    font = pygame.font.Font(font_type, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    place.blit(text_surface, text_rect)

def drawStartScreen():
    startscreen = True
    while startscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    startscreen = False

        draw_text( screen, "SPACE SHOOTER", 58, WIDTH / 2, HEIGHT / 4)
        draw_text(screen, "Move with A/D | SPACE to shoot", 24, WIDTH / 2, HEIGHT / 2)
        draw_text(screen, "Press ENTER to start game", 20, WIDTH / 2, HEIGHT * 3/4)
        pygame.display.update()
        clock.tick(15)

def loadEnemyGraphics():
    # Meteor files
    meteor_names =  ['meteorBrown_big1.png', 'meteorBrown_big2.png','meteorBrown_big3.png','meteorBrown_big4.png',
                    'meteorBrown_med1.png','meteorBrown_med3.png', 'meteorBrown_small1.png',
                    'meteorBrown_small2.png', 'meteorBrown_tiny1.png', 'meteorBrown_tiny2.png']
    meteor_files = []
    # Storing directories inside of meteor_files
    for image in meteor_names:
        meteor_files.append(pygame.image.load(path.join(img_dir, image)).convert_alpha())

    return meteor_files

instEnemies = []

def createEnemyInstance():
    enemy = Enemy(random.choice(enemy_graphic), WIDTH, HEIGHT)
    sprites.add(enemy)
    enemies.add(enemy)

# Init all game components
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

pygame.init()
loadSounds()

clock = pygame.time.Clock()

# Window creation
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Shoot em up')

# Defining graphics
background      =     pygame.image.load(path.join(img_dir, 'darkPurple.png')).convert()
background_rect =     background.get_rect()
player_sprite   =     pygame.image.load(path.join(img_dir, 'playerShip2_blue.png')).convert_alpha()
bullet_sprite   =     pygame.image.load(path.join(img_dir, 'laserBlue16.png' )).convert_alpha()

# def of player instance
player = Player(player_sprite, WIDTH, HEIGHT)

# add player sprite to sprite Group
sprites.add(player)

enemy_graphic      =       loadEnemyGraphics()
explosion_graphics =       loadExplosionGraphics() # load explosion graphics

for i in range(6):
    createEnemyInstance()

# Main loop variable
done = False
score = 0
# playBackgroundMusic()
inv_time = pygame.time.get_ticks()

drawStartScreen()

# Game loop
while not done:
    clock.tick(FPS)
    #Events (process inputs)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # shoot and play sound
                player.shoot(sprites, bullets)
                playShootingSound()

    # Testing between group enemy and group bullets
    collisions = pygame.sprite.groupcollide(enemies, bullets, True, True)
    # Recreating enemies when killed
    for enemy in collisions:
        playExplosionSound()
        score += 100 - enemy.radius
        explosion = Explosion(enemy.rect.center, 'explosion') # Spawning explosion
        sprites.add(explosion)
        createEnemyInstance()

        if random.random() > 0.95:
            powerup = Powerup(enemy.rect.center)
            sprites.add(powerup)
            powerups.add(powerup)

    # Testing between player and powerup
    collisions = pygame.sprite.spritecollide(player, powerups, True, pygame.sprite.collide_circle)
    for collision in collisions:
        if collision.type == 'shield_powerup':
            if player.shield >= 100:
                player.shield = 100
            else:
                player.alterShieldNumber(25)

    # Test for collisions between player and enemy sprites. Circular cols
    if playerInvincible == False:
        collisions = pygame.sprite.spritecollide(player, enemies, True, pygame.sprite.collide_circle)
        for collision in collisions:
            createEnemyInstance()
            player.alterShieldNumber(-(collision.radius * 1.5))
            if player.getShield() <= 0:
                explosion = Explosion(player.rect.center, 'ship_explosion')
                sprites.add(explosion)
                player.lives -= 1
                player.hide()
                playerInvincible = True
                inv_time = pygame.time.get_ticks()
                player.alterShieldNumber(1000)

    else:
        if pygame.time.get_ticks() - inv_time > 4000:
            playerInvincible = False

    #Update the Game
    sprites.update()
    #Render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    sprites.draw(screen)
    draw_text(screen, str(score), 20, WIDTH / 2, 15)
    pygame.display.flip()

pygame.quit()
