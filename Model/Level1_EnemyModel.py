class FirstLevelEnemyModel:
    def __init__(self, position):
        self.position = position
        self.speed_x = 1
        self.speed_y = 3
        self.angle = 180
        self.health = 1
        self.move_timer = 0
        self.is_active = True
        self.movement_phase = 1

        # Новые свойства для режимов стрельбы
        self.shooting_modes = ["default", "wave", "barrage"]
        self.current_shooting_mode = "default"
        self.last_shot_time = 0
        self.shoot_delay = 350
        self.wave_shot_count = 0
        self.wave_delay = 150
        self.trajectory_x = 0

    def update_position(self):
        #Логика движения врагов
        self.move_timer += 1
        if self.move_timer > 50:
            self.speed_x *= -1
            self.move_timer = 0

        if self.movement_phase == 1 or self.movement_phase == 0:
            self.position = (self.position[0] + self.speed_x,
                             self.position[1] + self.speed_y)
        elif self.movement_phase == 2:
            self.position = (self.position[0] + self.speed_x,
                             self.position[1] - self.speed_y)
        return self.position

