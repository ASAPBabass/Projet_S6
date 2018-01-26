#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import random
import sys
from math import pi

import pygame
import pygame.gfxdraw
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Vue/Image/redball.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (640 / 2, 480 / 2)
        # self.image = pygame.Surface((50,50))
        # self.image.fill(color)
        # self.image.fill(a)
        # self.image.set_alpha(128)
        # pygame.gfxdraw.filled_circle(self.image,25,25,25,RED)

    def jump(self):
        self.rect.y -= 40

    def update(self):  # gravite
        if self.rect.y < 410:
            self.rect.y += 2


class Circle(pygame.sprite.Sprite):

    def __init__(self, screen):
        pygame.sprite.Sprite(self)
        coord_3 = 75
        i = 0.02  # vitesse de rotation

        def draw(self):
            pygame.draw.arc(
                screen, WHITE, [320, 75, coord_3, 75], 0 + i, pi / 2 + i, 2)
            pygame.draw.arc(
                screen, GREEN, [320, 75, coord_3, 75], pi / 2 + i, pi + i, 2)
            pygame.draw.arc(
                screen, BLUE, [320, 75, coord_3, 75], pi + i, 3 * pi / 2 + i, 2)
            pygame.draw.arc(
                screen, RED,  [320, 75, coord_3, 75], 3 * pi / 2 + i, 2 * pi + i, 2)

        def update(self):
            self.coord_3 += 1

        def set(self):
            self.coord_3 = 75


def start(screen, sprites, font):
    print("Début de la partie")
    player = Ball()
    circle = Circle(screen)
    font.add(circle)
    sprites.add(player)


def create_ball():
    print("Creation ball")
    player = Ball()
    return player


def create():
    print ("Création de la fenêtre")
