class EnemyBulletModel:
    def __init__(self, position, trajectory_x, speed_y=5):
        self.position = position
        self.trajectory_x = 0
        self.speed_x = -2 + trajectory_x
        self.speed_y = speed_y
        self.is_active = True

    def update_position(self):
        #Обновление позиции пули
        self.position = (self.position[0] + self.speed_x,
                         self.position[1] + self.speed_y)
        return self.position

    def check_bounds(self, screen_width, screen_height):
        #Проверка вылета пули за границу
        x, y = self.position
        if (x < 0 or x > screen_width or y < 0 or y > screen_height):
            self.is_active = False
        return self.is_active