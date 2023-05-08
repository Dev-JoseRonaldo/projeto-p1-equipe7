import pygame as pg
import random
from assets.scripts.Image import *
from assets.scripts.Speed import *

class Enemy(Image):
    collision_detected = False
    
    def __init__(self, id, image, size, x, y, speed, height, positions_x):
        super().__init__(image, size, x, y)
        self.rect.x = random.choice(positions_x)
        self.rect.y = y
        self.size = size
        self.speed = speed
        self.height = height
        self.positions_x = positions_x
        self.id = id

    def update(self, player, speed):
        self.move_y(speed)
        self.colision_detect(player)

    def disable_enemy(self):
        self.set_speed(0)
        self.set_y(1000)

    def move_y(self, speed):
        speed_value = speed.get_speed()
        self.rect.y += speed_value

        if self.get_y() > self.height + 200:
            self.disable_enemy()

    def get_y(self):
        return self.rect.y
    
    def set_y(self, y):
        self.rect.y = y

    def get_x(self):
        return self.rect.x
    
    def set_x(self, x):
        self.rect.x = x
    
    def set_speed(self, speed):
        self.speed = speed

    def get_collision_detected(self):
        return self.collision_detected

    def colision_detect(self, player):
        if self.rect.colliderect(player.rect) and not self.collision_detected:
            self.collision_detected = True
            
            self.disable_enemy()

            player.lifes.remove(player.lifes.sprites()[0])