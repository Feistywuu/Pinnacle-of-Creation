#Projectile Class

import random
import pygame
from pygame.locals import *
from LoadedAssets import *

ProjList = []

#List of Projectile Subclasses

class Projectile():     #make subclass for surfaces

    def __init__(self, surf, move):
        self.x = 300
        self.y = 800
        self.surf = surf
        self.rect = self.surf.get_rect(topleft=(self.x,800))
        self.move = move
        
    def ProjMovement(self):
        '''
        Moves Projectile across the screen
        :return: Rect
        '''
        newpos = self.rect.move((0, self.move))
        self.rect = newpos

    def Collide(self, Mob):
        '''
        Detects is projectile hits a Mob  
        :Return: Bool
        '''
        if Mob.rect.right >= self.rect.x >= Mob.rect.x\
        and Mob.rect.bottom >= self.rect.y >= Mob.rect.y\
        or Mob.rect.right >= self.rect.right >= Mob.rect.x\
        and Mob.rect.bottom >= self.rect.bottom >= Mob.rect.y:
        #Checks if TopLeft has Collided with Mob +
        #Checks if BottomRight has collided with Mob (To cover entire square)
                return True
        return False

    def Explode(self):
        '''
        Makes sound if Collide() == True
        Deletes projectile
        :return: None
        '''
        explode_sound.play()                                #Plays sound
        self.move = 0
        self.rect = self.surf.get_rect(topleft=(1000,800))

class LuckySometimes(Projectile):

    def __init__(self):
        Projectile.__init__(self)
        
        
        
