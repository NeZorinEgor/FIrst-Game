import math
import sys
import pygame as pg
from settings import *
from player import Player
from field import world_field
from raycast import raycast

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
player = Player()
running_game = True

while running_game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()


    player.moving()
    screen.fill(WHITE)

    #Добавлено
    pg.draw.rect(screen, WHITE, (0, 0, WIDTH, HALF_HEIGHT)) #Небо
    pg.draw.rect(screen, LIGHTGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT)) #Земля

    raycast(screen, player.get_position, player.angle) #Отображение лучей

    #Убрано
    # pg.draw.circle(screen, GREEN, (int(player.x), int(player.y)), 12)
    # pg.draw.line(screen, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
    #                                          player.y + WIDTH * math. sin(player.angle)), 2)
    # for x,y in world_field:
    #     pg.draw.rect(screen, BLACK, (x, y, BLOCK, BLOCK), 2)

    pg.display.flip()
    clock.tick(FPS)