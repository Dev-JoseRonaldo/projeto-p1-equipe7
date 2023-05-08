from assets.scripts.Powerup import *
from assets.scripts.Speed import *

import time


class Score():
    score = 0
    collision_detected = True

    def __init__(self, start_time, initial_speed):
        self.end_time = time.time()
        self.start_time = start_time
        self.additional_points = 0
        self.initial_speed = initial_speed

    def end_timer(self):
        self.end_time = time.time()

    def update(self, speed):
        self.end_timer()
        self.set_score(speed)

    def set_additional_score_on_collect_powerup(self, additional_points):
        self.score += additional_points
        self.additional_points += additional_points

    def set_score(self, speed):
        score_value = int(self.end_time * 10) - int(self.start_time * 10)
        self.score = score_value * 10 + self.additional_points
        speed_value = speed.get_speed()
        self.score *= speed_value / self.initial_speed
        self.score = self.score // 10 * 10

    def get_score(self):
        return self.score
