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


def updateScreen(screen, sprites, font):
    print("UpdateScreen")
    sprites.update()
    font.update()
    screen.fill(WHITE)
    font.draw(screen)
    sprites.draw(screen)
