import pygame
import math
from settings import *
from field import world_field

def raycast(sc, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_pos
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            pygame.draw.line(sc, RED, player_pos, (x, y), 2)
            if (x // BLOCK * BLOCK, y // BLOCK * BLOCK) in world_field:
                break
        cur_angle += DELTA_ANGLE 
