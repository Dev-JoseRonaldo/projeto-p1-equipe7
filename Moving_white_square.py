from square_user import *

pg.init()
# tela
WIDTH = 700
HEIGHT = 700
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Moving White Square")

# quadrado
SIZE = 50
WHITE = (255, 255, 255)
X_MIDDLE = WIDTH//2 - SIZE//2
Y_INICIAL = 500
square = Square_user(X_MIDDLE, Y_INICIAL, WHITE, SIZE)


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

    screen.fill((0, 0, 0))
    square.draw(screen)
    pg.display.flip()

pg.quit()
