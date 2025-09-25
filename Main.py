import sys
from all_menu.Main_menu import main_menu
from all_menu.Settings_menu import settings_menu
from all_menu.Level_select_menu import level_select_menu
from all_menu.Controls_menu import controls_menu
from level1 import game
from Constants import *

# Инициализация pygame
pg.init()
pg.font.init()
pg.mixer.init()

# Добавление музыки
pg.mixer.music.load(menu_music)
pg.mixer.music.set_volume(0.5)
if music_enabled:
    pg.mixer.music.play(-1)

# Создание экрана
clock = pg.time.Clock()
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('plane')

# Основной цикл программы
current_screen = "menu"

while True:
    if current_screen == "menu":
        current_screen = main_menu(screen, font_large, font_medium, font_small, white, blue, gray, menu_space, music_enabled, menu_music)
    elif current_screen == "level_select":
        current_screen = level_select_menu(screen, font_large, font_medium, font_small, white, blue, gray, menu_space, music_enabled)
    elif current_screen == "settings":
        result = settings_menu(screen, font_large, font_medium, font_small, white, blue, gray, menu_space, music_enabled, menu_music)
        if isinstance(result, tuple):
            current_screen, music_enabled = result
        else:
            current_screen = result
    elif current_screen == "controls":
        current_screen = controls_menu(screen, font_large, font_medium, font_small, white, blue, gray, menu_space)
    elif current_screen == "game":
        current_screen = game(screen, screen_width, screen_height, FPS, clock, font_small, white, black, blue, gray, music_enabled)
    elif current_screen == "quit":
        pg.quit()
        sys.exit()