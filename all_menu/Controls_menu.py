import pygame as pg
import sys
from ButtonFactory import ButtonFactory
from Constants import screen_width, FPS, clock


def controls_menu(screen, font_large, font_medium, font_small, white, blue, gray, menu_space):
    pg.mouse.set_visible(True)

    # Создаем фабрику кнопок
    colors = {'blue': blue, 'gray': gray, 'white': white}
    button_factory = ButtonFactory(font_medium, font_small, colors)

    # Создаем кнопку
    back_button = button_factory.create_button(
        screen_width // 2 - 100, 650, 200, 60, "Назад", "settings"
    )

    buttons = [back_button]

    #Логика работы кнопки
    while True:
        mouse_pos = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in buttons:
                        if button.model.rect.collidepoint(event.pos):
                            return button.handle_click()

        screen.fill((0, 0, 0))
        screen.blit(menu_space, (0, 0))

        title = font_large.render("Управление", True, white)
        screen.blit(title, (230, 150))

        controls = [
            "w - вперёд",
            "s - назад",
            "a - влево",
            "d - вправо",
            "space - стрелять",
            "v - супер удар",
            "esc - пауза"
        ]

        #Отрисовка всех надписей
        for i, control in enumerate(controls):
            text = font_medium.render(control, True, white)
            screen.blit(text, (260, 250 + i * 50))

        # Отрисовка всех кнопок
        for button in buttons:
            button.handle_hover(mouse_pos)
            button.render(screen)

        pg.display.flip()
        clock.tick(FPS)