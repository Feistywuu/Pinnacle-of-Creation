#Functions to load Images and Sounds

import os, sys
import pygame
from pygame.locals import *

os.chdir('''C:\\Users\\Philip\\Documents\\Programming\\BasicMovement''')
picture_dir = os.path.join(os.getcwd(), "Pictures")
#Could use os.walk instead
#Check 'Anaconda'


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

#Sounds
explode_sound = load_sound('rocket_flare_explode.ogg')

#Normal Surfaces
cebSurf1 = load_image('ceb1.png', -1)            
anaSurf1 = load_image('ana.png', -1)
flowerSurf1 = load_image('flower.png', -1)
godsonSurf1 = load_image('godson.png', -1)
jeraxSurf1 = load_image('jerax.png', -1)
#Blue Surfaces
cebSurf2 = load_image('ceb1.png', -1)           
anaSurf2 = load_image('ana.png', -1)
flowerSurf2 = load_image('flower.png', -1)
godsonSurf2 = load_image('godson.png', -1)
jeraxSurf2 = load_image('jerax.png', -1)
#Blue Surface list + Normal Surface list
Imgs = ( cebSurf1, anaSurf1, flowerSurf1, godsonSurf1, jeraxSurf1)
Imgs2 = ( cebSurf2, anaSurf2, flowerSurf2, godsonSurf2, jeraxSurf2)
#Mob Surfaces
MobImgs = [ load_image('aa.png', -1), \
            load_image('dark willow.png', -1),\
            load_image('axe.png', -1)]


#Projectile Surfaces
bulletSurf1 = pygame.Surface((2,20))
bulletSurf1.fill((12,23,180))
bulletSurf2 = pygame.Surface((3,25))
bulletSurf2.fill((199,69,123))
