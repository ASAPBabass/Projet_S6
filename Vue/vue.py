#!/usr/bin/python
#-*- coding: utf-8 -*-

from math import pi
import pygame as py
import pygame.gfxdraw
from pygame.locals import *

WIDTH = 640
HEIGHT = 480
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


def ligne(l):
    if l < 640:
        return l + 1
    else:
        return 0


def createScreen():
    screen = py.display.set_mode((WIDTH, HEIGHT))
    py.display.set_caption("SwitchColor")
    clock = py.time.Clock()
    py.key.set_repeat(400, 30)
    screen.fill(BLACK)
    py.display.flip()  # met à jour la fenetre
    clock.tick(60)

    return screen


def startScreen(sprites):

    screen = py.display.set_mode((WIDTH, HEIGHT))
    py.display.set_caption("SwitchColor")
    clock = py.time.Clock()
    py.key.set_repeat(400, 30)

    coord = 75
    coord1 = 75
    coord2 = 75
    coord3 = 75
    i = 1
    # parametrage des lignes mutlicolor
    wgreen = 426
    wred = 0
    wblue = 213

    wgreen2 = 640
    wred2 = 213
    wblue2 = 426

    # Update
    sprites.update()  # met a jour tous les sprites

    # Draw / render
    screen.fill(BLACK)
    # screen.blit(background,(0,0))
    sprites.draw(screen)  # affiche tous les sprites

    # cercle multicolor
    py.draw.arc(
        screen, WHITE, [320, coord2, coord + i, coord1 + i], 0 + i, pi / 2 + i, 2)
    py.draw.arc(
        screen, GREEN, [320, coord2, coord + i, coord1 + i], pi / 2 + i, pi + i, 2)
    py.draw.arc(
        screen, BLUE, [320, coord2, coord + i, coord1 + i], pi + i, 3 * pi / 2 + i, 2)
    py.draw.arc(
        screen, RED,  [320, coord2, coord + i, coord1 + i], 3 * pi / 2 + i, 2 * pi + i, 2)

    py.draw.arc(
        screen, WHITE, [100, coord2, coord, coord1], 0 + i, pi / 2 + i, 10)
    py.draw.arc(
        screen, GREEN, [100, coord2, coord, coord1], pi / 2 + i, pi + i, 10)
    py.draw.arc(
        screen, BLUE, [100, coord2, coord, coord1], pi + i, 3 * pi / 2 + i, 10)
    py.draw.arc(
        screen, RED,  [100, coord2, coord, coord1], 3 * pi / 2 + i, 2 * pi + i, 10)

    # pygame.draw.lines(screen, RED, False, [[0, 80], [50, 90], [200, 80],
    # [220, 30]], 5)

    # pygame.draw.aaline(screen, GREEN, [0, 400],[640, 400], True) #
    # [width,height] to [width,height] une ligne

    # ligne multicolor
    wblue = ligne(wblue)
    wblue2 = ligne(wblue2)
    wgreen = ligne(wgreen)
    wgreen2 = ligne(wgreen2)
    wred = ligne(wred)
    wred2 = ligne(wred2)

    # pygame.draw.lines(screen, GREEN, False, [[426,400],[640,400]],6)
    py.draw.lines(screen, BLUE, False, [[wblue, 400], [wblue2, 400]], 6)
    py.draw.lines(screen, GREEN, False, [[wgreen, 400], [wgreen2, 400]], 6)
    py.draw.lines(screen, RED, False, [[wred, 400], [wred2, 400]], 6)
    py.draw.lines(screen, BLUE, False, [[wblue, 400], [wblue2, 400]], 6)

    # pygame.draw.lines(screen, RED, False, [[400-l,400],[400,400]],6)

    # pygame.draw.lines(screen, GREEN, False, [[600,300],[10,300]],6)
    # py.gfxdraw.line(screen, 600, 300, 10, 300, GREEN)
    # pygame.gfxdraw.hline(screen,50,200,300,RED)

    center = [150, 200]
    # pygame.gfxdraw.aacircle(screen, center[0], center[1], 105, WHITE)
    # pygame.gfxdraw.aacircle(screen, center[0], center[1], 120, WHITE)
    # pygame.draw.arc(screen,RED, [30,70,240,245],0+i, pi/2+i, 20)

    coord = 200
    coord1 = 200
    i += 0.02

    # Flip
    py.display.flip()  # met à jour la fenetre
    clock.tick(60)

    return screen
