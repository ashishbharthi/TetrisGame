import pygame


class TetrisGrid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = self.create_empty_grid()

    def create_empty_grid(self):
        return [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self, screen, block_size):
        for row in range(self.rows):
            for col in range(self.columns):
                cell_color = (0, 0, 0) if self.grid[row][col] == 0 else (255, 255, 255)
                cell_rect = pygame.Rect(col * block_size, row * block_size, block_size, block_size)
                pygame.draw.rect(screen, cell_color, cell_rect)
                pygame.draw.rect(screen, (128, 128, 128), cell_rect, 1)  # Add grid lines