import pygame as pg
from Model.planeModel import PlaneModel
from View.planeView import PlaneView

class PlaneController(pg.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()

        self.model = PlaneModel(position)
        self.view = PlaneView(image)

        # Cвойства самолётика
        self.original_image = image
        self.image = self.view.image
        self.rect = self.view.get_rect(position)
        self.speed = self.model.speed
        self.health = self.model.health
        self.super_blow = self.model.super_blow

    def move(self, keys, screen_width, screen_height):
        # Движение модели
        self.model.move(keys, screen_width, screen_height)
        # Обновление позиции самолётика
        self.rect.center = self.model.position

    def draw(self, screen):
        # Отрисовка самолётика через View
        self.view.draw(screen, self.model.position)
