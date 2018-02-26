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


class Point:

    def __init__(self, a, b):
        self.x = a
        self.y = b


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
        self.image = pygame.Surface([200, 200]).convert_alpha()
        self.image.fill((0, 0, 0, 0))
        self.rect = rect
        self.i = 1
        self.color = color
        self.mask = None
        self.update(start_angle, stop_angle, width)

    def update(self, start_angle, stop_angle, width):
        self.image.fill((0, 0, 0, 0))
        rect_bis = self.rect.move(0, 1)
        pygame.draw.arc(
            self.image, self.color, self.rect, start_angle, stop_angle, width)
        pygame.draw.arc(
            self.image, self.color, rect_bis, start_angle, stop_angle, width)

        # anti-aliasing
        # pygame.gfxdraw.aacircle(
        #   self.image, arc_2.x, arc_2.y, 199, GREY)

        self.rect.center = (100, 100)
        self.mask = pygame.mask.from_surface(self.image)


class Arete(pygame.sprite.Sprite):

    def __init__(self, rect, a, b, color, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([300, 300]).convert_alpha()
        self.image.fill((0, 0, 0, 0))
        self.rect = rect
        self.color = color
        self.mask = pygame.mask.from_surface(self.image)
        self.width = width

    def update(self, a, b):
        self.image.fill((0, 0, 0, 0))
        """
        pygame.draw.line(
            self.image, self.color, (a.x + 1, a.y - 1), (b.x - 1, b.y - 1), 1)
        """
        pygame.draw.line(
            self.image, self.color, (a.x, a.y), (b.x, b.y), self.width)

        """
        pygame.draw.line(
            self.image, self.color, (a.x, a.y + self.width), (b.x, b.y + self.width), 1)
        """
        self.rect.center = (150, 150)

        self.mask = pygame.mask.from_surface(self.image)


class Cross(pygame.sprite.Sprite):  # TODO

    def __init__(self, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([300, 300]).convert()
        self.rect = self.image.get_rect()
        self.image.fill((0, 0, 0, 0))
        self.height = height
        self.all_aretes = pygame.sprite.Group()

        self.angle = 0  # vitesse de rotatio
        self.scroll = 0  # permet le scrolling

        self.rect_1 = None
        self.rect_2 = None
        self.rect_3 = None
        self.rect_4 = None

        self.O = Point(150, 150)  # centre
        self.A = Point(0, 0)
        self.B = Point(0, 0)
        self.C = Point(0, 0)
        self.D = Point(0, 0)
        self.rayon = 70

        self.angleRadian = pi * self.angle / 180

        self.angleRadian2 = pi * (self.angle + 90) / 180

        self.angleRadian3 = pi * (self.angle + 180) / 180

        self.angleRadian4 = pi * (self.angle + 270) / 180

        self.arete_1 = Arete(
            self.rect, self.A, self.O, YELLOW, 20)
        self.arete_2 = Arete(
            self.rect, self.B, self.O, BLUE, 20)
        self.arete_3 = Arete(
            self.rect, self.C, self.O, ROSE, 20)
        self.arete_4 = Arete(
            self.rect, self.D, self.O, PURPLE, 20)

        self.all_aretes.add(self.arete_2)
        self.all_aretes.add(self.arete_3)
        self.all_aretes.add(self.arete_4)
        self.all_aretes.add(self.arete_1)

        self.rect.center = (640 / 2, self.height)

    def update(self):

        self.image.fill((41, 41, 41))
        self.angle += 1  # vitesse de rotation
        self.angleRadian = pi * self.angle / 180

        self.angleRadian2 = pi * (self.angle + 90) / 180

        self.angleRadian3 = pi * (self.angle + 180) / 180

        self.angleRadian4 = pi * (self.angle + 270) / 180

        self.A.x = self.O.x + self.rayon * \
            cos(self.angleRadian) - self.rayon * sin(self.angleRadian)
        self.A.y = self.O.y + self.rayon * \
            sin(self.angleRadian) + self.rayon * cos(self.angleRadian)

        self.B.x = self.O.x + self.rayon * \
            cos(self.angleRadian2) - self.rayon * sin(self.angleRadian2)
        self.B.y = self.O.y + self.rayon * \
            sin(self.angleRadian2) + self.rayon * cos(self.angleRadian2)

        self.C.x = self.O.x + self.rayon * \
            cos(self.angleRadian3) - self.rayon * sin(self.angleRadian3)
        self.C.y = self.O.y + self.rayon * \
            sin(self.angleRadian3) + self.rayon * cos(self.angleRadian3)

        self.D.x = self.O.x + self.rayon * \
            cos(self.angleRadian4) - self.rayon * sin(self.angleRadian4)
        self.D.y = self.O.y + self.rayon * \
            sin(self.angleRadian4) + self.rayon * cos(self.angleRadian4)

        self.arete_2.update(self.B, self.O)
        self.arete_3.update(self.C, self.O)
        self.arete_4.update(self.D, self.O)
        self.arete_1.update(self.A, self.O)

        self.all_aretes.draw(self.image)

        self.rect.center = (640 / 2 + 50, self.height + self.scroll)

    def collide(self, player):
        color = player.color
        if pygame.sprite.collide_mask(player, self.arete_1) and color != self.arete_1.color:
            print("Collision couleur YELLOW")
            return True
        elif pygame.sprite.collide_mask(player, self.arete_2) and color != self.arete_2.color:
            print("Collision couleur BLUE")
            return True
        elif pygame.sprite.collide_mask(player, self.arete_3) and color != self.arete_3.color:
            print("Collision couleur ROSE")
            return True
        elif pygame.sprite.collide_mask(player, self.arete_4) and color != self.arete_4.color:
            print("Collision couleur PURPLE")
            return True
        else:
            pass
        """
        elif player.rect.y < self.star.rect.y + self.rect.y + 45 and self.star.bool == False:  # collision temporaire
            self.star.image.fill((0, 0, 0, 0))
            player.score += 1
            self.star.bool = True
        """


class Circle(pygame.sprite.Sprite):

    def __init__(self, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([200, 200]).convert()
        self.rect = self.image.get_rect()
        pygame.gfxdraw.aacircle(self.image, 100, 100, 101, BLACK)
        self.height = height

        self.i = 0  # vitesse de rotatio
        self.scroll = 0  # permet le scrolling

        self.all_arcs = pygame.sprite.Group()

        self.star = Star()
        self.star.circle()

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

        self.image.fill((41, 41, 41))

    def update(self):
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


class Square(pygame.sprite.Sprite):

    def __init__(self, height):
        try:
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([300, 300]).convert()
            self.rect = self.image.get_rect()
            self.image.fill((0, 0, 0, 0))
            self.height = height

            self.angle = 0  # vitesse de rotatio
            self.scroll = 0  # permet le scrolling

            self.all_aretes = pygame.sprite.Group()
            self.star = Star()
            self.star.square()
            self.O = Point(150, 150)  # centre
            self.A = Point(0, 0)
            self.B = Point(0, 0)
            self.C = Point(0, 0)
            self.D = Point(0, 0)
            self.rayon = 80

            self.angleRadian = pi * self.angle / 180

            self.angleRadian2 = pi * (self.angle + 90) / 180

            self.angleRadian3 = pi * (self.angle + 180) / 180

            self.angleRadian4 = pi * (self.angle + 270) / 180

            self.arete_1 = Arete(
                self.rect, self.A, self.B, YELLOW, 20)
            self.arete_2 = Arete(
                self.rect, self.B, self.C, BLUE, 20)
            self.arete_3 = Arete(
                self.rect, self.C, self.D, ROSE, 20)
            self.arete_4 = Arete(
                self.rect, self.D, self.A, PURPLE, 20)

            self.all_aretes.add(self.arete_2)
            self.all_aretes.add(self.arete_3)
            self.all_aretes.add(self.arete_4)
            self.all_aretes.add(self.arete_1)

            self.all_aretes.add(self.star)

            self.rect.center = (640 / 2, self.height)

        except Exception:
            print("erreur constructeur")

        # self.image.fill((0, 0, 0, 0))
        # self.image.fill((41, 41, 41))

    def update(self):

        self.image.fill((41, 41, 41))
        self.angle += 0.9  # vitesse de rotation
        self.angleRadian = pi * self.angle / 180

        self.angleRadian2 = pi * (self.angle + 90) / 180

        self.angleRadian3 = pi * (self.angle + 180) / 180

        self.angleRadian4 = pi * (self.angle + 270) / 180
        self.A.x = self.O.x + self.rayon * \
            cos(self.angleRadian) - self.rayon * sin(self.angleRadian)
        self.A.y = self.O.y + self.rayon * \
            sin(self.angleRadian) + self.rayon * cos(self.angleRadian)

        self.B.x = self.O.x + self.rayon * \
            cos(self.angleRadian2) - self.rayon * sin(self.angleRadian2)
        self.B.y = self.O.y + self.rayon * \
            sin(self.angleRadian2) + self.rayon * cos(self.angleRadian2)

        self.C.x = self.O.x + self.rayon * \
            cos(self.angleRadian3) - self.rayon * sin(self.angleRadian3)
        self.C.y = self.O.y + self.rayon * \
            sin(self.angleRadian3) + self.rayon * cos(self.angleRadian3)

        self.D.x = self.O.x + self.rayon * \
            cos(self.angleRadian4) - self.rayon * sin(self.angleRadian4)
        self.D.y = self.O.y + self.rayon * \
            sin(self.angleRadian4) + self.rayon * cos(self.angleRadian4)

        self.arete_1.update(self.A, self.B)
        self.arete_2.update(self.B, self.C)
        self.arete_3.update(self.C, self.D)
        self.arete_4.update(self.D, self.A)

        self.all_aretes.draw(self.image)

        self.rect.center = (640 / 2, self.height + self.scroll)

    def collide(self, player):
        color = player.color
        if pygame.sprite.collide_mask(player, self.arete_1) and color != self.arete_1.color:
            print("Collision couleur YELLOW")
            return True
        elif pygame.sprite.collide_mask(player, self.arete_2) and color != self.arete_2.color:
            print("Collision couleur BLUE")
            return True
        elif pygame.sprite.collide_mask(player, self.arete_3) and color != self.arete_3.color:
            print("Collision couleur ROSE")
            return True
        elif pygame.sprite.collide_mask(player, self.arete_4) and color != self.arete_4.color:
            print("Collision couleur PURPLE")
            return True
        else:
            pass


class Star(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            "Vue/Image/star3.png").convert_alpha()
        self.rect = self.image.get_rect()  # correspond a la surface du cercle
        # self.rect.move_ip(77, 80)  # permet de centrer l'etoile dans le
        # cercle
        # self.rect.center = (WIDTH / 2, -50)
        self.mask = pygame.mask.from_surface(self.image)
        self.bool = False
        self.scroll = 0

    def update(self):
        self.rect.center = (WIDTH / 2, self.rect.y + self.scroll)
        self.mask = pygame.mask.from_surface(self.image)

    def circle(self):
        self.rect.move_ip(77, 80)  # permet de centrer l'etoile dans le
        # cercle
        self.mask = pygame.mask.from_surface(self.image)

    def square(self):
        self.rect.move_ip(125, 125)  # permet de centrer l'etoile dans le
        # cercle
        self.mask = pygame.mask.from_surface(self.image)

    def ligne(self):
        self.rect.move_ip(205, 250)  # permet de centrer l'etoile dans le
        # cercle
        self.mask = pygame.mask.from_surface(self.image)

    def collide(self, player):
        pass


class Rectangle(pygame.sprite.Sprite):

    def __init__(self, rect, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height]).convert_alpha()
        self.rect = self.image.get_rect()
        self.color = color
        self.image.fill(color)
        self.mask = pygame.mask.from_surface(self.image)
        self.debordement = False

    def update(self):
        self.rect.x += 4  # vitesse de defilement
        self.mask = pygame.mask.from_surface(self.image)


class Ligne(pygame.sprite.Sprite):  # TODO

    def __init__(self, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([WIDTH, 100]).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill((0, 0, 0, 0))
        self.height = height
        self.scroll = 0
        self.star = None
        self.mask = pygame.mask.from_surface(self.image)
        self.all_rect = pygame.sprite.OrderedUpdates()

        if(height == 150):
            self.star = Star()
            self.star.ligne()
            self.all_rect.add(self.star)

        self.initialisation()

    def initialisation(self):
        rect_1 = Rectangle(self.rect, WIDTH / 4, 25, BLUE)
        rect_2 = Rectangle(self.rect, WIDTH / 4, 25, YELLOW)
        rect_2.rect.x += WIDTH / 4
        rect_3 = Rectangle(self.rect, WIDTH / 4, 25, PURPLE)
        rect_3.rect.x += WIDTH / 2
        rect_4 = Rectangle(self.rect, WIDTH / 4, 25, ROSE)
        rect_4.rect.x += WIDTH / 2 + WIDTH / 4

        self.all_rect.add(rect_4)
        self.all_rect.add(rect_3)
        self.all_rect.add(rect_2)
        self.all_rect.add(rect_1)

        self.mask = pygame.mask.from_surface(self.image)

        self.all_rect.draw(self.image)
        self.rect.center = (640 / 2, self.height + self.scroll)

    def update(self):
        self.all_rect.update()

        liste_rect = self.all_rect.sprites()
        if (liste_rect[0].rect.x + WIDTH / 4 + 10) >= WIDTH / 2 and liste_rect[0].debordement == False:
            color = liste_rect[0].color
            liste_rect[0].debordement = True
            self.all_rect.add(Rectangle(self.rect, WIDTH / 4, 25, color))
            liste_rect = self.all_rect.sprites()
            liste_rect[-1].rect.x -= 150
            self.all_rect.update()

        if liste_rect[0].rect.x + 5 > WIDTH:
            self.all_rect.remove(liste_rect[0])

        self.all_rect.draw(self.image)
        # self.image.fill((0, 0, 0))
        self.rect.center = (640 / 2, self.height + self.scroll)

    def collide(self, player):

        for rec in self.all_rect.sprites():
            if rec.color == player.color:
                if (rec.rect.x > player.rect.x or (rec.rect.x + WIDTH / 4) < player.rect.x) and player.rect.y <= self.rect.y + 35 and player.rect.y > self.rect.y:
                    return True


def obstacles(player, all_obstacles, all_switch):
    list_obstacles = all_obstacles.sprites()
    nb = len(list_obstacles)
    if nb == 0:
        print("Creation du 1er obstacle")
        # all_obstacles.add(Switch(100))
        all_switch.add(Switch(100))
        # all_obstacles.add(Cross(-150))
        all_obstacles.add(Ligne(-150))
        # star = Star()
        # star.ligne()
        # star.rect.move_ip(0, -50)
        # all_obstacles.add(star)
        all_obstacles.add(Ligne(-70))
        # all_obstacles.add(Circle(-150))
        # all_obstacles.add(Square(-150))
    else:
        if list_obstacles[-1].rect.y > player.rect.y:
            # all_obstacles.add(Switch(-50))
            all_switch.add(Switch(100))
            ran = random.randint(1, 4)
            # choix aleatoire
            if ran == 1:
                all_obstacles.add(Circle(-150))
            elif ran == 2:
                all_obstacles.add(Ligne(-150))
            elif ran == 3:
                all_obstacles.add(Square(-150))
            elif ran == 4:
                all_obstacles.add(Cross(-150))


def collisions(player, all_obstacles, all_switch):

    for switch in all_switch:
        switch.collide(player)
    for obstacle in all_obstacles:
        if obstacle.collide(player):
            return True
