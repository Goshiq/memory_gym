import pygame
from pygame.event import Event

NEXT_GAME_EVENT, NEW_GAME_EVENT, FAILED_EVENT, TIMER_EVENT = [Event(pygame.USEREVENT + 1 + i) for i in range(4)]
