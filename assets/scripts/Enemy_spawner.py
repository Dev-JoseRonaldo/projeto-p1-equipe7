import pygame as pg
import random
from assets.scripts.Enemy import *

class Enemy_spawner:
    lasts_drawn = []
    def __init__(self, enemys):
        self.enemys = enemys
        self.enemy_group = pg.sprite.Group()
        self.spawn_timer = random.randrange(50, 300)

    def update(self, player, speed, sound):
        self.enemy_group.update(player, speed, sound)
        if self.spawn_timer == 0:
            self.spawn_enemy(speed)
            if speed.get_speed() >= 8:
                self.spawn_timer = random.randrange(100, 200)
            elif speed.get_speed() >= 10:
                self.spawn_timer = random.randrange(80, 150)
            elif speed.get_speed() >= 13:
                self.spawn_timer = random.randrange(50, 100)
            else: 
                self.spawn_timer = random.randrange(200, 300)
        else:
            self.spawn_timer -= 1

    def spawn_enemy(self, speed):
        #escolhendo um inimigo aleatoriamente
        enemy = random.choices(self.enemys)[0]

        #evitando redenrizar inimigos na mesma posição
        if len(self.lasts_drawn) <= 5:
            dif1 = set(enemy['positions_x']).difference(set(self.lasts_drawn))
            dif2 = set(set(self.lasts_drawn)).difference(enemy['positions_x'])

            ENEMY_POSITION_X = list(dif1.union(dif2))
        else:
            ENEMY_POSITION_X = enemy['positions_x']
            self.lasts_drawn.clear()

        new_enemy = Enemy(enemy['id'], pg.image.load(enemy['image']), enemy['size'], enemy['x'], enemy['y'], speed, enemy['height'], ENEMY_POSITION_X)

        self.lasts_drawn.append(new_enemy.get_x())
        self.enemy_group = pg.sprite.Group(new_enemy)