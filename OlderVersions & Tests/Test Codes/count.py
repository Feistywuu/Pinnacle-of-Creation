#Test

import pygame

clock = pygame.time.Clock()

def Count():
    run = True
    count = 0
    while run == True:
        
        clock.tick(1)
        
        count += 1
        print(count)

    
Count()
