import pygame as pg
from ButtonFactory import ButtonFactory
import sys
from Constants import FPS, clock


def pause_menu(screen, font_medium, font_small, white, blue, gray, black):
    pg.mouse.set_visible(True)
    menu_length = 400
    menu_height = 500
    fill = 400
    x = 150
    y = 300

    #Создание рамок меню паузы
    outline_rect = pg.Rect(x, y, menu_length, menu_height)
    fill_rect = pg.Rect(x, y, fill, menu_height)
    pg.draw.rect(screen, black, fill_rect, 500)
    pg.draw.rect(screen, white, outline_rect, 1)

    font = pg.font.SysFont('Arial', 60)
    text = font.render("Пауза", True, (255, 255, 255))
    screen.blit(text, (285, 300))

    # Создаем фабрику кнопок
    colors = {'blue': blue, 'gray': gray, 'white': white}
    button_factory = ButtonFactory(font_medium, font_small, colors)

    # Создаем кнопки
    continue_button = button_factory.create_button(240, 450, 235, 65, "Продолжить", "continue")
    quit_menu_button = button_factory.create_button(240, 550, 235, 65, "Выйти в меню", "menu")
    quit_button = button_factory.create_button(240, 650, 235, 65, "Выйти из игры", "quit")

    pause_buttons = [continue_button, quit_menu_button, quit_button]
    pause = True

    # Логика работы кнопок
    while pause:
        mouse_pos = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return "continue"

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in pause_buttons:
                        if button.model.rect.collidepoint(event.pos):
                            result = button.handle_click()
                            if result == "quit":
                                pg.quit()
                                sys.exit()
                            return result

        # Отрисовка кнопок
        for button in pause_buttons:
            button.handle_hover(mouse_pos)
            button.render(screen)

        pg.display.flip()
        clock.tick(FPS)