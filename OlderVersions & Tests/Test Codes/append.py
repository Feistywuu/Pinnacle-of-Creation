#append test

import pygame

pygame.init()
screen = pygame.display.set_mode((300,300))
pygame.display.set_caption('you da king')
pygame.mouse.set_visible(1)
Surf = pygame.Surface((20,20))
Surf.fill((12,120,120))
Surf1 = pygame.Surface((20,20))
Surf1.fill((12,120,200))
blit1 = (Surf1, (0,0))




SurfaceList = [ (Surf, (50,150)) , ]


SurfaceList.append(blit1)

test = screen.blits(   (SurfaceList )   )


pygame.display.update()


print(SurfaceList)



