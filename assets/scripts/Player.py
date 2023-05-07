from assets.scripts.Animation import *
from assets.scripts.Image import *

class Player(Animacao):
    def __init__(self,image, image2, size, x, y, lifes):
        super().__init__(image, image2, size, x, y)
        self.x = x
        self.y = y
        self.size = size
        self.lifes = lifes
        self.powerups_colleteds = [0,0,0]

    def move_left(self, width_screen):
        if self.rect.x > 200:
            self.rect.x -= 100

    def move_right(self, width_screen):
        if self.rect.x < width_screen - 200:
            self.rect.x += 100

    def set_powerups_colleteds(self, index):
        self.powerups_colleteds[index] += 1

    def get_powerups_colleteds(self):
        return self.powerups_colleteds
    
    def check_die(self):
        if len(self.lifes) == 0:
            return True
        return False

    def reset_data(self, width_screen):
        #reset lifes
        IMAGE_LIFE = pg.image.load('./assets/sprites/life.png')
        SIZE_LIFE = 25
        life_positions_x = [720, 750, 780]
            
        for x in life_positions_x:
            life = Image(IMAGE_LIFE, SIZE_LIFE, x, 20)
            self.lifes.add(life)

        self.rect.x = (width_screen / 2) - (self.size / 2) #tentativa de colocar a capivara para o meio novamente

        #reset powerups
        self.powerups_colleteds = [0,0,0]
