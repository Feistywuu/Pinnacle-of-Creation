#Mob Class

import random, pygame
#from pygame.locals import *
from LoadedAssets import *

#List of Mob Subclasses
SpawnedMobs = []

class Mob():
     
    def __init__(self):  

        self.surf = MobImgs[self.image]
        self.rect = self.surf.get_rect(topleft=(0,380))     #Starting Pos
        self.CentX = 0
        self.CentY = 0
        
        

    def Movement(self):
        '''
        Moves Mobs across the screen
        :return: Rect
        '''
        self.newpos = self.rect.move((self.move, 0))
        self.rect = self.newpos
        self.CentX =  (self.newpos.x) + ((self.surf.get_width())/2)
        self.CentY =  (self.newpos.y) + ((self.surf.get_height())/2)



class AA(Mob):

    def __init__(self, move):
        self.image = 0                      #Is this order okay?
        Mob.__init__(self)                  #Come back to super()
        self.move = move
        

        
        
class DarkWillow(Mob):

    def __init__(self):
        image = 1

class Axe(Mob):

    def __init__(self):
        image = 2

    
    
