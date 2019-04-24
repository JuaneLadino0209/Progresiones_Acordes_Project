import sys, pygame
from pygame.locals import *
letrasProposicionales = ["A","a","B","C","c","D","d","E","F","f","G","g"]
#inter = Interpretaciones/ dicionario a jugar
inter = {"A":0,"a":0,"B":0,"C":1,"c":0,"D":0,"d":0,"E":1,"F":0,"f":0,"G":1,"g":0}#Ingrese aqui su interpretacion deseada
tru = []
for i in inter:
    if(inter.get(i) == 1):
        tru.append(i)
print(tru)
pygame.init()

white = [255,255,255]
black = [0,0,0]
size=[1000,600]
screen=pygame.display.set_mode(size)
clock = pygame.time.Clock()

penImg = pygame.image.load('Imagen1.png')
noteImg = pygame.image.load('Imagen3.png')
note2Img = pygame.image.load('Imagen2.png')
def pen(x,y):
    screen.blit(penImg,(x,y))

def note(x,y):
    screen.blit(noteImg,(x,y))

def note2(x,y):
        screen.blit(note2Img,(x,y))

crashed = False
#screen.fill(white)
#pygame.display.flip()
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        #print(event)

    screen.fill(white)
    pen(0,0)
    for i in tru:
        if(i == "A"):
            note(500,208)
        elif(i == "a"):
            note2(462,208)
        elif(i == "B"):
            note(500,180)
        elif(i == "C"):
            note(500,152)
        elif(i == "c"):
            note2(462,152)
        elif(i == "D"):
            note(500,124)
        elif(i == "d"):
            note2(462,124)
        elif(i == "E"):
            note(500,96)
        elif(i == "F"):
            note(500,68)
        elif(i == "f"):
            note2(462,68)
        elif(i == "G"):
            note(500,40)
        elif(i == "g"):
            note2(462,40)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
