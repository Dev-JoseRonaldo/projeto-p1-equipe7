import pygame as pg
from assets.scripts.Player import *
from assets.scripts.Enemy import *
from assets.scripts.Powerup import *
from assets.scripts.Powerup_spawner import *
from assets.scripts.Enemy_spawner import *
from assets.scripts.Score import *
from assets.scripts.Text import *
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
    life = Image(IMAGE_LIFE, SIZE_LIFE, x, 20)
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
IMAGE_PLAYER = pg.image.load('./assets/sprites/capibara1.png')
IMAGE_PLAYER2 = pg.image.load('./assets/sprites/capibara2.png')
SIZE_PLAYER = 75
X_INITIAL = WIDTH//2 - SIZE_PLAYER//2
Y_INITIAL = 600

player_group = pg.sprite.Group()
player = Player(IMAGE_PLAYER, IMAGE_PLAYER2, SIZE_PLAYER, X_INITIAL, Y_INITIAL, lifes)
player_group.add(player)

# score inicial
start_time = time.time()
score = Score(start_time)
current_score = score.get_score
SIZE_POWERUP_UI = 30
apple_image =  Image(pg.image.load('./assets/sprites/powerups/apple.png'), SIZE_POWERUP_UI, WIDTH/2 - SIZE_POWERUP_UI*3, 20)
avocado_image =  Image(pg.image.load('./assets/sprites/powerups/avocado.png'), SIZE_POWERUP_UI, WIDTH/2, 20)
watermelon_image =  Image(pg.image.load('./assets/sprites/powerups/watermelon.png'), SIZE_POWERUP_UI, WIDTH/2 + SIZE_POWERUP_UI*3, 20)

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
fps = 144
last_update_time = pg.time.get_ticks()

# Clique mouse nos botões
def mouse_click(position_click, postion_button_play, postion_button_menu, button_width, button_height):
    click_x, click_y = position_click
    button_x, button_y = postion_button_play
    button_a, button_b = postion_button_menu
    if button_x - (button_width//2) < click_x < button_x + (button_width//2) and button_y - (button_height//2) < click_y < button_y + (button_height//2):
        # score zera
        start_time = time.time()
        score = Score(start_time)
        return False, score
    elif button_a - (button_width//2) < click_x < button_a + (button_width//2) and button_b - (button_height//2) < click_y < button_b + (button_height//2):
        # score zera
        start_time = time.time()
        score = Score(start_time)
        return False, score
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
        if event.type == pg.MOUSEBUTTONUP and GAME_OVER == True:
            GAME_OVER, score = mouse_click(pg.mouse.get_pos(), (350, 400), (350, 480), 150, 100)
            player.return_life()
            player.powerups_colleteds = [0,0,0]

    if GAME_OVER == False:

        # score atual
        current_score = score.get_score()

        GAME_OVER = player.check_die()

        #updates
        powerup_spawner.update(player, score)
        enemy_spawner.update(player)
        enemy_spawner2.update(player)
        enemy_spawner3.update(player)
        enemy_spawner4.update(player)
        enemy_spawner5.update(player)
        player.get_powerups_colleteds()
        score.update() # printa o score atual na tela
        score_text = text(30, 10, 5, int(current_score), "topleft", (255,255,255))
        apple_count = text(25, WIDTH/2 - 75, 7, f'x{player.powerups_colleteds[0]}', "topleft", (255,255,255))
        avocado_count = text(25, WIDTH/2 + 20, 7, f'x{player.powerups_colleteds[1]}', "topleft", (255,255,255))
        watermelon_count = text(25, WIDTH/2 + 115, 7, f'x{player.powerups_colleteds[2]}', "topleft", (255,255,255))

        current_time = pg.time.get_ticks()
        time_elapsed = current_time - last_update_time
        if time_elapsed > 200:
        # atualiza o sprite
            player.update()
            last_update_time = current_time


        #renderiza os elemetos em tela
        screen.fill((0, 0, 0))
        player_group.draw(screen)
        powerup_spawner.powerup_group.draw(screen)
        enemy_spawner.enemy_group.draw(screen)
        enemy_spawner2.enemy_group.draw(screen)
        enemy_spawner3.enemy_group.draw(screen)
        enemy_spawner4.enemy_group.draw(screen)
        enemy_spawner5.enemy_group.draw(screen)
        score_text.blit(screen)
        apple_image.blit(screen)
        apple_count.blit(screen)
        avocado_image.blit(screen)
        avocado_count.blit(screen)
        watermelon_image.blit(screen)
        watermelon_count.blit(screen)
        lifes.draw(screen)
        pg.display.flip()
    else:
        game_over = GameOver(screen, int(current_score), player.powerups_colleteds)
        game_over.game_over_screen()
        

    pg.display.flip()