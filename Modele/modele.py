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
        self.bestScore = 0
        self.mask = None

    def initialization(self):
        self.color = random.choice(colors)  # couleur aleatoire
        self.image = pygame.Surface([20, 20]).convert_alpha()
        self.image.fill((0, 0, 0, 0))  # fond transparent
        pygame.gfxdraw.aacircle(
            self.image, 9, 9, 9, self.color)  # anti aliasing
        pygame.gfxdraw.filled_circle(self.image, 9, 9, 9, self.color)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (640 / 2, 150)

    def jump(self, jump):
        self.rect.y -= jump

    def update(self):  # gravite
        pygame.gfxdraw.aacircle(self.image, 9, 9, 9, self.color)
        pygame.gfxdraw.filled_circle(self.image, 9, 9, 9, self.color)

        if self.rect.y < 2000:
            self.rect.y += 7.5

    def switch(self):
        self.color = random.choice(colors)  # couleur aleatoire


class Switch(pygame.sprite.Sprite):  # class du joueur

    def __init__(self, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            "Vue/Image/switch4.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, pos_y)
        self.mask = None
        self.pos_y = pos_y
        self.scroll = 0
        self.bool = False

    def update(self):
        self.rect.center = (WIDTH / 2, self.pos_y + self.scroll)
        # self.rect.y = self.pos.y + self.scroll
        self.mask = pygame.mask.from_surface(self.image)

    def collide(self, player):
        if player.rect.y - 35 < self.rect.y and self.bool == False:
            player.switch()
            print("collision avec le switch")
            self.image.fill((0, 0, 0, 0))
            self.bool = True


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

    def __init__(self, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([200, 200]).convert()
        self.rect = self.image.get_rect()
        pygame.gfxdraw.aacircle(self.image, 100, 100, 101, BLACK)
        # self.rect.y = -height
        self.height = height

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
        self.rect.center = (640 / 2, self.height)

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
        # anti aliasing
        pygame.gfxdraw.aacircle(self.image, 100, 100, 102, GREY)
        pygame.gfxdraw.aacircle(self.image, 100, 100, 101, GREY)
        # pygame.gfxdraw.aacircle(self.image, 100, 100, 100, GREY)
        pygame.gfxdraw.aacircle(self.image, 100, 100, 85, GREY)
        pygame.gfxdraw.aacircle(self.image, 100, 100, 84, GREY)

        # self.rect.move_ip(640 / 2, self.rect.y + self.scroll)
        # print(str(self.rect.y) + "  " + str(self.scroll))
        self.rect.center = (640 / 2, self.height + self.scroll)

    def collide(self, player):
        color = player.color
        if pygame.sprite.collide_mask(player, self.arc_1) and color != self.arc_1.color:
            print("Collision couleur PURPLE")
            return True
        elif pygame.sprite.collide_mask(player, self.arc_2) and color != self.arc_2.color:
            print("Collision couleur YELLOW")
            return True
        elif pygame.sprite.collide_mask(player, self.arc_3) and color != self.arc_3.color:
            print("Collision couleur BLUE")
            return True
        elif pygame.sprite.collide_mask(player, self.arc_4) and color != self.arc_4.color:
            print("Collision couleur ROSE")
            return True
        elif player.rect.y < self.star.rect.y + self.rect.y + 45 and self.star.bool == False:  # collision temporaire
            self.star.image.fill((0, 0, 0, 0))
            player.score += 1
            self.star.bool = True

        else:
            pass
            # self.star.collide(player)

class Point:

    def __init__(self,a,b):
        self.x=a
        self.y=b

class Square(pygame.sprite.Sprite):

    def __init__(self, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([200, 200]).convert()
        self.rect = self.image.get_rect()
        self.height = height

        self.angle = 0  # vitesse de rotatio
        self.scroll = 0  # permet le scrolling

        #self.all_arcs = pygame.sprite.Group()
        #self.star = Star(self.rect)
        self.O=Point(100,100)
        self.A=Point(0,0)
        self.B=Point(0,0)
        self.C=Point(0,0)
        self.D=Point(0,0)
        self.rayon= 70

        self.angleRadian = pi * self.angle / 180
    
        self.angleRadian2 = pi * (self.angle+90) / 180

        self.angleRadian3 = pi * (self.angle+180) / 180
        
        self.angleRadian4 = pi * (self.angle+270) / 180

        self.rect.center = (640 / 2, self.height)

        # self.image.fill((0, 0, 0, 0))
        # self.image.fill((41, 41, 41))

    def update(self):
        
        self.image.fill((41, 41, 41))
        self.angle += 0.5  # vitesse de rotation
        self.angleRadian = pi * self.angle / 180
    
        self.angleRadian2 = pi * (self.angle+90) / 180

        self.angleRadian3 = pi * (self.angle+180) / 180
        
        self.angleRadian4 = pi * (self.angle+270) / 180
        self.A.x= self.O.x + self.rayon* cos(self.angleRadian) - self.rayon * sin(self.angleRadian)
        self.A.y= self.O.y + self.rayon * sin(self.angleRadian) + self.rayon * cos(self.angleRadian)

        self.B.x= self.O.x + self.rayon * cos(self.angleRadian2) - self.rayon * sin(self.angleRadian2)
        self.B.y= self.O.y+ self.rayon * sin(self.angleRadian2) + self.rayon * cos(self.angleRadian2)

        self.C.x= self.O.x + self.rayon * cos(self.angleRadian3) - self.rayon * sin(self.angleRadian3)
        self.C.y= self.O.y + self.rayon * sin(self.angleRadian3) + self.rayon * cos(self.angleRadian3)

        self.D.x= self.O.x + self.rayon * cos(self.angleRadian4) - self.rayon * sin(self.angleRadian4)
        self.D.y= self.O.y + self.rayon * sin(self.angleRadian4) + self.rayon * cos(self.angleRadian4)

        pygame.draw.line(self.image, YELLOW, (250, 250), (250, 250), 5)
        pygame.draw.line(self.image, YELLOW, (self.A.x, self.A.y), (self.B.x, self.B.y), 15)
        pygame.draw.line(self.image, BLUE, (self.B.x, self.B.y), (self.C.x, self.C.y), 15)
        pygame.draw.line(self.image, ROSE, (self.C.x, self.C.y), (self.D.x, self.D.y), 15)
        pygame.draw.line(self.image, PURPLE, (self.D.x, self.D.y), (self.A.x, self.A.y), 15)

        self.rect.center = (640 / 2, self.height + self.scroll)
        

    def collide(self, player):
        pass


class Star(pygame.sprite.Sprite):

    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            "Vue/Image/star3.png").convert_alpha()
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


def obstacles(player, all_obstacles, all_switch):
    list_obstacles = all_obstacles.sprites()
    nb = len(list_obstacles)
    if nb == 0:
        print("Creation du 1er obstacle")
        # all_obstacles.add(Switch(100))
        caree=Square(-150)
        all_switch.add(Switch(100))
        all_obstacles.add(caree)
    else:
        if list_obstacles[-1].rect.y > player.rect.y:
            # all_obstacles.add(Switch(-50))
            all_switch.add(Switch(100))
            all_obstacles.add(Circle(- 150))


def collisions(player, all_obstacles, all_switch):
    pass
    
    die = False
    for switch in all_switch:
        switch.collide(player)
    for obstacle in all_obstacles:
        if obstacle.collide(player):
            return True
    