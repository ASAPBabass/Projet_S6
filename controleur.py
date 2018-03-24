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
from Modele.constantes import *
from Vue.vue import *


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

    end_menu = False
    end = False  # variable d'arret

    menu(view.all_sprites)
    view.menu()
    # Evenements
    while not end_menu:
        space = False  # vrai si le joueur appuie sur la touche espace
        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    view.quit()
                else:
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            # musique de fond du jeu
                            pygame.mixer.music.load(
                                '/home/bastien/Documents/Project/SwitchColor/Vue/Sounds/gameTheme.mp3')
                            pygame.mixer.music.play(-1)
                            view.all_sprites.empty()
                            end_menu = True

                        if event.key == K_ESCAPE:
                            view.quit()

                if event.type == MOUSEBUTTONDOWN or space:
                    # musique de fond du jeu
                    pygame.mixer.music.load(
                        '/home/bastien/Documents/Project/SwitchColor/Vue/Sounds/gameTheme.mp3')
                    pygame.mixer.music.play(-1)
                    view.all_sprites.empty()
                    end_menu = True

            view.update_menu()
            view.draw_menu()

        except Exception:
            print("Erreur Menu !")

    end2 = False
    pause = False

    while not end2:

        view.all_sprites.add(player)
        # Evenements
        while not end:
            space = False  # touche espace
            try:

                for event in pygame.event.get():

                    if event.type == QUIT:
                        quit()
                    else:

                        if event.type == KEYDOWN:

                            if event.key == K_ESCAPE:
                                if pause:
                                    pause = False
                                else:
                                    pause = True
                            if event.key == K_SPACE:
                                jump(player, view)

                if event.type == MOUSEBUTTONDOWN:  # si le joueur appuie sur la touche espace ou la souris
                    s_x, s_y = pygame.mouse.get_pos()
                    if s_y < HEIGHT / 2:
                        jump(player, view)
                    else:
                        player.switch()

            except Exception:
                print("Erreur !")

            if not pause:
                # update
                view.update()

                # on verifie les collisions
                end = collisions(player, view.all_obstacles, view.all_switch)

                view.scroll()

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


def jump(player, view):
    sound_jump = pygame.mixer.Sound(
        '/home/bastien/Documents/Project/SwitchColor/Vue/Sounds/jump.wav')
    sound_jump.play()

    for i in range(7):
        player.jump(9)
        if collisions(player, view.all_obstacles, view.all_switch):
            end = True
            break
        view.update()
        view.scroll()
        view.draw()

    player.jump(10)

    # permet d'ajouter une figure si le joueur
    # saute assez haut
    obstacles(
        player, view.all_obstacles, view.all_switch)

if __name__ == '__main__':
    main()
    quit()
