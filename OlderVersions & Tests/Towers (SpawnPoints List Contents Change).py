#Tower Class

import pygame, random
from pygame.locals import *
from LoadedAssets import *

#Global Variables defined, thus can be used in InstanceObjects

PlacedTowers = []           #List of form - [ (TowerSurf,((xpos,ypos))), ]

#List of Form [ ( (x,y), bool, int ) , ]
#Contains x,y position of Placed towers, bool(Shooting), Projectile Type

SpawnPoints = []

#SpawnPoint should contain Tower Objects
#Different Subclasses for Different ProjTypes?

class Tower():

    def __init__(self, image):
        self.BlueTrue = False   #Tower blueprint state
        self.Shooting = False 
        self.x = 0
        self.y = 0
        self.image = image      #Defined so Surf from Imgs[] can be chosen
        self.BlueSurf = pygame.Surface((0,0)) 
        self.TowerSurf = pygame.Surface((0,0))
        #self.ProjType
        
    def ToggleBlue(self):
        '''
        Checks for keypress, then changes state
        :return: Bool
        '''
        if self.BlueTrue == False:
            self.BlueTrue = True
            print('Toggled: Blue == True')
        else: pass
      
    def Blueprint(self):            
        '''
        Fills Tower surface with blue colour if ToggleBlue() is called
        :return: Surf
        '''
        if self.BlueTrue == False:
            self.BlueSurf = pygame.Surface((0,0))       
            pass
        if self.BlueTrue == True:
            self.BlueSurf = Imgs[self.image]
            self.BlueSurf.fill((0,128,255))
            pygame.mouse.set_visible(0)
            
    def Build(self):
        '''
        Places Tower at current mouse pos, adds current TowerSurf + x,y
        to TowerList
        :return: x, y
        '''
        if self.BlueTrue == True:               #Removes Blueprint
            self.BlueTrue = False               
            self.TowerSurf = Imgs2[self.image]
            self.x, self.y = pygame.mouse.get_pos()            
            self.centre = ( (self.x - (self.TowerSurf.get_width()/2)),\
                            (self.y - (self.TowerSurf.get_height()/2))  )
            PlacedTowers.append( ((self.TowerSurf),(self.centre)) )
            pygame.mouse.set_visible(1)
            print('Tower placed at x,y = ('+str(self.x)+','+str(self.y)+')')
        else:
            print('No Blueprint: Press Q,W,E,R,T')
            pass
        
    def Cancel(self):
        '''
        Upon right click, sets blue surface to clear
        :return: Surf
        '''
        if self.BlueTrue == True:
            self.BlueSurf = pygame.Surface((0,0))

    def IsBlue(self):
        '''
        Checks if Blueprint is active, if not, clears BlueSurf
        :return: Surf
        '''
        if self.BlueTrue == False:
            self.BlueSurf = pygame.Surface((0,0))
        else: pass
        
    def CreateSpawn(self):
        '''
        Checks elements in PlacedTowers List: Makes List with same elements
        + respective of Surf, a Proj object + Shooting == True by default
        :return: x, y, Surf, bool 
        '''

    def Detection():
        pass
    
    #def DumbShoot(self):
        #'''


    #for x in self.PlacedTowers:
        #if x[0] == Imgs2[0]:                    
            #(Projs[0].x , Projs[0].y) = x[1]

            #appends to ProjectileList



#DumbShoot()      
# Create SpawnedProjectiles List: x,y based PlacedTowers x,y ; bool - Shooting
# Shooting == True by default
# After Shooting == True, periodically spawns 




#For Detection:
# When Detection == True
# Sets Shooting = True on SpawnPoint element

#Projectiles will spawn from each x,y in PlacedTowers
#Depending on TowerSurf type, different Proj
    #Dependent on i.image 
             















            
