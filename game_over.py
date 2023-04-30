import pygame
pygame.init()
pygame.display.set_caption("Capivara Game")

#variáveis pré-estabelecidas
largura_tela = 640
altura_tela = 480
tela = pygame.display.set_mode((largura_tela, altura_tela))

#button class
class Button():
	def __init__(self, x, y, img, scale):
		largura = img.get_width()
		altura = img.get_height()
		self.img = pygame.transform.scale(img, (int(largura * scale), int(altura * scale)))
		self.rect = self.img.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.img, (self.rect.x, self.rect.y))

		return action

#modelo de mensagem
def mensagem_tela(mensagem, tamanho, cor):
    fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)
    mensagem_apresentada = f'{mensagem}'
    mensagem_formatada = fonte.render(mensagem_apresentada, True, cor)
    return mensagem_formatada

#Quando houver 0 vidas
def game_over():
    tela.fill((255,255,255))

    #botões
    play_img = pygame.image.load('imagens_game_over/botao.png').convert_alpha()
    play = pygame.transform.scale(play_img, (40,30))

    menu_img = pygame.image.load('imagens_game_over/botao.png').convert_alpha()
    menu = pygame.transform.scale(menu_img, (40,30))

    #coletáveis
    item1 = pygame.image.load('imagens_game_over/laranja.png')
    item1 = pygame.transform.scale(item1, (40,40))

    item2 = pygame.image.load('imagens_game_over/laranja.png')
    item2 = pygame.transform.scale(item2, (40,40))

    item3 = pygame.image.load('imagens_game_over/laranja.png')
    item3 = pygame.transform.scale(item3, (40,40))

    #mensagens
    mensagem_game_over = mensagem_tela('GAME OVER', 30, (0,0,0))
    mensagem_score = mensagem_tela('SCORE: 1000', 20, (0,0,0)) #para o score colocar varíavel de pontos no local do 1000 
    mensagem_item1 = mensagem_tela('x 00', 20, (0,0,0)) #colocar varíavel de pontos no local do 00 
    mensagem_item2 = mensagem_tela('x 00', 20, (0,0,0)) #colocar varíavel de pontos no local do 00 
    mensagem_item3 = mensagem_tela('x 00', 20, (0,0,0)) #colocar varíavel de pontos no local do 00 

    #apresenta na tela
    tela.blit(mensagem_game_over, (237,100))
    tela.blit(mensagem_score, (263, 145))
    tela.blit(item1, (180,190))
    tela.blit(mensagem_item1, (220, 190))
    tela.blit(item2, (280,190))
    tela.blit(mensagem_item2, (320, 190))
    tela.blit(item3, (380,190))
    tela.blit(mensagem_item3, (420, 190))

    botao_play = Button(290, 230, play, 2)
    botao_menu = Button(290, 275, menu, 2)
    botao_play.draw(tela)
    botao_menu.draw(tela)
          

game_ativo = True
while game_ativo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_ativo = False
        
    game_over()
    pygame.display.update()

pygame.quit()