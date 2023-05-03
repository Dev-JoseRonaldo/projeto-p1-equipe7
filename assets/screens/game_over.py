import pygame 

class GameOver():
    pygame.init()

    def __init__(self, screen, score, powerups):
        self.screen = screen #tela
        self.score = score #score final
        self.powerups = powerups #powerups 
                
    def game_over_screen(self):
        #modelo de mensagem
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

        #mensagens
        message_game_over = message_screen('GAME OVER', 50, (0,0,0))
        message_score = message_screen(f'Score: {self.score}', 30, (0,0,0)) #para o scolore colocar varíavel de pontos no local do 1000 
        message_powerup1 = message_screen(f'x {self.powerups[0]}', 30, (0,0,0)) #colocar varíavel de pontos no local do 00 
        message_powerup2 = message_screen(f'x {self.powerups[1]}', 30, (0,0,0)) #colocar varíavel de pontos no local do 00 
        message_powerup3 = message_screen(f'x {self.powerups[2]}', 30, (0,0,0)) #colocar varíavel de pontos no local do 00 

        #apresenta na tela
        self.screen.blit(message_game_over, (200,160))
        self.screen.blit(message_score, (260, 245))

        self.screen.blit(powerup1, (180,290))
        self.screen.blit(message_powerup1, (230, 290))
        self.screen.blit(powerup2, (300,290))
        self.screen.blit(message_powerup2, (350, 290))
        self.screen.blit(powerup3, (420,290))
        self.screen.blit(message_powerup3, (470, 290))

        self.screen.blit(play, (270,400))
        self.screen.blit(menu, (270,480))
        