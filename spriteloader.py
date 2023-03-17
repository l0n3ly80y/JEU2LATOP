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

    def update(self,screen):
        size=(self.sizex,self.sizey)
        #scaled_img=
        self.sprite=pygame.transform.scale(self.img,size).convert_alpha()
        screen.blit(self.sprite, (self.posx,self.posy))
