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
from Vue.vue import createScreen, startScreen


def CtlCreate():
    # sprites = create()
    screen = createScreen()
    return screen


def Ctl_create_ball():  # création de la balle
    create_ball()


def CtlStart():
    print("Debut CtlStart")
    sprites = start()
    screen = startScreen(sprites)


def CtlUpdate():

    print("Update")
    startScreen(sprites)


def main():
    # initialisation
    py.display.init()

    screen = CtlCreate()

    try:

        end = False
        print("Début")
        while not end:
            for event in py.event.get():
                if event.type == QUIT:
                    end = True
                else:
                    if event.type == KEYDOWN:
                        if event.key == K_q:
                            screen = CtlStart()

        # CtlUpdate(screen)

    except Exception:
        print("Erreur !")

    py.quit()
    quit()


def __init__():
    main()
