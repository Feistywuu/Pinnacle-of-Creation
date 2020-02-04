#Tower Class

import pygame, random, math
from pygame.locals import *
from LoadedAssets import *
import Mobs
import Projectiles

#Global Variables defined, thus can be used in InstanceObjects
PlacedTowers = []           #List of form - [ (TowerSurf,((xpos,ypos))), ]

#List containing Tower Subclasses, contains placed (x,y) position
SpawnPoints = []


class Tower():

    def __init__(self):
        self.BlueTrue = False                   #Tower blueprint state 
        self.x = 0
        self.y = 0
        self.BlueCentre = (0,0)
        self.BlueSurf = pygame.Surface((0,0)) 
        self.TowerSurf = pygame.Surface((0,0))
        self.range = 300                        #Change w/Tower subclass
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
        :return: x, y, list, class
        '''
        if self.BlueTrue == True:               #Removes Blueprint
            self.BlueTrue = False               
            self.TowerSurf = Imgs2[self.image]
            self.x, self.y = pygame.mouse.get_pos()
            self.centre = ( ( self.x - (self.TowerSurf.get_width())/2),\
                            ( self.y - (self.TowerSurf.get_height())/2)  )
            PlacedTowers.append( ((self.TowerSurf),(self.centre)) )
            SpawnPoints.append(self)
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
        Checks if Blueprint is active: if not, clears BlueSurf; if yes,
        returns BlueCentre
        :return: Surf
        '''
        if self.BlueTrue == False:
            self.BlueSurf = pygame.Surface((0,0))
        if self.BlueTrue == True:
            self.x, self.y = pygame.mouse.get_pos()
            self.BlueCentre = ( ( self.x - (self.BlueSurf.get_width())/2),\
                                ( self.y - (self.BlueSurf.get_height())/2)  )
        else: pass
        
    def Detect(self):
        '''
        Checks if Mobs in MobList are within Tower Range, depending on
        Tower pos to Mob pos, checks 1 point on the mob to determine
        if in range
        :return: bool
        '''
        #This chooses which part of mob to calculate distance on
        #If tower.x is within mob.x then distance is mapped to distance
        #between self.y and mob.y
        #Else Tower distance based on distance to corners
        for mob in Mobs.MobList:
            a = mob.surf.get_width()
            b = mob.surf.get_height()

            #Top side of Hitbox:
            if self.y <= mob.CentY - a/2:
                #TopRight
                if self.x >= mob.CentX + a/2:
                    dis1 =(abs(self.x -(mob.CentX + a/2)))**2+\
                          (abs(self.y -(mob.CentY - b/2)))**2
                    dis = math.sqrt(dis1)
                #TopMiddle
                if mob.CentX - a/2 < self.x < mob.CentX +\
                   mob.surf.get_width()/2:
                    dis = abs(self.y -(mob.CentY - b/2))
                #TopLeft
                if self.x <= mob.CentX - a/2:
                    dis2 = (abs(self.x - a/2))**2+\
                           (abs(self.y - b/2))**2
                    dis = math.sqrt(dis2)
            #Bottom Side of Hitbox:
            if self.y >= mob.CentY + b/2:
                #BotRight
                if self.x >= mob.CentX + a/2:
                    dis3 =(abs(mob.CentX + a/2-(self.x)))**2+\
                          (abs(self.y -(mob.CentY + b/2)))**2
                    dis = math.sqrt(dis3)
                #BotMiddle
                if mob.CentX + a/2 > self.x > mob.CentX - a/2:
                    dis = abs(self.y-(mob.CentY + b/2))
                #BotLeft
                if self.x < mob.CentX - a/2:
                    dis4=(abs(mob.CentX - a/2-(self.x)))**2+\
                         (abs(self.y -(mob.CentY + b/2)))**2
                    dis = math.sqrt(dis4)
            #Middle Left/Right of Hitbox:
            if mob.CentY + mob.surf.get_height()/2 > self.y > mob.CentY \
               - mob.surf.get_height()/2:
                if self.x >= mob.CentX:
                    dis = abs(self.x - (mob.CentX + mob.surf.get_width()/2))
                if self.x < mob.CentY:
                    dis = abs(self.x - (mob.CentX - mob.surf.get_width()/2))
            
            if dis == 0:
                print('on point')
            if dis <= self.range:
                print('woo, IN RANGE')
                self.Shoot()
        
                    
        
    

    
    #def DumbShoot(self):
        #'''
    
    #for x in self.PlacedTowers:
        #if x[0] == Imgs2[0]:                    
            #(Projs[0].x , Projs[0].y) = x[1]

            #appends to ProjectileList


class ceb(Tower):

    def __init__(self):
        Tower.__init__(self)
        self.image = 0

    #Simple Shoot
    def Shoot(self):
        print(Projectiles.ProjList)
        #Projectiles.ProjList.append('3')
        #print(Projectiles.ProjList)

class ana(Tower):

    def __init__(self):
        Tower.__init__(self)
        self.image = 1

    def Shoot(self):
        print('1')

class BigDaddy(Tower):

    def __init__(self):
        Tower.__init__(self)
        self.image = 2

    def Shoot(self):
        print('6')
              
class godson(Tower):

    def __init__(self):
        Tower.__init__(self)
        self.image = 3

    def Shoot(self):
        print('2')
        
class jerax(Tower):

    def __init__(self):
        Tower.__init__(self)
        self.image = 4

    def Shoot(self):
        print('4')
        
        

        
#DumbShoot()      
# Create SpawnedProjectiles List: x,y based PlacedTowers x,y ; bool - Shooting
# Shooting == True by default
# After Shooting == True, periodically spawns 




#For Detection:
# Looks up (x,y) in MobList, then makes calculation
# When Detection == True
# Sets Shooting = True on SpawnPoint element

#Projectiles will spawn from each x,y in PlacedTowers
#Depending on TowerSurf type, different Proj
    #Dependent on i.image 
             














            
