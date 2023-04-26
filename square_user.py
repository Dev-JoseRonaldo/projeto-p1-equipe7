import pygame as pg


class Square_user:
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, surface):
        pg.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))

    def move_left(self):
        if self.x > 100:
            self.x -= 100

    def move_right(self):
        if self.x < 600:
            self.x += 100

    def move_center(self, MIDDLE):
        self.x = MIDDLE