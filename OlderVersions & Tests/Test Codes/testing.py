#testing


import pygame


pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption('you da king')
pygame.mouse.set_visible(1)
clock = pygame.time.Clock()



def Main():
    run = True
    while run:
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.button)
                if print(event.button) == 1:
                    'do thing'





Main()
