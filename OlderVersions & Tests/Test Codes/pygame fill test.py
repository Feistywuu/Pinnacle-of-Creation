

import pygame


class Projectile():

    def __init__(self, surf, move, x):
        self.x = x
        self.surf = surf
        self.rect = self.surf.get_rect(topleft=(self.x,800))
        self.move = move



Projs = []
bulletSurf1 = pygame.Surface((200,200))
bulletSurf1.fill((120,23,111))              #2
test = bulletSurf1.fill((200,23,1))         #assigns rect to test

# 2 apparently changes bulletSurf1 whilst bulletSurf2.fill((120,23,111))
# itself is a rect.


def test():
    
    screen = pygame.display.set_mode((300,300))
    
    print(bulletSurf1)
    
    print(bulletSurf1.fill((122,23,180)))
    screen.blit(bulletSurf1, (50,50))
    pygame.display.update()

    
    print(bulletSurf1)
    print(bulletSurf1)


test()

