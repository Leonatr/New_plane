import pygame as pg
from ButtonFactory import ButtonFactory
import sys
from Constants import FPS, clock


def main_menu(screen, font_large, font_medium, font_small, white, blue, gray, menu_space, music_enabled, menu_music):
    if music_enabled and not pg.mixer.music.get_busy():
        pg.mixer.music.load(menu_music)
        pg.mixer.music.play(-1)
        pg.mixer.music.unpause()

    pg.mouse.set_visible(True)

    # Создаем фабрику кнопок
    colors = {'blue': blue, 'gray': gray, 'white': white}
    button_factory = ButtonFactory(font_medium, font_small, colors)

    # Создаем кнопки
    play_button = button_factory.create_button(240, 400, 220, 60, "Играть", "game")
    settings_button = button_factory.create_button(240, 500, 220, 60, "Настройки", "settings")
    quit_button = button_factory.create_button(240, 600, 220, 60, "Выйти", "quit")

    buttons = [play_button, settings_button, quit_button]

    #Логика работы кнопок
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
                            if result == "quit":
                                pg.quit()
                                sys.exit()
                            elif result == "settings":
                                return "settings"
                            elif result == "game":
                                return "level_select"
                            return result

        screen.fill((0, 0, 0))
        screen.blit(menu_space, (0, 0))

        title = font_large.render("Plane Game", True, white)
        screen.blit(title, (240, 150))

        # Отрисовка кнопок
        for button in buttons:
            button.handle_hover(mouse_pos)
            button.render(screen)

        pg.display.flip()
        clock.tick(FPS)