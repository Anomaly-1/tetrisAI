import random
import pygame
from settings import BLOCK_SIZE, COLORS, SHAPES, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, GHOST_COLOR

class Tetrimino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = SCREEN_WIDTH // BLOCK_SIZE // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

    def draw(self, screen):
        for i, row in enumerate(self.shape):
            for j, value in enumerate(row):
                if value:
                    pygame.draw.rect(screen, self.color, pygame.Rect((self.x + j) * BLOCK_SIZE, (self.y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def get_ghost_position(self, grid):
        ghost_y = self.y
        while not self.check_collision(grid, 0, ghost_y - self.y + 1):
            ghost_y += 1
        return ghost_y

    def check_collision(self, grid, x_offset, y_offset):
        for i, row in enumerate(self.shape):
            for j, value in enumerate(row):
                if value:
                    x = self.x + j + x_offset
                    y = self.y + i + y_offset
                    if x < 0 or x >= SCREEN_WIDTH // BLOCK_SIZE or y >= SCREEN_HEIGHT // BLOCK_SIZE or grid[y][x] != BLACK:
                        return True
        return False

    def draw_ghost(self, screen, ghost_y):
        for i, row in enumerate(self.shape):
            for j, value in enumerate(row):
                if value:
                    pygame.draw.rect(screen, GHOST_COLOR, pygame.Rect((self.x + j) * BLOCK_SIZE, (ghost_y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
