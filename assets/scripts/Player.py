from assets.scripts.Image import *

class Player(Image):
    def __init__(self,image, size, x, y, lifes):
        super().__init__(image, size, x, y)
        self.x = x
        self.y = y
        self.size = size
        self.lifes = lifes
        self.points = 0
        self.powerups_colleteds = [0,0,0]

    def move_left(self):
        if self.rect.x > 100:
            self.rect.x -= 100

    def move_right(self):
        if self.rect.x < 600:
            self.rect.x += 100

    def set_powerups_colleteds(self, index):
        self.powerups_colleteds[index] += 1

    def get_powerups_colleteds(self):
        return self.powerups_colleteds
    
    def check_die(self):
        if len(self.lifes) == 0:
            print('Game Over - Carregar tela de game over aqui')

            #codigo para retornar 3 vidas do personagem ao retartar o jogo
            IMAGE_LIFE = pg.image.load('./assets/sprites/life.png')
            SIZE_LIFE = 25
            life_positions_x = [620, 650, 680]
            
            for x in life_positions_x:
                life = Image(IMAGE_LIFE, SIZE_LIFE, x, 10)
                self.lifes.add(life)
