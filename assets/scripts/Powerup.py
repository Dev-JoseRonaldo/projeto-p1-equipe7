import random
from assets.scripts.Image import *
from assets.scripts.Score import *

class Powerup(Image):
    collision_detected = False
    
    def __init__(self, id, image, size, x, y, speed, height, positions_x, additional_points):
        super().__init__(image, size, x, y)
        self.id = id
        self.rect.x = random.choice(positions_x)
        self.rect.y = y
        self.size = size
        self.speed = speed
        self.height = height
        self.positions_x = positions_x
        self.additional_points = additional_points

    def update(self, player, score):
        self.move_y()
        self.colision_detect(player, score)

    def disable_powerup(self):
        self.set_speed(0)
        self.set_y(1000)

    def move_y(self):
        self.rect.y += self.speed

        if self.get_y() > self.height + 200:
            self.disable_powerup()

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

    def colision_detect(self, player, score):
        if self.rect.colliderect(player.rect) and not self.collision_detected:
            self.collision_detected = True

            self.disable_powerup()
            score.set_additional_score_on_collect_powerup(self.additional_points)
    
            print(f'Ganhou {self.additional_points} pontos')
            player.set_powerups_colleteds(self.id)
            score.set_additional_score_on_collect_powerup(self.additional_points)
    
     