import pygame

#parte de definição de janela
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLUE = (0, 0, 255)

pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Capivara")


# classe pra definir e gerar o elemento
class elemento_na_tela:
    def __init__(self, pos_x_y, pos_init, mensagem="", fonte=(pygame.font.SysFont("Arial", 20)), imagem=False, cor_mensagem=(255,255,255)):
        #parâmetros self
        self.fonte = fonte
        self.mensagem = mensagem
        self.imagem = imagem
        self.pos_x_y = pos_x_y
        self.pos_init = pos_init
        #topleft: tupla com as coordenadas (x, y) do canto superior esquerdo do retângulo
        #topright: tupla com as coordenadas (x, y) do canto superior direito do retângulo
        #bottomleft: tupla com as coordenadas (x, y) do canto inferior esquerdo do retângulo
        #bottomright: tupla com as coordenadas (x, y) do canto inferior direito do retângulo
        #midtop: tupla com as coordenadas (x, y) do ponto central da borda superior do retângulo
        #midleft: tupla com as coordenadas (x, y) do ponto central da borda esquerda do retângulo
        #midright: tupla com as coordenadas (x, y) do ponto central da borda direita do retângulo
        #midbottom: tupla com as coordenadas (x, y) do ponto central da borda inferior do retângulo
        #center: tupla com as coordenadas (x, y) do centro do retângulo
        self.cor_mensagem = cor_mensagem

        self.texto = self.fonte.render(str(self.mensagem), True, self.cor_mensagem)  #definindo a fonte
        self.texto_rect = self.texto.get_rect()
        

        if self.imagem == False:  #se não existir imagem, ele vai só colocar um texto
            setattr(self.texto_rect, self.pos_init, (self.pos_x_y))
        
        else:  #se existir imagem, ele vai colocar o texto e a imagem

            self.image_rect = self.imagem.get_rect()
            setattr(self.image_rect, self.pos_init, (self.pos_x_y))
            setattr(self.texto_rect, self.pos_init, (self.pos_x_y))
            
            
        



    def blit(self):

        if self.imagem == False:
            window.blit(self.texto, self.texto_rect)

        else:
            window.blit(self.imagem, self.image_rect)
            window.blit(self.texto, self.texto_rect)


#parte que roda a tela
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BLUE)

    vida = elemento_na_tela((WINDOW_WIDTH - 30, 30), "center", 3, pygame.font.SysFont("Arial", 20),pygame.image.load("heart_icon.png"), (255,255,255))
    vida.blit()

    pontuacao = 2023321321321321321
    score = elemento_na_tela((10, 10), "topleft", f"Pontuação: {pontuacao}")
    score.blit()

    pygame.display.update()

pygame.quit()