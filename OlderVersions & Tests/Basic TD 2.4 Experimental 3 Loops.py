#Basic TD #2

import os, sys, random
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

#Classes
class Mob():
     
    def __init__(self, name, image, move):  
        Imgs = [ load_image('aa.png', -1), \
                 load_image('dark willow.png', -1),\
                 load_image('axe.png', -1)] 
        self.surf = Imgs[image]
        self.rect = self.surf.get_rect(topleft=(0,380))
        self.move = move

    def movement(self):
        '''
        Moves Mobs across the screen
        :return: Rect
        '''
        newpos = self.rect.move((self.move, 0))
        self.rect = newpos

class Projectile():

    def __init__(self, surf, move, x):
        self.x = x
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


#Initialize Everything
pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption('you da king')
pygame.mouse.set_visible(1)
#Importing Tower, since load_image requires pygame.display initialized
from Towers import Tower

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

#Making Two lists containing class objects:
#Instantiating Mobs
Mobs = []
Mobs.append(Mob('AA', 0, 4))
Mobs.append(Mob('dark willow', 1, 2))
for i in Mobs:
    screen.blit(i.surf,(0,380))
    
#Instantiating Projectiles
Projs = []
bulletSurf1 = pygame.Surface((2,20))
bulletSurf1.fill((12,23,180))
bulletSurf2 = pygame.Surface((3,25))
bulletSurf2.fill((199,69,123))
Projs.append(Projectile(bulletSurf1, -4, 239))
Projs.append(Projectile(bulletSurf2, -2, 790))
for i in Projs:
    screen.blit(i.surf,(i.x, 800))

#Instantiating Towers
Towers = []
Towers.append(Tower(0))

#This method of storing events would require the KeyList to be periodically
#deleted to prevent List getting too big, but this would introduce bugs each
#time it's deleted

#Main Loop
def Main():
    run = True
    Frames = 0
    KeyList = []            #Stored list of Keypresses
    while run:
        clock.tick(30)
        
        screen.blit(bg1, (0,0))                 #Erasing Screen
        screen.blit(bg2, (0,350))

        #User Input/Events
        for i in Towers:                                                        
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    #event is a class object, calling on unicode(key) attribute
                    print(event.unicode)
                    KeyList.append(event.unicode)                   
                for x in KeyList:
                    if i.image == 1:
                        print('Checked 1 in List')
                    if i.image == 2:
                        print('Checked 2 in List')
                    if i.image == 3:
                        print('Checked 3 in List')
                    if i.image == 4:
                        print('Checked 4 in List')
                    if i.image == 5:
                        print('Checked 5 in List')
                    #Iterating through Towers/PermList                   
                    if x == 'q' and i == 0:
                        i.ToggleBlue()
                        i.Blueprint()
                    if x == 'w' and i.image == 1:
                        i.ToggleBlue()
                        i.Blueprint()       
                    if x == 'e' and i.image == 2:     
                        i.ToggleBlue()
                        i.Blueprint()
                    if x == 'r' and i.image == 3:
                        i.ToggleBlue()         
                        i.Blueprint()       
                    if x == 't' and i.image == 4:        
                        i.ToggleBlue() 
                        i.Blueprint()
                    
                    #if x.type == pygame.MOUSEBUTTONDOWN and x.button == 1:
                        #i.Build()
                   # if x.type == pygame.MOUSEBUTTONDOWN and x.button == 3:
                        #i.Cancel()
            
            i.TowerPlaced()                                                          
            #screen.blit(i.surf,(pygame.mouse.get_pos()))    #Toggle True
            screen.blit(i.BlueSurf,(pygame.mouse.get_pos()))#Toggle False
            screen.blits(i.TowerList)
        
#Combine all 3 loops later        
#Can split types of Events too
        
        for x in Mobs:                          #Iterating through List Mob/Proj
            for y in Projs:
                x.movement()                    #Provides new position of Mob/Proj
                y.ProjMovement()
        
                if y.Collide(x) == True:
                    print('Collision: Success')
                    y.Explode()
                                        
                screen.blit(x.surf,(x.rect))    #Draws Mobs/Projs
                screen.blit(y.surf,(y.rect))
                
        pygame.display.update()                 #Updates

        Frames += 1
        if Frames == 300:
            KeyList = []
            
    pygame.quit()



Main()

''' To Do '''

#Spawn Towers:
# On keypress - makes blueprint of tower
# On mouse-click puts tower there
# Tower spawns projectiles



#Make Projectile spawn multiple from a list of proj/w different speed from rand.

#Figure out projectile targetting
#-- Mob enters range:
#   Equation is solved so that proj accounts for Mob speed

#Scrap TD and make projectiles spawn from mouse position with click from
#from random pool of projectiles/ selected proj from pool

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
