from Constants import  screen


#Функция отрисовки спрайтов в группе
def custom_draw(group):
    for sprite in group:
        sprite.draw(screen)