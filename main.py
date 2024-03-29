from random import randint
import pygame
import math
import os
from spriteloader import *
from time import time
#might be useful later


#fps calculator
from time import time
nombreDeParties=0
monClic=False
FPScpt=0
initTime=time()
pygame.init()
maPolice= pygame.font.Font('fonts/pixel-font.TTF', 30) #Chargement de la police dans la variable maPolice
police_Titre= pygame.font.Font('fonts/pixel-font.TTF', 50)
random_sentences=[
"90% des commits effectués hier soir !",
"l'idée n'as pas été copié a minecraft !",
"On a eu la flemme de faire d'autre langue ",
"Featuring David Goodenough !",
"en collab avec rafael mais il sait pas shhh",
"pas tant de contenu mais plein de crossovers !",
"l'esp du bouton jaune signifie mexique",
"faraway sea mode marche pas faites 2 parties"
]

def averageFPS():
    return FPScpt/(time()-initTime)
def distance(xA,yA,xB,yB):
    return math.sqrt((xB-xA)**2+(yB-yA)**2)
def afficherScore(texteEnPlus,scoreAafficher):
    affichage=maPolice.render ( texteEnPlus+" score : "+str(scoreAafficher),  1,(255,255,255) )#Creation de l'étiquette "Gagné"
    monEcran.blit(affichage, (10,10))



width ,height=1000,600
monEcran=pygame.display.set_mode((width ,height ))


nombreDeParties=0
def game(gamemode):
    sblouch_sound=pygame.mixer.Sound('assets/sound_effects/sblouch.wav')
    if gamemode=="mexique":
        background_image=pygame.image.load("assets/mexico-background.png")
    elif gamemode=="starship":
        background_image=pygame.image.load("assets/background_starship.jpg")
    elif gamemode=="sea":
        background_image=pygame.image.load("assets/baackground-sea.jpg")

    else:
        background_image=pygame.image.load("assets/background.png")

    print("[*]starting a new game")
    if gamemode=="mexique":
        main_theme=pygame.mixer.Sound('assets/sound_effects/MEXICO.wav')
    elif gamemode=="starship":
        main_theme=pygame.mixer.Sound('assets/sound_effects/fight.mp3')
    elif gamemode=="sea":
        main_theme=pygame.mixer.Sound('assets/sound_effects/Playing_God_pixel.mp3')

    else:
        main_theme=pygame.mixer.Sound('assets/sound_effects/main_theme.wav')
    main_theme.set_volume(0.5)
    main_theme.play()
    theme_initTime=time()
    slime=target(10,10,0,0,gamemode)

    vie=3
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

        if vie==0:
            main_theme.stop()
            menu(True)
            break


        if cycle%3000==0:
            #pour l'animation des particules qui vont vers la bar de score
            sblouch_triggered=False
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
        if gamemode=="mexique":
            afficherScore("vidas : "+str(vie),score)
        else:
            afficherScore("vie : "+str(vie),score)
        #affichage des sprites
        if not touche:
            slime.update(monEcran)
        if touche:
            if not dejaPaticule:
                sblouch_sound.play()
                particles_fini=0
                particles=[]
                for i in range(10):
                    particles.append(death_particle(slime.posx+randint(-40,40),slime.posy+randint(-40,40),gamemode))
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
                            sblouch_sound.stop()
                    else:
                        print("[*] all particles aren't done")

            #relencement du theme si il est fini
            if gamemode=="mexique":
                if time()-theme_initTime>114:
                    main_theme.stop()
                    main_theme.play()
                    theme_initTime=time()
            else:
                if time()-theme_initTime>180:
                    main_theme.stop()
                    main_theme.play()
                    theme_initTime=time()



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
def menu(dead):
    global nombreDeParties
    nombreDeParties+=1
    sentence_jiggle_y_up=True
    sentence_jiggle_y=0
    gamemode=""
    background_image=pygame.image.load("assets/background.png")
    #ca ce le theme du jeu
    menu_theme=pygame.mixer.Sound('assets/sound_effects/menu_theme.wav')
    menu_theme.play()
    initTime=time()
    pygame.init()
    play_button=playButton(100,100,0,0)
    mexico_button=EspagnolButton(300,300,height/2+300,width/2-300/2)
    starship_button=StarshipButton(70,70,10,60)
    sea_button=SeaButton(100,70,10,500)
    cycle=0
    clicked=False
    monClic=False
    mexico_status =maPolice.render ("mode mexique activé",  1,(255,0,0) )
    starship_status =maPolice.render ("mode starship savior crossover activé",  1,(255,0,0) )
    sea_status =maPolice.render ("mode faraway sea crossover activé ",  1,(255,0,0) )
    sentence=maPolice.render(random_sentences[randint(0,len(random_sentences)-1)],  1,(255,0,0) )

    while True:



        monEcran.fill((100,40,70))
        monEcran.blit(pygame.transform.scale(background_image,(width,height)),(0,0))

        if gamemode=="mexique":
            monEcran.blit(mexico_status,(10,10))
        elif gamemode=="sea":
            monEcran.blit(sea_status,(10,10))
        elif gamemode=="starship":
            monEcran.blit(starship_status,(10,10))


        if dead:
            gameover =police_Titre.render ("GAME OVER",  1,(255,0,0) )
            monEcran.blit(gameover,(width/2-200,height/2-height/4-40))
            #print("[affichage du titre]")
        else:
            titre =pygame.image.load("assets/Titre.png")
            #monEcran.blit(pygame.transform.scale(background_image,(width,height)),(0,0))
            monEcran.blit(pygame.transform.scale(titre,(800,800)),(width/2-400,height/2-height/4-400))
            print("[affichage du titre]")
        if cycle%2==0:
            if sentence_jiggle_y_up:
                sentence_jiggle_y+=1
            else:
                sentence_jiggle_y-=1

        if cycle%20==0:
            sentence_jiggle_y_up= not sentence_jiggle_y_up

        monEcran.blit(sentence,(width/3+width/2-sentence.get_width()+130,height/2-100+sentence_jiggle_y))

        play_button.posx=width/2-play_button.sizex/2
        play_button.posy=height/2-play_button.sizey/2+100
        play_button.sizex=300
        play_button.sizey=300
        play_button.update(monEcran)
        mexico_button.update(monEcran)
        starship_button.update(monEcran)
        if nombreDeParties>2:
            sea_button.update(monEcran)
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
                game(gamemode)
        if mexico_button.isTouched(mouseX,mouseY) and not mexico_button.state=="clicked":
            if monClic:
                if gamemode=="":
                    mexico_button.state="clicked"
                    gamemode="mexique"
        if starship_button.isTouched(mouseX,mouseY) and not starship_button.state=="clicked":
            if monClic:
                if gamemode=="":
                    starship_button.state="clicked"
                    gamemode="starship"
        if sea_button.isTouched(mouseX,mouseY) and not sea_button.state=="clicked":
            if monClic:
                if gamemode=="":
                    sea_button.state="clicked"
                gamemode="sea"

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

        cycle+=1
        #include following in the while loop
        pygame.display.update()
if __name__ == '__main__':
    menu(False)
    nombreDeParties+=1






#include the followinf at the end of the script
