import pygame
from settings import *
from field import world_field
EPS = 0.00001

def mapping(a, b):
    return (a // BLOCK) * BLOCK, (b // BLOCK) * BLOCK

def raycast(sc, position, angle, textures):
    xo, yo = position
    angle_relative_to_fov = angle - HALF_FOV
    x_on_map, y_on_map = mapping(xo, yo)
    for rays in range(NUM_RAYS):
        sin_a = math.sin(angle_relative_to_fov)
        cos_a = math.cos(angle_relative_to_fov)

        x, dx = (x_on_map + BLOCK, 1) if cos_a >= 0 else (x_on_map, -1)
        for i in range(0, WIDTH, BLOCK):
            depth_vertical = (x - xo) / cos_a
            y_vertical = yo + depth_vertical * sin_a
            field_v = mapping(x + dx, y_vertical)
            if field_v in world_field:
                texture_v = world_field[field_v]
                break
            x += dx * BLOCK

        y, dy = (y_on_map + BLOCK, 1) if sin_a >= 0 else (y_on_map, -1)
        for i in range(0, HEIGHT, BLOCK):
            depth_horizontal = (y - yo) / sin_a
            x_horizontal = xo + depth_horizontal * cos_a
            block_horizontal = mapping(x_horizontal, y + dy)
            if block_horizontal in world_field:
                texture_horizontal = world_field[block_horizontal]
                break
            y += dy * BLOCK

        depth, offset, texture = (depth_vertical, y_vertical, texture_v) if depth_vertical < depth_horizontal else (depth_horizontal, x_horizontal, texture_horizontal)
        offset = int(offset) % BLOCK
        depth *= math.cos(angle - angle_relative_to_fov)
        depth = max(depth, EPS)
        projection_height = min(int(PROJECTION_COEFFICIENT / depth), 2 * HEIGHT)

        wall = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        wall = pygame.transform.scale(wall, (FOV_SIZE, projection_height))
        sc.blit(wall, (rays * FOV_SIZE, HALF_HEIGHT - projection_height // 2))

        angle_relative_to_fov += DELTA_ANGLE
