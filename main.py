import pygame as pg
from assets.scripts.Player import *
from assets.scripts.Enemy import *
from assets.scripts.Powerup import *
from assets.scripts.Powerup_spawner import *
from assets.scripts.Enemy_spawner import *
from assets.scripts.Score import *
from assets.scripts.Text import *
from assets.scripts.Button import *
from assets.scripts.Speed import *
from assets.screens.game_over import *
from assets.screens.menu import *

#carrega os sons do jogo
def load_sounds():
    enemyhit = pg.mixer.Sound('./assets/sounds/enemy_hit.wav')
    getfood = pg.mixer.Sound('./assets/sounds/get_food.wav')
    gameover = pg.mixer.Sound('./assets/sounds/game_over.wav')
    menu_som = pg.mixer.Sound('./assets/sounds/menu_som.wav')
    music = pg.mixer.Sound('./assets/sounds/background_music.mp3')

    music.play(-1)
    music.set_volume(0.4)
    gameover.set_volume(0.4)
    enemyhit.set_volume(1)

    return (enemyhit, getfood, gameover, menu_som, music)

pg.init()
pg.mixer.init()

(enemyhit, getfood, gameover, menu_som, music) = load_sounds()

tocando_music = True

#tela
WIDTH = 896
HEIGHT = 704
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Game p1")

#define telas abertas
MENU = True
GAME_OVER = False

#variáveis tela menu 
pos_x_game_title1 = 250
pos_y_game_title1 = 130
pos_x_game_title2 = 380
pos_y_game_title2 = 220
width_menu_button = 100
height_menu_button = 100
pos_x_play_menu = 320
pos_y_play_menu = 340
pos_x_end_menu = 450
pos_y_end_menu = 340

#variáveis tela game over
width_game_over_button = 100
height_game_over_button = 100
width_powerup_img = 40
height_powerup_img = 40
pos_x_title_game_over = 250
pos_y_title_game_over = 140
pos_x_message_score = 360
pos_y_message_score = 225
pos_x_image_powerup1 = 290
pos_x_image_powerup2 = 400
pos_x_image_powerup3 = 510
pos_y_image_powerup1 = 280
pos_y_image_powerup2 = 280
pos_y_image_powerup3 = 280
pos_x_label_powerup1 = 330
pos_x_label_powerup2 = 440
pos_x_label_powerup3 = 550
pos_y_label_powerup1 = 280
pos_y_label_powerup2 = 280
pos_y_label_powerup3 = 280
pos_x_restart_game_over = 320
pos_y_restart_game_over = 340
pos_x_menu_game_over = 450
pos_y_menu_game_over = 340

# Vidas
IMAGE_LIFE = pg.image.load('./assets/sprites/life.png')
SIZE_LIFE = 25

lifes = pg.sprite.Group()

# velocidade inicial do game
initial_speed = 4
increase_value = 0.5  # é somado a velocidade conforme o score aumenta
speed = Speed(initial_speed, increase_value)
game_speed = speed.get_speed()

#powerups
POWERUP_POSITIONS_X = [100,200,300,400,500,600]

POWERUPS_MOCK = [{
                'id': 0,
                'image': './assets/sprites/powerups/apple.png', 
                'size': 50,
                'x': POWERUP_POSITIONS_X[0], 
                'y': -100, 
                'speed': game_speed, 
                'height': HEIGHT, 
                'positions_x': POWERUP_POSITIONS_X, 
                'additional_points': 250
            },
            {
                'id': 1,
                'image': './assets/sprites/powerups/blueberry.png', 
                'size': 60,
                'x': POWERUP_POSITIONS_X[0], 
                'y': -100, 
                'speed': game_speed, 
                'height': HEIGHT, 
                'positions_x': POWERUP_POSITIONS_X, 
                'additional_points': 500
            },
            {
                'id': 2,
                'image': './assets/sprites/powerups/watermelon.png', 
                'size': 50,
                'x': POWERUP_POSITIONS_X[0], 
                'y': -100, 
                'speed': game_speed, 
                'height': HEIGHT, 
                'positions_x': POWERUP_POSITIONS_X, 
                'additional_points': 1000
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
score = Score(start_time, initial_speed)
current_score = score.get_score()
SIZE_POWERUP_UI = 30
apple_image =  Image(pg.image.load('./assets/sprites/powerups/apple.png'), SIZE_POWERUP_UI, WIDTH/2 - SIZE_POWERUP_UI*3, 20)
blueberry_image =  Image(pg.image.load('./assets/sprites/powerups/blueberry.png'), SIZE_POWERUP_UI, WIDTH/2, 20)
watermelon_image =  Image(pg.image.load('./assets/sprites/powerups/watermelon.png'), SIZE_POWERUP_UI, WIDTH/2 + SIZE_POWERUP_UI*3, 20)

#inimigo

ENEMY_POSITIONS_X = [100,200,300,400,500,600]

ENEMYS_MOCK = [
    {
        'id': 0,
        'image': './assets/sprites/enemys/trunk.png', 
        'size': 100,
        'x': ENEMY_POSITIONS_X[0], 
        'y': -100, 
        'speed': game_speed, 
        'height': HEIGHT, 
        'positions_x': ENEMY_POSITIONS_X, 
    },
    {
        'id': 1,
        'image': './assets/sprites/enemys/rock.png', 
        'size': 75,
        'x': ENEMY_POSITIONS_X[0], 
        'y': -100, 
        'speed': game_speed, 
        'height': HEIGHT, 
        'positions_x': ENEMY_POSITIONS_X, 
    },
    {
        'id': 2,
        'image': './assets/sprites/enemys/tree.png', 
        'size': 100,
        'x': ENEMY_POSITIONS_X[0], 
        'y': -100, 
        'speed': game_speed, 
        'height': HEIGHT, 
        'positions_x': ENEMY_POSITIONS_X, 
    },
]

enemy_spawner = Enemy_spawner(ENEMYS_MOCK)
enemy_spawner2 = Enemy_spawner(ENEMYS_MOCK)
enemy_spawner3 = Enemy_spawner(ENEMYS_MOCK)
enemy_spawner4 = Enemy_spawner(ENEMYS_MOCK)
enemy_spawner5 = Enemy_spawner(ENEMYS_MOCK)
enemy_spawner6 = Enemy_spawner(ENEMYS_MOCK)
enemy_spawner7 = Enemy_spawner(ENEMYS_MOCK)
enemy_spawner8 = Enemy_spawner(ENEMYS_MOCK)

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
                player.move_left()
            elif event.key == pg.K_RIGHT:
                player.move_right(WIDTH)
        elif event.type == pg.MOUSEBUTTONUP:
            if MENU == True and GAME_OVER == False:
                click_menu = Button(pg.mouse.get_pos(), (pos_x_play_menu + width_menu_button/2, pos_y_play_menu + height_menu_button/2), (pos_x_end_menu + width_menu_button/2, pos_y_end_menu + height_menu_button/2), width_menu_button, height_menu_button, 0)
                MENU, running = click_menu.mouse_click_menu()

                music.stop()
                gameover.stop()
                music.play(-1)
                tocando_music = True

            elif GAME_OVER == True:
                player.reset_data(WIDTH)
                click_game_over = Button(pg.mouse.get_pos(), (pos_x_restart_game_over + width_game_over_button/2 , pos_y_restart_game_over + height_game_over_button/2), (pos_x_menu_game_over + width_game_over_button/2, pos_y_menu_game_over + height_game_over_button/2), width_game_over_button, height_game_over_button, current_score)
                GAME_OVER, MENU = click_game_over.mouse_click_game_over()
            # score zera
            start_time = time.time()
            score = Score(start_time, initial_speed)

    if (MENU == True or score.get_score() == 0) and tocando_music == False:
        music.stop()
        gameover.stop()
        music.play(-1)
        tocando_music = True

    if MENU == True and GAME_OVER == False:    
        menu = Menu(screen, pos_x_game_title1, pos_y_game_title1, pos_x_game_title2, pos_y_game_title2, width_menu_button, height_menu_button, pos_x_play_menu, pos_y_play_menu, pos_x_end_menu, pos_y_end_menu)
        menu.menu_screen()

    
    elif MENU == False and GAME_OVER == False:
        # score atual
        current_score = score.get_score()

        GAME_OVER = player.check_die()

        #updates
        speed.update(score)
        powerup_spawner.update(player, score, speed, getfood)

        enemy_spawner.update(player, speed, enemyhit)
        enemy_spawner2.update(player, speed, enemyhit)
        enemy_spawner3.update(player, speed, enemyhit)
        enemy_spawner4.update(player, speed, enemyhit)
        enemy_spawner5.update(player, speed, enemyhit)

        if(speed.get_speed() >= 10):
            enemy_spawner6.update(player, speed, enemyhit)
            enemy_spawner7.update(player, speed, enemyhit)
            enemy_spawner8.update(player, speed, enemyhit)

        player.get_powerups_colleteds()
        score.update(speed) # printa o score atual na tela
        score_text = text(30, 120, 5, int(current_score), "topleft", (0,0,0))
        apple_count = text(25, WIDTH/2 - 75, 7, f'x{player.powerups_colleteds[0]}', "topleft", (0,0,0))
        blueberry_count = text(25, WIDTH/2 + 15, 7, f'x{player.powerups_colleteds[1]}', "topleft", (0,0,0))
        watermelon_count = text(25, WIDTH/2 + 110, 7, f'x{player.powerups_colleteds[2]}', "topleft", (0,0,0))

        current_time = pg.time.get_ticks()
        time_elapsed = current_time - last_update_time
        if time_elapsed > 200:
        # atualiza o sprite
            player.update()
            last_update_time = current_time

        if scroll <= bg_heigh*3/4:
            scroll += speed.get_speed()
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


        if(speed.get_speed() >= 10):
            enemy_spawner6.enemy_group.draw(screen)
            enemy_spawner7.enemy_group.draw(screen)
            enemy_spawner8.enemy_group.draw(screen)

        score_text.blit(screen)
        apple_image.blit(screen)
        apple_count.blit(screen)
        blueberry_image.blit(screen)
        blueberry_count.blit(screen)
        watermelon_image.blit(screen)
        watermelon_count.blit(screen)
        lifes.draw(screen)
        
        pg.display.flip()

    elif GAME_OVER == True and MENU == False: 
        game_over = GameOver(screen, int(current_score), player.powerups_colleteds, width_game_over_button, height_game_over_button, width_powerup_img, height_powerup_img, pos_x_title_game_over, pos_y_title_game_over,pos_x_message_score, pos_y_message_score, pos_x_image_powerup1, pos_x_image_powerup2, pos_x_image_powerup3, pos_y_image_powerup1, pos_y_image_powerup2, pos_y_image_powerup3, pos_x_label_powerup1, pos_x_label_powerup2, pos_x_label_powerup3, pos_y_label_powerup1, pos_y_label_powerup2, pos_y_label_powerup3, pos_x_restart_game_over, pos_y_restart_game_over, pos_x_menu_game_over, pos_y_menu_game_over)
        game_over.game_over_screen()

        music.stop()
        gameover.play()
        tocando_music = False
    pg.display.flip()