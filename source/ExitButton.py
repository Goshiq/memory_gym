import sys

import pygame
from pygame.sprite import Group

from source.ImageLoader import load_image


class ExitButton(pygame.sprite.Sprite):
    def __init__(self, group: Group, screen_size):
        super().__init__(group)
        self.image = load_image("exit.png")
        self.rect = self.image.get_rect()
        self.rect.x = screen_size[0] - self.rect.size[0] - 20
        self.rect.y = screen_size[1] - self.rect.size[1] - 20

    def update(self, *args):
        if args and len(args) > 1 and args[1].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[1].pos):
            sys.exit()
