from assets.scripts.Score import *


class Speed:
    def __init__(self, initial_speed, increase_value):
        self.initial_speed = initial_speed
        self.speed = initial_speed
        self.increase_value = increase_value

    def set_speed(self, score):
        score_value = score.get_score()
        if score_value > 0:
            speed_upgraded = self.initial_speed + score_value//2000 * self.increase_value
            if self.speed != speed_upgraded:
                print(f'era {self.speed} agora virou {speed_upgraded}')
                self.speed = speed_upgraded

    def get_speed(self):
        return self.speed

    def update(self, score):
        self.set_speed(score)
