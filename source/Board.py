import random

from pygame import Surface
from pygame.sprite import Group

from data.constants import BORDER_LEFT, BORDER_TOP, EMPTY_CELL, FIELD_WIDTH, FIELD_HEIGHT, \
    DEFAULT_SECRETS_NUM, FILLED_CELL
from source.ImageLoader import load_image
from source.Tile import Tile


class Board:
    def __init__(self, width=FIELD_WIDTH, height=FIELD_HEIGHT):
        self.width = width
        self.height = height
        self.board = [[EMPTY_CELL] * width for _ in range(height)]
        self.left_border = BORDER_LEFT
        self.top_border = BORDER_TOP
        self.cell_size = load_image("lamp_on.png").get_size()[0]
        self.secret_num = DEFAULT_SECRETS_NUM
        self.secret_cells = []

    def generate_field(self, group: Group, screen: Surface):
        secrets = self.secret_num
        if secrets > self.width * self.height // 2:
            if self.width <= self.height:
                self.width += 1
            else:
                self.height += 1
            self.secret_num = DEFAULT_SECRETS_NUM
        self.secret_cells = []
        self.board = [[EMPTY_CELL] * self.width for _ in range(self.height)]
        secret_cells = random.sample(range(self.width * self.height), self.secret_num)
        self.secret_cells = secret_cells
        [self.update_cell(cell) for cell in secret_cells]
        screen_size = screen.get_size()
        top = (screen_size[1] - (self.cell_size + self.top_border) * self.height) // 2
        left = (screen_size[0] - (self.cell_size + self.left_border) * self.width) // 2
        for y, row in enumerate(self.board):
            for x, item in enumerate(row):
                coord = left + x * (self.cell_size + self.left_border), top + y * (self.cell_size + self.top_border)
                Tile(group, self.board[y][x], coord)

    def update_cell(self, cell_index, new_status=FILLED_CELL):
        y_index = cell_index // self.width
        x_index = cell_index - y_index * self.width
        self.board[y_index][x_index] = new_status
