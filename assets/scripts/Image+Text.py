import pygame
from Image import *

#parte de definição de janela
#WINDOW_WIDTH = 800
#WINDOW_HEIGHT = 600
#BLUE = (0, 0, 255)
#
#pygame.init()
#
#window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#pygame.display.set_caption("Capivara")


# classe pra definir e gerar o elemento
class image_plus_text(Image):

    def __init__(self, image=False, size=100, x=0, y=0, mensagem="", fonte=(pygame.font.SysFont("Arial", 20)), pos_init_image="center", pos_init_mensagem="center", cor_mensagem=(255,255,255)):   
        super().__init__(image, size, x, y)
        #parâmetros self
        self.fonte = fonte #fonte do mensagem
        self.mensagem = mensagem #conteúdo da mensagem
        self.image = image #imagem
        self.x = x #posição x
        self.y = y #posição y
        self.cor_mensagem = cor_mensagem #cor da mensagem
        self.pos_init_image = pos_init_image #posicao relativa da imagem
        self.pos_init_mensagem = pos_init_mensagem #posição relativa da mensagem
        #topleft: tupla com as coordenadas (x, y) do canto superior esquerdo do retângulo
        #topright: tupla com as coordenadas (x, y) do canto superior direito do retângulo
        #bottomleft: tupla com as coordenadas (x, y) do canto inferior esquerdo do retângulo
        #bottomright: tupla com as coordenadas (x, y) do canto inferior direito do retângulo
        #midtop: tupla com as coordenadas (x, y) do ponto central da borda superior do retângulo
        #midleft: tupla com as coordenadas (x, y) do ponto central da borda esquerda do retângulo
        #midright: tupla com as coordenadas (x, y) do ponto central da borda direita do retângulo
        #midbottom: tupla com as coordenadas (x, y) do ponto central da borda inferior do retângulo
        #center: tupla com as coordenadas (x, y) do centro do retângulo

        self.texto = self.fonte.render(str(self.mensagem), True, self.cor_mensagem)  #definindo a fonte
        self.texto_rect = self.texto.get_rect()
        
        if self.image == False:  #se não existir imagem, ele vai só colocar um texto
            setattr(self.texto_rect, self.pos_init_mensagem, (self.x, self.y))
        
        else:  #se existir imagem, ele vai colocar o texto e a imagem

            
            self.image_rect = self.image.get_rect()
            setattr(self.image_rect, self.pos_init_image, (self.x, self.y))
            setattr(self.texto_rect, self.pos_init_mensagem, (self.x, self.y))
            

    def blit(self):  #ativação de

        if self.image == False:
            window.blit(self.texto, self.texto_rect)

        else:
            window.blit(self.image, self.image_rect)
            window.blit(self.texto, self.texto_rect)


#parte que roda a tela
#running = True
#while running:
#
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#
#    window.fill(BLUE)
#
#    vida = image_plus_text(pygame.image.load("C:\\Users\\henri\\OneDrive\\Área de Trabalho\\Programação\\Projetos\\P1\\Projeto final\\assets\\sprites\\heart_icon.png"), 100, WINDOW_WIDTH - 30, 30, 3, pygame.font.SysFont("Arial", 20), "center", "center", (255,255,255))
#    vida.blit()
#
#    pygame.display.update()
#
#pygame.quit()