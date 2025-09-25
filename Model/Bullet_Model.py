class BulletModel:
    def __init__(self, position):
        self.position = position
        self.speed_y = 0

    def update_position(self):
        #Обновление позиции пуль
        self.position = (self.position[0], self.position[1] - self.speed_y)
        return self.position