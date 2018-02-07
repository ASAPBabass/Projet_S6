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


def menu():

    end = False

    while not end:
    # Evenements

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return True
                else:
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            return False
                        if event.key == K_ESCAPE:
                            end = True

        except Exception:
            print("Erreur Menu !")

        return True


def main():
    # initialisation

    player = Player()

    view = View(player)  # on ajoute le player dans la Vue

    cercle = Circle()

    view.all_fonts.add(cercle)  # on ajoute le cercle dans la Vue
    view.all_sprites.add(cercle)

    end_menu = False
    end = False  # variable d'arret

    while not end_menu:
    # Evenements
        view.menu()
        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    end_menu = True
                    end = True
                else:
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            end_menu = True
                        if event.key == K_ESCAPE:
                            end_menu = True
                            end = True

        except Exception:
            print("Erreur Menu !")

    while not end:
    # Evenements

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    end = True
                else:
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            for i in range(6):
                                player.jump(15)
                                # view.all_sprites.update()
                                view.update()
                                cercle.collisions(player)
                                view.scroll()
                                view.draw()
                            player.jump(10)

                        if event.key == K_q:
                            end = True

        except Exception:
            print("Erreur !")
        # print(cercle.rect.y)
        # update
        view.update()

        # on verifie les collisions
        cercle.collisions(player)
        # print(cercle.rect.y)

        view.scroll()
        # draw/render
        view.draw()  # met à jour l'ecran et affiche les sprites

    view.quit()


main()
quit()
