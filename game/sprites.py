import pygame
from settings import *
from collections import deque

class Sprites:
    def __init__(self):
        self.sprite_settings = {
            'sprite_pin': {
                'sprite': pygame.image.load('sprites/pin/base/1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.7,
                'scale': 0.6,
                'animation': deque([pygame.image.load(f'sprites/pin/anim/{i}.png').convert_alpha() for i in range(15)]),
                'animation_dist': 1000000,
                'animation_speed': 8,
                'blocked': True,
            },
            'sprite_flame': {
                'sprite': pygame.image.load('sprites/flame/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.1,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'sprites/flame/anim/{i}.png').convert_alpha() for i in range(8)]),
                'animation_dist': 800000,
                'animation_speed': 10,
                'blocked': True,
            },
            'sprite_tree': {
                'sprite': pygame.image.load('sprites/tree/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': -0.5,
                'scale': 5,
                'animation': deque(
                    [pygame.image.load(f'sprites/tree/anim/{i}.png').convert_alpha() for i in range(10)]),
                'animation_dist': 10000000,
                'animation_speed': 5,
                'blocked': True,
            },
            'sprite_bushes': {
                'sprite': pygame.image.load('sprites/bushes/base/1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 1,
                'scale': 0.6,
                'animation': deque(
                    [pygame.image.load(f'sprites/bushes/anim/{i}.png').convert_alpha() for i in range(20)]),
                'animation_dist': 10000000,
                'animation_speed': 10,
                'blocked': True,
            },
            'sprite_panda': {
                'sprite': pygame.image.load('sprites/panda/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.1,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'sprites/panda/anim/{i}.png').convert_alpha() for i in range(37)]),
                'animation_dist': 10000000,
                'animation_speed': 5,
                'blocked': True,
            },
            'sprite_pingvin': {
                'sprite': pygame.image.load('sprites/pingvin/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.7,
                'scale': 0.6,
                'animation': deque(
                    [pygame.image.load(f'sprites/pingvin/anim/{i}.png').convert_alpha() for i in range(22)]),
                'animation_dist': 10000000,
                'animation_speed': 15,
                'blocked': True,
            },
            'sprite_tigr': {
                'sprite': pygame.image.load('sprites/tigr/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.7,
                'scale': 0.8,
                'animation': deque(
                    [pygame.image.load(f'sprites/tigr/anim/{i}.png').convert_alpha() for i in range(6)]),
                'animation_dist': 10000000,
                'animation_speed': 15,
                'blocked': True,
            },
            'sprite_lev': {
                'sprite': pygame.image.load('sprites/lev/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.5,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'sprites/lev/anim/{i}.png').convert_alpha() for i in range(9)]),
                'animation_dist': 10000000,
                'animation_speed': 15,
                'blocked': True,
            },
            'sprite_monkey': {
                'sprite': pygame.image.load('sprites/monkey/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.1,
                'scale': 1.3,
                'animation': deque(
                    [pygame.image.load(f'sprites/monkey/anim/{i}.png').convert_alpha() for i in range(14)]),
                'animation_dist': 10000000,
                'animation_speed': 15,
                'blocked': True,
            },
            'sprite_turtle': {
                'sprite': pygame.image.load('sprites/turtle/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.7,
                'scale': 0.6,
                'animation': deque(
                    [pygame.image.load(f'sprites/turtle/anim/{i}.png').convert_alpha() for i in range(12)]),
                'animation_dist': 10000000,
                'animation_speed': 15,
                'blocked': True,
            },
            'sprite_rabbit': {
                'sprite': pygame.image.load('sprites/rabbit/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.7,
                'scale': 0.6,
                'animation': deque(
                    [pygame.image.load(f'sprites/rabbit/anim/{i}.png').convert_alpha() for i in range(14)]),
                'animation_dist': 10000000,
                'animation_speed': 15,
                'blocked': True,
            },
            'sprite_zyc': {
                'sprite': pygame.image.load('sprites/zyc/base/1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.7,
                'scale': 0.6,
                'animation': deque(
                    [pygame.image.load(f'sprites/zyc/anim/{i}.png').convert_alpha() for i in range(6)]),
                'animation_dist': 10000000,
                'animation_speed': 25,
                'blocked': True,
            },
            'sprite_crocodile': {
                'sprite': pygame.image.load('sprites/crocodile/base/1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.5,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'sprites/crocodile/anim/{i}.png').convert_alpha() for i in range(38)]),
                'animation_dist': 10000000,
                'animation_speed': 10,
                'blocked': True,
            },
            'sprite_bird': {
                'sprite': pygame.image.load('sprites/bird/base/1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.1,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'sprites/bird/anim/{i}.png').convert_alpha() for i in range(6)]),
                'animation_dist': 10000000,
                'animation_speed': 10,
                'blocked': True,
            },
            'sprite_bird1': {
                'sprite': pygame.image.load('sprites/bird1/base/1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.7,
                'scale': 0.6,
                'animation': deque(
                    [pygame.image.load(f'sprites/bird1/anim/{i}.png').convert_alpha() for i in range(11)]),
                'animation_dist': 10000000,
                'animation_speed': 10,
                'blocked': True,
            },
            'sprite_bird2': {
                'sprite': pygame.image.load('sprites/bird2/base/1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.7,
                'scale': 0.6,
                'animation': deque(
                    [pygame.image.load(f'sprites/bird2/anim/{i}.png').convert_alpha() for i in range(11)]),
                'animation_dist': 10000000,
                'animation_speed': 10,
                'blocked': True,
            },
            'sprite_bird3': {
                'sprite': pygame.image.load('sprites/bird3/base/1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 1.3,
                'scale': 0.6,
                'animation': deque(
                    [pygame.image.load(f'sprites/bird3/anim/{i}.png').convert_alpha() for i in range(1)]),
                'animation_dist': 10000000,
                'animation_speed': 10,
                'blocked': True,
            },
            'sprite_svyatoslav': {
                'sprite': pygame.image.load('sprites/svyatoslav/base/1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.3,
                'scale': 1.5,
                'animation': deque(
                    [pygame.image.load(f'sprites/svyatoslav/anim/{i}.png').convert_alpha() for i in range(17)]),
                'animation_dist': 10000000,
                'animation_speed': 10,
                'blocked': True,
            },
            'sprite_makar': {
                'sprite': pygame.image.load('sprites/makar/base/1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.5,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'sprites/makar/anim/{i}.png').convert_alpha() for i in range(4)]),
                'animation_dist': 10000000,
                'animation_speed': 10,
                'blocked': True,
            },
            'sprite_kirill': {
                'sprite': pygame.image.load('sprites/kirill/base/1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.5,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'sprites/kirill/anim/{i}.png').convert_alpha() for i in range(12)]),
                'animation_dist': 10000000,
                'animation_speed': 10,
                'blocked': True,
            },
            'sprite_egor': {
                'sprite': pygame.image.load('sprites/egor/base/1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.4,
                'scale': 1.3,
                'animation': deque(
                    [pygame.image.load(f'sprites/egor/anim/{i}.png').convert_alpha() for i in range(1)]),
                'animation_dist': 10000000,
                'animation_speed': 10,
                'blocked': True,
            },
            'sprite_dugar': {
                'sprite': pygame.image.load('sprites/dugar/base/1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.4,
                'scale': 1.1,
                'animation': deque(
                    [pygame.image.load(f'sprites/dugar/anim/{i}.png').convert_alpha() for i in range(6)]),
                'animation_dist': 10000000,
                'animation_speed': 10,
                'blocked': True,
            },
            'sprite_danil': {
                'sprite': pygame.image.load('sprites/danil/base/1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.6,
                'scale': 1.5,
                'animation': deque(
                    [pygame.image.load(f'sprites/danil/anim/{i}.png').convert_alpha() for i in range(10)]),
                'animation_dist': 10000000,
                'animation_speed': 10,
                'blocked': True,
            },

            'sprite_tree1': {
                'sprite': pygame.image.load('sprites/tree1/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': -0.5,
                'scale': 5,
                'animation': deque(
                    [pygame.image.load(f'sprites/tree1/anim/{i}.png').convert_alpha() for i in range(12)]),
                'animation_dist': 10000000,
                'animation_speed': 10,
                'blocked': True,
            },
            'sprite_zabor': {
                'sprite': pygame.image.load('sprites/zabor/base/1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': -0.1,
                'scale': 1.35,
                'animation': deque(
                    [pygame.image.load(f'sprites/zabor/anim/{i}.png').convert_alpha() for i in range(1)]),
                'animation_dist': 10000000,
                'animation_speed': 10,
                'blocked': True,
            },
            'sprite_god': {
                'sprite': pygame.image.load('sprites/god/base/1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': -0.8,
                'scale': 5,
                'animation': deque(
                    [pygame.image.load(f'sprites/god/anim/{i}.png').convert_alpha() for i in range(1)]),
                'animation_dist': 10000000,
                'animation_speed': 10,
                'blocked': True,
            },
            'sprite_cactus': {
                'sprite': pygame.image.load('sprites/cactus/base/1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.5,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'sprites/cactus/anim/{i}.png').convert_alpha() for i in range(1)]),
                'animation_dist': 10000000,
                'animation_speed': 10,
                'blocked': True,
            },

        }

        self.list_of_objects = [
            SpriteObject(self.sprite_settings['sprite_pin'], (1.5, 1.5)),
            SpriteObject(self.sprite_settings['sprite_rabbit'], (3.5, 1.5)),
            SpriteObject(self.sprite_settings['sprite_flame'], (5.5, 1.5)),
            SpriteObject(self.sprite_settings['sprite_tree'], (18, 6)),
            SpriteObject(self.sprite_settings['sprite_panda'], (7.5, 1.5)),
            SpriteObject(self.sprite_settings['sprite_pingvin'], (9.5, 1.5)),
            SpriteObject(self.sprite_settings['sprite_tigr'], (11.5, 1.5)),
            SpriteObject(self.sprite_settings['sprite_lev'], (13.5, 1.5)),
            SpriteObject(self.sprite_settings['sprite_monkey'], (15.5, 1.5)),
            SpriteObject(self.sprite_settings['sprite_turtle'], (17.5, 1.5)),
            SpriteObject(self.sprite_settings['sprite_zyc'], (19.5, 1.5)),
            SpriteObject(self.sprite_settings['sprite_crocodile'], (21.5, 1.5)),
            SpriteObject(self.sprite_settings['sprite_bird'], (3.5, 14.5)),
            SpriteObject(self.sprite_settings['sprite_bird1'], (5.5, 14.5)),
            SpriteObject(self.sprite_settings['sprite_bird2'], (7.5, 14.5)),
            SpriteObject(self.sprite_settings['sprite_bird3'], (9.5, 14.5)),
            SpriteObject(self.sprite_settings['sprite_tree1'], (6, 6)),
            SpriteObject(self.sprite_settings['sprite_tree'], (6, 10)),
            SpriteObject(self.sprite_settings['sprite_tree1'], (20, 10)),
            SpriteObject(self.sprite_settings['sprite_tree'], (14, 10)),
            SpriteObject(self.sprite_settings['sprite_svyatoslav'], (22, 11)),
            SpriteObject(self.sprite_settings['sprite_makar'], (22, 12)),
            SpriteObject(self.sprite_settings['sprite_kirill'], (22, 10)),
            SpriteObject(self.sprite_settings['sprite_egor'], (22, 9)),
            SpriteObject(self.sprite_settings['sprite_dugar'], (22, 8)),
            SpriteObject(self.sprite_settings['sprite_danil'], (22, 7)),
            SpriteObject(self.sprite_settings['sprite_bushes'], (2.5, 2.2)),
            SpriteObject(self.sprite_settings['sprite_bushes'], (4.5, 2.2)),
            SpriteObject(self.sprite_settings['sprite_bushes'], (6.5, 2.2)),
            SpriteObject(self.sprite_settings['sprite_bushes'], (8.5, 2.2)),
            SpriteObject(self.sprite_settings['sprite_bushes'], (10.5, 2.2)),
            SpriteObject(self.sprite_settings['sprite_bushes'], (12.5, 2.2)),
            SpriteObject(self.sprite_settings['sprite_bushes'], (14.5, 2.2)),
            SpriteObject(self.sprite_settings['sprite_bushes'], (16.5, 2.2)),
            SpriteObject(self.sprite_settings['sprite_bushes'], (18.5, 2.2)),
            SpriteObject(self.sprite_settings['sprite_bushes'], (20.5, 2.2)),
            SpriteObject(self.sprite_settings['sprite_bushes'], (22.5, 2.2)),
            SpriteObject(self.sprite_settings['sprite_zabor'], (1.5, 2)),
            SpriteObject(self.sprite_settings['sprite_zabor'], (3.5, 2)),
            SpriteObject(self.sprite_settings['sprite_zabor'], (5.5, 2)),
            SpriteObject(self.sprite_settings['sprite_zabor'], (7.5, 2)),
            SpriteObject(self.sprite_settings['sprite_zabor'], (9.5, 2)),
            SpriteObject(self.sprite_settings['sprite_zabor'], (11.5, 2)),
            SpriteObject(self.sprite_settings['sprite_zabor'], (13.5, 2)),
            SpriteObject(self.sprite_settings['sprite_zabor'], (15.5, 2)),
            SpriteObject(self.sprite_settings['sprite_zabor'], (17.5, 2)),
            SpriteObject(self.sprite_settings['sprite_zabor'], (19.5, 2)),
            SpriteObject(self.sprite_settings['sprite_zabor'], (21.5, 2)),
            SpriteObject(self.sprite_settings['sprite_god'], (25, 7)),
            SpriteObject(self.sprite_settings['sprite_cactus'], (12, 14.5)),
            SpriteObject(self.sprite_settings['sprite_cactus'], (13.5, 14.5)),
            SpriteObject(self.sprite_settings['sprite_cactus'], (15, 14.5)),
            SpriteObject(self.sprite_settings['sprite_cactus'], (16.5, 14.5)),
            SpriteObject(self.sprite_settings['sprite_cactus'], (18, 14.5)),
            SpriteObject(self.sprite_settings['sprite_cactus'], (19.5, 14.5)),
            SpriteObject(self.sprite_settings['sprite_cactus'], (21, 14.5)),
        ]


class SpriteObject:
    def __init__(self, parameters, pos):
        self.object = parameters['sprite']
        self.viewing_angles = parameters['viewing_angles']
        self.shift = parameters['shift']
        self.scale = parameters['scale']
        self.animation = parameters['animation'].copy()
        self.animation_distance = parameters['animation_dist']
        self.animation_speed = parameters['animation_speed']
        self.blocked = parameters['blocked']
        self.side = 30
        self.animation_count = 0
        self.x, self.y = pos[0] * BLOCK, pos[1] * BLOCK
        self.pos = self.x - self.side // 2, self.y - self.side // 2
        if self.viewing_angles:
            self.sprite_angles = [frozenset(range(i, i + 45))
                                  for i in range(0, 360, 45)]
            self.sprite_positions = {angle: pos for angle,
                                     pos in zip(self.sprite_angles, self.object)}

    def object_place(self, player):

        dx, dy = self.x - player.pos, self.y - player.ang
        distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI

        delta_rays = int(gamma / DELTA_ANGLE)
        current_ray = CENTER_RAY + delta_rays
        distance_to_sprite *= math.cos(HALF_FOV - current_ray * DELTA_ANGLE)

        fake_ray = current_ray + FAKE_RAYS
        if 0 <= fake_ray <= FAKE_RAYS_RANGE and distance_to_sprite > 30:
            projection_height = min(
                int(PROJECTION_COEFFICIENT / distance_to_sprite * self.scale), TWO_HEIGHT)
            half_projection_height = projection_height // 2
            shift = half_projection_height * self.shift
            if self.viewing_angles:
                if theta < 0:
                    theta += DOUBLE_PI
                theta = 360 - int(math.degrees(theta))

                for angles in self.sprite_angles:
                    if theta in angles:
                        self.object = self.sprite_positions[angles]
                        break

            sprite_object = self.object
            if self.animation and distance_to_sprite < self.animation_distance:
                sprite_object = self.animation[0]
                if self.animation_count < self.animation_speed:
                    self.animation_count += 1
                else:
                    self.animation.rotate()
                    self.animation_count = 0

            sprite_position = (current_ray * FOV_SIZE - half_projection_height,
                          HALF_HEIGHT - half_projection_height + shift)
            sprite = pygame.transform.scale(
                sprite_object, (projection_height, projection_height))
            return (distance_to_sprite, sprite, sprite_position)
        else:
            return (False,)
