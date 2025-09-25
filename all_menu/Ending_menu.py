import pygame as pg
import sys
from ButtonFactory import ButtonFactory
from Constants import screen_width, screen_height, FPS, clock


def ending_menu(screen, font_large, font_medium, font_small, white, blue, gray):
    pg.mouse.set_visible(True)

    # Создаем фабрику кнопок
    colors = {'blue': blue, 'gray': gray, 'white': white}
    button_factory = ButtonFactory(font_medium, font_small, colors)

    # Создание кнопок
    restart_button = button_factory.create_button(
        screen_width // 2 - 100, 450, 200, 60, "Заново", "restart_level"
    )
    menu_button = button_factory.create_button(
        screen_width // 2 - 100, 530, 200, 60, "Меню", "menu"
    )
    quit_button = button_factory.create_button(
        screen_width // 2 - 100, 610, 200, 60, "Выйти", "quit"
    )

    buttons = [restart_button, menu_button, quit_button]

    # Размеры черного квадрата
    rect_width = screen_width // 2
    rect_height = screen_height // 2
    rect_x = (screen_width - rect_width) // 2
    rect_y = (screen_height - rect_height) // 2

    # Создаем поверхность для черного квадрата
    black_rect = pg.Surface((rect_width, rect_height))
    black_rect.fill((0, 0, 0))

    # Создаем рамку для квадрата
    outline_rect = pg.Rect(rect_x, rect_y, rect_width, rect_height)

    # Логика работы кнопок
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
                            if result == "restart_level":
                                return "restart"
                            elif result == "menu":
                                return "menu"
                            elif result == "quit":
                                pg.quit()
                                sys.exit()

        # Отрисовка фона
        overlay = pg.Surface((screen_width, screen_height))
        overlay.set_alpha(128)  # Полупрозрачность
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        # Отрисовка черного квадрата посередине
        screen.blit(black_rect, (rect_x, rect_y))
        pg.draw.rect(screen, white, outline_rect, 2)  # Рамка вокруг квадрата

        # Отрисовка текста внутри квадрата
        title = font_large.render("Конец игры", True, white)
        screen.blit(title, (screen_width // 2 - title.get_width() // 2, rect_y + 50))

        # Отрисовка кнопок внутри квадрата
        for button in buttons:
            button.handle_hover(mouse_pos)
            button.render(screen)

        pg.display.flip()
        clock.tick(FPS)