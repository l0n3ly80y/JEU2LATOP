from random import randint
import pygame
import math
#might be useful later


#fps calculator
from time import time
FPScpt=0
initTime=time()
def averageFPS():
    return FPScpt/(time()-initTime)












def distance(xA,yA,xB,yB):
    return math.sqrt((xB-xA)**2+(yB-yA)**2)
pygame.init()
touche=False
resultat=False
width ,height=800,600
monEcran=pygame.display.set_mode((width ,height ))
jeu_en_cours=True
cycle=0
maPolice = pygame.font.SysFont('arial', 30) #Chargement de la police dans la variable maPolice
texteGagne = maPolice.render ( "Gagné",  1,(0,255,255) )#Creation de l'étiquette "Gagné"
textePerdu = maPolice.render ( "Perdu",  1, (0,255,255) )#Creation de l'étiquette "Perdu"
while jeu_en_cours==True:
    monEcran.fill((100,40,70))

    if cycle%3000==0:
        touche=False
        resultat=True
        monClic=False
        posx=randint(1,width)# width est la largeur de la fenétre
        posy=randint(1,height)# height est la hauteur de la fenetre
        rayon=randint(10,100)
    pygame.draw.rect(monEcran,(255, 255, 255),(posx,posy,rayon,rayon))

    cycle=cycle+1

    #mouseX,mouseY=pygame.mouse.get_pos()
    mouseX,mouseY=pygame.mouse.get_pos()
    if posx<mouseX<posx+rayon and posy<mouseY<posy+rayon and monClic and resultat:
        touche=True
        resultat=False

        print('[*] monClic :',monClic)
        print('[*] touche :',touche)


    elif resultat:
        resultat=False
        print('[*] monClic :',monClic)
        print('[*] touche :',touche)

    if touche:
        monEcran.blit(texteGagne, (10,10))

    else:

        monEcran.blit(textePerdu, (10,10))
    for evenement in pygame.event.get():# Boucle sur les evenements
        if evenement.type==pygame.QUIT: #Si l'evenement est quitter
            print('[*] average fps: ',averageFPS())
            pygame.quit()  #arret de pygame
            jeu_en_cours=False #arret de la boucle
        if evenement.type==pygame.MOUSEBUTTONDOWN:
            monClic=True
            resultat=True
    #include following in the while loop
    FPScpt+=1
    pygame.display.update()
#include the followinf at the end of the script