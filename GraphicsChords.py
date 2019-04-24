import sys, pygame
from pygame.locals import *
letrasProposicionales = ["A","a","B","C","c","D","d","E","F","f","G","g"]
inter = ["A","B","C","D","-E","-F","-G"]
tru = []
for i in inter:
    if(i[0] in letrasProposicionales):
        tru.append(i);
pygame.init()
window =True

white = [255,255,255]
black = [0,0,0]
size=[700,500]
screen=pygame.display.set_mode(size)
screen.fill(white)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('#',True,black,None)
textRect = text.get_rect()
textRect.center = (350,130)
pygame.draw.line(screen, black, [100,100],[600,100], 3)
pygame.draw.line(screen, black, [100,120],[600,120], 3)
pygame.draw.line(screen, black, [100,140],[600,140], 3)
pygame.draw.line(screen, black, [100,160],[600,160], 3)
pygame.draw.line(screen, black, [100,180],[600,180], 3)

for i in tru:
    if(i == "B"):
        pygame.draw.ellipse(screen, black, [350,130,20,20] , 4)
    elif(i == "D"):
        pygame.draw.ellipse(screen, black, [350,110,20,20] , 4)
    elif(i == "F"):
        pygame.draw.ellipse(screen, black, [350,90,20,20] , 4)
    elif(i == "A"):
        pygame.draw.ellipse(screen, black, [350,140,20,20] , 4)
    elif(i == "C"):
        pygame.draw.ellipse(screen, black, [350,120,20,20] , 4)
    elif(i == "E"):
        pygame.draw.ellipse(screen, black, [350,100,20,20] , 4)
    elif(i == "G"):
        pygame.draw.ellipse(screen, black, [350,80,20,20] , 4)




pygame.display.flip()


while window:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window = False

pygame.quit()
