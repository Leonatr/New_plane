import pygame as pg

class ButtonView:
    def __init__(self, font_medium, font_small, colors):
        self.font_medium = font_medium
        self.font_small = font_small
        self.colors = colors

    def draw(self, surface, button_model, is_small=False):
        #Проверка на наведение курсора и выбор цвета
        if button_model.is_hovered:
            color = self.colors['blue']
        else:
            color = self.colors['gray']

        #Создание вида кнопок
        pg.draw.rect(surface, color, button_model.rect, border_radius=10)
        pg.draw.rect(surface, self.colors['white'], button_model.rect, 2, border_radius=10)

        if is_small:
            font = self.font_small
        else:
            font = self.font_medium

        #Отрисовка текста
        text_surf = font.render(button_model.text, True, self.colors['white'])
        text_rect = text_surf.get_rect(center=button_model.rect.center)
        surface.blit(text_surf, text_rect)