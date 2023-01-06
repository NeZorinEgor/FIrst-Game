import pygame
from settings import *
from raycast import raycast


class Area:
    def __init__(self, screen, screen_field):
        self.screen = screen
        self.screen_field = screen_field
        self.textures = {'|': pygame.image.load('images/texture1.png').convert(),
                         'I': pygame.image.load('images/texture2.png').convert(),
                         'SKY': pygame.image.load('images/sky.png').convert()
                         }

    def environment(self, angle):
        sky_offset = -5 * math.degrees(angle) % WIDTH
        self.screen.blit(self.textures['SKY'], (sky_offset, 0))
        self.screen.blit(self.textures['SKY'], (sky_offset - WIDTH, 0))
        self.screen.blit(self.textures['SKY'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.screen, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, pos, angle):
        raycast(self.screen, pos, angle, self.textures)