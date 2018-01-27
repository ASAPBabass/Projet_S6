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


def CtlStart(sprites, font):
    # screen = CtlCreate()
    print("Debut CtlStart")
    start(sprites, font)
    print("start reussi")
    # startScreen(screen, sprites, font)


def CtlUpdate(screen, sprites, font):

    print("Update")
    updateScreen(screen, sprites, font)


def main():
    # initialisation
    py.init()
    screen = py.display.set_mode((WIDTH, HEIGHT))
    py.display.set_caption("SwitchColor")

    clock = pygame.time.Clock()  # fps
    all_sprites = pygame.sprite.Group()
    font = pygame.sprite.Group()

    py.key.set_repeat(400, 30)

    print("bonjour")
    try:

        # CtlStart(screen, all_sprites, font)

        end = False
        print("Début")
        while not end:
            for event in py.event.get():
                if event.type == QUIT:
                    end = True
                else:
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            print("space")
                            CtlStart(all_sprites, font)

            # update
            all_sprites.update()
            font.update()

            # draw/render
            screen.fill(WHITE)
            font.draw(screen)
            all_sprites.draw(screen)

            # flip
            py.display.flip()
            clock.tick(60)

    except Exception:
        print("Erreur !")

    py.quit()
    quit()


main()
