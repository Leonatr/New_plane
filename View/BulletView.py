import pygame as pg


class BulletView:
    def __init__(self, image):
        self.image = image
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, screen, position):
        #Отрисовка пуль
        rect = self.image.get_rect(center=position)
        screen.blit(self.image, rect)
        return rect