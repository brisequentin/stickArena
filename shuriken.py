#on va factoriser tout cela

import pygame, sys
from pygame.locals import *

class ShurikenDR(pygame.sprite.Sprite):

 # initialisation (en fonction de la vitesse voulue et aussi lors du passage du shuriken dans un portail)
    def __init__(self):
        super().__init__()

        #chargement de l'image
        self.image=pygame.image.load('ShurikenRouge1.png').convert_alpha()
        self.rect = self.image.get_rect()

      #mouvement du shuriken
    def update(self):
        self.rect.x+=8
        if self.rect.x>1100:
            self.kill()

        tp0=0

        if self.rect.x>1050:
            if 400<self.rect.y<500:
                tp0=1

        if tp0==1:
            self.rect.x = 50
            self.rect.y = 130

        tp1=0
        if self.rect.x>1050:
            if 200<self.rect.y<250:
                tp1=1
        if tp1==1:
            self.rect.x = 50
            self.rect.y= 330

class ShurikenGR(pygame.sprite.Sprite):
 # initialisation (en fonction de la vitesse voulue et aussi lors du passage du shuriken dans un portail)
    def __init__(self):
        super().__init__()

        self.image=pygame.image.load('ShurikenRouge1.png').convert_alpha()
        self.rect = self.image.get_rect()

        #mvt shuriken
    def update(self):
        self.rect.x-=7
        if self.rect.x<-21:
            self.kill()


        tp2=0
        if self.rect.x<50:
            if 300<self.rect.y<350:
                tp2=1
        if tp2==1:
            self.rect.x= 1040
            self.rect.y= 250
        tp3=0
        if self.rect.x<50:
            if 120<self.rect.y<190:
                tp3=1
        if tp3==1:
            self.rect.x= 1040
            self.rect.y= 445
