#Load image (Surface) > blit surface to display (Surface) > update display

#Importing Modules

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
    return image.get_rect()


#Classes for Game Objects
class Mob():

    def __init__(self):
        self.rect = load_image('aa.png', -1)
        self.move = 4

    def move(self, surf, move):
        '''
        Moves Mobs across the screen
        :return: Rect
        '''
        newpos = self.rect.move((self.move, 0))
        self.rect = newpos

#To do:
#Bullets moving up from center bottom of screen
#Make Collide class


#Main Function 

def main():
    
    #Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((1000,800))
    pygame.display.set_caption('you da king')
    pygame.mouse.set_visible(0)

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

    #Prepare Game Objects
    clock = pygame.time.Clock()
    AA = Mob()
    #['abbadon','alchemist','aa','anti-mage',\
                     #'arc warden','axe','bane','dark willow']

        
    
    #Main Update Loop
    run = True
    while run:
        clock.tick(60)

        
        AA.move()

        #Handle Input Events




        # Draw Everything
        screen.blit(self.rect)
        pygame.display.update()                

    pygame.quit()      

main()





