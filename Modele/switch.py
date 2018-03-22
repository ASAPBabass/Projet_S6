import pygame

from player import *


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
        self.mask = pygame.mask.from_surface(self.image)

    def collide(self, player):
        if player.rect.y - 35 < self.rect.y and self.bool == False:
            player.switch()
            print("collision avec le switch")
            self.image.fill((0, 0, 0, 0))
            self.bool = True
