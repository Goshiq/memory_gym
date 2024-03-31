import os
import sys

import pygame


def load_image(name):
    fullname = os.path.join("data", "img", name)
    if not os.path.isfile(fullname):
        sys.exit(f"Файл с изображением '{fullname}' не найден")
    image = pygame.image.load(fullname)
    return image


def load_images():
    image_names = [
        "back.jpg",
        "lamp_green.png",
        "lamp_red.png",
        "lamp_off.png",
        "lamp_on.png",
    ]
    return {name.split('.')[0]: load_image(name) for name in image_names}
