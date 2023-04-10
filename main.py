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
maPolice= pygame.font.Font('fonts/pixel-font.TTF', 30) #Chargement de la police dans la variable maPolice
background_image=pygame.image.load("assets/background.png")
def averageFPS():
    return FPScpt/(time()-initTime)
def distance(xA,yA,xB,yB):
    return math.sqrt((xB-xA)**2+(yB-yA)**2)
def afficherScore(texteEnPlus,scoreAafficher):
    affichage=maPolice.render ( texteEnPlus+" score : "+str(scoreAafficher),  1,(255,255,255) )#Creation de l'étiquette "Gagné"
    monEcran.blit(affichage, (10,10))



width ,height=900,600
monEcran=pygame.display.set_mode((width ,height ))



def game():

    print("[*]starting a new game")
    main_theme=pygame.mixer.Sound('assets/sound_effects/main_theme.wav')
    main_theme.play()

    slime=target(10,10,0,0)
    vie=10
    max_speed=5
    touche=False
    resultat=False
    score=0
    texteScore=""
    jeu_en_cours=True
    cycle=0
    monClic=False

    while jeu_en_cours==True:
        monEcran.fill((100,40,70))
        monEcran.blit(pygame.transform.scale(background_image,(width,height)),(0,0))


        if cycle%3000==0:
            #pour l'animation des particules qui vont vers la bar de score
            particles=[]
            dejaPaticule=False
            particules_finis=0
            ####
            touche=False#
            resultat=True
            monClic=False
            slime.posx=randint(1,width-20)# width est la largeur de la fenétre corriger pour eviter un bug d'affichage
            slime.posy=randint(1,height-20)# height est la hauteur de la fenetre
            slime.dead=False
            rayon=randint(50,400)
            slime.sizex=rayon
            slime.sizey=rayon
            #pallier de vitesse
            if score%5==0:
                max_speed+=4

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
        if slime.posx+10<mouseX<slime.posx+rayon-10 and slime.posy+15<mouseY<slime.posy+rayon-10 and monClic and resultat:
            if not touche:
                score+=1
            touche=True

            resultat=False

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
        if touche:
            if not dejaPaticule:
                particles_fini=0
                particles=[]
                for i in range(10):
                    particles.append(death_particle(slime.posx+randint(-40,40),slime.posy+randint(-40,40)))
                print("[*] particles :")
                print(particles)
                dejaPaticule=True
            else:
                print("[*]loading particles")
                print(particles)
                for i in particles:
                    print(i)
                    i.update(monEcran)
                    print('updated ?')
                    if i.finished:
                        print("idk")
                        particules_finis+=1
                        if particles_fini==10:
                            print("[*] tout est fini")
                            particles=[]
                            particles_fini=0
                            dejaPaticule=False
                    else:
                        print("[*] all particles aren't done")




            slime.dead=True
            slime.update(monEcran)
            if slime.dead==False:
                cycle=3000


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
        pygame.display.update()


#that's what's going on at the beginning of the script, basically the game menu
def menu():
    #ca ce le theme du jeu
    menu_theme=pygame.mixer.Sound('assets/sound_effects/menu_theme.wav')
    menu_theme.play()
    initTime=time()
    pygame.init()
    play_button=playButton(100,100,0,0)
    clicked=False
    monClic=False
    while True:
        monEcran.fill((100,40,70))
        monEcran.blit(pygame.transform.scale(background_image,(width,height)),(0,0))

        play_button.posx=width/2-play_button.sizex/2
        play_button.posy=height/2-play_button.sizey/2+100
        play_button.sizex=300
        play_button.sizey=300
        play_button.update(monEcran)
        mouseX,mouseY=pygame.mouse.get_pos()
        if play_button.isTouched(mouseX,mouseY):# and monClic and resultat:
            play_button.state="hover"
            if monClic:
                if not clicked:
                    print("[*]processing click")
                    clicked=True
                    cycle_since_click=0
        elif not clicked:
            play_button.state="regular"
        if clicked:
            play_button.state="clicked"
            cycle_since_click+=1
            if cycle_since_click%10==0:
                print("[*] cycle since click :",cycle_since_click)
            if cycle_since_click>300:
                menu_theme.stop()
                game()

        for evenement in pygame.event.get():# Boucle sur les evenements
            if evenement.type==pygame.QUIT: #Si l'evenement est quitter
                print('[*] average fps: ',averageFPS())
                pygame.quit()  #arret de pygame
                jeu_en_cours=False #arret de la boucle
            if evenement.type==pygame.MOUSEBUTTONDOWN:
                monClic=True
                resultat=True
            else:
                monClic=False
        #include following in the while loop
        pygame.display.update()
if __name__ == '__main__':
    menu()






#include the followinf at the end of the script
