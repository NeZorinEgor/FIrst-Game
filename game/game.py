import math
import pygame as pg
from settings import *
from player import Player 
from field import world_field
from raycast import raycast

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
player = Player()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    player.movement()
    screen.fill(WHITE)

    raycast(screen, player.pos, player.angle) #Отображение лучей
    
    pg.draw.circle(screen, GREEN, (int(player.x), int(player.y)), 12)
    pg.draw.line(screen, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
                                             player.y + WIDTH * math. sin(player.angle)), 2)
    for x,y in world_field:
        pg.draw.rect(screen, BLACK, (x, y, BLOCK, BLOCK), 2)

    pg.display.flip()
    clock.tick(FPS)

