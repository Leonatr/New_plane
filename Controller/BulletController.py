import pygame as pg
from View.BulletView import BulletView
from Model.Bullet_Model import BulletModel
from Constants import screen_width, screen_height

class BulletController(pg.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        # Логика инициализации
        self.original_image = image
        self.image = pg.transform.rotate(self.original_image, -90)

        # Модель и представление
        self.model = BulletModel(position)
        self.view = BulletView(self.image)

        # Свойства пуль
        self.rect = self.image.get_rect(center=position)
        self.mask = self.view.mask
        self.speed_y = 0

    def update(self):
        # Обновляем позицию в модели
        self.model.speed_y = self.speed_y
        self.rect.center = self.model.update_position()

        # Проверка границ
        if (self.rect.right < 0 or self.rect.left > screen_width or
            self.rect.top > screen_height or self.rect.bottom < 0):
            self.kill()

