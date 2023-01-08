import sys
import pygame as pg
from player import Player
from sprites import *
from raycast import raycast
from area import Drawing
from music import Music

class Game:

    def start_game():
        running_game = True
        sc = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.mouse.set_visible(False)
        sprites = Sprites()
        clock = pygame.time.Clock()
        player = Player(sprites)
        drawing = Drawing(sc)
        Music.play_music()

        while running_game:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        sys.exit()

            player.moving()
            sc.fill(WHITE)

            drawing.environment(player.angle)
            walls = raycast(player, drawing.textures)
            drawing.world(walls + [obj.object_place(player)
                          for obj in sprites.list_of_objects])

            pygame.display.flip()
            clock.tick(FPS)

