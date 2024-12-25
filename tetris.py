import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, BLACK
from tetrimino import Tetrimino

class Tetris:
    def __init__(self):
        self.grid = [[BLACK for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
        self.current_tetrimino = Tetrimino()
        self.next_tetrimino = Tetrimino()
        self.score = 0
        self.game_over = False

    def check_collision(self):
        return self.current_tetrimino.check_collision(self.grid, 0, 0)

    def freeze_tetrimino(self):
        for i, row in enumerate(self.current_tetrimino.shape):
            for j, value in enumerate(row):
                if value:
                    self.grid[self.current_tetrimino.y + i][self.current_tetrimino.x + j] = self.current_tetrimino.color
        self.clear_lines()
        self.current_tetrimino = self.next_tetrimino
        self.next_tetrimino = Tetrimino()
        if self.check_collision():
            self.game_over = True

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(cell == BLACK for cell in row)]
        lines_cleared = len(self.grid) - len(new_grid)
        self.score += lines_cleared ** 2
        self.grid = [[BLACK for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(lines_cleared)] + new_grid

    def move(self, dx, dy):
        if not self.current_tetrimino.check_collision(self.grid, dx, dy):
            self.current_tetrimino.x += dx
            self.current_tetrimino.y += dy
        elif dy:
            self.freeze_tetrimino()

    def rotate(self):
        original_shape = self.current_tetrimino.shape[:]
        self.current_tetrimino.rotate()
        if self.check_collision():
            self.current_tetrimino.shape = original_shape

    def drop(self):
        while not self.current_tetrimino.check_collision(self.grid, 0, 1):
            self.current_tetrimino.y += 1
        self.freeze_tetrimino()

    def draw(self, screen):
        screen.fill(BLACK)
        for y, row in enumerate(self.grid):
            for x, color in enumerate(row):
                if color != BLACK:
                    pygame.draw.rect(screen, color, pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        ghost_y = self.current_tetrimino.get_ghost_position(self.grid)
        self.current_tetrimino.draw_ghost(screen, ghost_y)
        self.current_tetrimino.draw(screen)
        pygame.display.update()
