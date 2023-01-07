import pygame
from settings import *


class Sprites:
    def __init__(self):
        self.sprite_types = {
            'marlow': pygame.image.load('sprites/marlow/marlow.jpg').convert_alpha(),
            'shelbi': pygame.image.load('sprites/shelbi/shelbi.png').convert_alpha(),
            'giraffe': pygame.image.load(f'sprites/giraffe/giraffe.png').convert_alpha()
        }
        self.list_of_objects = [
            SpriteModel(self.sprite_types['marlow'], True, (6, 10), 1.8, 0.7),
            SpriteModel(self.sprite_types['marlow'], True, (7, 8), 1.8, 0.7),
            SpriteModel(self.sprite_types['marlow'], True, (8, 9), 1.8, 0.7),
            SpriteModel(self.sprite_types['shelbi'], True, (8.8, 7.5), 1.6, 0.5),
            SpriteModel(self.sprite_types['shelbi'], True, (8.8, 5.6), 1.6, 0.5),
            SpriteModel(self.sprite_types['giraffe'], True, (10, 5.5), 0.2, 0.5),
        ]


class SpriteModel:
    def __init__(self, object, static, pos, change, scale):
        self.object = object
        self.static = static
        self.pos = self.x, self.y = pos[0] * BLOCK, pos[1] * BLOCK
        self.change = change
        self.scale = scale

        if not static:
            self.sprite_angles = [frozenset(range(i, i + 45)) for i in range(0, 360, 45)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}

    def object_place(self, player, walls):
        fake_walls0 = [walls[0] for i in range(FAKE_RAYS)]
        fake_walls1 = [walls[-1] for i in range(FAKE_RAYS)]
        fake_walls = fake_walls0 + walls + fake_walls1

        dx, dy = self.x - player.pos, self.y - player.ang
        distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI

        delta_rays = int(gamma / DELTA_ANGLE)
        used_ray = CENTRALLY_RAY + delta_rays
        distance_to_sprite *= math.cos(HALF_FOV - used_ray * DELTA_ANGLE)

        fake_ray = used_ray + FAKE_RAYS
        if 0 <= fake_ray <= NUM_RAYS - 1 + 2 * FAKE_RAYS and distance_to_sprite < fake_walls[fake_ray][0]:
            proj_height = min(int(PROJECTION_COEFFICIENT / distance_to_sprite * self.scale), 2 * HEIGHT)
            half_projection_height = proj_height // 2
            shift = half_projection_height * self.change

            if not self.static:
                if theta < 0:
                    theta += DOUBLE_PI
                theta = 360 - int(math.degrees(theta))

                for angles in self.sprite_angles:
                    if theta in angles:
                        self.object = self.sprite_positions[angles]
                        break

            sprite_position = (used_ray * FOV_SIZE - half_projection_height, HALF_HEIGHT - half_projection_height + shift)
            sprite = pygame.transform.scale(self.object, (proj_height, proj_height))
            return (distance_to_sprite, sprite, sprite_position)
        else:
            return (False,)
