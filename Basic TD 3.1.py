#Main Code

import pygame, random, time
from pygame.locals import *

#Initialize Everything
pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption('you da king')
pygame.mouse.set_visible(1)

#Importing Assets, requiring pygame.display
from LoadedAssets import *
from Towers import Tower
from Mobs import Mob, AA, DarkWillow, Axe
from Projectiles import Projectile      #'#'?      
from InstanceObjects import *

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
clock = pygame.time.Clock()
RandX = random.randint(200,800)

#Level Functions
def Spawn():
    '''
    Spawns Mobs by appending to SpawnedMobs List
    :return: List
    '''
    MobAA = AA(4)
    MobList.append(MobAA)
    print('Mob Spawned. Current Mobs:')
    print(MobList)
        

#Why is the move*2?
# because x in spawnedmobs iterates over y in projs


#Main Loop
def Main():
    run = True
    t = 0
    print(pygame.time.get_ticks)
    while run:
        clock.tick(30)
        screen.blit(bg1, (0,0))                 #Erasing Screen
        screen.blit(bg2, (0,350))
        
        #Spawnings
        if t%60 == 0:
            Spawn()
        print('before tower')
        print(pygame.time.get_ticks)
        #User Input/Events
        for i in Towers:
            for event in pygame.event.get():
                #Checking type of inputs            
                if event.type == QUIT:
                    run = False
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    run = False
                elif event.type == KEYDOWN:
                    if event.key == K_q:
                        Towers[0] = ceb()        
                        i = Towers[0]
                        i.ToggleBlue()
                        i.Blueprint()
                    if event.key == K_w:
                        Towers[0] = ana()        
                        i = Towers[0]
                        i.ToggleBlue()
                        i.Blueprint()       
                    if event.key == K_e:
                        Towers[0] = BigDaddy()        
                        i = Towers[0]
                        i.ToggleBlue()
                        i.Blueprint()
                    if event.key == K_r:
                        Towers[0] = godson()        
                        i = Towers[0]
                        i.ToggleBlue()
                        i.Blueprint()       
                    if event.key == K_t:
                        Towers[0] = jerax()        
                        i = Towers[0]
                        i.ToggleBlue()
                        i.Blueprint()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    i.Build()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    i.Cancel()
              
            i.IsBlue()
            screen.blit(i.BlueSurf,(i.BlueCentre))#Draws Blueprints on mouse
            screen.blits(PlacedTowers)            #Draws Towers from PlacedTowers
        print(pygame.time.get_ticks)
        #Checking for Mobs in Tower's range:
        for x in SpawnPoints:
            x.Detect()
            #Needs to be before Proj.movement to be split over tick
        print(pygame.time.get_ticks)    
        #Mob/Projectile Movements/Interactions
        for x in MobList:
            x.Movement()                    #Provides new position of Mob/Proj           
            for y in ProjList:
                y.ProjMovement()
                if y.Collide(x) == True:
                    print('Collision: Success')
                    y.Explode()
                                                #Draws Mobs/Projs     
                screen.blit(y.surf,(y.rect))
            screen.blit(x.surf,(x.rect))
        print(pygame.time.get_ticks)
         
   
        t += 1
        
        pygame.display.update()                 #Updates
        print('end')
    pygame.quit()


Main()

''' To Do '''

#Can make Shooting type defined by self.image of each Tower object or
# make each object separate sub classes with

#Define levels:
# Spawns mobs at intervals for each level
# Different mobs for each level
# Stops when all are dead/Time passed

#Tower spawns projectiles
# Specific tower spawns specific projectiles
# Make Projectile spawn multiple from a list of proj/w different speed from rand.

#Figure out projectile targetting
#-- Mob enters range:
#   Equation is solved so that proj accounts for Mob speed

#Make Placing Towers on other towers invalid
# Collision Method for towers
# Checking if BlueSurf collides with TowerSurf in TowerList

' For True collision '
                    #if:
# inequalities with: self.x or self.x +1 .... self.x + width       
#                    self.y or self.y +1 .... self.y + height
#For every single pixel of projectule detected if inside a Mob


'''Efficiencies'''

#Can restrict event types retrieved from EventList

''' DONE '''    

#Generalize movement/collide/explode with lists of classes ////DONE///
#Figure out why 1 proj doesn't collide ///DONE/// (Collision checks for topleft)
#To Delete Projectile after Explode   ///DONE/// Moved offscreen, move = 0
