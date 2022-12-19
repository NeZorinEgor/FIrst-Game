import pygame as pg
from settings import *
import math


class Player:
    def __init__(self):
        self.pos, self.ang = player_pos
        self.angle = player_angle

    @property
    def get_position(self):
        return (self.pos, self.ang)

    def moving(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos += movement_speed * cos_a
            self.ang += movement_speed * sin_a
            print("W")
        if keys[pg.K_a]:
            self.pos += movement_speed * sin_a
            self.ang += -movement_speed * cos_a
            print("A")
        if keys[pg.K_s]:
            self.pos += -movement_speed * cos_a
            self.ang += -movement_speed * sin_a
            print("S")
        if keys[pg.K_d]:
            self.pos += -movement_speed * sin_a
            self.ang += movement_speed * cos_a
            print("D")
        if keys[pg.K_LEFT]:
            self.angle -= 0.02
            print("←")
        if keys[pg.K_RIGHT]:
            self.angle += 0.02
            print("→")