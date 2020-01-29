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

    def __init__(self, surf, move):
        self.surf = surf
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

    def __init__(self, surf, move):
        self.surf = surf
        self.rect = self.surf.get_rect(topleft=(450,800))
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
        if Mob.rect.x + (Mob.rect.right - Mob.rect.x)>= self.rect.x >= Mob.rect.x\
        and Mob.rect.y + (Mob.rect.bottom - Mob.rect.y)>= self.rect.y >= Mob.rect.y:
            return True
        return False
    
#if: Mob(X) + Mob(width)> Projectile(X) > Mob(X)
#and Mob(Y) + Mob(height) > Projectile(Y) > Mob(Y)

    def Explode(self):
        '''
        Makes sound if Collide() == True
        Deletes projectile
        :return: None
        '''
        #if bullet1.Collide(AA) == True:            Replaced by 'if' in loop
        explode_sound.play()   #Plays sound

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
clock = pygame.time.Clock()
RandX = random.randint(200,800)
explode_sound = load_sound('rocket_flare_explode.ogg')
#Mobs
DW = Mob(load_image('dark willow.png', -1), 2)
AA = Mob(load_image('aa.png', -1), 4)
screen.blit(AA.surf,(0,380))
#Projectiles
bulletSurf = pygame.Surface((2,20))
bulletSurf.fill((12,23,180))
bullet1 = Projectile(bulletSurf,-4)

#Main Loop
def Main():
    run = True
    while run:
        clock.tick(60)
        
        screen.blit(bg1, (0,0))         #Erasing Screen
        screen.blit(bg2, (0,350))
        
        AA.movement()                   #Provides new position of Mob/Proj
        DW.movement()
        bullet1.ProjMovement()
        
        if bullet1.Collide(AA) == True:
            bullet1.Explode()

            # if proj.collide(mob) == True:
                # proj.explode(mob) == True 
            


        screen.blit(AA.surf,(AA.rect))  #Draws new player
        screen.blit(DW.surf,(DW.rect))
        screen.blit(bullet1.surf,(bullet1.rect))
        pygame.display.update()         #Updates
        
    pygame.quit()



Main()

''' To Do '''

#Generalize movemenent/collide/explode with lists of classes

#///To Delete Projectile after Explode///

#Set rect off-screen and movement to zero
#(For only the instance of class) 
# //OR//
# Delete the rect + Stop drawing it

#Later on can put all Class instances (Mobs/Projs) into a list to condense code
# For i in Mob[i] - screen.blit(Mob[i].surf, Mob[i].rect) etc.

#Make Projectile spawn multiple from a list of proj/w different speed from rand.

    
