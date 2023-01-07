import sys
import pygame as pg
from settings import *

from player import Player
from sprites import *
from raycast import raycast
from area import Area

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))

clock = pg.time.Clock()
pg.mouse.set_visible(False)
player = Player()
running_game = True

#Отрисовка местности
screen_field = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
area = Area(screen, screen_field)

#Спрайты
sprites = Sprites()

while running_game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()

    player.moving()
    screen.fill(WHITE)

    area.environment(player.angle)
    walls = raycast(player, area.textures)
    area.world(walls + [obj.object_place(player, walls) for obj in sprites.list_of_objects])

    pg.display.flip()
    clock.tick(FPS)
