#Main Code

import pygame, random
from pygame.locals import *

#Initialize Everything
pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption('you da king')
pygame.mouse.set_visible(1)

#Importing Assets, requiring pygame.display
from LoadedAssets import *
from Towers import Tower
from Mobs import Mob
from Projectiles import Projectile
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
explode_sound = load_sound('rocket_flare_explode.ogg')

#Main Loop
def Main():
    run = True
    while run:
        clock.tick(30)
        
        screen.blit(bg1, (0,0))                 #Erasing Screen
        screen.blit(bg2, (0,350))

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
                        i.ToggleBlue()
                        i.image = 0
                        i.Blueprint()
                    if event.key == K_w:
                        i.ToggleBlue()
                        i.image = 1
                        i.Blueprint()       
                    if event.key == K_e:     
                        i.ToggleBlue()
                        i.image = 2
                        i.Blueprint()
                    if event.key == K_r:
                        i.ToggleBlue()
                        i.image = 3
                        i.Blueprint()       
                    if event.key == K_t:       
                        i.ToggleBlue()
                        i.image = 4
                        i.Blueprint()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    i.Build()
                    i.CreateSpawn()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    i.Cancel()
            
            i.IsBlue()
            #Getting Centre of Tower Blueprint Coordinates
            i.x, i.y = pygame.mouse.get_pos()
            BlueCentre = ( ( i.x - (i.BlueSurf.get_width())/2),\
                           ( i.y - (i.BlueSurf.get_height())/2)  )
            
            screen.blit(i.BlueSurf,(BlueCentre))    #Draws Blueprints on mouse
            screen.blits(PlacedTowers)            #Draws Towers from PlacedTowers 
             

        #Mob/Projectile movements and interactions
        for x in Mobs:                          
            for y in Projs:
                x.Movement()                    #Provides new position of Mob/Proj
                y.ProjMovement()
        
                if y.Collide(x) == True:
                    print('Collision: Success')
                    y.Explode()
                                        
                screen.blit(x.surf,(x.rect))    #Draws Mobs/Projs
                screen.blit(y.surf,(y.rect))
        
        pygame.display.update()                 #Updates
        
    pygame.quit()



Main()

''' To Do '''

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
