import pygame as pg

WIDTH, HEIGT = 1211, 723
fps = 60

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGT))
clock = pg.time.Clock()
background = pg.image.load('background.jpg')

run = True

while run:
    pg.display.flip()
    clock.tick(fps)