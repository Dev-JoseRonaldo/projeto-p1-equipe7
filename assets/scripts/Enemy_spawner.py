import pygame as pg
import random
from assets.scripts.Enemy import *

class Enemy_spawner:
    lasts_drawn = []
    def __init__(self, enemys):
        self.enemys = enemys
        self.enemy_group = pg.sprite.Group()
        self.spawn_timer = random.randrange(50, 550)

    def update(self, player):
        self.enemy_group.update(player)

        if self.spawn_timer == 0:
            self.spawn_enemy()
            self.spawn_timer = random.randrange(250, 550)
        else:
            self.spawn_timer -= 1

    def spawn_enemy(self):
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

        new_enemy = Enemy(enemy['id'], pg.image.load(enemy['image']), enemy['size'], enemy['x'], enemy['y'], enemy['speed'], enemy['height'], ENEMY_POSITION_X)

        self.lasts_drawn.append(new_enemy.get_x())
        self.enemy_group = pg.sprite.Group(new_enemy)