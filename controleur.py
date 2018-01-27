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
from Modele.modele import Ball
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

    # create_font(font)
    # create_player(player)
    cercle = Circle()
    font.add(cercle)

    player = Ball()

    all_sprites.add(player)
    all_sprites.add(font)

    print("bonjour")
    # CtlStart(player, font)

    end = False
    print("Début")
    while not end:
    # Events

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    end = True
                else:
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            for i in range(10):
                                player.jump()
                                all_sprites.update()
                                view.update(all_sprites)
                            player.jump()

                        if event.key == K_q:
                            end = True

        except Exception:
            print("Erreur !")

        # print(player.rect.x, player.rect.y)
        # update
        all_sprites.update()

        # draw/render
        view.update(all_sprites)
        # update_screen(screen)
        # all_sprites.draw(screen)

        # flip
        # py.display.flip()

    # py.display.quit()


main()
quit()
