import pygame as pg
import time

class Animacao(pg.sprite.Sprite):
    def __init__(self, image1, image2, size, x, y):
        pg.sprite.Sprite.__init__(self)

        self.images = [image1, image2]
        self.current_image = 0

        image_scale = size / image1.get_rect().width
        new_width = image1.get_rect().width * image_scale
        new_height = image1.get_rect().height * image_scale
        self.image = pg.transform.scale(self.images[self.current_image], (new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):

        self.current_image = (self.current_image + 1) % len(self.images)
        self.image = pg.transform.scale(self.images[self.current_image], self.rect.size)

