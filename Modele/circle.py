import pygame
from math import *

from constantes import *
from player import *
from arc import *


class Circle(pygame.sprite.Sprite):

    def __init__(self, height, width, rayon, sens_rotation, pos_x, vitesse_rotation, synchronisation):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([rayon * 2, rayon * 2]).convert_alpha()
        self.rect = self.image.get_rect()
        self.height = height
        self.width = width
        self.rayon = rayon
        self.pos_x = pos_x
        self.sens_rotation = sens_rotation
        self.v_r = vitesse_rotation
        self.synchro = synchronisation

        self.i = 0  # vit
        self.scroll = 0  # permet le scrolling

        self.all_arcs = pygame.sprite.Group()
        if self.synchro == 0:
            self.arc_1 = Arc(
                PURPLE, self.rect, 0 + self.i, pi / 2 + self.i, self.width, self.rayon)
            self.arc_2 = Arc(
                YELLOW, self.rect, pi / 2 + self.i, pi + self.i, self.width, self.rayon)
            self.arc_3 = Arc(
                BLUE, self.rect, pi + self.i, 3 * pi / 2 + self.i, self.width, self.rayon)
            self.arc_4 = Arc(
                ROSE, self.rect, 3 * pi / 2 + self.i, 2 * pi + self.i, self.width, self.rayon)
        elif self.synchro == 1:
            self.arc_1 = Arc(
                YELLOW, self.rect, 0 + self.i, pi / 2 + self.i, self.width, self.rayon)
            self.arc_2 = Arc(
                PURPLE, self.rect, pi / 2 + self.i, pi + self.i, self.width, self.rayon)
            self.arc_3 = Arc(
                ROSE, self.rect, pi + self.i, 3 * pi / 2 + self.i, self.width, self.rayon)
            self.arc_4 = Arc(
                BLUE, self.rect, 3 * pi / 2 + self.i, 2 * pi + self.i, self.width, self.rayon)
        if self.synchro == 2:
            self.arc_1 = Arc(
                ROSE, self.rect, 0 + self.i, pi / 2 + self.i, self.width, self.rayon)
            self.arc_2 = Arc(
                BLUE, self.rect, pi / 2 + self.i, pi + self.i, self.width, self.rayon)
            self.arc_3 = Arc(
                YELLOW, self.rect, pi + self.i, 3 * pi / 2 + self.i, self.width, self.rayon)
            self.arc_4 = Arc(
                PURPLE, self.rect, 3 * pi / 2 + self.i, 2 * pi + self.i, self.width, self.rayon)

        self.all_arcs.add(self.arc_1)
        self.all_arcs.add(self.arc_2)
        self.all_arcs.add(self.arc_3)
        self.all_arcs.add(self.arc_4)

        self.rect.center = (self.pos_x, self.height)

        self.image.fill((0, 0, 0, 0))

    def update(self):
        self.image.fill((0, 0, 0, 0))

        if self.sens_rotation == True:
            self.i += self.v_r  # vitesse de rotation
        else:
            self.i -= self.v_r

        self.arc_1.update(0 + self.i, pi / 2 + self.i, self.width)
        self.arc_1.update(0 + self.i, pi / 2 + self.i, self.width)
        self.arc_2.update(pi / 2 + self.i, pi + self.i, self.width)
        self.arc_3.update(pi + self.i, 3 * pi / 2 + self.i, self.width)
        self.arc_4.update(3 * pi / 2 + self.i, 2 * pi + self.i, self.width)

        self.all_arcs.draw(self.image)
        # anti aliasing

        pygame.gfxdraw.aacircle(
            self.image, self.rayon, self.rayon, self.rayon + 2, GREY)
        pygame.gfxdraw.aacircle(
            self.image, self.rayon, self.rayon, self.rayon + 1, GREY)
        pygame.gfxdraw.aacircle(
            self.image, self.rayon, self.rayon, self.rayon - self.width, GREY)
        pygame.gfxdraw.aacircle(
            self.image, self.rayon, self.rayon, self.rayon - self.width - 1, GREY)

        self.rect.center = (self.pos_x, self.height + self.scroll)

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
        else:
            pass
