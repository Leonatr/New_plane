import pygame as pg

class EnemyBulletView:
    def __init__(self, image):
        self.original_image = image
        self.image = image
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, screen, position):
        # Отрисовка пули
        rect = self.image.get_rect(center=position)
        screen.blit(self.image, rect)
        return rect

    def get_rect(self, position):
        #Получение расположения пули
        return self.image.get_rect(center=position)

