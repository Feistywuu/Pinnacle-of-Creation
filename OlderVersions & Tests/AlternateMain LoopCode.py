

def test():
    for n in range(0,4):
        for X in ['q','w','e','r']:
            Key= 'K_'+ X
            print(X)
            print(Key)


test()



for n in range(0,4):
    for m in ['q','w','e','r','t']:     #Possible Keys
        Key = 'K_'+ m
            if event.key == Key:
                i.ToggleBlue()
                i.image = n
                i.Blueprint()
