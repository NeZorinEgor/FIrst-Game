import pygame as pg
from settings import *
import math

class Player:
    def __init__(self):
        self.pos, self.ang = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.sensivity = 0.004

    @property
    def get_position(self):
        return (self.pos, self.ang)

    def moving(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos += MOVEMENT_SPEED * cos_a
            self.ang += MOVEMENT_SPEED * sin_a
            print("W")
        if keys[pg.K_a]:
            self.pos += MOVEMENT_SPEED * sin_a
            self.ang += -MOVEMENT_SPEED * cos_a
            print("A")
        if keys[pg.K_s]:
            self.pos += -MOVEMENT_SPEED * cos_a
            self.ang += -MOVEMENT_SPEED * sin_a
            print("S")
        if keys[pg.K_d]:
            self.pos += -MOVEMENT_SPEED * sin_a
            self.ang += MOVEMENT_SPEED * cos_a
            print("D")
        if keys[pg.K_LEFT]:
            self.angle -= 0.02
            print("←")
        if keys[pg.K_RIGHT]:
            self.angle += 0.02
            print("→")

    def mouse_control(self):
        if pg.mouse.get_focused():
            difference = pg.mouse.get_pos()[0] - HALF_WIDTH
            pg.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += difference * self.sensivity 
