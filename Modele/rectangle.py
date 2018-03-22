import pygame


class Rectangle(pygame.sprite.Sprite):

    def __init__(self, rect, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height]).convert_alpha()
        self.rect = self.image.get_rect()
        self.color = color
        self.image.fill(color)
        self.mask = pygame.mask.from_surface(self.image)
        self.debordement = False

    def update(self, speed):
        self.rect.x += speed  # vitesse de defilement
        self.mask = pygame.mask.from_surface(self.image)
