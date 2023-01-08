from settings import *
import pygame

ٮ = False
matrix_map = [
    [1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, ٮ, 2, ٮ, 2, ٮ, 2, ٮ, 2, ٮ, 2, ٮ, 2, ٮ, 2, ٮ, 2, ٮ, 2, ٮ, 2, ٮ, 2, 1],
    [2, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, 1],
    [2, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, 1],
    [2, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, 1],
    [1, 2, 2, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, 1],
    [3, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, 1],
    [3, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, 1],
    [1, 2, 2, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, 1],
    [2, 2, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, 1],
    [2, 2, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, 1],
    [2, 2, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, 1],
    [2, 2, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, 1],
    [4, 2, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, 1],
    [4, 2, 2, ٮ, 2, ٮ, 2, ٮ, 2, ٮ, 2, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, ٮ, 1],
    [1, 4, 2, 4, 1, 4, 1, 4, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

WORLD_WIDTH = len(matrix_map[0]) * BLOCK
WORLD_HEIGHT = len(matrix_map) * BLOCK
world_field = {}
coll_wall = []
for j, row in enumerate(matrix_map):
    for i, char in enumerate(row):
        if char:
            coll_wall.append(pygame.Rect(i * BLOCK, j * BLOCK, BLOCK, BLOCK))
            if char == 1:
                world_field[(i * BLOCK, j * BLOCK)] = 1
            elif char == 2:
                world_field[(i * BLOCK, j * BLOCK)] = 2
            elif char == 3:
                world_field[(i * BLOCK, j * BLOCK)] = 3
            elif char == 4:
                world_field[(i * BLOCK, j * BLOCK)] = 4

