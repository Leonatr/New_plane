import pygame as pg
from Model.Level1_EnemyModel import FirstLevelEnemyModel
from View.Level1_EnemyView import FirstLevelEnemyView


class FirstLevelEnemyController(pg.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()

        # Создаем модель и представление
        self.model = FirstLevelEnemyModel(position)
        self.view = FirstLevelEnemyView(image)

        # Свойства модели
        self.original_image = image
        self.image = self.view.image
        self.rect = self.view.get_rect(position)
        self.mask = self.view.mask
        self.speed_x = self.model.speed_x
        self.speed_y = self.model.speed_y
        self.angle = self.model.angle
        self.health = self.model.health
        self.move_timer = self.model.move_timer

    def update(self, current_time=None):
        # Обновление позиции врагов через Model
        self.model.update_position()
        self.rect.center = self.model.position

        # Движения врагов через Model
        self.speed_x = self.model.speed_x
        self.speed_y = self.model.speed_y
        self.move_timer = self.model.move_timer

    def draw(self, screen):
        # Отрисовка врагов
        self.view.draw(screen, self.model.position)

