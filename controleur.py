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
    start(player, font)
    print("start reussi")
    # startScreen(screen, sprites, font)


def main():
    # initialisation
    view = View()

    all_sprites = pygame.sprite.Group()
    font = pygame.sprite.Group()

    cercle = Circle()
    player = Player()

    # ligne = Ligne()

    font.add(cercle)
    all_sprites.add(player)
    all_sprites.add(font)
    # all_sprites.add(ligne)

    end = False  # variable d'arret

    while not end:
    # Events

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    end = True
                else:
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            for i in range(4):
                                player.jump(10)
                                all_sprites.update()
                                cercle.collisions(player)
                                view.draw(all_sprites)
                            player.jump(5)

                        if event.key == K_q:
                            end = True

        except Exception:
            print("Erreur !")

        # print(player.rect.x, player.rect.y)
        # update
        all_sprites.update()

        cercle.collisions(player)

        # draw/render
        view.draw(all_sprites)  # met à jour l'ecran et affiche les sprites
        # all_sprites.draw(view.screen)
        # ligne.initialization()
        # print(player.score)

    view.quit()


main()
quit()
