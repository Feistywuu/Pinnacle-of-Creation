#Basic movement

import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

os.chdir('''C:\\Users\\Philip\\Documents\\Programming\\BasicMovement''')

def load_player_image(name, colorkey=None):
    fullname = os.path.join('Pictures', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image         # +image.get_rect()
    

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('Sounds', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print('Cannot load sound:', wav)
        raise SystemExit(message)
    return sound
        
#bullet = 
screen = pygame.display.set_mode((1000,750))
player = load_player_image('warlock.png', None)
background = load_player_image('DotaBG.jpg', None)
screen.blit(background, (0,0))          #draw the background
position = player.get_rect(topleft= (0,300))            #rect of player at (0,0)
screen.blit(player, position)
pygame.display.update()
for x in range(1000):                   #animate 100 frames
    screen.blit(background, position, position) #erase
    position = position.move(1, 0)     #move player
    screen.blit(player, position)      #draw new player
    pygame.display.update()            #and show it all
    pygame.time.delay(100)             #stop the program for 1/10 second





#Towers = ['ceb1', 'flower','ana','godson','jerax']
#Enemies = ['abbadon','alchemist','aa','anti-mage',\
 #          'arc warden','axe','bane','dark willow']













