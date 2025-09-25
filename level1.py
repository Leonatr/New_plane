import random
import sys
from Controller import BulletController, EnemyBulletController, FirstLevelEnemyController, PlaneController
from all_menu.Pause_menu import pause_menu
from all_menu.Ending_menu import ending_menu
from draw_game_interface import draw_hearts, draw_health_bar, draw_super_blow
from group_draw import custom_draw
from Constants import *


def game(screen, screen_width, screen_height, FPS, clock, font_small, white, black, blue, gray, music_enabled):
    def reset_game_timers():
        nonlocal last_shot1, last_shot2, time_for_flag, mode_change_time, current_shooting_mode
        last_shot1 = 0
        last_shot2 = 0
        time_for_flag = pg.time.get_ticks()
        mode_change_time = pg.time.get_ticks()
        current_shooting_mode = "default"

    #Константы
    running = True
    BULLET_SPEED = 10
    shoot_delay = 250
    enemy_shoot_delay = 350
    last_shot1 = 0
    last_shot2 = 0
    trajectory_x = 0
    flag = 1
    time_for_flag = 0
    flag_delay = 6000
    pause_duration = 0

    #Данные для смены режима стрельбы врагов
    shooting_modes = ["default", "wave", "barrage"]
    copy_shooting_modes = shooting_modes.copy()
    current_shooting_mode = "default"
    mode_change_time = 0
    mode_duration = 15000
    wave_shot_count = 0
    wave_delay = 150

    #Все изображения
    background = pg.image.load('assets/sprites/Space.png')
    background = pg.transform.scale(background, (screen_width, screen_height))

    bullet_img = pg.image.load('assets/sprites/bullet.png')
    bullet_img = pg.transform.scale(bullet_img, (70, 35))

    super_bullet_img = pg.image.load('assets/sprites/bullet.png')
    super_bullet_img = pg.transform.scale(super_bullet_img, (200, 120))

    enemy_bullet_img = pg.image.load('assets/sprites/enemy_bullet.png')
    enemy_bullet_img = pg.transform.scale(enemy_bullet_img, (70, 45))

    enemy_img = pg.image.load('assets/sprites/first_enemy.png')
    enemy_img = pg.transform.scale(enemy_img, (300, 150))

    plane_img = pg.image.load('assets/sprites/ship.png')
    plane_img = pg.transform.scale(plane_img, (105, 90))

    #Создание групп спрайтов
    bullet_group = pg.sprite.Group()
    enemy_group = pg.sprite.Group()
    enemy_bullet_group = pg.sprite.Group()
    super_bullet_group = pg.sprite.Group()

    #Добавление музыки
    game_music = pg.mixer.Sound('assets/audio/game_music.mp3')
    game_music.set_volume(0.15)
    if music_enabled and game_music:
        game_music.play(-1)

    #Создание самолёта
    plane = PlaneController(plane_img, (250, 700))

    #Создание врагов
    for i in range(2):
        enemy = FirstLevelEnemyController(enemy_img, (190 + i * 300, -100))  # ПРАВИЛЬНО
        enemy_group.add(enemy)

    health_text = font_small.render('Health:', True, (255, 255, 255))
    super_blow_text = font_small.render('Super_blow:', True, (255, 255, 255))

    reset_game_timers()

    while running:
        current_time = pg.time.get_ticks() - pause_duration
        keys = pg.key.get_pressed()
        pg.mouse.set_visible(False)

        #Логика смены режимов стрельбы врагов
        if current_time - time_for_flag > flag_delay:
            flag = random.randint(1, 2)
            time_for_flag = current_time

        if current_time - mode_change_time > mode_duration:
            current_shooting_mode = random.choice(shooting_modes)
            mode_change_time = current_time
            wave_shot_count = 0
            shooting_modes = copy_shooting_modes.copy()

        #Логика обработки кликов
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pause_start_time = pg.time.get_ticks()
                    result = pause_menu(screen, font_medium, font_small, white, blue, gray, black)
                    if result == "menu":
                        game_music.stop()
                        return "menu"
                    elif result == "quit":
                        pg.quit()
                        sys.exit()
                    else:
                        pause_duration += pg.time.get_ticks() - pause_start_time

                elif event.key == pg.K_v and plane.model.super_blow >= 50:
                    #Добавление супер-удара
                    bullet_position = (plane.rect.centerx + 5, plane.rect.centery - 25)
                    super_bullet = BulletController(super_bullet_img, bullet_position)
                    super_bullet.speed_y += BULLET_SPEED
                    super_bullet_group.add(super_bullet)
                    plane.model.super_blow = 0

        if keys[pg.K_SPACE]:
            if current_time - last_shot1 > shoot_delay:
                bullet_position = (plane.rect.centerx + 5, plane.rect.centery - 25)
                # Создание обычных пуль
                bullet = BulletController(bullet_img, bullet_position)
                bullet.speed_y += BULLET_SPEED
                bullet_group.add(bullet)
                last_shot1 = current_time

        # Обработка смены режимов стрельбы
        if current_shooting_mode == "default":
            if "default" in shooting_modes:
                shooting_modes.remove("default")

            if flag == 1:
                for enemy in enemy_group:
                    if enemy.rect.bottom < 300:
                        enemy.rect.y += enemy.speed_y
                    else:
                        enemy.model.speed_y = 0

            elif flag == 2:
                for enemy in enemy_group:
                    if enemy.model.movement_phase == 1:
                        if enemy.rect.bottom < 800:
                            enemy.model.speed_y = 3
                            enemy.rect.y += enemy.model.speed_y
                        else:
                            enemy.model.speed_y = 0
                            enemy.model.movement_phase = 2

                    if enemy.model.movement_phase == 2:
                        if enemy.rect.bottom > 300:
                            enemy.model.speed_y = 3
                            enemy.rect.y -= enemy.model.speed_y
                        else:
                            enemy.model.speed_y = 0
                            enemy.model.movement_phase = 0

            if current_time - last_shot2 > enemy_shoot_delay:
                for enemy in enemy_group:
                    bullet_position = (enemy.rect.centerx, enemy.rect.bottom)
                    enemy_bullet = EnemyBulletController(enemy_bullet_img, bullet_position, trajectory_x)
                    enemy_bullet_group.add(enemy_bullet)

                trajectory_x += random.randint(1, 5)
                if trajectory_x >= 5:
                    trajectory_x = 0
                last_shot2 = current_time

        elif current_shooting_mode == "wave":
            if "wave" in shooting_modes:
                shooting_modes.remove("wave")

            if current_time - last_shot2 > wave_delay and wave_shot_count < 2:
                for enemy in enemy_group:
                    for i in range(-2, 3):
                        bullet_position = (enemy.rect.centerx, enemy.rect.bottom)
                        enemy_bullet = EnemyBulletController(enemy_bullet_img, bullet_position,i * 2)
                        enemy_bullet_group.add(enemy_bullet)

                wave_shot_count += 1
                if wave_shot_count >= 1:
                    last_shot2 = current_time
                    wave_shot_count = 0

        elif current_shooting_mode == "barrage":
            if "barrage" in shooting_modes:
                shooting_modes.remove("barrage")

            if current_time - last_shot2 > enemy_shoot_delay // 3:
                for enemy in enemy_group:
                    bullet_position = (enemy.rect.centerx, enemy.rect.bottom)
                    enemy_bullet = EnemyBulletController(enemy_bullet_img, bullet_position, trajectory_x, speed_y=3)
                    enemy_bullet_group.add(enemy_bullet)

                last_shot2 = current_time
                trajectory_x += random.randint(1, 5)
                if trajectory_x >= 5:
                    trajectory_x = 0

        #Отрисовка фона, полоски здоровья и супер-удара
        screen.blit(background, (0, 0))
        screen.blit(health_text, (5, 5))
        screen.blit(super_blow_text, (5, 50))

        draw_hearts(screen, 70, 6, plane.model.health, 10)

        #Отрисовка сердечек
        for enemy in enemy_group:
            draw_health_bar(screen, enemy.rect.x + 110, enemy.rect.top - 22, enemy.model.health, 100)

        draw_super_blow(screen, 110, 59, plane.model.super_blow, 50)

        #Отрисовка всех спрайтов
        custom_draw(enemy_group)
        enemy_group.update(current_time)

        plane.move(keys, screen_width, screen_height)
        plane.draw(screen)

        bullet_group.draw(screen)
        bullet_group.update()

        super_bullet_group.draw(screen)
        super_bullet_group.update()

        custom_draw(enemy_bullet_group)
        enemy_bullet_group.update()

        enemy_hits = pg.sprite.groupcollide(bullet_group, enemy_group, True, False, pg.sprite.collide_mask)

        #Обработка попаданий пуль во врагов
        for bullet, enemies in enemy_hits.items():
            for enemy in enemies:
                enemy.model.health -= 1
                plane.model.super_blow += 1
                if enemy.model.health <= 0:
                    enemy.kill()

        super_hits = pg.sprite.groupcollide(super_bullet_group, enemy_group, True, False, pg.sprite.collide_mask)

        # Обработка попаданий супер-удара во врагов
        for bullet, enemies in super_hits.items():
            for enemy in enemies:
                enemy.model.health -= 20
                if enemy.model.health <= 0:
                    enemy.kill()

        # Обработка попаданий врагами по самолётику
        for bullet in enemy_bullet_group:
            if pg.sprite.collide_mask(bullet, plane):
                bullet.kill()
                plane.model.health -= 1

                # Обработка смерти самолётика
                if plane.model.health <= 0:
                    running = False
                    result = ending_menu(screen, font_large, font_medium, font_small, white, blue, gray)
                    if result == "restart":
                        game_music.stop()
                        return "game"
                    elif result == "menu":
                        return "menu"

        # Обработка прикосновений врагов по самолётика
        for enemy in enemy_group:
            if pg.sprite.collide_mask(enemy, plane):
                plane.model.health -= 0.1
                # Обработка смерти самолётика
                if plane.model.health <= 0:
                    running = False
                    result = ending_menu(screen, font_large, font_medium, font_small, white, blue, gray)
                    if result == "restart":
                        game_music.stop()
                        return "game"
                    elif result == "menu":
                        return "menu"

        # Обработка смерти всех врагов
        if not enemy_group:
            running = False
            result = ending_menu(screen, font_large, font_medium, font_small, white, blue, gray)
            if result == "restart":
                game_music.stop()
                return "game"
            elif result == "menu":
                return "menu"

        pg.display.flip()
        clock.tick((FPS))

    game_music.stop()
    return "menu"