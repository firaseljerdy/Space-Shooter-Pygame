import pygame
import random
from os import path
from Globals import *

# C:\Users\jadje\Desktop\Pygame Project\Sounds\Explosion.wav
# C:\Users\jadje\Desktop\Pygame Project\Sounds\Explosion2.wav
# C:\Users\jadje\Desktop\Pygame Project\Sounds\Explosion3.wav

# Importing mixer
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)

# Fetching sounds directory path
sound_dir = path.join(path.dirname(__file__), 'Sounds')

# Defining variables and lists for sounds
explosion_sound_names = ['Explosion.wav', 'Explosion2.wav', 'Explosion3.wav']
shooting_sound_names = ['Laser_Shoot.wav', 'Laser_Shoot2.wav', 'Laser_Shoot3.wav']
background_music = pygame.mixer.Sound(path.join(sound_dir, 'Background_Music.ogg'))
files_explosion_sounds = []
files_shooting_sounds = []

# Fills lists with directory paths
def loadSounds():
    # Storing directories for sound files
    for sound in explosion_sound_names:
        files_explosion_sounds.append(pygame.mixer.Sound(path.join(sound_dir, sound)))
    for sound in shooting_sound_names:
        files_shooting_sounds.append(pygame.mixer.Sound(path.join(sound_dir, sound)))

# Functions that play certain sounds randomly
def playShootingSound():
    random.choice(files_shooting_sounds).play()

def playExplosionSound():
    random.choice(files_explosion_sounds).play()

def playBackgroundMusic():
    background_music.play()
