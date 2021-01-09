import pygame as pg

WIDTH, HEIGT = 1211, 723
fps = 60

paddle_w = 340
paddle_h = 35
paddle_speed = 14
paddle = pg.Rect(WIDTH // 2 - paddle_w // 2,
                 HEIGT - 10 -paddle_h,
                 paddle_w, paddle_h)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGT))
clock = pg.time.Clock()
background = pg.image.load('background.jpg').convert()

run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    screen.blit(background, (0, 0))
    pg.draw.rect(screen, pg.Color('yellow'), paddle)
    pg.display.flip()
    clock.tick(fps)