from assets.scripts.Powerup import *

import time


class Score():
    score = 0
    collision_detected = True

    def __init__(self, start_time):
        self.end_time = time.time()
        self.start_time = start_time
        self.additional_points = 0

    def end_timer(self):
        self.end_time = time.time()

    def update(self):        
        print(f'{self.score:.4f}')
        self.end_timer()
        self.set_score()
    
    def set_additional_score_on_collect_powerup(self, additional_points):
        self.score += additional_points
        self.additional_points += additional_points

    def set_score(self):
        self.score = (self.end_time - self.start_time)*1000 + self.additional_points

    def get_score(self):
        return self.score
