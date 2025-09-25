from Constants import *

class ButtonModel:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.is_hovered = False

    def check_hover(self, pos):
        # Проверка наведения мыши на кнопку
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered

    def execute_action(self):
        #Подтверждение активности кнопки
        return self.action