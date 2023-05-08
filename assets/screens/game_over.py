import pygame 

class GameOver():
    pygame.init()

    def __init__(self, screen, score, powerups, width_button, height_button, width_powerup, height_powerup, pos_x_game_over, pos_y_game_over, pos_x_score, pos_y_score, pos_x_powerup1, pos_x_powerup2, pos_x_powerup3, pos_y_powerup1, pos_y_powerup2, pos_y_powerup3, pos_x_label_powerup1, pos_x_label_powerup2, pos_x_label_powerup3, pos_y_label_powerup1, pos_y_label_powerup2, pos_y_label_powerup3, pos_x_restart, pos_y_restart, pos_x_menu, pos_y_menu):
        self.screen = screen #tela
        self.score = score #score final
        self.powerups = powerups #lista de powerups coletados
        self.width_button = width_button #largura botão
        self.height_button = height_button #altura botão
        self.width_powerup = width_powerup #largura imagem powerup
        self.height_powerup = height_powerup #altura imagem powerup
        self.pos_x_game_over = pos_x_game_over #posição no eixo x da mensagem 'GAME OVER'
        self.pos_y_game_over = pos_y_game_over #posição no eixo y da mensagem 'GAME OVER'
        self.pos_x_score = pos_x_score #posição no eixo x do Score
        self.pos_y_score = pos_y_score #posição no eixo y do Score
        self.pos_x_powerup1 = pos_x_powerup1 #posição no eixo x da imagem do powerup 1
        self.pos_x_powerup2 = pos_x_powerup2 #posição no eixo x da imagem do powerup 2
        self.pos_x_powerup3 = pos_x_powerup3 #posição no eixo x da imagem do powerup 3
        self.pos_y_powerup1 = pos_y_powerup1 #posição no eixo y da imagem do powerup 1
        self.pos_y_powerup2 = pos_y_powerup2 #posição no eixo y da imagem do powerup 2
        self.pos_y_powerup3 = pos_y_powerup3 #posição no eixo y da imagem do powerup 3
        self.pos_x_label_powerup1 = pos_x_label_powerup1 #posição no eixo x da mensagem do powerup 1
        self.pos_x_label_powerup2 = pos_x_label_powerup2 #posição no eixo x da mensagem do powerup 2
        self.pos_x_label_powerup3 = pos_x_label_powerup3 #posição no eixo x da mensagem do powerup 3
        self.pos_y_label_powerup1 = pos_y_label_powerup1 #posição no eixo y da mensagem do powerup 1
        self.pos_y_label_powerup2 = pos_y_label_powerup2 #posição no eixo y da mensagem do powerup 2
        self.pos_y_label_powerup3 = pos_y_label_powerup3 #posição no eixo y da mensagem do powerup 3
        self.pos_x_restart = pos_x_restart #posição no eixo x do botão restart
        self.pos_y_restart = pos_y_restart #posição no eixo y do botão restart
        self.pos_x_menu = pos_x_menu #posição no eixo x do botão menu
        self.pos_y_menu = pos_y_menu #posição no eixo y do botão menu
                
    def game_over_screen(self):
        #modelo de mensagem
        def message_screen(message, size, color):
            message_font = pygame.font.SysFont('comicsansms', size, True, False)
            message_screen = f'{message}'
            message_complete = message_font.render(message_screen, True, color)
            return message_complete

        self.screen.blit(pygame.image.load(f'assets/sprites/bg-menu-gameover.png').convert_alpha(), (0, 0))

        #botões
        img_restart_button = pygame.image.load('./assets/sprites/restart-button.png')
        img_menu_button = pygame.image.load('./assets/sprites/menu-button.png')

        restart = pygame.transform.scale(img_restart_button, (self.width_button,self.height_button))
        menu = pygame.transform.scale(img_menu_button, (self.width_button,self.height_button))

        #coletáveis
        img_powerup1 = pygame.image.load('./assets/sprites/powerups/apple.png')
        img_powerup2 = pygame.image.load('./assets/sprites/powerups/blueberry.png')
        img_powerup3 = pygame.image.load('./assets/sprites/powerups/watermelon.png')

        powerup1 = pygame.transform.scale(img_powerup1, (self.width_powerup,self.height_powerup))
        powerup2 = pygame.transform.scale(img_powerup2, (self.width_powerup,self.height_powerup))
        powerup3 = pygame.transform.scale(img_powerup3, (self.width_powerup,self.height_powerup))

        #mensagens
        message_game_over = message_screen('GAME OVER', 60, (0,0,0))
        message_score = message_screen(f'Score: {self.score}', 30, (0,0,0)) #para o scolore colocar varíavel de pontos no local do 1000 
        message_powerup1 = message_screen(f'x{self.powerups[0]}', 30, (0,0,0)) #colocar varíavel de pontos no local do 00 
        message_powerup2 = message_screen(f'x{self.powerups[1]}', 30, (0,0,0)) #colocar varíavel de pontos no local do 00 
        message_powerup3 = message_screen(f'x{self.powerups[2]}', 30, (0,0,0)) #colocar varíavel de pontos no local do 00 

        #apresenta na tela
        self.screen.blit(message_game_over, (self.pos_x_game_over,self.pos_y_game_over))
        self.screen.blit(message_score, (self.pos_x_score, self.pos_y_score))

        self.screen.blit(powerup1, (self.pos_x_powerup1,self.pos_y_powerup1))
        self.screen.blit(message_powerup1, (self.pos_x_label_powerup1, self.pos_y_label_powerup1))
        self.screen.blit(powerup2, (self.pos_x_powerup2,self.pos_y_powerup2))
        self.screen.blit(message_powerup2, (self.pos_x_label_powerup2, self.pos_y_label_powerup2))
        self.screen.blit(powerup3, (self.pos_x_powerup3,self.pos_y_powerup3))
        self.screen.blit(message_powerup3, (self.pos_x_label_powerup3, self.pos_y_label_powerup3))

        self.screen.blit(restart, (self.pos_x_restart,self.pos_y_restart))
        self.screen.blit(menu, (self.pos_x_menu,self.pos_y_menu))
        