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


def CtlStart(player, font):
    # screen = CtlCreate()
    print("Debut CtlStart")
    # start(player, font)
    print("start reussi")
    # startScreen(screen, sprites, font)


def main():
    # initialisation

    player = Player()

    view = View(player)

    cercle = Circle()

    view.all_sprites.add(cercle)

    end = False  # variable d'arret

    while not end:
    # Evenements

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    end = True
                else:
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            for i in range(4):
                                player.jump(10)
                                view.all_sprites.update()
                                cercle.collisions(player)
                                view.draw()
                            player.jump(5)

                        if event.key == K_q:
                            end = True

        except Exception:
            print("Erreur !")

        # print(player.rect.x, player.rect.y)
        # update
        view.update()

        cercle.collisions(player)

        # draw/render
        view.draw()  # met à jour l'ecran et affiche les sprites

    view.quit()


main()
quit()
