import random
from assets.scripts.Image import *
from assets.scripts.Score import *
from assets.scripts.Speed import *

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

    def update(self, player, score, speed, sound):
        self.move_y(speed)
        self.colision_detect(player, score, sound)

    def disable_powerup(self):
        self.set_speed(0)
        self.set_y(1000)

    def move_y(self, speed):
        speed_value = speed.get_speed()
        self.rect.y += speed.get_speed()

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

    def colision_detect(self, player, score, sound):
        if self.rect.colliderect(player.rect) and not self.collision_detected:
            self.collision_detected = True

            sound.play()

            self.disable_powerup()
            score.set_additional_score_on_collect_powerup(self.additional_points)
    
            player.set_powerups_colleteds(self.id)
            score.set_additional_score_on_collect_powerup(self.additional_points)
    
     