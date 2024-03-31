import pygame
from pygame.sprite import Group

from data.constants import DEFAULT_SECRETS_NUM, ERRORS_ALLOWED
from source.ImageLoader import load_image


class NextGameButton(pygame.sprite.Sprite):
    def __init__(self, group: Group, screen_size):
        super().__init__(group)
        self.image = load_image("next.png")
        self.rect = self.image.get_rect()
        self.rect.x = (screen_size[0] - self.rect.size[0]) // 2
        self.rect.y = (screen_size[1] - self.rect.size[1]) // 2

    def update(self, *args):
        if args and len(args) > 1 and args[1].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[1].pos):
            game = args[0]
            game.opened = 0
            game.errors_left = ERRORS_ALLOWED
            game.screen.fill((0, 0, 0))
            game.dynamic_sprites.empty()
            game.static_sprites.empty()
            game.board.secret_num = DEFAULT_SECRETS_NUM
            game.board.generate_field(game.dynamic_sprites, game.screen)
            game.next_game = True
            game.running = False

