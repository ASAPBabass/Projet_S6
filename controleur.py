#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import random
import sys
from math import pi

import pygame
import pygame.gfxdraw
from pygame.locals import *

from Modele.modele import *
from Vue.vue import *


def menu():

    end = False

    # Evenements
    while not end:

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    end = True
                else:
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            return False
                        if event.key == K_ESCAPE:
                            end = True

        except Exception:
            print("Erreur Menu !")

        return True


def retry(view):
    end = False
    view.retry(view.player)

    # Evenements
    while not end:

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return True
                else:
                    if event.type == KEYDOWN:
                        if event.key == K_RETURN:
                            return False
                        if event.key == K_ESCAPE:
                            return True

        except Exception:
            print("Erreur Retry !")


def main():
    # initialisation

    player = Player()

    view = View(player)  # on ajoute le player dans la Vue

    # cercle = Circle(player)

    # view.all_obstacles.add(cercle)  # on ajoute le cercle dans la Vue
    # view.all_sprites.add(cercle)

    end_menu = False
    end = False  # variable d'arret
    son = None

    # Evenements
    while not end_menu:

        view.menu()

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    view.quit()
                else:
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            # theme = pygame.mixer.Sound('colorswitch.wav')
                            # theme.set_volume(1.0)
                            # son = theme.play(-1)
                            end_menu = True
                        if event.key == K_ESCAPE:
                            view.quit()

        except Exception:
            print("Erreur Menu !")

    end2 = False
    pause = False
    # pygame.mixer.music.play(loops=-1)
    while not end2:
        # Evenements
        while not end:

            try:

                for event in pygame.event.get():
                    if event.type == QUIT:
                        quit()
                    else:

                        # while son.get_busy():
                        #    pygame.time.delay(100)

                        if event.type == KEYDOWN:
                            if event.key == K_SPACE:
                                sound_jump = pygame.mixer.Sound(
                                    '/home/bastien/Documents/Project/SwitchColor/Vue/Sounds/jump.wav')
                                sound_jump.play()
                                # mixer.music.load('colorswitch.wav')

                                for i in range(7):
                                    player.jump(9)
                                    # view.all_sprites.update()
                                    if collisions(player, view.all_obstacles, view.all_switch):
                                        end = True
                                        break
                                    view.update()
                                    # cercle.collisions(player)
                                    view.scroll()
                                    view.draw()

                                player.jump(10)

                                obstacles(
                                    player, view.all_obstacles, view.all_switch)

                            if event.key == K_ESCAPE:
                                if pause:
                                    pause = False
                                else:
                                    pause = True

            except Exception:
                print("Erreur !")

            if not pause:
                # print(cercle.rect.y)
                # update
                view.update()

                # on verifie les collisions
                end = collisions(player, view.all_obstacles, view.all_switch)

                """
                get_list = view.all_obstacles.sprites()
                if(len(get_list) > 1):
                    print(get_list[-1].rect.x, get_list[-1].rect.y)
                """
                view.scroll()
                # print(player.rect.x, player.rect.y)
                # obstacles(player, view.all_obstacles)

                # draw/render
                view.draw()  # met à jour l'ecran et affiche les sprites
            else:  # jeu en pause
                view.pause()
        # temporaire
        if(player.bestScore < player.score):
            player.bestScore = player.score
        if not retry(view):
            view = View(player)
            end = False
        else:
            end2 = True


if __name__ == '__main__':
    main()
    quit()
