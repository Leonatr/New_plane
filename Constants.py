import pygame as pg

# Базовые параметры
FPS = 60
screen_width = 700
screen_height = 1000
white = (255, 255, 255)
black = (0, 0, 0)
gray = (100, 100, 100)
blue = (0, 100, 255)




clock = pg.time.Clock()
screen = pg.display.set_mode((screen_width, screen_height))
pg.font.init()

# Загрузка музыки
music_enabled = True
menu_music = 'assets/audio/menu_music.ogg'
game_music = 'assets/audio/game_music.mp3'

# Используемые шрифты
font_large = pg.font.SysFont('Arial', 50)
font_medium = pg.font.SysFont('Arial', 35)
font_small = pg.font.SysFont('Arial', 20)
font = pg.font.SysFont('Arial', 80)

menu_space = pg.image.load('assets/sprites/menu_space.png')
menu_space = pg.transform.scale(menu_space, (screen_width, screen_height))