import pygame as pg


#Отрисовка полоски супер-удара
def draw_super_blow(surface, x, y, charge, max_charge):
    bar_length = 50
    bar_height = 10
    if charge < max_charge:
        fill = charge
    else:
        fill = max_charge
    outline_rect = pg.Rect(x, y, bar_length, bar_height)
    fill_rect = pg.Rect(x, y, fill, bar_height)
    pg.draw.rect(surface, (0, 255, 0), fill_rect)
    pg.draw.rect(surface, (255, 255, 255), outline_rect, 1)


#Отрисовка полосок здоровья для врагов
def draw_health_bar(surface, x, y, health, max_health):
    bar_length = 80
    bar_height = 7

    fill = (health / max_health) * bar_length
    outline_rect = pg.Rect(x, y, bar_length, bar_height)
    fill_rect = pg.Rect(x, y, fill, bar_height)
    pg.draw.rect(surface, (255, 0, 0), fill_rect)
    pg.draw.rect(surface, (255, 255, 255), outline_rect, 1)


#Отрисовка сердечек здоровья игрока
def draw_hearts(surface, x, y, health, max_health):
    hearts = max_health // 2
    heart_img = pg.Surface((30, 30), pg.SRCALPHA)
    pg.draw.polygon(heart_img, (255, 0, 0), [(15, 0), (5, 20), (15, 30), (25, 20)])
    for i in range(hearts):
        pos = (x + i * 35, y)
        if health >= (i+1)*2:
            surface.blit(heart_img, pos)
        elif health == (i*2)+1:
            half_heart = pg.Surface((15, 30), pg.SRCALPHA)
            half_heart.blit(heart_img, (0, 0), (0, 0, 15, 30))
            surface.blit(half_heart, pos)