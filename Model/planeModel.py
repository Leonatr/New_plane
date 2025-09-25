import pygame as pg


class PlaneModel:
    def __init__(self, position):
        self.position = position
        self.speed = 5
        self.health = 10
        self.super_blow = 0

    def move(self, keys, screen_width, screen_height):
        # Логика движения

        if keys[pg.K_LEFT] and self.position[0] > 0:
            self.position = (self.position[0] - self.speed, self.position[1])
        if keys[pg.K_RIGHT] and self.position[0] < screen_width:
            self.position = (self.position[0] + self.speed, self.position[1])
        if keys[pg.K_UP] and self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - self.speed)
        if keys[pg.K_DOWN] and self.position[1] < screen_height:
            self.position = (self.position[0], self.position[1] + self.speed)

