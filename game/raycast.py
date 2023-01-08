import pygame
from settings import *
from field import world_field, WORLD_WIDTH, WORLD_HEIGHT
EPS = 0.0000001

def display(a, b):
    return (a // BLOCK) * BLOCK, (b // BLOCK) * BLOCK

def raycast(player, textures):
    walls = []
    xo, yo = player.get_position
    texture_vertical, texture_horizontal = 1, 1
    x_on_field, y_on_field = display(xo, yo)
    angle_relative_to_fov = player.angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(angle_relative_to_fov)
        cos_a = math.cos(angle_relative_to_fov)
        sin_a = sin_a if sin_a else EPS
        cos_a = cos_a if cos_a else EPS

        # verticals
        x, dx = (x_on_field + BLOCK, 1) if cos_a >= 0 else (x_on_field, -1)
        for i in range(0, WORLD_WIDTH, BLOCK):
            depth_vertical = (x - xo) / cos_a
            y_vertical = yo + depth_vertical * sin_a
            tile_vertical = display(x + dx, y_vertical)
            if tile_vertical in world_field:
                texture_vertical = world_field[tile_vertical]
                break
            x += dx * BLOCK

        # horizontals
        y, dy = (y_on_field + BLOCK, 1) if sin_a >= 0 else (y_on_field, -1)
        for i in range(0, WORLD_HEIGHT, BLOCK):
            depth_horizontal = (y - yo) / sin_a
            x_horizontal = xo + depth_horizontal * cos_a
            tile_horizontal = display(x_horizontal, y + dy)
            if tile_horizontal in world_field:
                texture_horizontal = world_field[tile_horizontal]
                break
            y += dy * BLOCK

        # projection
        depth, displacement, texture = (depth_vertical, y_vertical, texture_vertical) if depth_vertical < depth_horizontal else (depth_horizontal, x_horizontal, texture_horizontal)
        displacement = int(displacement) % BLOCK
        depth *= math.cos(player.angle - angle_relative_to_fov)
        depth = max(depth, EPS)
        projection_height = min(int(PROJECTION_COEFFICIENT / depth), FIVE_HEIGHT)

        wall = textures[texture].subsurface(displacement * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        wall = pygame.transform.scale(wall, (FOV_SIZE, projection_height))
        wall_position = (ray * FOV_SIZE, HALF_HEIGHT - projection_height // 2)

        walls.append((depth, wall, wall_position))
        angle_relative_to_fov += DELTA_ANGLE
    return walls
