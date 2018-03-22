import pygame
from math import *

from constantes import *
from player import *
from arete import *


class Parallelogramme(pygame.sprite.Sprite):

    def __init__(self, height, r1, r2, angle1, angle2, vitesse_rotation):
        try:
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([4 * r1, 4 * r1]).convert()
            self.rect = self.image.get_rect()
            self.image.fill((0, 0, 0, 0))
            self.height = height

            self.angle = 0
            self.angle1 = angle1  # vitesse de rotation
            self.angle2 = angle2
            self.scroll = 0  # permet le scrolling

            self.all_aretes = pygame.sprite.Group()

            self.O = Point(2 * r1, 2 * r1)  # centre
            self.A = Point(0, 0)
            self.B = Point(0, 0)
            self.C = Point(0, 0)
            self.D = Point(0, 0)
            self.rayon1 = r1
            self.rayon2 = r2
            self.v_r = vitesse_rotation

            self.angleRadian = pi * self.angle / 180

            self.angleRadian2 = pi * (self.angle + self.angle1) / 180

            self.angleRadian3 = pi * \
                (self.angle + self.angle1 + self.angle2) / 180

            self.angleRadian4 = pi * \
                (self.angle + 2 * self.angle1 + self.angle2) / 180

            self.arete_1 = Arete(
                self.rect, self.A, self.B, YELLOW, 20, 4 * self.rayon1, 4 * self.rayon1)
            self.arete_2 = Arete(
                self.rect, self.B, self.C, BLUE, 20, 4 * self.rayon1, 4 * self.rayon1)
            self.arete_3 = Arete(
                self.rect, self.C, self.D, ROSE, 20, 4 * self.rayon1, 4 * self.rayon1)
            self.arete_4 = Arete(
                self.rect, self.D, self.A, PURPLE, 20, 4 * self.rayon1, 4 * self.rayon1)

            self.all_aretes.add(self.arete_2)
            self.all_aretes.add(self.arete_3)
            self.all_aretes.add(self.arete_4)
            self.all_aretes.add(self.arete_1)

            self.rect.center = (WIDTH / 2, self.height)

        except Exception:
            print("erreur constructeur")

    def update(self):

        self.image.fill((41, 41, 41))
        self.angle += self.v_r  # vitesse de rotation

        self.angleRadian = pi * self.angle / 180

        self.angleRadian2 = pi * (self.angle + self.angle1) / 180

        self.angleRadian3 = pi * (self.angle + self.angle1 + self.angle2) / 180

        self.angleRadian4 = pi * \
            (self.angle + 2 * self.angle1 + self.angle2) / 180
        self.A.x = self.O.x + self.rayon1 * \
            cos(self.angleRadian) - self.rayon1 * sin(self.angleRadian)
        self.A.y = self.O.y + self.rayon1 * \
            sin(self.angleRadian) + self.rayon1 * cos(self.angleRadian)

        self.B.x = self.O.x + self.rayon2 * \
            cos(self.angleRadian2) - self.rayon2 * sin(self.angleRadian2)
        self.B.y = self.O.y + self.rayon2 * \
            sin(self.angleRadian2) + self.rayon2 * cos(self.angleRadian2)

        self.C.x = self.O.x + self.rayon1 * \
            cos(self.angleRadian3) - self.rayon1 * sin(self.angleRadian3)
        self.C.y = self.O.y + self.rayon1 * \
            sin(self.angleRadian3) + self.rayon1 * cos(self.angleRadian3)

        self.D.x = self.O.x + self.rayon2 * \
            cos(self.angleRadian4) - self.rayon2 * sin(self.angleRadian4)
        self.D.y = self.O.y + self.rayon2 * \
            sin(self.angleRadian4) + self.rayon2 * cos(self.angleRadian4)

        self.arete_1.update(self.A, self.B)
        self.arete_2.update(self.B, self.C)
        self.arete_3.update(self.C, self.D)
        self.arete_4.update(self.D, self.A)

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
        elif pygame.sprite.collide_mask(player, self.arete_4) and color != self.arete_4.color:
            print("Collision couleur PURPLE")
            return True
        else:
            pass
