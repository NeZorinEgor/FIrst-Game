import math
####################

WIDTH = 1600
HEIGHT = 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 120
BLOCK = 50

####################
FOV = 3.14 / 3
HALF_FOV = FOV / 2
NUM_RAYS = 50
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS

####################
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
movement_speed = 2

####################
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 255)
LIGHTGRAY = (140, 140, 140)


#Добавлено
DISTANCE = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJECTION_COEFFICIENT = 3 * DISTANCE * BLOCK
FOV_SIZE = WIDTH // NUM_RAYS