#
#
#

    def Detect(self):
        '''
        Checks (x,y) elements in SpawnedMobs, if within Tower.range
        returns Shoot == True
        :return: bool
        '''
        for mob in Mobs.SpawnedMobs:
            
            if self.x >= mob.CentX and self.y >= mob.CentY:     #Checking BottRight
                for n in range(0, int(mob.surf.get_width()/2)+1):
                    if (self.range)**2 >= (abs(self.x - (mob.CentX + n)))**2 +\
                                         (abs(self.y - (mob.CentY + mob.surf.get_height()/2)))**2:
                        print('Mob Detected1X')
                for m in range(0, int(mob.surf.get_height()/2)+1):
                    if (self.range)**2 >= (abs(self.x - (mob.CentX + mob.surf.get_width()/2)))**2+\
                                          (abs(self.y - (mob.CentY + m)))**2:
                        print('Mob Detected1Y')

            if self.x < mob.CentX and self.y >= mob.CentY:
                for n in range(0, int(mob.surf.get_width()/2)):
                    if (self.range)**2 >= (abs(self.x - (mob.CentX + n)))**2+\
                                          (abs(self.y - (mob.CentY + mob.surf.get_height()/2)))**2:
                        print('Mob Detected2x')
                for m in range(0, int(mob.surf.get_height()/2)+1):
                    if (self.range)**2 >= (abs(self.x - (mob.CentX - mob.surf.get_width()/2)))**2+\
                                          (abs(self.y - (mob.CentY + m)))**2:
                        print('Mob Detected2Y')
                    
                        
            #Then continuing for TopLeft and TopRight quadrants... However code is too slow
                

    #Could shoot dummy projectile towards each mob in moblist, and check whether their collision
    #point is within distance, but that requires a unitmovement per frame to check if collided or not
    #it's an n*time runspeed






            
            #print( ((self.x, self.y)) )
            #print(mob)
            #print(mob.CentX)
            #print(mob.rect)
            #print
           # if (self.range)**2 > (abs ((self.centre[0])- mob.x))**2 +\
              # (abs((self.centre[1]) - mob.y))**2
               # print('Target lock on')
                #self.Shoot()

            #Checking edges of Mob Surfaces, in quadrants, clockwise
            
                    
                    
                        
                    
    
            #    for m in range(0, int(mob.surf.get_height()/2) +1 ):
            #       for n in range(0, int(mob.surf.get_width()/2) +1):
            #           print( (mob.CentX + mob.surf.get_width()/2 - n),\
            #                  (mob.CentY + mob.surf.get_height()/2 - m)  )
                        
                    #(mob.CentX + (mob.get_height())/2 - m)


                
 #           if self.x < mob.CentX and self.y >= mob.CentY:  #Checking BottLeft
 #               print('Tower Bottom Left of Mob')
 #           if self.x < mob.CentX and self.y < mob.CentY:   #TopLeft
 #               print('Tower Top Left of Mob')
  #          if self.x >= mob.CentX and self.y < mob.CentY:  #TopRight
  #              print('Tower Top Right of Mob')


