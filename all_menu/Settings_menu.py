import pygame as pg
from ButtonFactory import ButtonFactory
import sys
from Constants import FPS, clock


def settings_menu(screen, font_large, font_medium, font_small, white, blue, gray, menu_space, music_enabled,
                  menu_music):
    pg.mouse.set_visible(True)

    # Создаем фабрику кнопок
    colors = {'blue': blue, 'gray': gray, 'white': white}
    button_factory = ButtonFactory(font_medium, font_small, colors)

    # Создаем кнопки
    back_button = button_factory.create_button(240, 600, 220, 60, "Назад", "menu")
    controls_button = button_factory.create_button(240, 500, 220, 60, "Управление", "controls")
    music_toggle = button_factory.create_button(240, 400, 220, 60, "Музыка: Вкл" if music_enabled else "Музыка: Выкл",
                                                "toggle_music")

    buttons = [back_button, music_toggle, controls_button]

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
                            if result == "menu":
                                return "menu"
                            elif result == "controls":
                                return "controls"
                            elif result == "toggle_music":
                                music_enabled = not music_enabled
                                if music_enabled:
                                    music_toggle.model.text = "Музыка: Вкл"
                                    pg.mixer.music.unpause()
                                    if not pg.mixer.music.get_busy():
                                        pg.mixer.music.play(-1)
                                else:
                                    music_toggle.model.text = "Музыка: Выкл"
                                    pg.mixer.music.pause()
                                return "settings", music_enabled

        screen.fill((0, 0, 0))
        screen.blit(menu_space, (0, 0))

        title = font_large.render("Настройки", True, white)
        screen.blit(title, (250, 150))

        # Отрисовка кнопок
        for button in buttons:
            button.handle_hover(mouse_pos)
            button.render(screen)

        pg.display.flip()
        clock.tick(FPS)