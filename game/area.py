import pygame as pg
from settings import *

class Area:
    def __init__(self, screen, screen_field):
        self.screen = screen
        self.screen_field = screen_field

        self.textures = {'|': pg.image.load('images/texture1.png').convert(),
                         'I': pg.image.load('images/texture2.png').convert(),
                         'SKY': pg.image.load('images/skybox.jpg').convert()
                         }

    def environment(self, angle):
        sky_offset = -5 * math.degrees(angle) % WIDTH
        self.screen.blit(self.textures['SKY'], (sky_offset, 0))
        self.screen.blit(self.textures['SKY'], (sky_offset - WIDTH, 0))
        self.screen.blit(self.textures['SKY'], (sky_offset + WIDTH, 0))
        pg.draw.rect(self.screen, FLOOR, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.screen.blit(object, object_pos)