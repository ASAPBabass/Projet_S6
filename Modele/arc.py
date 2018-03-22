import pygame


class Arc(pygame.sprite.Sprite):

    def __init__(self, color, rect, start_angle, stop_angle, width, rayon):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([rayon * 2, rayon * 2]).convert_alpha()
        self.image.fill((0, 0, 0, 0))
        self.rect = rect
        self.rayon = rayon
        self.i = 1
        self.color = color
        self.mask = None
        self.update(start_angle, stop_angle, width)

    def update(self, start_angle, stop_angle, width):
        self.image.fill((0, 0, 0, 0))
        rect_bis = self.rect.move(0, 1)
        pygame.draw.arc(
            self.image, self.color, self.rect, start_angle, stop_angle, width)
        pygame.draw.arc(
            self.image, self.color, rect_bis, start_angle, stop_angle, width)

        # anti-aliasing
        # pygame.gfxdraw.aacircle(self.image, arc_2.x, arc_2.y, 199, GREY)

        self.rect.center = (self.rayon, self.rayon)
        self.mask = pygame.mask.from_surface(self.image)
