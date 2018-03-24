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

        all_switch.add(Switch(H_S))
        try:
            all_obstacles.add(
                Circle(HEIGHT_O, with_G, RAYON_G, True, (WIDTH / 2) - RAYON_G, V_M, 0))
            all_obstacles.add(
                Circle(HEIGHT_O, with_M, RAYON_P, False, (WIDTH / 2) + RAYON_P, V_M, 1))
            all_obstacles.add(Star(H_E))
        except:
            print("erreur class")

    else:
        if list_obstacles[-1].rect.y > player.rect.y:
            ran = 2
            ran = random.randint(1, 13)
            # choix aleatoire
            if ran == 1:
                print("cercles")
                ran_circle = random.randint(1, 3)
                if ran_circle == 1:
                    all_switch.add(Switch(H_S))
                    all_obstacles.add(
                        Circle(HEIGHT_O, with_G, RAYON_G, True, WIDTH / 2, V_M, 0))
                    all_switch.add(Star(H_E_M))

                elif ran_circle == 2:
                    all_switch.add(Switch(H_S))
                    all_obstacles.add(
                        Circle(HEIGHT_O, with_G, RAYON_T, True, WIDTH / 2, V_M, 0))
                    all_obstacles.add(
                        Circle(HEIGHT_O, with_G, RAYON_G, False, WIDTH / 2, V_M, 1))
                    all_switch.add(Star(H_E_M))

                elif ran_circle == 3:
                    all_switch.add(Switch(H_S))
                    all_obstacles.add(
                        Circle(HEIGHT_O, with_G, RAYON_T, True, WIDTH / 2, V_M, 0))
                    all_obstacles.add(
                        Circle(HEIGHT_O,  with_G, RAYON_G, False, WIDTH / 2, V_M, 1))
                    all_obstacles.add(
                        Circle(HEIGHT_O, with_G, RAYON_M, True, WIDTH / 2, V_M, 0))
                    all_switch.add.add(Star(H_E_M))
            elif ran == 2:  # lignes
                print("ligne")
                all_switch.add(Switch(H_S - 200))
                all_obstacles.add(Ligne(HEIGHT_O, True))
                all_obstacles.add(Ligne(HEIGHT_O + 150, False))
                all_switch.add(Star(H_E - 75))
                all_obstacles.add(Ligne(HEIGHT_O - 150, False))
                all_switch.add(Star(H_E + 75))

            elif ran == 3:  # carre
                print("losange")
                all_switch.add(Switch(H_S))
                all_obstacles.add(
                    Parallelogramme(HEIGHT_O, with_G, RAYON_M, RAYON_G, 90, 90, V_G))
                all_switch.add(Star(H_E_M))

            elif ran == 4:  # rectangle
                print("carre")
                all_switch.add(Switch(H_S))
                all_obstacles.add(
                    Parallelogramme(HEIGHT_O, with_G, RAYON_G, RAYON_G, 90, 90, V_G))
                all_switch.add(Star(H_E_M))

            elif ran == 5:  # losange
                print("rectangle")
                all_switch.add(Switch(H_S))
                all_obstacles.add(
                    Parallelogramme(HEIGHT_O, with_G, RAYON_G, RAYON_G, 120, 60, V_G))
                all_switch.add(Star(H_E_M))

            elif ran == 6:  # triangle
                print("triangle + cercle")
                all_switch.add(Switch(H_S))
                all_obstacles.add(Triangle(HEIGHT_O, with_G, RAYON_T, V_G))
                all_obstacles.add(
                    Circle(HEIGHT_O, with_G, RAYON_M - 5, True, WIDTH / 2, V_M, 1))
                all_switch.add(Star(H_E_M))

            elif ran == 7:  # double cercles
                print("double cercle")
                # deux cercles cote à cote
                try:
                    all_switch.add(Switch(H_S))
                    all_obstacles.add(
                        Circle(HEIGHT_O,  with_G, RAYON_G, True, (WIDTH / 2) - RAYON_G, V_M, 0))
                    all_obstacles.add(
                        Circle(HEIGHT_O,  with_G, RAYON_G, False,  (WIDTH / 2) + RAYON_G, V_M, 1))
                    all_switch.add(Star(H_E))

                except:
                    print("Erreur double cercles")
            elif ran == 8:
                print("triple cercle")
                all_switch.add(Switch(2 * H_S))
                all_obstacles.add(
                    Circle(HEIGHT_O,  with_G, RAYON_G, True, WIDTH / 2, V_M, 0))
                all_switch.add(Star(H_E_M))
                all_obstacles.add(
                    Circle(HEIGHT_O - 2 * RAYON_G,  with_G, RAYON_G, False, WIDTH / 2, V_M, 2))
                all_switch.add(Star(H_E_M - 2 * RAYON_G))
                all_obstacles.add(
                    Circle(HEIGHT_O - 4 * RAYON_G,  with_G, RAYON_G, True, WIDTH / 2, V_M, 0))
                all_switch.add(Star(H_E_M - 4 * RAYON_G))

            elif ran == 9:  # cercle + croix
                print("cercle + croix")
                all_switch.add(Switch(H_S))
                all_obstacles.add(
                    Circle(HEIGHT_O,  with_G, RAYON_T, False, WIDTH / 2, V_M, 0))
                all_obstacles.add(
                    Cross((WIDTH / 2) - 20, HEIGHT_O,  with_G, 50, -V_G, 0))
                all_switch.add(Star(H_E-RAYON_T/2))

            elif ran == 10:  # croix
                print("croix")
                all_switch.add(Switch(H_S))
                all_obstacles.add(
                    Cross((WIDTH / 2) - RAYON_P, HEIGHT_O,  with_G, RAYON_P, -V_G, 0))
                all_switch.add(Star(H_E_M - RAYON_G))

            elif ran == 11:  # croix
                print("double croix")
                all_switch.add(Switch(H_S))
                all_obstacles.add(
                    Cross((WIDTH / 2) - 1.5 * RAYON_P, HEIGHT_O,  with_G, RAYON_P, -V_G, 0))
                all_obstacles.add(
                    Cross((WIDTH / 2) + 1.5 * RAYON_P, HEIGHT_O,  with_G, RAYON_P, V_G, 1))
                all_switch.add(Star(H_E - RAYON_P))
            elif ran == 12:  # double cercle (1 petit et 1 grand)
                print("cercle cote a cote")
                # deux cercles cote à cote
                random_circle = random.randint(1, 2)
                if random_circle == 1:
                    all_switch.add(Switch(H_S))
                    all_obstacles.add(
                        Circle(HEIGHT_O,  with_M, RAYON_P, True, (WIDTH / 2) - RAYON_P, V_M, 0))
                    all_obstacles.add(
                        Circle(HEIGHT_O,  with_G, RAYON_G, False, (WIDTH / 2) + RAYON_G, V_M, 1))
                    all_switch.add(Star(H_E))
                else:
                    all_switch.add(Switch(H_S))
                    all_obstacles.add(
                        Circle(HEIGHT_O,  with_G, RAYON_G, True, (WIDTH / 2) - RAYON_G, V_M, 1))
                    all_obstacles.add(
                        Circle(HEIGHT_O,  with_M, RAYON_P, False, (WIDTH / 2) + RAYON_P, V_M, 0))
                    all_switch.add(Star(H_E))
            elif ran == 13:
                    all_switch.add(Switch(H_S))
                    all_obstacles.add(Triangle(HEIGHT_O, with_G, RAYON_M, V_G))
                    all_switch.add(Star(H_E_M))


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
