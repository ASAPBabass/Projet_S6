import pygame
import random

from constantes import *


class Point:

    def __init__(self, a, b):
        self.x = a
        self.y = b


class Player(pygame.sprite.Sprite):  # classe du joueur

    def __init__(self):  # constructeur
        pygame.sprite.Sprite.__init__(self)
        self.color = random.choice(colors)  # couleur aleatoire
        self.image = None
        self.score = 0  # score de la partie actuelle
        self.bestScore = 0  # meilleur score
        self.mask = None

    def initialization(self):
        self.color = random.choice(colors)  # couleur aleatoire
        # surface sur laquelle sera dessine le joueur
        self.image = pygame.Surface([20, 20]).convert_alpha()
        self.image.fill((0, 0, 0, 0))  # fond transparent
        pygame.gfxdraw.aacircle(
            self.image, 9, 9, 9, self.color)  # anti aliasing
        # cercle rempli
        pygame.gfxdraw.filled_circle(self.image, 9, 9, 9, self.color)
        # permet de recuperer les valeurs de la surface du joueur
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (WIDTH / 2, 150)

    def jump(self, jump):
        self.rect.y -= jump

    def update(self):  # gravite
        pygame.gfxdraw.aacircle(self.image, 9, 9, 9, self.color)
        pygame.gfxdraw.filled_circle(self.image, 9, 9, 9, self.color)

        if self.rect.y < 2000:
            self.rect.y += 3

    def switch(self):
        self.color = random.choice(colors)  # couleur aleatoire
