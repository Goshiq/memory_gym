from typing import Iterable

import pygame

from data.constants import POINTS_PER_TILE
from source.Events import FAILED_EVENT, NEXT_GAME_EVENT
from source.ImageLoader import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(self, all_sprites: pygame.sprite.Group, is_on: bool, coord: Iterable):
        super().__init__(all_sprites)
        self.image = load_image("lamp_on.png" if is_on else "lamp_off.png")
        self.is_on = is_on
        self.is_pressed = False
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coord

    def update(self, *args, **kwargs):
        if not self.is_pressed and len(args) > 1 and args[1].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[1].pos):
            game = args[0]
            if not game.is_started:
                return
            self.is_pressed = True
            if self.is_on:
                self.image = game.images["lamp_green"]
                game.opened += 1
                game.score += POINTS_PER_TILE * game.board.secret_num // (game.board.width * game.board.height)
                if game.board.secret_num == game.opened:
                    pygame.event.post(NEXT_GAME_EVENT)
            else:
                self.image = game.images["lamp_red"]
                game.errors_left -= 1
                if not game.errors_left:
                    pygame.event.post(FAILED_EVENT)
            self.image = pygame.transform.scale(self.image, [s + 10 for s in self.image.get_size()])
            self.rect = self.rect.move(-5, -5)
