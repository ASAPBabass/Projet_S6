#!/usr/bin/python
#-*- coding: utf-8 -*-

from math import pi

import pygame as py
import pygame.gfxdraw
from pygame.locals import *
from Modele.constantes import *


class View():  # classe s'occupant de la vue

    def __init__(self, player):
        self.screen = None
        self.clock = None  # fps
        self.player = player
        self.all_sprites = pygame.sprite.Group()
        self.all_obstacles = pygame.sprite.OrderedUpdates()
        self.all_switch = pygame.sprite.OrderedUpdates()
        self.rect = None
        self.son = None

        self.start_pos = 0  # position de depart

        self.scroll_up = 250
        self.scroll_down = 410

        self.initialization()

    def initialization(self):
        py.display.init()  # initialisation de la fenetre
        pygame.font.init()  # initialisation de la police d'ecriture
        pygame.mixer.pre_init(22050, -16, 2, 1024)
        pygame.mixer.init()
        py.display.set_caption("SwitchColor")
        # pygame.key.set_repeat(400, 30)
        self.screen = py.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
        self.screen.fill((41, 41, 41))  # fond gris
        self.clock = pygame.time.Clock()
        self.rect = self.screen.get_rect()
        # sounds
        start = pygame.mixer.Sound(
            '/home/bastien/Documents/Project/SwitchColor/Vue/Sounds/colorswitch.wav')
        start.play()

        self.player.initialization()  # on initialise le player

    def draw(self):  # affichage du jeu
        self.screen.fill((41, 41, 41))  # fond gris

        self.all_obstacles.draw(self.screen)
        self.all_switch.draw(self.screen)

        self.all_sprites.draw(self.screen)  # affiche tous les sprites

        self.score()
        pygame.display.flip()  # met à jour la fenetre
        self.clock.tick(40)  # on definit la vitesse d'affichage

    def update(self):  # on met a jour les

        list = self.all_obstacles.sprites()
        nb = len(list)
        if nb > 6:
            self.all_obstacles.remove(list[0])

        self.all_obstacles.update()
        self.all_switch.update()
        self.all_sprites.update()

    def update_menu(self):
        self.all_sprites.update()

    def draw_menu(self):
        self.all_sprites.draw(self.screen)
        pygame.display.flip()  # met à jour la fenetre
        self.clock.tick(40)  # on definit la vitesse d'affichage

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
        """
        self.screen.fill((41, 41, 41))  # fond gris
        background_menu = pygame.image.load(
            "Vue/Image/titre.png").convert()
        # self.screen.blit(background_menu, (50, 50))
        #self.screen.blit(
        #    background_menu, (WIDTH / 2 - WIDTH / 6, HEIGHT / 2 - HEIGHT / 5))
        font = pygame.font.Font(None, (WIDTH - HEIGHT) / 10)
        titre = font.render(
            "APPUYEZ SUR ESPACE", 10, (254, 254, 254))
        # self.screen.blit(titre, (130, 300))
        self.screen.blit(titre, (WIDTH / 2 - WIDTH / 8, HEIGHT / 2))
        pygame.display.flip()
        """

    def retry(self, player):
        self.screen.fill((41, 41, 41))  # fond gris
        font = pygame.font.Font(None, 28)
        font_2 = pygame.font.Font(
            "/home/bastien/Documents/Project/SwitchColor/Vue/Fonts/Jura-Italic.ttf", 15)
        font_2.set_italic(True)
        score = font.render(
            "SCORE : " + str(self.player.score), 10, (254, 254, 254))

        mon_fichier = open("fichier.txt", "r")
        score_max = mon_fichier.read()
        mon_fichier.close()
        self.player.bestScore = int(score_max)
        if(self.player.score > self.player.bestScore):
            self.player.bestScore = self.player.score
            mon_fichier = open("fichier.txt", "w")
            mon_fichier.write(str(self.player.bestScore))
            mon_fichier.close()
        else:
            pass

        best = font.render("MEILLEUR SCORE : " + str(
            self.player.bestScore), 10, (254, 254, 254))
        self.player.score = 0
        titre = font_2.render(
            "APPUYER SUR ENTRER POUR RECOMMENCER", 10, (253, 253, 253))
        self.screen.blit(score, (WIDTH / 2 - 60, 200))
        self.screen.blit(best, (WIDTH / 2 - 110, 230))
        self.screen.blit(titre, (WIDTH / 2 - 150, 270))
        pygame.display.flip()

    def pause(self):
        font = pygame.font.Font(None, 30)
        pause = font.render(
            "JEU EN PAUSE", 10, (254, 254, 254))
        self.screen.blit(pause, (50, 100))
        pygame.display.flip()

    def quit(self):
        pygame.mixer.quit()
        pygame.font.quit()
        pygame.display.quit()
        quit()
