#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import random
import sys
from math import pi

import pygame as py
import pygame.gfxdraw
from pygame.locals import *

from Modele.modele import *
from Vue.vue import *


def CtlCreate():
    # sprites = create()
    screen = createScreen()
    return screen


def Ctl_create_ball():  # création de la balle
    create_ball()


def CtlStart(screen, sprites, font):
    print("Debut CtlStart")

    startScreen(screen, sprites, font)


def CtlUpdate(screen, sprites, font):

    print("Update")
    updateScreen(screen, sprites, font)


def main():
    # initialisation
    py.display.init()
    screen = CtlCreate()

    sprites = pygame.sprite.Group()

    font = pygame.sprite.Groupe()

    try:

        end = False
        print("Début")
        while not end:
            for event in py.event.get():
                if event.type == QUIT:
                    end = True
                else:
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            CtlStart(screen, sprites, font)

        CtlUpdate(screen, sprites, font)

    except Exception:
        print("Erreur !")

    py.quit()
    quit()


def __init__():
    main()
