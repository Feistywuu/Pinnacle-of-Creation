#Classtest 

import os, sys
import pygame
from pygame.locals import *

os.chdir('''C:\\Users\\Philip\\Documents\\Programming\\BasicMovement''')
picture_dir = os.path.join(os.getcwd(), "Pictures")

#Functions to load images,sound
def load_image(name, colorkey=None):
    fullname = os.path.join(picture_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print("Cannot load image:", fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image


class Mob():

    def __init__(self, surf):
        self.surf = surf
        self.rect = self.surf.get_rect()
        self.move = 4
        
    def movement(self):
        '''
        Moves Mobs across the screen
        :return: Rect
        '''
        newpos = self.rect.move((self.move, 0))
        self.rect = newpos

#Initialize Everything
pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption('you da king')
pygame.mouse.set_visible(1)

#Create Background - Screen + Road
bg1 = pygame.Surface(screen.get_size())
bg1 = bg1.convert()
bg1.fill((0,0,0))
bg2 = pygame.Surface((1000,100))     #Road
bg2 = bg2.convert()
bg2.fill((12,60,123))

#Display The Background
screen.blit(bg1, (0,0))
screen.blit(bg2, (0,350))
pygame.display.flip()

#Preparing Objects
AA = Mob(load_image('aa.png', -1))
AA.movement()

#Main
screen.blit(AA.surf,(0,380))
pygame.display.update()

    
