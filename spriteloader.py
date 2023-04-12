import pygame
from random import randint

class death_particle:
    """le petit machin quand le slime il meurt death_particle."""

    def __init__(self, posx,posy):
        self.posx=posx
        self.posy=posy
        self.img= pygame.image.load("assets/particles-"+str(randint(1,3))+".png")#selection aleatoir de sprite de la particule
        self.current_anim_frame=0
        self.current_travel_step=0
        self.counter=0
        self.step_x=round((self.posx+randint(1,14))/10) #il doit parcourir ca a chaque fois pour arriver jusqu'à la bar de score
        self.step_y=round((self.posy+randint(1,14))/10)
        self.exploding_sprites=[]
        self.exploding_sprites.append(pygame.image.load("assets/particles-explo1.png"))
        self.exploding_sprites.append(pygame.image.load("assets/particles-explo2.png"))
        self.finished=False
    def update(self,screen):
        self.counter+=1
        print("OH U MF")

        print("[*]travel setp :"+str(self.current_travel_step))
        if not self.current_travel_step==10:
            print('plsss')
            if self.counter%15==0:
                self.posx-=self.step_x
                self.posy-=self.step_y
                self.current_travel_step+=1

            self.sprite=pygame.transform.scale(self.img,(50,50)).convert_alpha()

            print("[*]blitted")


        else:
            print("why")
            if not self.current_anim_frame==2:
                self.sprite=pygame.transform.scale(self.exploding_sprites[self.current_anim_frame],(100,100)).convert_alpha()
                if self.counter%20==0:
                    self.current_anim_frame+=1
                #screen.blit(self.sprite, (self.posx,self.posy))
                print("[*]blitted")

            else:
                self.finished=True
        screen.blit(self.sprite, (self.posx,self.posy))







class target:
    """the slime basically"""

    def __init__(self, sizex,sizey, posx, posy,mexico):
        self.mexico=mexico

        self.sizex=sizex
        self.sizey=sizey
        self.posx=posx
        self.posy=posy
        if self.mexico:
            self.img = pygame.image.load("assets/slime-mexico.png")
        else:
            self.img = pygame.image.load("slime.png")#.convert_alpha()
        self.scaled_img=pygame.transform.scale(self.img,(self.sizex,self.sizey) )
        self.sprite=self.scaled_img.convert_alpha()
        self.dead=False
        self.current_anim_frame=0
        self.counter=0
        #chargement des animations de mort
        self.death_anim_sprites=[]
        for i in range(1,9):
            self.death_anim_sprites.append(pygame.image.load("assets/mort"+str(i)+".png"))
            print("[**] list of sprites ",self.death_anim_sprites)


    def update(self,screen):
        size=(self.sizex,self.sizey)
        ##scaled_img=
        if self.dead:
            print("[*]current frame : "+str(self.current_anim_frame))
            self.sprite=pygame.transform.scale(self.death_anim_sprites[self.current_anim_frame],size).convert_alpha()
            screen.blit(self.sprite, (self.posx,self.posy))
            self.counter+=1
            if self.current_anim_frame==7:
                self.counter=0
                self.current_anim_frame=-1
                self.dead=False

            if self.current_anim_frame<=2:
                if self.counter%30==0:
                    self.current_anim_frame+=1
            else:
                if self.counter%15==0:
                    self.current_anim_frame+=1

        else:
            i=1
            self.sprite=pygame.transform.scale(self.img,size).convert_alpha()
            screen.blit(self.sprite, (self.posx,self.posy))


class playButton:
    """button for the play button"""

    def __init__(self, sizex,sizey,posx,posy):

        self.state="regular"
        self.sizex=sizex
        self.sizey=sizey
        self.posx=posx
        self.posy=posy
        #loading the base sprite
        self.img = pygame.image.load("assets/play-regular.png")#.convert_alpha()
        self.scaled_img=pygame.transform.scale(self.img,(self.sizex,self.sizey) )
        self.sprite=self.scaled_img.convert_alpha()
        #loading the hover sprite
        self.img_hover = pygame.image.load("assets/play-hover.png")#.convert_alpha()
        #loading the clicked sprite
        self.img_clicked = pygame.image.load("assets/play-clicked.png")#.convert_alpha()
        #We need to load the images first cuz it takes hella time so we don't wanna do it inside a while loop



    def update(self,screen):
        size=(self.sizex,self.sizey)
        if self.state=="hover":
            self.sprite=pygame.transform.scale(self.img_hover,size).convert_alpha()
            screen.blit(self.sprite, (self.posx,self.posy))
        elif self.state=="regular":
            #print("[*]regular")
            self.sprite=pygame.transform.scale(self.img,size).convert_alpha()
            screen.blit(self.sprite, (self.posx,self.posy))
        else:
            self.sprite=pygame.transform.scale(self.img_clicked,size).convert_alpha()
            screen.blit(self.sprite, (self.posx,self.posy))
    #size bias correction : y-30
    def isTouched(self,cursorx,cursory):
        if  self.posx<cursorx<self.posx+self.sizex and self.posy<cursory<self.posy+self.sizey-30:
            return True
        else:
            return False




class EspagnolButton:
    """button for the espagnol button"""

    def __init__(self, sizex,sizey,posx,posy):
        self.state="regular"
        self.sizex=sizex
        self.sizey=sizey
        self.posx=posx
        self.posy=posy
        #loading the base sprite
        self.img = pygame.image.load("assets/espagnol-1.png")#.convert_alpha()
        self.scaled_img=pygame.transform.scale(self.img,(self.sizex,self.sizey) )
        self.sprite=self.scaled_img.convert_alpha()
        #loading the hover sprite
        self.img_hover = pygame.image.load("assets/espagnol-1.png")#.convert_alpha()
        #loading the clicked sprite
        self.img_clicked = pygame.image.load("assets/espagnol-2.png")#.convert_alpha()
        #We need to load the images first cuz it takes hella time so we don't wanna do it inside a while loop



    def update(self,screen):
        size=(self.sizex,self.sizey)
        if self.state=="hover":
            self.sprite=pygame.transform.scale(self.img_hover,size).convert_alpha()
            screen.blit(self.sprite, (self.posx,self.posy))
        elif self.state=="regular":
            #print("[*]regular")
            self.sprite=pygame.transform.scale(self.img,size).convert_alpha()
            screen.blit(self.sprite, (self.posx,self.posy))
        else:
            self.sprite=pygame.transform.scale(self.img_clicked,size).convert_alpha()
            screen.blit(self.sprite, (self.posx,self.posy))
    #size bias correction : y-30
    def isTouched(self,cursorx,cursory):
        if  self.posx<cursorx<self.posx+self.sizex and self.posy<cursory<self.posy+self.sizey-30:
            return True
        else:
            return False
