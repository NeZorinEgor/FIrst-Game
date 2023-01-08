import pygame
from settings import *
from player import Player
from sprites import *
from raycast import raycast
from area import Drawing
from music import Music

class Game:
    def start_game():
        sc = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.mouse.set_visible(False)

        sprites = Sprites()
        clock = pygame.time.Clock()
        player = Player(sprites)
        drawing = Drawing(sc)
        Music.play_music()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            player.moving()
            sc.fill(WHITE)

            drawing.environment(player.angle)
            walls = raycast(player, drawing.textures)
            drawing.world(walls + [obj.object_place(player)
                          for obj in sprites.list_of_objects])

            pygame.display.flip()
            clock.tick(FPS)
