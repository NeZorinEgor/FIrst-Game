import pygame as pg
from settings import *

class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.textures = {1: pg.image.load('images/wall1.png').convert(),
                         2: pg.image.load('images/wall2.png').convert(),
                         3: pg.image.load('images/wall3.png').convert(),
                         4: pg.image.load('images/wall4.png').convert(),
                         'SKY': pg.image.load('images/sky.png').convert()
                         }

    def environment(self, angle):
        sky_offset = -10 * math.degrees(angle) % WIDTH
        self.screen.blit(self.textures['SKY'], (sky_offset, 0))
        self.screen.blit(self.textures['SKY'], (sky_offset - WIDTH, 0))
        self.screen.blit(self.textures['SKY'], (sky_offset + WIDTH, 0))
        pg.draw.rect(self.screen, FLOOR, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.screen.blit(object, object_pos)
