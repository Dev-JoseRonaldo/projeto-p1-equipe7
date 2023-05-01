import pygame as pg
from assets.scripts.Player import *
from assets.scripts.Enemy import *

pg.init()

#tela
WIDTH = 700
HEIGHT = 700
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Game p1")

GAME_OVER = False

# Vidas
IMAGE_LIFE = pg.image.load('./assets/sprites/life.png')
SIZE_LIFE = 25

lifes = pg.sprite.Group()
life_positions_x = [620, 650, 680]

for x in life_positions_x:
    life = Image(IMAGE_LIFE, SIZE_LIFE, x, 10)
    lifes.add(life)


#player
IMAGE_PLAYER = pg.image.load('./assets/sprites/capibara.png')
SIZE_PLAYER = 50
X_INITIAL = WIDTH//2 - SIZE_PLAYER//2
Y_INITIAL = 600

player_group = pg.sprite.Group()
player = Player(IMAGE_PLAYER, SIZE_PLAYER, X_INITIAL, Y_INITIAL, lifes)
player_group.add(player)

#inimigos
ENEMY_Y = 0
ENEMY_SPEED = 2.5

#inimigo (tronco)
IMAGE_ENEMY = pg.image.load('./assets/sprites/tronco.png')
ENEMY_SIZE = 75
ENEMY_POSITIONS_X = [100,200,300,400,500,600]

enemy_group = pg.sprite.Group()
enemy = Enemy(IMAGE_ENEMY, ENEMY_SIZE, ENEMY_POSITIONS_X[0], ENEMY_Y, ENEMY_SPEED, HEIGHT, ENEMY_POSITIONS_X)
enemy_group.add(enemy)


running = True
clock = pg.time.Clock()
fps = 120

while running:
    clock.tick(fps)
    
    #movimentação do personagem
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player.move_left()
            elif event.key == pg.K_RIGHT:
                player.move_right()
    

    player.check_die()
    
    #updates
    enemy.update(player)

    if enemy.get_collision_detected():
        # continua o jogo
        enemy = Enemy(IMAGE_ENEMY, ENEMY_SIZE, random.choice(ENEMY_POSITIONS_X), ENEMY_Y, ENEMY_SPEED, HEIGHT, ENEMY_POSITIONS_X)
        enemy_group = pg.sprite.Group(enemy)

    #renderiza os elemetos em tela
    screen.fill((0, 0, 0))
    enemy_group.draw(screen)
    player_group.draw(screen)
    lifes.draw(screen)
    pg.display.flip()