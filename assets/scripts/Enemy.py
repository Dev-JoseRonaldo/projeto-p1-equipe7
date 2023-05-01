import pygame as pg
import random
from assets.scripts.Image import *

class Enemy(Image):
    collision_detected = False
    
    def __init__(self,image, size, x, y, speed, height, positions_x):
        super().__init__(image, size, x, y)
        self.rect.x = random.choice(positions_x)
        self.rect.y = y
        self.size = size
        self.speed = speed
        self.height = height
        self.positions_x = positions_x

    def update(self, player):
        self.move_y()
        self.colision_detect(player)

    def move_y(self):
        self.rect.y += self.speed

        if self.get_y() > self.height:
            self.set_y(0)
            self.set_x(random.choice(self.positions_x))

    def get_y(self):
        return self.rect.y
    
    def set_y(self, y):
        self.rect.y = y

    def get_x(self):
        return self.rect.x
    
    def set_x(self, x):
        self.rect.x = x

    def get_collision_detected(self):
        return self.collision_detected

    def colision_detect(self, player):
        if self.rect.colliderect(player.rect) and not self.collision_detected:
            print("Colisão detectada")
            self.collision_detected = True
            self.speed = 0
            player.lifes.remove(player.lifes.sprites()[0])