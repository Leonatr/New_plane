import pygame as pg
import sys
from ButtonFactory import ButtonFactory
from Constants import FPS, clock


def level_select_menu(screen, font_large, font_medium, font_small, white, blue, gray, menu_space, music_enabled):
    pg.mouse.set_visible(True)

    # Создаем фабрику кнопок
    colors = {'blue': blue, 'gray': gray, 'white': white}
    button_factory = ButtonFactory(font_medium, font_small, colors)

    # Создаем кнопки
    level1_button = button_factory.create_button(240, 500, 220, 60, "Уровень 1", "game")
    back_button = button_factory.create_button(240, 600, 220, 60, "Назад", "menu")

    buttons = [level1_button, back_button]

    # Логика работы кнопки
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
                            result = button.handle_click()
                            if result == "menu":
                                return "menu"
                            pg.mixer.music.stop()
                            return result

        screen.fill((0, 0, 0))
        screen.blit(menu_space, (0, 0))

        title = font_large.render("Выбор уровня", True, white)
        screen.blit(title, (200, 150))

        # Отрисовка кнопок
        for button in buttons:
            button.handle_hover(mouse_pos)
            button.render(screen)

        pg.display.flip()
        clock.tick(FPS)