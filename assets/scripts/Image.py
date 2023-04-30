import pygame as pg

class Image(pg.sprite.Sprite):
    def __init__(self, image, size, x, y):
        pg.sprite.Sprite.__init__(self)

        image_scale = size / image.get_rect().width
        new_width= image.get_rect().width*image_scale
        new_height = image.get_rect().height*image_scale
        self.image = pg.transform.scale(image, (new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]