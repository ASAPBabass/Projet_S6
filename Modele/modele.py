#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import random
import sys
from math import *

import pygame
import pygame.gfxdraw
import pygame.mask
from pygame.locals import *

from player import *
from arete import *
from star import *
from switch import *
from parallelogramme import *
from triangle import *
from ligne import *
from circle import *
from cross import *


from constantes import *


def obstacles(player, all_obstacles, all_switch):
    list_obstacles = all_obstacles.sprites()
    nb = len(list_obstacles)

    if nb == 0:
        print("Creation du 1er obstacle")

        all_switch.add(Switch(-370))
        try:
            all_obstacles.add(
                Circle(-150, 15, RAYON_G, False, (WIDTH/2)-RAYON_G, -0.04, 1))
            all_obstacles.add(
                Circle(-150, 8, RAYON_P, True, (WIDTH/2)+RAYON_P, -0.04, 0))

            all_obstacles.add(Star(-250))
        except:
            print("erreur class")

    else:
        if list_obstacles[-1].rect.y > player.rect.y:
            ran = random.randint(1, 8)
            # choix aleatoire
            if ran == 1:
                print("cercles")
                ran_circle = random.randint(1, 3)
                if ran_circle == 1:
                    all_switch.add(Switch(-350))
                    all_obstacles.add(
                        Circle(-150, 15, 120, True, WIDTH/2, 0.04, 0))
                    all_switch.add(Star(-150))

                elif ran_circle == 2:
                    all_switch.add(Switch(-350))
                    all_obstacles.add(
                        Circle(-150, 15, RAYON_TG, True, WIDTH/2, 0.04, 0))
                    all_obstacles.add(
                        Circle(-150, 15, RAYON_G, False, WIDTH/2, 0.04, 1))
                    all_switch.add(Star(-150))

                elif ran_circle == 3:
                    all_switch.add(Switch(-350))
                    all_obstacles.add(
                        Circle(-150, 15, RAYON_TG, True, WIDTH/2, 0.05, 0))
                    all_obstacles.add(
                        Circle(-150, 15, RAYON_G, False, WIDTH/2, 0.05, 1))
                    all_obstacles.add(
                        Circle(-150, 15, RAYON_P, True, WIDTH/2, 0.05, 0))
                    all_switch.add.add(Star(-150))

            elif ran == 2:  # lignes
                print("ligne")
                all_switch.add(Switch(-450))
                all_obstacles.add(Ligne(-150, True))
                all_obstacles.add(Ligne(-300, False))
                all_switch.add.add(Star(-320))

            elif ran == 3:  # carre
                print("carre")
                all_switch.add(Switch(-300))
                all_obstacles.add(Parallelogramme(-150, 90, 90, 90, 90, 0.9))
                all_switch.add(Star(-150))

            elif ran == 4:  # rectangle
                print("losange")
                all_switch.add(Switch(-350))
                all_obstacles.add(
                    Parallelogramme(-150, 100, 80, 90, 90, 1.2))
                all_switch.add(Star(-150))

            elif ran == 5:  # losange
                print("rectangle")
                all_switch.add(Switch(-350))
                all_obstacles.add(Parallelogramme(-150, 90, 90, 60, 120, 1.2))
                all_switch.add(Star(-150))

            elif ran == 6:  # triangle
                print("triangle")
                all_switch.add(Switch(-250))
                # all_obstacles.add(Triangle(-150, 90, 1.1))
                # all_obstacles.add(Circle(-150, 15,75, False,320,0.07,True))
                all_switch.add(Star(-150))

            elif ran == 7:  # double cercles
                print("double cercle")
                # deux cercles cote à cote
                try:
                    all_switch.add(Switch(-370))
                    all_obstacles.add(
                        Circle(-150, 15, 100, True, (WIDTH/2)-100, 0.04, 0))
                    all_obstacles.add(
                        Circle(-150, 15, 100, False,  (WIDTH/2)+100, 0.04, 1))
                    all_switch.add(Star(-250))

                except:
                    print("Erreur double cercles")
            elif ran == 8:
                print("triple cercle")
                all_switch.add(Switch(-700))
                all_obstacles.add(Circle(-150, 15, RAYON_G, True, WIDTH/2, 0.05, 0))
                all_obstacles.add(Star(-150))
                all_obstacles.add(Circle(-350, 15, RAYON_G, False, WIDTH/2, 0.05, 2))
                all_obstacles.add(Star(-350))
                all_obstacles.add(Circle(-550, 15, RAYON_G, True, WIDTH/2, 0.05, 0))
                all_switch.add(Star(-550))

            elif ran == 9:  # cercle + croix
                print("cercle + croix")
                all_switch.add(Switch(-350))
                all_obstacles.add(Circle(-150, 15, RAYON_TG, True, WIDTH/2, 0.05, 0))
                all_obstacles.add(Cross(WIDTH / 2 + 25, -150, 10, 50, 0.9))
                all_switch.add(Star(-300))

            elif ran== 10:  # croix
                print("croix")
                all_switch.add(Switch(-170))
                all_obstacles.add(Cross(WIDTH / 2 + 20, -150, 15, 100))
                all_switch.add(Star(-10))

            elif ran == 11:  # croix
                print("double croix")
                all_switch.add(Switch(-170))
                all_obstacles.add(Cross(WIDTH / 2 - 20, -150, 15, 50))
                all_obstacles.add(Cross(WIDTH / 2 + 20, -150, 15, 50))
                all_switch.add(Star(-10))
            elif ran == 12:  # double cercle (1 petit et 1 grand)
                print("cercle cote a cote")
                # deux cercles cote à cote
                random_circle = random.randint(1, 2)
                if random_circle == 1:
                    all_switch.add(Switch(-370))
                    all_obstacles.add(
                        Circle(-150, 8, RAYON_P, True, 260, 0.04, 0))
                    all_obstacles.add(
                        Circle(-150, 15, RAYON_G, False, 420, 0.04, 1))
                    all_switch.add(Star(-250))
                else:
                    all_switch.add(Switch(-370))
                    all_obstacles.add(
                        Circle(-150, 15, RAYON_G, False, 220, -0.04, 1))
                    all_obstacles.add(
                        Circle(-150, 8, RAYON_P, True, 380, -0.04, 0))
                    all_switch.add(Star(-250))


def collisions(player, all_obstacles, all_switch):

    for switch in all_switch:
        switch.collide(player)
    for obstacle in all_obstacles:
        if obstacle.collide(player):
            sound_jump = pygame.mixer.Sound(
                'C:/Users/Affadine/Documents/ColorSwitch/Vue/Sounds/dead.wav')
            sound_jump.play()
            return True


def menu(all_sprites):
    all_sprites.add(Circle(117, 14, 39, False, 255, 0.05, 2))
    all_sprites.add(Circle(117, 14, 39, True, 385, -0.05, 2))
