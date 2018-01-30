#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import random
import sys
from math import pi

import pygame
import pygame.gfxdraw
import pygame.mask
from pygame.locals import *

WIDTH = 640
HEIGHT = 480

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

colors = (WHITE, BLACK, BLUE, RED, GREEN)


class Ball(pygame.sprite.Sprite):  # class du joueur

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image =
        # pygame.image.load("Vue/Image/redball.png").convert_alpha()
        self.color = random.choice(colors)  # couleur aleatoire
        self.image = pygame.Surface([20, 20]).convert_alpha()
        self.image.fill((0, 0, 0, 0))  # fond transparent
        pygame.gfxdraw.filled_circle(self.image, 9, 9, 9, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (640 / 2, 410)
        self.mask = pygame.mask.from_surface(self.image)

    def jump(self, jump):
        # print("jump")
        self.rect.y -= jump

    def update(self):  # gravite
        if self.rect.y < 410:
            self.rect.y += 2.5


class Arc(pygame.sprite.Sprite):

    def __init__(self, color, rect, start_angle, stop_angle, width):
        pygame.sprite.Sprite.__init__(self)
        self.i = 1
        self.color = color
        self.image = pygame.Surface([400, 400]).convert_alpha()
        self.image.fill((0, 0, 0, 0))
        # self.image.fill(BLACK)
        self.rect = rect
        pygame.draw.arc(
            self.image, color, self.rect, start_angle, stop_angle, width)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (100, 100)


class Circle(pygame.sprite.Sprite):  # TODO

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([200, 200]).convert_alpha()
        self.rect = self.image.get_rect()

        self.mask = None
        self.coord_3 = 75
        self.i = 1

        self.all_arcs = pygame.sprite.Group()

        self.arc_1 = None
        self.arc_2 = None
        self.arc_3 = None
        self.arc_4 = None

        self.initialization()

    def initialization(self):
        self.image.fill((0, 0, 0, 0))  # permet la transparence
        self.all_arcs.empty()  # on supprime les précedents sprites
        """
        pygame.draw.arc(
            self.image, WHITE, self.rect, 0 + self.i, pi / 2 + self.i, 6)
        pygame.draw.arc(
            self.image, GREEN, self.rect, pi / 2 + self.i, pi + self.i, 6)
        pygame.draw.arc(
            self.image, BLUE, self.rect, pi + self.i, 3 * pi / 2 + self.i, 6)
        pygame.draw.arc(
            self.image, RED,  self.rect, 3 * pi / 2 + self.i, 2 * pi + self.i, 6)
        """
        self.arc_1 = Arc(
            WHITE, self.rect, 0 + self.i, pi / 2 + self.i, 6)

        self.arc_2 = Arc(
            GREEN, self.rect, pi / 2 + self.i, pi + self.i, 6)
        self.arc_3 = Arc(
            BLUE, self.rect, pi + self.i, 3 * pi / 2 + self.i, 6)
        self.arc_4 = Arc(
            RED, self.rect, 3 * pi / 2 + self.i, 2 * pi + self.i, 6)

        self.all_arcs.add(self.arc_1)
                          # on ajoute les arcs au groupe de sprites

        self.all_arcs.add(self.arc_2)
        self.all_arcs.add(self.arc_3)
        self.all_arcs.add(self.arc_4)

        self.all_arcs.draw(self.image)
                           # on affiche les arcs pour former le cercle

        self.rect.center = (640 / 2, 200)  # on recentre la surface

        self.mask = pygame.mask.from_surface(
            self.image)  # permet de gerer au mieux les collisions

    def update(self):
        self.coord_3 += 1
        self.i += 0.02  # vitesse de rotation
        self.initialization()

    def set(self):
        self.coord_3 = 75

    def collisions(self, ball):
        color = ball.color
        if pygame.sprite.collide_mask(ball, self.arc1) and color != self.arc_1.color:
            print("Collision couleur WHITE")
        elif pygame.sprite.collide_mask(ball, self.arc2) and color != self.arc_2.color:
            print("Collision couleur GREEN")
        elif pygame.sprite.collide_mask(ball, self.arc3) and color != self.arc_3.color:
            print("Collision couleur BLUE")
        elif pygame.sprite.collide_mask(ball, self.arc4) and color != self.arc_4.color:
            print("Collision couleur RED")
        else:
            pass


class Ligne(pygame.sprite.Sprite):  # TODO

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([WIDTH, 400]).convert_alpha()
        self.rect = None

        self.w_green_1 = 426
        self.w_green_2 = 640
        self.w_red_1 = 0
        self.w_red_2 = 213
        self.w_blue_1 = 213
        self.w_blue_2 = 426

        self.speed = 2

        self.initialization()

    def initialization(self):
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()

        pygame.draw.lines(
            self.image, BLUE, False, [[self.w_blue_1, 400], [self.w_blue_2, 400]], 6)
        pygame.draw.lines(
            self.image, GREEN, False, [[self.w_green_1, 400], [self.w_green_2, 400]], 6)
        pygame.draw.lines(
            self.image, RED, False, [[self.w_red_1, 400], [self.w_red_2, 400]], 6)
        pygame.draw.lines(
            self.image, BLUE, False, [[self.w_blue_1, 400], [self.w_blue_2, 400]], 6)

        self.rect.center = (0, 350)

    def update(self):
        # print("update ligne")
        self.initialization()

    def incremente(self, width):
        if width < 640:
            return width + 1
        # else:
         #   return 0


def start(player, font):
    print("Début de la partie")
    p1 = Ball()
    circle = Circle()
    print("Début de la partie")
    font.add(circle)
    player.add(p1)


def create_font(font):
    f = Circle()
    font.add(f)
    return font


def create_player(player):
    p = Ball()
    player.add(p)
    return player
