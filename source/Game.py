import pygame
from pygame import Surface

from data.constants import GAME_FPS, ERRORS_ALLOWED, TIME_TO_HIDE
from source.Board import Board
from source.Events import FAILED_EVENT, NEXT_GAME_EVENT, TIMER_EVENT
from source.ExitButton import ExitButton
from source.ImageLoader import load_image, load_images
from source.NextGameButton import NextGameButton
from source.TextProcessor import TextProcessor


class Game:

    def __init__(self):
        self.score = 0
        self.opened = 0
        self.running = False
        self.is_started = False
        self.next_game = False
        self.errors_left = ERRORS_ALLOWED
        self.dynamic_sprites = pygame.sprite.Group()
        self.static_sprites = pygame.sprite.Group()
        self.images = load_images()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # генерируем игровое поле.
        board = Board()
        self.board = board
        board.generate_field(self.dynamic_sprites, self.screen)

    def init_static(self):
        # вставляем фон
        background: Surface = self.images["back"]
        screen_size = self.screen.get_size()
        background = pygame.transform.scale(background, screen_size)
        self.screen.blit(background, (0, 0))
        # logo
        logo = pygame.transform.scale(load_image("logo.png"), (100, 100))
        self.screen.blit(logo, (20, 20))
        # отрисовываем меню
        ExitButton(self.static_sprites, screen_size)

    def start_game(self):
        self.running = True
        text_processor = TextProcessor()
        clock = pygame.time.Clock()
        pygame.time.set_timer(TIMER_EVENT, TIME_TO_HIDE, loops=1)
        while self.running:
            self.screen.fill((255, 255, 255))
            clock.tick(GAME_FPS)
            self.init_static()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event == TIMER_EVENT:
                    for sprite in self.dynamic_sprites:
                        sprite.image = self.images["lamp_off"]
                    self.is_started = True
                if event == FAILED_EVENT:
                    self.screen.fill((0, 0, 0))
                    self.dynamic_sprites.empty()
                    self.static_sprites.empty()
                    self.score = 0
                    self.is_started = False
                    NextGameButton(self.static_sprites, self.screen.get_size())
                if event == NEXT_GAME_EVENT:
                    self.opened = 0
                    self.errors_left = ERRORS_ALLOWED
                    self.screen.fill((0, 0, 0))
                    self.dynamic_sprites.empty()
                    self.board.secret_num += 1
                    self.running = False
                    self.next_game = True
                    self.board.generate_field(self.dynamic_sprites, self.screen)
                self.dynamic_sprites.update(self, event)
                self.static_sprites.update(self, event)
            self.static_sprites.draw(self.screen)
            self.dynamic_sprites.draw(self.screen)
            text_processor.show_score(self.score, self.screen)
            pygame.display.update()
        if self.next_game:
            self.is_started = False
            self.start_game()
