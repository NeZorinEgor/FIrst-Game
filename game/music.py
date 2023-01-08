import pygame

class Music:

    def play_music():
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        audio = pygame.mixer.Sound('bgmusic/ost.mp3')
        audio.set_volume(0.3)
        audio.play(-1)