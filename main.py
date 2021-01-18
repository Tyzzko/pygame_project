import pygame as pg
from random import randrange

WIDTH, HEIGHT = 1211, 783
fps = 60

paddle_w = 340
paddle_h = 35
paddle_speed = 17
paddle = pg.Rect(WIDTH // 2 - paddle_w // 2,
                 HEIGHT - 10 - paddle_h,
                 paddle_w, paddle_h)

ball_radius = 25
ball_speed = 3
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pg.Rect(randrange(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# lives = [pg.Rect(10 + 60 * i, 5, 60, 60) for i in range(3)]
lives = 3
block_list = [pg.Rect(10 + 120 * i, 60 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
colours = [(73, 188, 12), (30, 142, 234), (238, 169, 26)]
color_list = [colours[randrange(0, 3)] for i in range(10) for j in range(4)]
text1 = ''

exit_code = 0
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
background = pg.image.load('background.jpg').convert()


def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top
    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    key = pg.key.get_pressed()
    if key[pg.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pg.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_speed
    screen.blit(background, (0, 0))

    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = -dx
    if ball.centery < ball_radius:
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    if ball.collidelist(block_list) != -1:
        hit_index = ball.collidelist(block_list)
        if color_list[hit_index] == colours[2]:
            color_list[hit_index] = colours[1]
        elif color_list[hit_index] == colours[1]:
            color_list[hit_index] = colours[0]
        else:
            hit_rect = block_list.pop(hit_index)
            hit_color = color_list.pop(hit_index)
            dx, dy = detect_collision(dx, dy, ball, hit_rect)
            hit_rect.inflate_ip(ball.width * 3, ball.height * 3)
            pg.draw.rect(screen, hit_color, hit_rect)
            fps += 2

    [pg.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]
    [pg.draw.circle(screen, (255, 0, 0), (40 + 70 * i, 28), 30) for i in range(lives)]
    pg.draw.rect(screen, pg.Color('yellow'), paddle)
    pg.draw.circle(screen, pg.Color('white'), ball.center, ball_radius)
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

    if ball.bottom > HEIGHT:
        if lives > 0:
            lives -= 1
            ball.left, ball.top = 600, 450
        else:
            block_list, color_list = [], []
            text1 = pg.font.Font(None, 120).render('GAME OVER!', True,
                              (255, 255, 255))
    elif not len(block_list):
        block_list, color_list = [], []
        text1 = pg.font.Font(None, 120).render('YOU WIN!', True,
                          (255, 255, 255))
    if text1:
        screen.blit(text1, (370, 360))
    pg.display.flip()
    clock.tick(fps)
run = True
