class ButtonController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_hover(self, pos):
        #Проверка наведения мыши на кнопку
        return self.model.check_hover(pos)

    def handle_click(self):
        #Проверка клика по кнопке, если курсор наведён
        if self.model.is_hovered and self.model.action:
            return self.model.execute_action()
        return None

    def render(self, surface, is_small=False):
        #Отрисовка кнопки
        self.view.draw(surface, self.model, is_small)