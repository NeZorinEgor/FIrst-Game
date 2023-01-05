import pygame
from settings import *
from raycast import raycast


class Area:
    def __init__(self, screen):
        self.screen = screen

    def environment(self):
        pygame.draw.rect(self.screen, SKY, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.screen, FLOOR,
                         (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, pos, angle):
        raycast(self.screen, pos, angle)
