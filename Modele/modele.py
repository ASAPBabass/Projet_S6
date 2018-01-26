#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys
import os
import random
from math import pi
import pygame
from pygame.locals import *
import pygame.gfxdraw


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


def start():
    print("Début de la partie")
    sprites = pygame.sprite.Group()  # permet de regrouper les sprites
    player = Ball()
    sprites.add(player)
    return sprites


def create_ball():
    print("Creation ball")
    player = Ball()
    return player


def create():
    print ("Création de la fenêtre")
