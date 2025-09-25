from Model import ButtonModel
from View.ButtonView import ButtonView
from Controller.ButtonController import ButtonController


class ButtonFactory:
    def __init__(self, font_medium, font_small, colors):
        self.font_medium = font_medium
        self.font_small = font_small
        self.colors = colors

    def create_button(self, x, y, width, height, text, action=None):
        #Создание кнопкок
        model = ButtonModel(x, y, width, height, text, action)
        view = ButtonView(self.font_medium, self.font_small, self.colors)
        controller = ButtonController(model, view)
        return controller