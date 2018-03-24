import pygame

from constantes import *
from player import *
from rectangle import *


class Ligne(pygame.sprite.Sprite):

    def __init__(self, height, sens):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([WIDTH, 200]).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill((0, 0, 0, 0))
        self.sens = sens
        self.height = height
        self.scroll = 0
        self.all_rect = pygame.sprite.OrderedUpdates()

        rect_1 = Rectangle(self.rect, WIDTH / 4, 25, BLUE)
        rect_2 = Rectangle(self.rect, WIDTH / 4, 25, YELLOW)
        rect_2.rect.x += WIDTH / 4
        rect_3 = Rectangle(self.rect, WIDTH / 4, 25, PURPLE)
        rect_3.rect.x += WIDTH / 2
        rect_4 = Rectangle(self.rect, WIDTH / 4, 25, ROSE)
        rect_4.rect.x += WIDTH / 2 + WIDTH / 4

        if self.sens == True:
            self.all_rect.add(rect_4)
            self.all_rect.add(rect_3)
            self.all_rect.add(rect_2)
            self.all_rect.add(rect_1)
        else:
            self.all_rect.add(rect_1)
            self.all_rect.add(rect_2)
            self.all_rect.add(rect_3)
            self.all_rect.add(rect_4)

        self.mask = pygame.mask.from_surface(self.image)

        self.all_rect.draw(self.image)
        self.rect.center = (WIDTH / 2, self.height + self.scroll)

    def update(self):

        liste_rect = self.all_rect.sprites()
        if(self.sens == True):
            self.all_rect.update(4)
            if (liste_rect[0].rect.x + WIDTH / 4 + 10) >= WIDTH / 2 and liste_rect[0].debordement == False:
                color = liste_rect[0].color
                liste_rect[0].debordement = True
                self.all_rect.add(
                    Rectangle(self.rect, WIDTH / 4, 25, color))
                liste_rect = self.all_rect.sprites()
                liste_rect[-1].rect.x -= 150
                self.all_rect.update(4)

            if liste_rect[0].rect.x + 5 > WIDTH:
                self.all_rect.remove(liste_rect[0])
        else:
            self.all_rect.update(-4)
            if (liste_rect[0].rect.x) <= 0 and liste_rect[0].debordement == False:
                color = liste_rect[0].color
                liste_rect[0].debordement = True
                rectangle = Rectangle(self.rect, WIDTH / 4, 25, color)
                self.all_rect.add(rectangle)
                liste_rect = self.all_rect.sprites()
                liste_rect[-1].rect.x = WIDTH
                self.all_rect.update(-4)

            if liste_rect[0].rect.x + WIDTH / 4 < 0:
                self.all_rect.remove(liste_rect[0])

        self.all_rect.draw(self.image)
        self.rect.center = (WIDTH / 2, self.height + self.scroll)

    def collide(self, player):
        for rec in self.all_rect.sprites():
            if rec.color == player.color:
                if (rec.rect.x > player.rect.x or (rec.rect.x + WIDTH / 4) < player.rect.x) and player.rect.y <= self.rect.y + 23 and player.rect.y > self.rect.y - 23:
                    return True
