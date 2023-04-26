import pygame as pg
import random
from square_user import *

pg.init()

# Tela
WIDTH = 700
HEIGHT = 700
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Moving White Square")

# Quadrado
SIZE = 50
WHITE = (255, 255, 255)
X_MIDDLE = WIDTH//2 - SIZE//2
Y_INICIAL = 500
square = Square_user(X_MIDDLE, Y_INICIAL, WHITE, SIZE)

# Retângulo para colisão
RECT_WIDTH = 100
RECT_HEIGHT = 50
RECT_X = WIDTH//2 - RECT_WIDTH//2
RECT_Y = 300
rect = pg.Rect(RECT_X, RECT_Y, RECT_WIDTH, RECT_HEIGHT)

# Quadrado branco
WHITE_RECT = (255, 255, 255)
rect_size = SIZE
rect_x = random.randint(0, WIDTH-rect_size)
rect_y = 0
rect_speed = 2.5

# Fonte para a mensagem de colisão
FONT_SIZE = 30
font = pg.font.SysFont('Arial', FONT_SIZE)

# Mensagem de colisão
collision_text = font.render('Colisão detectada!', True, WHITE)
collision_text_rect = collision_text.get_rect(center=(WIDTH//2, HEIGHT//2))

# Variável para indicar se houve colisão
collision_detected = False

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                square.move_left()
            elif event.key == pg.K_RIGHT:
                square.move_right()
            elif event.key == pg.K_SPACE:
                square.move_center(X_MIDDLE)

    # Atualiza a posição do quadrado branco
    rect_y += rect_speed
    if rect_y > HEIGHT:
        rect_y = 0
        rect_x = random.randint(0, WIDTH-rect_size)

    # Atualiza os retângulos do quadrado e do retângulo de colisão
    square_rect = pg.Rect(square.x, square.y, square.size, square.size)
    rect = pg.Rect(rect_x, rect_y, rect_size, rect_size)

    # Detecta colisão
    if square_rect.colliderect(rect) and not collision_detected:
        print("Colisão detectada")
        collision_detected = True
        rect_speed = 0

    screen.fill((0, 0, 0))
    square.draw(screen)
    pg.draw.rect(screen, WHITE_RECT, rect)
    pg.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, rect_size, rect_size), 2)  # Desenha borda do quadrado branco
    
    # Se houve colisão, imprime a mensagem na tela
    if collision_detected:
        screen.blit(collision_text, collision_text_rect)

    pg.display.flip()

pg.quit()
