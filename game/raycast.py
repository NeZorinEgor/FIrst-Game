import pygame
import math
from settings import *
from field import world_field

def raycast(sc, position, angle):
    cur_angle = angle - HALF_FOV
    xo, yo = position
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            # pygame.draw.line(sc, RED, player_pos, (x, y), 2)
            if (x // BLOCK * BLOCK, y // BLOCK * BLOCK) in world_field:
                
                depth *= math.cos(angle - cur_angle)
                projection_height = min(PROJECTION_COEFFICIENT / (depth + 0.0001), HEIGHT)
                c = 255 / (1 + depth * depth * 0.0001)
                color = (c // 2, c // 2.5, c // 3)
                pygame.draw.rect(sc, color, (ray * FOV_SIZE, HALF_HEIGHT - projection_height // 2, FOV_SIZE, projection_height))
                break
            
        cur_angle += DELTA_ANGLE  
