import pygame
from math import *

from constantes import *
from player import *
from arete import *


class Cross(pygame.sprite.Sprite):  # TODO

    def __init__(self, pos_x, pos_y, width, rayon, speed_rotation,synchr):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([4 * rayon, 4 * rayon]).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill((0, 0, 0, 0))
        self.speed = speed_rotation
        self.all_aretes = pygame.sprite.Group()

        self.angle = 0  # vitesse de rotatio
        self.scroll = 0  # permet le scrolling

        self.rayon = rayon
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.O = Point(2 * rayon, 2 * rayon)  # centre
        self.A = Point(0, 0)
        self.B = Point(0, 0)
        self.C = Point(0, 0)
        self.D = Point(0, 0)

        self.synchr=synchr

        self.angleRadian = pi * self.angle / 180

        self.angleRadian2 = pi * (self.angle + 90) / 180

        self.angleRadian3 = pi * (self.angle + 180) / 180

        self.angleRadian4 = pi * (self.angle + 270) / 180

        if(self.synchr==1):
            self.arete_1 = Arete(
                self.rect, self.A, self.O, BLUE, width, 4 * rayon, 4 * rayon)
            self.arete_2 = Arete(
                self.rect, self.B, self.O, YELLOW, width, 4 * rayon, 4 * rayon)
            self.arete_3 = Arete(
                self.rect, self.C, self.O, PURPLE, width, 4 * rayon, 4 * rayon)
            self.arete_4 = Arete(
                self.rect, self.D, self.O, ROSE, width, 4 * rayon, 4 * rayon)
        else :
            self.arete_1 = Arete(
                self.rect, self.A, self.O, YELLOW, width, 4 * rayon, 4 * rayon)
            self.arete_2 = Arete(
                self.rect, self.B, self.O, BLUE, width, 4 * rayon, 4 * rayon)
            self.arete_3 = Arete(
                self.rect, self.C, self.O, ROSE, width, 4 * rayon, 4 * rayon)
            self.arete_4 = Arete(
                self.rect, self.D, self.O, PURPLE, width, 4 * rayon, 4 * rayon)

        self.all_aretes.add(self.arete_2)
        self.all_aretes.add(self.arete_3)
        self.all_aretes.add(self.arete_4)
        self.all_aretes.add(self.arete_1)

        self.rect.center = (self.pos_x, self.pos_y + self.scroll)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):

        self.image.fill((0, 0, 0, 0))
        self.angle += self.speed  # vitesse de rotation

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

        self.rect.center = (self.pos_x, self.pos_y + self.scroll)
        self.mask = pygame.mask.from_surface(self.image)

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
