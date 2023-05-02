import pygame as pg
import random
from assets.scripts.Powerup import *

class Powerup_spawner:
    powerups_collected = [0,0,0]
    def __init__(self, powerups):
        self.powerups = powerups
        self.powerup_group = pg.sprite.Group()
        self.spawn_timer = random.randrange(1905, 2008)

    def update(self, player):
        self.powerup_group.update(player)

        if self.spawn_timer == 0:
            self.spawn_powerup()
            self.spawn_timer = random.randrange(1905, 2008)
        else:
            self.spawn_timer -= 1

    def spawn_powerup(self):
        powerup = random.choices(self.powerups, weights=[60,20,10])[0]
        index = self.powerups.index(powerup)
        new_powerup = Powerup(powerup['id'], pg.image.load(powerup['image']), powerup['size'], powerup['x'], powerup['y'], powerup['speed'], powerup['height'], powerup['positions_x'], powerup['additional_points'])
        
        self.powerup_group = pg.sprite.Group(new_powerup)