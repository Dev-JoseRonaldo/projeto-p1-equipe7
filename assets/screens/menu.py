import pygame 

class Menu():
    pygame.init()

    def __init__(self, screen, pos_x_game_title1, pos_y_game_title1, pos_x_game_title2, pos_y_game_title2, width_button, height_button, pos_x_play, pos_y_play, pos_x_end, pos_y_end):
        self.screen = screen #tela
        self.pos_x_game_title1 = pos_x_game_title1 #posição no eixo x do título do jogo
        self.pos_y_game_title1 = pos_y_game_title1 #posição no eixo y do título do jogo
        self.pos_x_game_title2 = pos_x_game_title2 #posição no eixo x do título do jogo
        self.pos_y_game_title2 = pos_y_game_title2 #posição no eixo y do título do jogo
        self.width_button = width_button #larguras dos botões
        self.height_button = height_button #altura dos botões
        self.pos_x_play = pos_x_play #posição no eixo x do botão play
        self.pos_y_play = pos_y_play #posição no eixo y do botão play
        self.pos_x_end = pos_x_end #posição no eixo x do botão end
        self.pos_y_end = pos_y_end #posição no eixo y do botão end

    def menu_screen(self):
        #modelo de mensagem
        def message_screen(message, size, color):
            message_font = pygame.font.SysFont('comicsansms', size, True, False)
            message_screen = f'{message}'
            message_complete = message_font.render(message_screen, True, color)
            return message_complete
        
        self.screen.blit(pygame.image.load(f'assets/sprites/bg-menu-gameover.png').convert_alpha(), (0, 0))

        #botões
        img_play_button = pygame.image.load('./assets/sprites/play-button.png')
        img_end_button = pygame.image.load('./assets/sprites/close-button.png')

        play = pygame.transform.scale(img_play_button, (self.width_button,self.height_button))
        end = pygame.transform.scale(img_end_button, (self.width_button,self.height_button))

        #mensagens
        message_game_title1 = message_screen('A Fuga de', 75, (0,0,0))
        message_game_title2 = message_screen('Filó', 75, (0,0,0))

        #apresenta na tela
        self.screen.blit(message_game_title1, (self.pos_x_game_title1,self.pos_y_game_title1))
        self.screen.blit(message_game_title2, (self.pos_x_game_title2, self.pos_y_game_title2))

        self.screen.blit(play, (self.pos_x_play,self.pos_y_play))
        self.screen.blit(end, (self.pos_x_end,self.pos_y_end)) 
        
    