import pygame as pg


class FirstLevelEnemyView:
    def __init__(self, original_image):
        self.original_image = original_image
        self.image = pg.transform.rotate(self.original_image, 180)
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, screen, position):
        #Отрисовка врагов
        rect = self.image.get_rect(center=position)
        screen.blit(self.image, rect)
        return rect

    def get_rect(self, position):
        #Обновление позиции врагов
        return self.image.get_rect(center=position)
