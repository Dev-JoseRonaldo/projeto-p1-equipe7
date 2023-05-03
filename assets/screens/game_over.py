import pygame 
from assets.scripts.Button import *

class GameOver():
    pygame.init()

    def __init__(self, screen, powerups):
        self.screen = screen #tela
        self.powerups = powerups #powerups 
                
    def game_over_screen(self):
        #estilo de fonte
        def get_font(size): 
            return pygame.font.Font("./assets/scripts/font.ttf", size)

        #modelo de message
        def message_screen(message, size, color):
            message_font = pygame.font.SysFont('comicsansms', size, True, False)
            message_screen = f'{message}'
            message_complete = message_font.render(message_screen, True, color)
            return message_complete
    
        self.screen.fill((255,255,255))

        #botões
        img_play_button = pygame.image.load('./assets/sprites/botao.png')
        img_menu_button = pygame.image.load('./assets/sprites/botao.png')

        play = pygame.transform.scale(img_play_button, (150,100))
        menu = pygame.transform.scale(img_menu_button, (150,100))

        #coletáveis
        img_powerup1 = pygame.image.load('./assets/sprites/powerups/apple.png')
        img_powerup2 = pygame.image.load('./assets/sprites/powerups/avocado.png')
        img_powerup3 = pygame.image.load('./assets/sprites/powerups/watermelon.png')

        powerup1 = pygame.transform.scale(img_powerup1, (40,40))
        powerup2 = pygame.transform.scale(img_powerup2, (40,40))
        powerup3 = pygame.transform.scale(img_powerup3, (40,40))

        #powerups coletados
        powerup_list = []
        for powerup in self.powerups:
            powerup_list.append(powerup)

        #mensagens
        message_game_over = message_screen('GAME OVER', 50, (0,0,0))
        message_score = message_screen('Score: 1000', 30, (0,0,0)) #para o scolore colocar varíavel de pontos no local do 1000 
        message_powerup1 = message_screen(f'x {powerup_list[0]}', 30, (0,0,0)) #colocar varíavel de pontos no local do 00 
        message_powerup2 = message_screen(f'x {powerup_list[1]}', 30, (0,0,0)) #colocar varíavel de pontos no local do 00 
        message_powerup3 = message_screen(f'x {powerup_list[2]}', 30, (0,0,0)) #colocar varíavel de pontos no local do 00 

        #apresenta na tela
        self.screen.blit(message_game_over, (200,160))
        self.screen.blit(message_score, (260, 245))
        self.screen.blit(powerup1, (180,290))
        self.screen.blit(message_powerup1, (230, 290))
        self.screen.blit(powerup2, (300,290))
        self.screen.blit(message_powerup2, (350, 290))
        self.screen.blit(powerup3, (420,290))
        self.screen.blit(message_powerup3, (470, 290))

        botao_play = Button(image=play, pos=(350, 400), text_input="", font=get_font(75), base_color="White", hovering_color="Green")
        botao_menu = Button(image=menu, pos=(350, 480), text_input="", font=get_font(75), base_color="White", hovering_color="Green")
        botao_play.update(self.screen)
        botao_menu.update(self.screen)