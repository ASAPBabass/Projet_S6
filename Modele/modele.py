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

WHITE = (254, 254, 254)
BLACK = (0, 0, 0)
BLUE = (54, 225, 243)
PURPLE = (141, 19, 250)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (247, 222, 15)
ROSE = (252, 2, 128)
GREY = (41, 41, 41)

colors = (BLUE, YELLOW, PURPLE, ROSE)


class Player(pygame.sprite.Sprite):  # class du joueur

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.color = random.choice(colors)  # couleur aleatoire
        self.image = None
        self.score = 0
        self.mask = None

    def initialization(self):
        self.color = random.choice(colors)  # couleur aleatoire
        self.image = pygame.Surface([20, 20]).convert_alpha()
        self.image.fill((0, 0, 0, 0))  # fond transparent
        pygame.gfxdraw.filled_circle(self.image, 9, 9, 9, self.color)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (640 / 2, 150)

    def jump(self, jump):
        self.rect.y -= jump

    def update(self):  # gravite
        if self.rect.y < 2000:
            self.rect.y += 6


class Arc(pygame.sprite.Sprite):

    def __init__(self, color, rect, start_angle, stop_angle, width):
        pygame.sprite.Sprite.__init__(self)
        self.i = 1
        self.color = color
        self.image = pygame.Surface([200, 200]).convert_alpha()
        self.image.fill((0, 0, 0, 0))
        self.rect = rect
        self.mask = None
        self.update(start_angle, stop_angle, width)

    def update(self, start_angle, stop_angle, width):
        self.image.fill((0, 0, 0, 0))
        rect_bis = self.rect.move(0, 1)
        arc_1 = pygame.draw.arc(
            self.image, self.color, self.rect, start_angle, stop_angle, width)
        arc_2 = pygame.draw.arc(
            self.image, self.color, rect_bis, start_angle, stop_angle, width)

        # anti-aliasing
        # pygame.gfxdraw.aacircle(
         #   self.image, arc_2.x, arc_2.y, 199, GREY)

        self.rect.center = (100, 100)
        self.mask = pygame.mask.from_surface(self.image)


class Circle(pygame.sprite.Sprite):  # TODO

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([200, 200]).convert()
        self.rect = self.image.get_rect()
        self.rect.y = 200

        self.i = 0  # vitesse de rotatio
        self.scroll = 0  # permet le scrolling

        self.all_arcs = pygame.sprite.Group()

        self.star = Star(self.rect)
        # self.rect = self.rect.clamp(self.star.rect)

        self.arc_1 = Arc(
            PURPLE, self.rect, 0 + self.i, pi / 2 + self.i, 15)
        self.arc_2 = Arc(
            YELLOW, self.rect, pi / 2 + self.i, pi + self.i, 15)
        self.arc_3 = Arc(
            BLUE, self.rect, pi + self.i, 3 * pi / 2 + self.i, 15)
        self.arc_4 = Arc(
            ROSE, self.rect, 3 * pi / 2 + self.i, 2 * pi + self.i, 15)

        self.all_arcs.add(self.arc_1)
        self.all_arcs.add(self.arc_2)
        self.all_arcs.add(self.arc_3)
        self.all_arcs.add(self.arc_4)

        self.all_arcs.add(self.star)
        self.rect.center = (640 / 2, self.rect.y)

        # self.image.fill((0, 0, 0, 0))
        self.image.fill((41, 41, 41))

    def update(self):
        # self.image.fill((0, 0, 0, 0))
        self.image.fill((41, 41, 41))

        self.i += 0.02  # vitesse de rotation

        self.arc_1.update(0 + self.i, pi / 2 + self.i, 15)
        self.arc_1.update(0 + self.i, pi / 2 + self.i, 15)
        self.arc_2.update(pi / 2 + self.i, pi + self.i, 15)
        self.arc_3.update(pi + self.i, 3 * pi / 2 + self.i, 15)
        self.arc_4.update(3 * pi / 2 + self.i, 2 * pi + self.i, 15)

        self.all_arcs.draw(self.image)

        self.rect.center = (640 / 2, self.rect.y + self.scroll)

    def collisions(self, player):
        color = player.color
        if pygame.sprite.collide_mask(player, self.arc_1) and color != self.arc_1.color:
            print("Collision couleur PURPLE")
        elif pygame.sprite.collide_mask(player, self.arc_2) and color != self.arc_2.color:
            print("Collision couleur YELLOW")
        elif pygame.sprite.collide_mask(player, self.arc_3) and color != self.arc_3.color:
            print("Collision couleur BLUE")
        elif pygame.sprite.collide_mask(player, self.arc_4) and color != self.arc_4.color:
            print("Collision couleur ROSE")
        elif player.rect.y < self.star.rect.y + self.rect.y + 45 and self.star.bool == False:  # collision temporaire
            self.star.image.fill((0, 0, 0, 0))
            player.score += 1
            self.star.bool = True

        else:
            pass
            # self.star.collide(player)


class Star(pygame.sprite.Sprite):

    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            "Vue/Image/star2.png").convert_alpha()
        self.rect = self.image.get_rect()  # correspond a la surface du cercle
        self.rect.move_ip(77, 80)  # permet de centrer l'etoile dans le
        # cercle
        self.mask = pygame.mask.from_surface(self.image)
        self.bool = False

    def update(self):
        pass

    def collide(self, player):
        if self.rect.colliderect(player):
            print("Collision Star")
        elif self.rect.contains(player.rect):
            print("Collision Star")
        elif self.rect.collidepoint(player.rect.center):
            print("Collision Star")
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
    p1 = Player()
    circle = Circle()
    print("Début de la partie")
    font.add(circle)
    player.add(p1)


def create_font(font):
    f = Circle()
    font.add(f)
    return font


def create_player(player):
    p = Player()
    player.add(p)
    return player
