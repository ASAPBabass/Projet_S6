import pygame
from math import *

from constantes import *
from player import *
from arete import *


class Triangle(pygame.sprite.Sprite):

    def __init__(self, height,width, rayon, vitesse_rotation):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([4 * rayon, 4 * rayon]).convert()
        self.rect = self.image.get_rect()
        self.image.fill((0, 0, 0, 0))
        self.height = height
        self.width=width

        self.angle = 0  # vitesse de rotation
        self.scroll = 0  # permet le scrolling

        self.all_aretes = pygame.sprite.Group()
        self.O = Point(2 * rayon, 2 * rayon)  # centre
        self.A = Point(0, 0)
        self.B = Point(0, 0)
        self.C = Point(0, 0)
        self.rayon = rayon
        self.v_r = vitesse_rotation

        self.angleRadian = pi * (self.angle + 60) / 180

        self.angleRadian2 = pi * (self.angle + 60) / 180

        self.angleRadian3 = pi * (self.angle + 60) / 180

        self.arete_1 = Arete(
            self.rect, self.A, self.B, YELLOW, self.width, 4 * self.rayon, 4 * self.rayon)
        self.arete_2 = Arete(
            self.rect, self.B, self.C, BLUE, self.width, 4 * self.rayon, 4 * self.rayon)
        self.arete_3 = Arete(
            self.rect, self.C, self.A, ROSE, self.width, 4 * self.rayon, 4 * self.rayon)

        self.all_aretes.add(self.arete_1)
        self.all_aretes.add(self.arete_2)
        self.all_aretes.add(self.arete_3)

        # self.all_aretes.add(self.star)

        self.rect.center = (WIDTH / 2, self.height)

    def update(self):

        self.image.fill((41, 41, 41))
        self.angle += self.v_r  # vitesse de rotation
        self.angleRadian = pi * self.angle / 180

        self.angleRadian2 = pi * (self.angle + 120) / 180
        self.angleRadian3 = pi * (self.angle + 240) / 180

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

        self.arete_1.update(self.A, self.B)
        self.arete_2.update(self.B, self.C)
        self.arete_3.update(self.C, self.A)

        self.all_aretes.draw(self.image)

        self.rect.center = (WIDTH / 2, self.height + self.scroll)

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
        else:
            pass
