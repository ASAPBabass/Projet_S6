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
        self.all_fonts = pygame.sprite.Group()

        self.start_pos = 0  # position de depart

        self.scroll_up = HEIGHT / 2
        self.scroll_down = 425

        self.initialization()

    def initialization(self):  # initialisation de la fenetre
        py.display.init()
        py.display.set_caption("SwitchColor")
        pygame.key.set_repeat(400, 30)
        self.screen = py.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
        self.background = pygame.image.load(
            "Vue/Image/fond_gris.jpg").convert()
        self.clock = pygame.time.Clock()

        self.player.initialization()  # on initialise le player
        self.all_sprites.add(self.player)  # puis on l'ajoute aux sprites

    def draw(self):
        self.screen.fill((41, 41, 41))  # fond gris
        self.all_sprites.draw(self.screen)  # affiche tous les sprites
        pygame.display.flip()  # met à jour la fenetre
        self.clock.tick(FPS)  # on definit la vitesse d'affichage

    def update(self):

        self.all_sprites.update()

    def quit(self):
        py.display.quit()

    def scroll(self):  # scrolling de l'ecran et des sprites
        scroll = 0
        pos_y = self.player.rect.y
        # permet de deplacer le decor et non le player
        if(pos_y <= self.scroll_up):  # si le player jump
            scroll = self.scroll_up - pos_y
            self.player.rect.y = self.scroll_up
            for sprite in self.all_fonts:
                sprite.scroll += scroll
        if(pos_y >= self.scroll_down):  # gravite
            scroll = self.scroll_down - pos_y
            self.player.rect.y = self.scroll_down
            for sprite in self.all_fonts:
                sprite.scroll += scroll

        self.start_pos += scroll
