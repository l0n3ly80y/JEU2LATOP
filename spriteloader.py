import pygame

class target:
    """the slime basically"""

    def __init__(self, sizex,sizey, posx, posy):

        self.sizex=sizex
        self.sizey=sizey
        self.posx=posx
        self.posy=posy
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
