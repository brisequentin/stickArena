

import pygame, sys
from pygame.locals import *
import shuriken
import stickman


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
