from assets.scripts.Image import *

class Player(Image):
    points = 0

    def __init__(self,image, size, x, y, lifes):
        super().__init__(image, size, x, y)
        self.x = x
        self.y = y
        self.size = size
        self.lifes = lifes

    def move_left(self):
        if self.rect.x > 100:
            self.rect.x -= 100

    def move_right(self):
        if self.rect.x < 600:
            self.rect.x += 100

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