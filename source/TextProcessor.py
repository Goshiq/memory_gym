import os

import pygame

from data.constants import FONT_NAME


class TextProcessor:
    def __init__(self):
        pygame.font.init()
        full_font_name = os.path.join("data", "font", FONT_NAME)
        self.font = pygame.font.Font(full_font_name, 48)
        self.font_shadow = pygame.font.Font(full_font_name, 54)

    def show_score(self, score, screen):
        screen_size = screen.get_size()
        score_text = self.font.render(f'Баллы: {score}', True, (180, 180, 180))
        score_text_shadow = self.font_shadow.render(f'Баллы: {score}', True, (0, 0, 0))
        screen.blit(score_text_shadow, ((screen_size[0] - score_text_shadow.get_size()[0]) // 2, 60))
        screen.blit(score_text, ((screen_size[0] - score_text.get_size()[0]) // 2, 50))
