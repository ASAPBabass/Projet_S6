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

        self.initialization()

    def initialization(self):  # initialisation de la fenetre
        py.display.init()
        py.display.set_caption("SwitchColor")
        pygame.key.set_repeat(400, 30)
        self.screen = py.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.image.load(
            "Vue/Image/fond_gris.jpg").convert()
        self.clock = pygame.time.Clock()

        self.player.initialization()
        self.all_sprites.add(self.player)

    def draw(self):
        # self.screen.blit(self.background, (0, 0))
        self.screen.fill((41, 41, 41))
        self.all_sprites.draw(self.screen)  # affiche tous les sprites
        pygame.display.flip()  # met à jour la fenetre
        self.clock.tick(FPS)

    def update(self):
        self.all_sprites.update()

    def quit(self):
        py.display.quit()

    def defilement(self, font, player):  # permet le defilement verticale
        p_x = player.rect.x
        p_y = player.rect.y
