#!/usr/bin/python
#-*- coding: utf-8 -*-

from math import pi
import pygame as py
import pygame.gfxdraw
from pygame.locals import *

WIDTH = 640
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class View():  # classe s'occupant de la vue

    def __init__(self):
        self.screen = None
        self.clock = None  # fps
        self.initialization()

    def initialization(self):  # initialisation de la fenetre
        py.display.init()
        py.display.set_caption("SwitchColor")
        pygame.key.set_repeat(400, 30)
        self.screen = py.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.image.load(
            "Vue/Image/fond_gris.jpg").convert()
        self.clock = pygame.time.Clock()

    def draw(self, all_sprites):
        # self.screen.blit(self.background, (0, 0))
        self.screen.fill((41, 41, 41))
        all_sprites.draw(self.screen)  # affiche tous les sprites
        pygame.display.flip()  # met à jour la fenetre
        self.clock.tick(FPS)

    def quit(self):
        py.display.quit()
