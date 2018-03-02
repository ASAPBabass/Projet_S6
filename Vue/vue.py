#!/usr/bin/python
#-*- coding: utf-8 -*-

from math import pi

import pygame as py
import pygame.gfxdraw
from pygame.locals import *

WIDTH = 640
HEIGHT = 480
FPS = 30

WHITE = (254, 254, 254)
BLACK = (0, 0, 0)
BLUE = (54, 225, 243)
PURPLE = (141, 19, 250)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (247, 222, 15)
ROSE = (252, 2, 128)
GREY = (41, 41, 41)

colors = (BLUE, YELLOW, PURPLE, ROSE)


class View():  # classe s'occupant de la vue

    def __init__(self, player):
        self.screen = None
        self.clock = None  # fps
        self.player = player
        self.all_sprites = pygame.sprite.Group()
        self.all_obstacles = pygame.sprite.OrderedUpdates()
        self.all_switch = pygame.sprite.OrderedUpdates()

        self.start_pos = 0  # position de depart

        self.scroll_up = 250
        self.scroll_down = 410

        self.initialization()

    def initialization(self):
        py.display.init()  # initialisation de la fenetre
        pygame.font.init()  # initialisation de la police d'ecriture
        py.display.set_caption("SwitchColor")
        # pygame.key.set_repeat(400, 30)
        self.screen = py.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill((41, 41, 41))  # fond gris
        self.clock = pygame.time.Clock()

        self.player.initialization()  # on initialise le player
        self.all_sprites.add(self.player)  # puis on l'ajoute aux sprites

    def draw(self):  # affichage du jeu
        self.screen.fill((41, 41, 41))  # fond gris
        self.all_switch.draw(self.screen)
        self.all_obstacles.draw(self.screen)

        self.all_sprites.draw(self.screen)  # affiche tous les sprites

        self.score()
        pygame.display.flip()  # met à jour la fenetre
        self.clock.tick(40)  # on definit la vitesse d'affichage

    def update(self):  # on met a jour les sprites
        self.all_obstacles.update()
        self.all_switch.update()
        self.all_sprites.update()

    def scroll(self):  # scrolling de l'ecran et des sprites
        scroll = 0
        pos_y = self.player.rect.y
        # permet de deplacer le decor et non le player
        if(pos_y <= self.scroll_up):  # si le player jump
            scroll = self.scroll_up - pos_y
            self.player.rect.y = self.scroll_up
            for sprite in self.all_obstacles:
                sprite.scroll += scroll
            for sprite in self.all_switch:
                sprite.scroll += scroll
        if(pos_y >= self.scroll_down):  # gravite
            scroll = self.scroll_down - pos_y
            self.player.rect.y = self.scroll_down
            for sprite in self.all_obstacles:
                sprite.scroll += scroll
            for sprite in self.all_switch:
                sprite.scroll += scroll

        self.start_pos += scroll

    def score(self):  # affichage du score
        font = pygame.font.Font(None, 45)
        score = font.render(str(self.player.score), 10, (254, 254, 254))
        self.screen.blit(score, (50, 50))

    def menu(self):  # Menu du jeu
        self.screen.fill((41, 41, 41))  # fond gris
        background_menu = pygame.image.load(
            "Vue/Image/titre.png").convert()
        self.screen.blit(background_menu, (50, 50))
        font = pygame.font.Font(None, 50)
        titre = font.render(
            "APPUYEZ SUR ESPACE", 10, (254, 254, 254))
        self.screen.blit(titre, (130, 300))
        pygame.display.flip()

    def retry(self, player):
        self.screen.fill((41, 41, 41))  # fond gris
        font = pygame.font.Font(None, 30)
        score = font.render(
            "SCORE : " + str(self.player.score), 10, (254, 254, 254))

        mon_fichier = open("fichier.txt","r") 
        score_max=mon_fichier.read()
        mon_fichier.close()
        self.player.bestScore=int(score_max)
        if(self.player.score > self.player.bestScore):
            self.player.bestScore=self.player.score
            mon_fichier = open("fichier.txt", "w") 
            mon_fichier.write(str(self.player.bestScore))
            mon_fichier.close()
        else:
            pass

        best = font.render("MEILLEUR SCORE : " + str(
            self.player.bestScore), 10, (254, 254, 254))
        self.player.score=0
        titre = font.render(
            "POUR RECOMMENCER APPUYER SUR ENTRER", 10, (254, 254, 254))
        self.screen.blit(score, (50, 200))
        self.screen.blit(best, (50, 230))
        self.screen.blit(titre, (50, 270))
        pygame.display.flip()

    def pause(self):
        font = pygame.font.Font(None, 30)
        pause = font.render(
            "JEU EN PAUSE", 10, (254, 254, 254))
        self.screen.blit(pause, (50, 100))
        pygame.display.flip()

    def quit(self):
        py.display.quit()
