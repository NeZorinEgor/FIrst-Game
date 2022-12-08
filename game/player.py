from settings import *
import pygame
import math

class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += movement_speed * cos_a
            self.y += movement_speed * sin_a
            print("W")
        if keys[pygame.K_s]:
            self.x += -movement_speed * cos_a
            self.y += -movement_speed * sin_a
            print("S")
        if keys[pygame.K_a]:
            self.x += movement_speed * sin_a
            self.y += -movement_speed * cos_a
            print("A")
        if keys[pygame.K_d]:
            self.x += -movement_speed * sin_a
            self.y += movement_speed * cos_a
            print("D")
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
            print("←")
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
            print("→")
