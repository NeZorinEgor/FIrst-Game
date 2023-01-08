from settings import *
import pygame
import math
from field import coll_wall


class Player:
    def __init__(self, sprites):
        self.pos, self.ang = PLAYER_POSITION
        self.sprites = sprites
        self.angle = PLAYER_ANGLE
        self.sensitivity = 0.004
        self.side = 50
        self.rect = pygame.Rect(*PLAYER_POSITION, self.side, self.side)
        self.coll_sprites = [pygame.Rect(*obj.pos, obj.side, obj.side) for obj in
                             self.sprites.list_of_objects if obj.blocked]
        self.coll_list = coll_wall + self.coll_sprites

    @property
    def get_position(self):
        return (self.pos, self.ang)

    def check_collision(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(self.coll_list)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = self.coll_list[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.pos += dx
        self.ang += dy

    def moving(self):
        self.keyboard_keys()
        self.mouse_control()
        self.rect.center = self.pos, self.ang
        self.angle %= DOUBLE_PI

    def keyboard_keys(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()

        if keys[pygame.K_w]:
            dx = PLAYER_MOVEMENT * cos_a
            dy = PLAYER_MOVEMENT * sin_a
            self.check_collision(dx, dy)
        if keys[pygame.K_s]:
            dx = -PLAYER_MOVEMENT * cos_a
            dy = -PLAYER_MOVEMENT * sin_a
            self.check_collision(dx, dy)
        if keys[pygame.K_a]:
            dx = PLAYER_MOVEMENT * sin_a
            dy = -PLAYER_MOVEMENT * cos_a
            self.check_collision(dx, dy)
        if keys[pygame.K_d]:
            dx = -PLAYER_MOVEMENT * sin_a
            dy = PLAYER_MOVEMENT * cos_a
            self.check_collision(dx, dy)
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += difference * self.sensitivity
