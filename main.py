from random import randint
import pygame
import math
import os
from spriteloader import *
from time import sleep
#might be useful later


#fps calculator
from time import time
monClic=False
FPScpt=0
initTime=time()
pygame.init()
maPolice = pygame.font.SysFont('arial', 30) #Chargement de la police dans la variable maPolice
def averageFPS():
    return FPScpt/(time()-initTime)
def distance(xA,yA,xB,yB):
    return math.sqrt((xB-xA)**2+(yB-yA)**2)
def afficherScore(texteEnPlus,scoreAafficher):
    affichage=maPolice.render ( texteEnPlus+" score : "+str(scoreAafficher),  1,(0,255,255) )#Creation de l'étiquette "Gagné"
    monEcran.blit(affichage, (10,10))


pygame.init()
width ,height=800,600
monEcran=pygame.display.set_mode((width ,height ))

slime=target(10,10,0,0)
vie=10
max_speed=5
touche=False
resultat=False
score=0
texteScore=""
jeu_en_cours=True
cycle=0
maPolice = pygame.font.SysFont('arial', 30) #Chargement de la police dans la variable maPolice
while jeu_en_cours==True:
    monEcran.fill((100,40,70))

    if cycle%3000==0:
        touche=False
        resultat=True
        monClic=False
        slime.posx=randint(1,width)# width est la largeur de la fenétre
        slime.posy=randint(1,height)# height est la hauteur de la fenetre

        rayon=randint(50,400)
        slime.sizex=rayon
        slime.sizey=rayon
        #pallier de vitesse
        if score%5==0:
            max_speed+=1

    if cycle%500==0:
        #definition des vitesse de deplacement de la taupe
        xspeed=randint(-max_speed,max_speed)
        yspeed=randint(-max_speed,max_speed)
    #deplacement du carre
    if cycle%100==0:
        slime.posx+=xspeed
        slime.posy+=yspeed



    cycle=cycle+1

    #mouseX,mouseY=pygame.mouse.get_pos()
    mouseX,mouseY=pygame.mouse.get_pos()
    if slime.posx<mouseX<slime.posx+rayon and slime.posy<mouseY<slime.posy+rayon and monClic and resultat:
        if not touche:
            score+=1
        touche=True

        resultat=False
        cycle=3000
        print("[*]score ",score)


        print('[*] monClic :',monClic)
        print('[*] touche :',touche)


    elif monClic and resultat:
        vie-=1
        resultat=False
        print('[*] monClic :',monClic)
        print('[*] touche :',touche)
    elif resultat:
        resultat=False
        print('[*] monClic :',monClic)
        print('[*] touche :',touche)

    #affichage du score
    afficherScore("vie : "+str(vie),score)
    #affichage des sprites
    if not touche:
        #pygame.draw.rect(monEcran,(255, 255, 255),(posx,posy,rayon,rayon))
        slime.update(monEcran)

    #a corriger
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
