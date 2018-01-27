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
    py.display.init()
    screen = py.display.set_mode((WIDTH, HEIGHT))
    py.display.set_caption("SwitchColor")

    clock = pygame.time.Clock()  # fps

    all_sprites = pygame.sprite.Group()

    font = pygame.sprite.Group()
    player = pygame.sprite.Group()

    # create_font(font)
    # create_player(player)
    cercle = Circle()
    font.add(cercle)

    p = Ball()
    player.add(p)

    all_sprites.add(player)
    all_sprites.add(font)

    py.key.set_repeat(400, 30)

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
                            # ball.jump()
                            player.jump()

                        if event.key == K_q:
                            end = True

        except Exception:
            print("Erreur !")

        # update
        all_sprites.update()

        # draw/render
        screen.fill(WHITE)
        all_sprites.draw(screen)

        # flip
        py.display.flip()
        clock.tick(30)

    py.display.quit()
    quit()


main()
