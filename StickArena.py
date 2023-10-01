#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      matth
#
# Created:     21/05/2019
# Copyright:   (c) matth 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame, sys
from pygame.locals import *
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
                self.image = self.baseGR
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

class ShurikenDB(pygame.sprite.Sprite):
 # initialisation (en fonction de la vitesse voulue et aussi lors du passage du shuriken dans un portail)
    def __init__(self):
        super().__init__()

        self.image=pygame.image.load('ShurikenBleu1.png').convert_alpha()
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

class ShurikenGB(pygame.sprite.Sprite):
 # initialisation (en fonction de la vitesse voulue et aussi lors du passage du shuriken dans un portail)
    def __init__(self):
        super().__init__()

        self.image=pygame.image.load('ShurikenBleu1.png').convert_alpha()
        self.rect = self.image.get_rect()

        #mvt Shuriken
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









noir = 0, 0, 0
Blanc = 255, 255, 255


def main():
    """ Programme principal """
    pygame.init()

    # definition de la fenetre
    screen = pygame.display.set_mode((1100,600))
    pygame.display.set_caption("StickArena !")

    # Boucle Pour introduction
    stick=1

    while stick ==1:
        background = pygame.Surface(screen.get_size())
        background.fill(noir)





        # Definition de la police
        bigText = pygame.font.SysFont('arial', 50)

        # Definition du texte
        # render(text, antialias, rgb color tuple)
        title_text = bigText.render("Stick Arena !", True, Blanc)

        # Le centre du texte est au centre quelque soit le texte
        # Le texte est inscrit dans un rectangle
        textpos = title_text.get_rect()
        # Placement du texte en x et y
        textpos.centerx = screen.get_rect().centerx
        textpos.centery = 100
        # Collage du texte sur le fond
        background.blit(title_text, textpos,)



        lancer_text=bigText.render("Appuyer pour jouer",True, Blanc)

        textpos1 = lancer_text.get_rect()
        textpos1.centerx = screen.get_rect().centerx
        textpos1.centery = 500

        background.blit(lancer_text, textpos1)
# Images collees sur le fond de l'introduction
        persobleu = pygame.image.load("src/ninja/idle-Sheet.png").convert()

        

        background.blit(persobleu, (200,300))

        persorouge = pygame.image.load("src/ninja/idle-Sheet.png").convert() #rouge intro
        background.blit(persorouge, (700,300), (0, 0, 33, 100)) #afficher un ninja
                                                #

        shurintro= pygame.image.load("src/ninja/idle-Sheet.png").convert() #bleu intro
        background.blit(shurintro, (475,300))


        # Ajout du fond dans la fentre
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                stick=0




        pygame.display.update()


    fond1=pygame.image.load('fond1.png').convert_alpha() # chargement et collage du fond
    screen.blit(fond1, (0, 0))

            # creation personnage
    stickmanbleu = Stickmanbleu()
    stickmanbleu.rect.x = 250
    stickmanbleu.rect.y = 100
    stickmanrouge = Stickmanrouge()
    stickmanrouge.rect.x = 750
    stickmanrouge.rect.y = 100
    shuriken_list = pygame.sprite.Group()

        #creation des listes de sprites
    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(stickmanbleu)
    active_sprite_list.add(stickmanrouge)
    shuriken_sprite_list = pygame.sprite.Group()





        #reglage de l'horloge
    clock = pygame.time.Clock()

        # Boucle principale
    continuer=1
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer=0

                # touches enfoncees
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                        stickmanrouge.mvtgauche()
                if event.key == pygame.K_d:
                        stickmanrouge.mvtdroit()
                if event.key == pygame.K_LEFT:
                        stickmanbleu.mvtgauche()
                if event.key == pygame.K_RIGHT:
                        stickmanbleu.mvtdroit()
                if event.key == pygame.K_w:
                        stickmanrouge.jump()
                if event.key==pygame.K_UP:
                        stickmanbleu.jump()

                if event.key == pygame.K_s:
                        if stickmanrouge.tir<=2 :
                            if stickmanrouge.orientation==1:
                                stickmanrouge.tir+=1
                                shuriken=ShurikenDR()
                                shuriken.rect.x=stickmanrouge.rect.x+21
                                shuriken.rect.y=stickmanrouge.rect.y+20
                                shuriken_sprite_list.add(shuriken)
                                active_sprite_list.add(shuriken)
                                active_sprite_list.add(shuriken)
                            if stickmanrouge.orientation==0:
                                stickmanrouge.tir+=1
                                Shuriken=ShurikenGR()
                                Shuriken.rect.x=stickmanrouge.rect.x-21
                                Shuriken.rect.y=stickmanrouge.rect.y+20
                                shuriken_sprite_list.add(Shuriken)
                                active_sprite_list.add(Shuriken)
                if event.key==pygame.K_DOWN:
                    if event.key == pygame.K_DOWN:
                        if stickmanbleu.tir<=2 :
                            if stickmanbleu.orientation==1:
                                stickmanbleu.tir+=1
                                shuriken=ShurikenDB()
                                shuriken.rect.x=stickmanbleu.rect.x+21
                                shuriken.rect.y=stickmanbleu.rect.y+20
                                shuriken_sprite_list.add(shuriken)
                                active_sprite_list.add(shuriken)

                            if stickmanbleu.orientation==0:
                                stickmanbleu.tir+=1
                                shuriken=ShurikenGB()
                                shuriken.rect.x=stickmanbleu.rect.x-21
                                shuriken.rect.y=stickmanbleu.rect.y+20
                                shuriken_sprite_list.add(shuriken)
                                active_sprite_list.add(shuriken)



              # touches relevees
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and stickmanbleu.change_x < 0:
                    stickmanbleu.stop()
                if event.key == pygame.K_a and stickmanrouge.change_x < 0:
                    stickmanrouge.stop()
                if event.key == pygame.K_RIGHT and stickmanbleu.change_x > 0:
                    stickmanbleu.stop()
                if event.key == pygame.K_d and stickmanrouge.change_x > 0:
                    stickmanrouge.stop()



        # Mise a jour des Sprites
                """gestions des collisions stickman/ shuriken"""
        active_sprite_list.update()
        if len(shuriken_sprite_list)==0:
            stickmanrouge.tir=0
        hit_list = pygame.sprite.spritecollide(stickmanrouge,shuriken_sprite_list,False)
        for hit in hit_list:
            fondvictoireBleu=pygame.image.load('victoireBleu.png').convert_alpha()
            screen.blit(fondvictoireBleu,(0, 0))
            pygame.display.update()
            pygame.time.delay(4000)
            main()
            return()

        if len(shuriken_sprite_list)==0:
            stickmanbleu.tir=0

        hit_list = pygame.sprite.spritecollide(stickmanbleu,shuriken_sprite_list,False)
        for hit in hit_list:
            fondvictoirerouge=pygame.image.load('victoireRouge.png').convert_alpha()
            screen.blit(fondvictoirerouge,(0, 0))
            pygame.display.update()
            pygame.time.delay(4000)
            main()
            return()



        # Tous les objets a dessiner doivent se trouver ici
        screen.blit(fond1, (0, 0))

        active_sprite_list.draw(screen)


        # On limite le nombre d'images a 60 images par seconde
        clock.tick(60)

        # On raffraichit l'ecran avec tout ce qu'on a dessine
        pygame.display.flip()

    pygame.quit()





main()
