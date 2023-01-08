import pygame
import pygame_menu
from game import Game

class StartMenu:
    def __init__(self, menu_widht, menu_height):
        self.menu_widht = menu_widht
        self.menu_height = menu_height

    def start_main_menu(self):
        surface = pygame.display.set_mode((self.menu_widht, self.menu_height))

        mytheme = pygame_menu.themes.THEME_ORANGE.copy()
        mytheme.background_color =  (68,148,74)
        mytheme.border_width = 10
        mytheme.border_color = (23,79,61)
        mytheme.widget_font_color = (0, 0, 0)
        mytheme.widget_border_width = 0
        mytheme.widget_shadow_color = (0, 0, 0)
        mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE

        menu = pygame_menu.Menu('', self.menu_widht // 1.7, self.menu_height // 1.7, theme=mytheme)
        menu.add.vertical_margin(20)
        menu.add.button('Начать игру', Game.start_game, font_size=35)
        menu.add.button('Об игре', self.information)
        menu.add.button('Выйти из игры', pygame_menu.events.EXIT)

        bg_image = pygame.image.load("images/image.png")
        text_bg = pygame.image.load("images/text.png")
        while True:
            surface.blit(bg_image, (0, 0))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
            if menu.is_enabled():
                menu.update(events)
                menu.draw(surface)
            surface.blit(text_bg, (340, 140))
            pygame.display.update()

    def information(self):
        surface = pygame.display.set_mode((self.menu_widht, self.menu_height))

        mytheme = pygame_menu.themes.THEME_ORANGE.copy()
        mytheme.background_color = (68, 148, 74)
        mytheme.border_width = 10
        mytheme.border_color = (23, 79, 61)
        mytheme.widget_font_color = (0, 0, 0)
        mytheme.widget_border_width = 0
        mytheme.widget_shadow_color = (0, 0, 0)
        mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE

        menu = pygame_menu.Menu('', self.menu_widht // 1.7, self.menu_height // 1.7, theme=mytheme)
        menu.add.vertical_margin(50)
        menu.add.label("Симулятор зоопарка", font_size=35)
        menu.add.vertical_margin(10)
        information = "В игре можно ходить и любоваться животными :)"
        menu.add.label(information, max_char=-1, font_size=25)
        menu.add.vertical_margin(50)
        menu.add.button('Вернуться назад', self.start_main_menu)

        bg_image = pygame.image.load("images/image.png")
        text_bg = pygame.image.load("images/text.png")
        while True:
            surface.blit(bg_image, (0, 0))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
            if menu.is_enabled():
                menu.update(events)
                menu.draw(surface)
            surface.blit(text_bg, (340, 140))
            pygame.display.update()

pygame.init()
menu_sh = StartMenu(1200, 800)
menu_sh.start_main_menu()
