import pygame

from player import *


class Star(pygame.sprite.Sprite):

    def __init__(self, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            "Vue/Image/star3.png").convert_alpha()
        self.rect = self.image.get_rect()  # correspond a la surface du cercle
        self.mask = None
        self.pos_y = pos_y
        self.scroll = 0
        self.rect.center = (WIDTH / 2, self.pos_y + self.scroll)
        self.bool = False

    def update(self):
        self.rect.center = (WIDTH / 2, self.pos_y + self.scroll)

    def collide(self, player):
        if player.rect.y < self.rect.y + 45 and self.bool == False:  # collision
            self.image.fill((0, 0, 0, 0))
            player.score += 1
            self.bool = True
