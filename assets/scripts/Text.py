import pygame

# classe pra definir e gerar o elemento
class text():

    def __init__(self, size=100, x=0, y=0, mensagem="", pos_init_mensagem="center", cor_mensagem=(255,255,255), tipo_elemento='texto'):
        #parâmetros self
        self.mensagem = mensagem #conteúdo da mensagem
        self.x = x #posição x
        self.y = y #posição y
        self.cor_mensagem = cor_mensagem #cor da mensagem
        self.pos_init_mensagem = pos_init_mensagem #posição relativa da mensagem
        self.texto = pygame.font.SysFont('Arial', size).render(str(self.mensagem), True, cor_mensagem) if tipo_elemento == 'texto' else None
        
        #criando a variável texto_rect
        self.texto_rect = self.texto.get_rect()
        setattr(self.texto_rect, self.pos_init_mensagem, (self.x, self.y))

    def blit(self, screen_name):
        #criando a variável texto_rect
        self.texto_rect = self.texto.get_rect()
        setattr(self.texto_rect, self.pos_init_mensagem, (self.x, self.y))
        screen_name.blit(self.texto, self.texto_rect)
    