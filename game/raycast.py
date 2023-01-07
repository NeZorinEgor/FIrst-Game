import pygame
from settings import *
from field import world_field
EPS = 0.00001

def mapping(a, b):
    return (a // BLOCK) * BLOCK, (b // BLOCK) * BLOCK

def raycast(player, textures):
    walls = []
    xo, yo = player.get_position
    x_on_map, y_on_map = mapping(xo, yo)
    angle_relative_to_fov = player.angle - HALF_FOV
    for rays in range(NUM_RAYS):
        sin_a = math.sin(angle_relative_to_fov)
        cos_a = math.cos(angle_relative_to_fov)

        x, dx = (x_on_map + BLOCK, 1) if cos_a >= 0 else (x_on_map, -1)
        for i in range(0, WIDTH, BLOCK):
            depth_vertical = (x - xo) / cos_a
            y_vertical = yo + depth_vertical * sin_a
            block_vertical = mapping(x + dx, y_vertical)
            if block_vertical in world_field:
                texture_vertical = world_field[block_vertical]
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

        depth, displacement, texture = (depth_vertical, y_vertical, texture_vertical) if depth_vertical < depth_horizontal else (depth_horizontal, x_horizontal, texture_horizontal)
        displacement = int(displacement) % BLOCK
        depth *= math.cos(player.angle - angle_relative_to_fov)
        depth = max(depth, EPS)
        projection_height = min(int(PROJECTION_COEFFICIENT / depth), 2 * HEIGHT)

        wall = textures[texture].subsurface(displacement * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        wall = pygame.transform.scale(wall, (FOV_SIZE, projection_height))
        wall_position = (rays * FOV_SIZE, HALF_HEIGHT - projection_height // 2)

        walls.append((depth, wall, wall_position))
        angle_relative_to_fov += DELTA_ANGLE
    return walls
