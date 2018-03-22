import pygame


class Arete(pygame.sprite.Sprite):

    def __init__(self, rect, a, b, color, width, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([pos_x, pos_y]).convert_alpha()
        self.image.fill((0, 0, 0, 0))
        self.rect = rect
        self.color = color
        self.mask = pygame.mask.from_surface(self.image)
        self.width = width
        self.pos_x = pos_x
        self.pos_y = pos_y

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

        self.rect.center = (self.pos_x / 2, self.pos_y / 2)
        self.mask = pygame.mask.from_surface(self.image)
