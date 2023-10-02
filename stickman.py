import pygame, sys
from pygame.locals import *

#l 15-180;254-418


class Stickman(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()

        #importer les images des persos.
        #https://www.geeksforgeeks.org/pygame-flip-the-image/
        #tobeused for left side

        # initialisation des caracteristiques

        #position
        self.change_x =0
        self.change_y =0
        self.vie=4

        self.color=color   #0 red, 1 blue
        self.orientation=color #0 left, 1 right
        
        self.anim=0
        self.tir=0
        self.score=0

#creation d'une classe du Bonhomme Rouge
class Stickmanrouge(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.Run1DR=pygame.image.load("1RunDR.png").convert_alpha()
        self.Run2DR=pygame.image.load('2RunDR.png').convert_alpha()
        self.Run3DR=pygame.image.load('3RunDR.png').convert_alpha()
        self.Run4DR=pygame.image.load('4RunDR.png').convert_alpha()
        self.Run5DR=pygame.image.load('5RunDR.png').convert_alpha()
        self.Run6DR=pygame.image.load('6RunDR.png').convert_alpha()
        self.Run1GR=pygame.image.load('1RunGR.png').convert_alpha()
        self.Run2GR=pygame.image.load('2RunGR.png').convert_alpha()
        self.Run3GR=pygame.image.load('3RunGR.png').convert_alpha()
        self.Run4GR=pygame.image.load('4RunGR.png').convert_alpha()
        self.Run5GR=pygame.image.load('5RunGR.png').convert_alpha()
        self.Run6GR=pygame.image.load('6RunGR.png').convert_alpha()
        self.baseGR=pygame.image.load('deboutGR.png').convert_alpha()
        self.baseDR=pygame.image.load('deboutDR.png').convert_alpha()
        self.Jump1DR=pygame.image.load('1JumpDR.png').convert_alpha()
        self.Jump2DR=pygame.image.load('2JumpDR.png').convert_alpha()
        self.Jump1GR=pygame.image.load('1JumpGR.png').convert_alpha()
        self.Jump2GR=pygame.image.load('2JumpGR.png').convert_alpha()

        self.image = self.baseDR

        self.rect = self.image.get_rect()

# initialisation des caracteristiques
        self.change_x =0
        self.change_y =0
        self.vie=4
        self.orientation=0
        self.anim=0
        self.tir=0
        self.score=0





    def update(self):
        #actualisation de l'image

        self.rect.x += self.change_x
        self.rect.y += self.change_y
        self.anim+=1
        if self.rect.y<430:
            self.change_y+=0.5

        if self.rect.x<0:
            self.rect.x-=self.change_x

        if self.rect.x>1050:
            self.rect.x-=self.change_x

        if self.rect.y==430:
            self.saut=0

        if self.rect.y>430:
            self.rect.y=430
            self.change_y=0
            self.saut=0

        if self.orientation==0:
            if self.change_x==0 and self.change_y==0:
                self.image = self.baseGR  #orientation 0 gauche rouge ?
            elif self.change_y==0 :
                self.rect.y=455
                if 0<self.anim and self.anim<10:
                    self.image=self.Run1GR
                if 10<=self.anim and self.anim<20:
                    self.image=self.Run2GR
                if 20<=self.anim and self.anim<30:
                    self.image=self.Run3GR
                if 30<=self.anim and self.anim<40:
                    self.image=self.Run4GR
                if 40<=self.anim and self.anim<50:
                  self.image=self.Run5GR
                if 50<=self.anim and self.anim<60:
                   self.image=self.Run6GR
                if self.anim>=60:

                    self.anim=0
            else :
                if 0<self.anim and self.anim<40:
                    self.image=self.Jump1GR
                if 40<=self.anim and self.anim<80:
                    self.image=self.Jump2GR

                    self.anim=0


        if self.orientation==1:

            if self.change_x==0 and self.change_y==0:
                self.image = self.baseDR
            elif self.change_y==0 :
                self.rect.y=455
                if 0<self.anim and self.anim<10:
                    self.image=self.Run1DR
                if 10<=self.anim and self.anim<20:
                    self.image=self.Run2DR
                if 20<=self.anim and self.anim<30:
                    self.image=self.Run3DR
                if 30<=self.anim and self.anim<40:
                    self.image=self.Run4DR
                if 40<=self.anim and self.anim<50:
                  self.image=self.Run5DR
                if 50<=self.anim and self.anim<60:
                   self.image=self.Run6DR
                if self.anim>=60:
                    self.anim=0

                    self.anim=0

            else :
                if 0<self.anim and self.anim<40:
                    self.image=self.Jump1DR
                if 40<=self.anim and self.anim<80:
                    self.image=self.Jump2DR

                    self.anim=0



# Controles du joueur

    def mvtgauche(self):
       """Mouvement gauche """
       self.change_x = -3
       self.change_y = 0
       self.orientation=0

    def mvtdroit(self):
        """Mouvement droite"""
        self.change_x = 3
        self.change_y = 0
        self.orientation=1

    def jump(self):
        if self.saut==0:
            self.saut=1
            self.change_y=-18
        if self.orientation==0:
            if self.change_y==0:
                self.image = self.baseGR
            else :
                if 0<self.anim and self.anim<-2:
                    self.image=self.Jump1GR
                if self.anim>=-2:
                    self.anim=0
        if self.orientation==1:
            if self.change_y==0:
                self.image = self.baseDB
            else :
                if 0<self.anim and self.anim<-2:
                    self.image=self.Jump1DR
                if self.anim>=-2:
                    self.anim=0





    def stop(self):
        """arret"""
        self.change_x=0


class Stickmanbleu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.Run1DB=pygame.image.load('1RunDB.png').convert_alpha()
        self.Run2DB=pygame.image.load('2RunDB.png').convert_alpha()
        self.Run3DB=pygame.image.load('3RunDB.png').convert_alpha()
        self.Run4DB=pygame.image.load('4RunDB.png').convert_alpha()
        self.Run5DB=pygame.image.load('5RunDB.png').convert_alpha()
        self.Run6DB=pygame.image.load('6RunDB.png').convert_alpha()
        self.Run1GB=pygame.image.load('1RunGB.png').convert_alpha()
        self.Run2GB=pygame.image.load('2RunGB.png').convert_alpha()
        self.Run3GB=pygame.image.load('3RunGB.png').convert_alpha()
        self.Run4GB=pygame.image.load('4RunGB.png').convert_alpha()
        self.Run5GB=pygame.image.load('5RunGB.png').convert_alpha()
        self.Run6GB=pygame.image.load('6RunGB.png').convert_alpha()
        self.baseGB=pygame.image.load('deboutGB.png').convert_alpha()
        self.baseDB=pygame.image.load('deboutDB.png').convert_alpha()
        self.Jump1DB=pygame.image.load('1JumpDB.png').convert_alpha()
        self.Jump2DB=pygame.image.load('2JumpDB.png').convert_alpha()
        self.Jump1GB=pygame.image.load('1JumpGB.png').convert_alpha()
        self.Jump2GB=pygame.image.load('2JumpGB.png').convert_alpha()
        self.image = self.baseGB
        self.rect = self.image.get_rect()

# initialisation des caracteristiques
        self.change_x =0
        self.change_y =0
        self.vie=4
        self.orientation=1
        self.anim=0
        self.tir=0
        self.score=0





    def update(self):
        #actualisation de l'image
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        self.anim+=1
        if self.rect.y<430:
            self.change_y+=0.5

        if self.rect.x<0:
            self.rect.x-=self.change_x

        if self.rect.x>1050:
            self.rect.x-=self.change_x

        if self.rect.y==430:
            self.saut=0

        if self.rect.y>430:
            self.rect.y=430
            self.change_y=0
            self.saut=0

        if self.orientation==0:

            if self.change_x==0 and self.change_y==0:
                self.image = self.baseGB
            elif self.change_y==0 :
                self.rect.y=455
                if 0<self.anim and self.anim<10:
                    self.image=self.Run1GB
                if 10<=self.anim and self.anim<20:
                    self.image=self.Run2GB
                if 20<=self.anim and self.anim<30:
                    self.image=self.Run3GB
                if 30<=self.anim and self.anim<40:
                    self.image=self.Run4GB
                if 40<=self.anim and self.anim<50:
                  self.image=self.Run5GB
                if 50<=self.anim and self.anim<60:
                   self.image=self.Run6GB
                if self.anim>=60:

                    self.anim=0
            else :
                if 0<self.anim and self.anim<40:
                    self.image=self.Jump1GB
                if 40<=self.anim and self.anim<80:
                    self.image=self.Jump2GB

                    self.anim=0





        if self.orientation==1:

            if self.change_x==0 and self.change_y==0:
                self.image = self.baseDB
            elif self.change_y==0 :
                self.rect.y=455
                if 0<self.anim and self.anim<10:
                    self.image=self.Run1DB
                if 10<=self.anim and self.anim<20:
                    self.image=self.Run2DB
                if 20<=self.anim and self.anim<30:
                    self.image=self.Run3DB
                if 30<=self.anim and self.anim<40:
                    self.image=self.Run4DB
                if 40<=self.anim and self.anim<50:
                  self.image=self.Run5DB
                if 50<=self.anim and self.anim<60:
                   self.image=self.Run6DB
                if self.anim>=60:
                    self.anim=0



            else :
                if 0<self.anim and self.anim<40:
                    self.image=self.Jump1DB
                if 40<=self.anim and self.anim<80:
                    self.image=self.Jump2DB

                    self.anim=0


# Controles du joueur

    def mvtgauche(self):
        """Mouvement gauche """
        self.change_x = -3
        self.change_y = 0
        self.orientation=0

    def mvtdroit(self):
        """Mouvement droite"""
        self.change_x = 3
        self.change_y = 0
        self.orientation=1

    def jump(self):
        if self.saut==0:
            self.saut=1
            self.change_y=-18
        if self.orientation==0:
            if self.change_y==0:
                self.image = self.baseGB
            else :
                if 0<self.anim and self.anim<-2:
                    self.image=self.Jump1GB
                if self.anim>=-2:
                    self.anim=0
        if self.orientation==1:
            if self.change_y==0:
                self.image = self.baseDB
            else :
                if 0<self.anim and self.anim<-2:
                    self.image=self.Jump1DB
                if self.anim>=-2:
                    self.anim=0




    def stop(self):
        """arret"""
        self.change_x=0