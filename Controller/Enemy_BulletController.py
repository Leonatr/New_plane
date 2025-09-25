import pygame as pg
from View.Enemy_BulletView import EnemyBulletView
from Model.Enemy_bulletModel import  EnemyBulletModel
from Constants import screen_width, screen_height


class EnemyBulletController(pg.sprite.Sprite):
    def __init__(self, image, position, trajectory_x = -2, speed_y=5):
        super().__init__()
        # Модель и представление
        self.model = EnemyBulletModel(position, trajectory_x, speed_y)
        self.view = EnemyBulletView(image)

        # Изображение пули
        self.original_image = image
        self.image = self.view.image

        # Свойства пули
        self.rect = self.view.get_rect(position)
        self.mask = self.view.mask
        self.trajectory_x = trajectory_x
        self.speed_x = self.model.speed_x
        self.speed_y = self.model.speed_y

    def update(self):
        # Движение пули
        self.model.update_position()
        self.rect.center = self.model.position

        # Удаление, если пуля вылетела за границу
        if not self.model.check_bounds(screen_width, screen_height):
            self.kill()

    def draw(self, screen):
        #Отрисовка пули через view
        self.view.draw(screen, self.model.position)