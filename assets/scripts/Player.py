from assets.scripts.Image import *

class Player(Image):
    points = 0

    def __init__(self,image, size, x, y):
        super().__init__(image, size, x, y)
        self.x = x
        self.y = y
        self.size = size

    def move_left(self):
        if self.rect.x > 100:
            self.rect.x -= 100

    def move_right(self):
        if self.rect.x < 600:
            self.rect.x += 100
