import pygame as pg
from assets.scripts.Player import *
from assets.scripts.Enemy import *
from assets.scripts.Powerup import *
from assets.scripts.Powerup_spawner import *
from assets.scripts.Enemy_spawner import *
from assets.scripts.Score import *
from assets.scripts.Text import *
from assets.scripts.Button import *
from assets.screens.game_over import *
from assets.screens.menu import *

pg.init()

#tela
WIDTH = 896
HEIGHT = 704
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Game p1")

#define telas abertas
MENU = True
GAME_OVER = False

#variáveis tela menu 
pos_x_game_title1 = 320 #mudar resolução aqui 
pos_y_game_title1 = 160 #mudar resolução aqui 
pos_x_game_title2 = 400 #mudar resolução aqui 
pos_y_game_title2 = 245 #mudar resolução aqui 
width_menu_button = 150
height_menu_button = 100
pos_x_play_menu = 370 #mudar resolução aqui 
pos_y_play_menu = 340 #mudar resolução aqui 
pos_x_end_menu = 370 #mudar resolução aqui 
pos_y_end_menu = 420 #mudar resolução aqui 

#variáveis tela game over
width_game_over_button = 150
height_game_over_button = 100
width_powerup_img = 40
height_powerup_img = 40
pos_x_title_game_over = 300 #mudar resolução aqui 
pos_y_title_game_over = 160 #mudar resolução aqui 
pos_x_message_score = 360 #mudar resolução aqui 
pos_y_message_score = 245 #mudar resolução aqui 
pos_x_image_powerup1 = 280 #mudar resolução aqui 
pos_x_image_powerup2 = 400 #mudar resolução aqui 
pos_x_image_powerup3 = 520 #mudar resolução aqui 
pos_y_image_powerup1 = 290 #mudar resolução aqui 
pos_y_image_powerup2 = 290 #mudar resolução aqui 
pos_y_image_powerup3 = 290 #mudar resolução aqui 
pos_x_label_powerup1 = 330 #mudar resolução aqui 
pos_x_label_powerup2 = 450 #mudar resolução aqui 
pos_x_label_powerup3 = 570 #mudar resolução aqui 
pos_y_label_powerup1 = 290 #mudar resolução aqui 
pos_y_label_powerup2 = 290 #mudar resolução aqui 
pos_y_label_powerup3 = 290 #mudar resolução aqui 
pos_x_restart_game_over = 370 #mudar resolução aqui 
pos_y_restart_game_over = 400 #mudar resolução aqui 
pos_x_menu_game_over = 370 #mudar resolução aqui 
pos_y_menu_game_over = 480 #mudar resolução aqui 

# Vidas
IMAGE_LIFE = pg.image.load('./assets/sprites/life.png')
SIZE_LIFE = 25

lifes = pg.sprite.Group()

#powerups
POWERUP_SPEED = 4
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
player.reset_data(WIDTH)

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
ENEMY_SPEED = 4

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
fps = 60
last_update_time = pg.time.get_ticks()

#paralax
bg_image = pg.image.load(f'assets/sprites/paralax/bg.png').convert_alpha()
bg_heigh = bg_image.get_height()

scroll = 0


while running:
    clock.tick(fps)

    #movimentação do personagem
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player.move_left(WIDTH)
            elif event.key == pg.K_RIGHT:
                player.move_right(WIDTH)
        elif event.type == pg.MOUSEBUTTONUP:
            if MENU == True and GAME_OVER == False:
                click_menu = Button(pg.mouse.get_pos(), (450, pos_y_play_menu), (450, pos_y_end_menu), width_menu_button, height_menu_button, 0)
                MENU, running = click_menu.mouse_click_menu()
            elif GAME_OVER == True:
                player.reset_data(WIDTH)
                click_game_over = Button(pg.mouse.get_pos(), (450, pos_y_restart_game_over), (450, pos_y_menu_game_over), width_game_over_button, height_game_over_button, current_score)
                GAME_OVER, MENU, score = click_game_over.mouse_click_game_over()

    if MENU == True and GAME_OVER == False:
        menu = Menu(screen, pos_x_game_title1, pos_y_game_title1, pos_x_game_title2, pos_y_game_title2, width_menu_button, height_menu_button, pos_x_play_menu, pos_y_play_menu, pos_x_end_menu, pos_y_end_menu)
        menu.menu_screen()
    elif MENU == False and GAME_OVER == False:

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
        score_text = text(30, 120, 5, int(current_score), "topleft", (0,0,0))
        apple_count = text(25, WIDTH/2 - 75, 7, f'x{player.powerups_colleteds[0]}', "topleft", (0,0,0))
        avocado_count = text(25, WIDTH/2 + 15, 7, f'x{player.powerups_colleteds[1]}', "topleft", (0,0,0))
        watermelon_count = text(25, WIDTH/2 + 110, 7, f'x{player.powerups_colleteds[2]}', "topleft", (0,0,0))

        current_time = pg.time.get_ticks()
        time_elapsed = current_time - last_update_time
        if time_elapsed > 200:
        # atualiza o sprite
            player.update()
            last_update_time = current_time

        if scroll <= bg_heigh*3/4:
            scroll += 4
        else:
            scroll = 0
        
        #renderiza os elemeNtos em tela
        screen.fill((0, 0, 0))
        screen.blit(bg_image, (0, -bg_heigh*3/4 + scroll))
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
        game_over = GameOver(screen, int(current_score), player.powerups_colleteds, width_game_over_button, height_game_over_button, width_powerup_img, height_powerup_img, pos_x_title_game_over, pos_y_title_game_over,pos_x_message_score, pos_y_message_score, pos_x_image_powerup1, pos_x_image_powerup2, pos_x_image_powerup3, pos_y_image_powerup1, pos_y_image_powerup2, pos_y_image_powerup3, pos_x_label_powerup1, pos_x_label_powerup2, pos_x_label_powerup3, pos_y_label_powerup1, pos_y_label_powerup2, pos_y_label_powerup3, pos_x_restart_game_over, pos_y_restart_game_over, pos_x_menu_game_over, pos_y_menu_game_over)
        game_over.game_over_screen()
    pg.display.flip()