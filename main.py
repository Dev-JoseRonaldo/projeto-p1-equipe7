import pygame as pg
from assets.scripts.Player import *
from assets.scripts.Enemy import *
from assets.scripts.Powerup import *
from assets.scripts.Powerup_spawner import *
from assets.scripts.Enemy_spawner import *
from assets.screens.game_over import *

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

#powerups
POWERUP_SPEED = 3.5
POWERUP_POSITIONS_X = [100,200,300,400,500,600]

POWERUPS_MOCK = [{
                'id': 0,
                'image': './assets/sprites/powerups/apple.png', 
                'size': 50,
                'x': POWERUP_POSITIONS_X[0], 
                'y': -100, 
                'speed': POWERUP_SPEED, 
                'height': HEIGHT, 
                'positions_x': POWERUP_POSITIONS_X, 
                'additional_points': 2500
            },
            {
                'id': 1,
                'image': './assets/sprites/powerups/avocado.png', 
                'size': 50,
                'x': POWERUP_POSITIONS_X[0], 
                'y': -100, 
                'speed': POWERUP_SPEED, 
                'height': HEIGHT, 
                'positions_x': POWERUP_POSITIONS_X, 
                'additional_points': 5000
            },
            {
                'id': 2,
                'image': './assets/sprites/powerups/watermelon.png', 
                'size': 50,
                'x': POWERUP_POSITIONS_X[0], 
                'y': -100, 
                'speed': POWERUP_SPEED, 
                'height': HEIGHT, 
                'positions_x': POWERUP_POSITIONS_X, 
                'additional_points': 10000
            }
]

powerup_spawner = Powerup_spawner(POWERUPS_MOCK)

#player
IMAGE_PLAYER = pg.image.load('./assets/sprites/capibara.png')
SIZE_PLAYER = 50
X_INITIAL = WIDTH//2 - SIZE_PLAYER//2
Y_INITIAL = 600

player_group = pg.sprite.Group()
player = Player(IMAGE_PLAYER, SIZE_PLAYER, X_INITIAL, Y_INITIAL, lifes)
player_group.add(player)

#inimigo

ENEMY_POSITIONS_X = [100,200,300,400,500,600]
ENEMY_SPEED = 3.5

ENEMYS_MOCK = [
    {
        'id': 0,
        'image': './assets/sprites/enemys/trunk.png', 
        'size': 75,
        'x': ENEMY_POSITIONS_X[0], 
        'y': -100, 
        'speed': ENEMY_SPEED, 
        'height': HEIGHT, 
        'positions_x': ENEMY_POSITIONS_X, 
    },
    {
        'id': 1,
        'image': './assets/sprites/enemys/rock.png', 
        'size': 75,
        'x': ENEMY_POSITIONS_X[0], 
        'y': -100, 
        'speed': ENEMY_SPEED, 
        'height': HEIGHT, 
        'positions_x': ENEMY_POSITIONS_X, 
    },
    {
        'id': 2,
        'image': './assets/sprites/enemys/enemy3.png', 
        'size': 75,
        'x': ENEMY_POSITIONS_X[0], 
        'y': -100, 
        'speed': ENEMY_SPEED, 
        'height': HEIGHT, 
        'positions_x': ENEMY_POSITIONS_X, 
    },
]

enemy_spawner = Enemy_spawner(ENEMYS_MOCK)
enemy_spawner2 = Enemy_spawner(ENEMYS_MOCK)
enemy_spawner3 = Enemy_spawner(ENEMYS_MOCK)
enemy_spawner4 = Enemy_spawner(ENEMYS_MOCK)
enemy_spawner5 = Enemy_spawner(ENEMYS_MOCK)

running = True
clock = pg.time.Clock()
fps = 120

def mouse_click(position_click, postion_button_play, postion_button_menu, button_width, button_height):
    click_x, click_y = position_click
    button_x, button_y = postion_button_play
    button_a, button_b = postion_button_menu
    if button_x - (button_width//2) < click_x < button_x + (button_width//2) and button_y - (button_height//2) < click_y < button_y + (button_height//2):
        return False
    elif button_a - (button_width//2) < click_x < button_a + (button_width//2) and button_b - (button_height//2) < click_y < button_b + (button_height//2):
        return False
    return True

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
        if event.type == pygame.MOUSEBUTTONUP and GAME_OVER == True:
            GAME_OVER = mouse_click(pygame.mouse.get_pos(), (350, 400), (350, 480), 150, 100)
            player.return_life()

    if GAME_OVER == False:

        GAME_OVER = player.check_die()

        #updates
        powerup_spawner.update(player)
        enemy_spawner.update(player)
        enemy_spawner2.update(player)
        enemy_spawner3.update(player)
        enemy_spawner4.update(player)
        enemy_spawner5.update(player)
        player.get_powerups_colleteds()

        #renderiza os elemetos em tela
        screen.fill((0, 0, 0))
        player_group.draw(screen)
        powerup_spawner.powerup_group.draw(screen)
        enemy_spawner.enemy_group.draw(screen)
        enemy_spawner2.enemy_group.draw(screen)
        enemy_spawner3.enemy_group.draw(screen)
        enemy_spawner4.enemy_group.draw(screen)
        enemy_spawner5.enemy_group.draw(screen)
        lifes.draw(screen)
    else:
        game_over = GameOver(screen, player.powerups_colleteds)
        game_over.game_over_screen()

    pg.display.flip()