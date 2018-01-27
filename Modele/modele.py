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

colors = {WHITE, BLACK, BLUE, RED, GREEN}


class Ball(pygame.sprite.Sprite):  # class du joueur

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Vue/Image/redball.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (640 / 2, 410)
        # self.image = pygame.Surface((50,50))
        # self.image.fill(color)
        # self.image.fill(a)
        # self.image.set_alpha(128)
        # pygame.gfxdraw.filled_circle(self.image,25,25,25,RED)

    def jump(self):
        # print("jump")
        self.rect.y -= 7

    def update(self):  # gravite
        if self.rect.y < 410:
            self.rect.y += 2


class Circle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([200, 200]).convert_alpha()
        self.rect = self.image.get_rect()
        # permet la transparence avec convert_alpha
        self.image.fill((0, 0, 0, 0))
        self.coord_3 = 75
        self.i = 1

        pygame.draw.arc(
            self.image, WHITE, self.rect, 0 + self.i, pi / 2 + self.i, 6)
        pygame.draw.arc(
            self.image, GREEN, self.rect, pi / 2 + self.i, pi + self.i, 6)
        pygame.draw.arc(
            self.image, BLUE, self.rect, pi + self.i, 3 * pi / 2 + self.i, 6)
        pygame.draw.arc(
            self.image, RED,  self.rect, 3 * pi / 2 + self.i, 2 * pi + self.i, 6)

        self.rect.center = (640 / 2, 200)

    def initialization(self):
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()

        pygame.draw.arc(
            self.image, WHITE, self.rect, 0 + self.i, pi / 2 + self.i, 6)
        pygame.draw.arc(
            self.image, GREEN, self.rect, pi / 2 + self.i, pi + self.i, 6)
        pygame.draw.arc(
            self.image, BLUE, self.rect, pi + self.i, 3 * pi / 2 + self.i, 6)
        pygame.draw.arc(
            self.image, RED,  self.rect, 3 * pi / 2 + self.i, 2 * pi + self.i, 6)

        self.rect.center = (640 / 2, 200)

    def update(self):
        self.coord_3 += 1
        self.i += 0.02  # vitesse de rotation
        self.initialization()

    def set(self):
        self.coord_3 = 75


def start(player, font):
    print("Début de la partie")
    p1 = Ball()
    circle = Circle()
    print("Début de la partie")
    font.add(circle)
    player.add(p1)


def create_font(font):
    f = Circle()
    font.add(f)
    return font


def create_player(player):
    p = Ball()
    player.add(p)
    return player
