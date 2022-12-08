from settings import *

text_map = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'W..............................W',
    'W..............................W',
    'W..............................W',
    'W..............................W',
    'W..............................W',
    'W........WWWWWWWWWWWWW.........W',
    'W........W...........W.........W',
    'W........W...........W.........W',
    'W........W...............W.....W',
    'W........W...........W.........W',
    'W........WWWWWWWWWWWWW.........W',
    'W..............................W',
    'W..............................W',
    'W..............................W',
    'W..............................W',
    'W..............................W',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
]

world_field = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_field.add((i * BLOCK, j * BLOCK))
