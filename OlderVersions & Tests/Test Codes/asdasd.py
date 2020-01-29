

import pygame


class Projectile():

    def __init__(self, surf, move, x):
        self.x = x
        self.surf = surf
        self.rect = self.surf.get_rect(topleft=(self.x,800))
        self.move = move



Projs = []
bulletSurf1 = pygame.Surface((200,200))
bulletSurf1.fill((120,23,111))          #rect
bulletSurf1.fill((200,23,1))     #assigns rect to test 


def test():
    print(bulletSurf1)
    print(bulletSurf1.fill((122,23,180)))
    print(bulletSurf1)
    print(bulletSurf1)

screen = pygame.display.set_mode((300,300))
screen.blit(bulletSurf1, (50,50))
pygame.display.update()
test()
