import pygame


class TetrisGrid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = self.create_empty_grid()

    def create_empty_grid(self):
        return [[0 for _ in range(self.columns)] for _ in range(self.rows)]


    def check_collision(self, piece, x, y):
        piece_shape = piece.get_current_shape()
        for row, row_data in enumerate(piece_shape):
            for col, cell_value in enumerate(row_data):
                if cell_value:
                    grid_x = x + col
                    grid_y = y + row
                    if grid_x < 0 or grid_x >= self.columns or grid_y >= self.rows:
                        return True
                    if self.grid[grid_y][grid_x]:
                        return True
        return False

    def merge_piece(self, piece, x, y):
        piece_shape = piece.get_current_shape()
        for row, row_data in enumerate(piece_shape):
            for col, cell_value in enumerate(row_data):
                if cell_value:
                    self.grid[y + row][x + col] = piece.get_color(cell_value)

    def clear_full_lines(self):
        cleared_lines = 0
        new_grid = [[] for _ in range(self.rows)]
        empty_row = [0 for _ in range(self.columns)]

        current_row = self.rows - 1
        for row in reversed(self.grid):
            if all(cell_value for cell_value in row):
                cleared_lines += 1
            else:
                new_grid[current_row] = row
                current_row -= 1

        # Fill the remaining rows with empty rows
        for row in range(current_row + 1):
            new_grid[row] = empty_row.copy()

        self.grid = new_grid
        return cleared_lines

    def get_spawn_location(self, piece):
        spawn_x = self.columns // 2 - len(piece.shape[0]) // 2
        spawn_y = 0 #0 - max([row_idx for row_idx, row in enumerate(piece.shape) if any(cell_value for cell_value in row)])
        return spawn_x, spawn_y
    
    def game_over(self, piece, x, y):
        return self.check_collision(piece, x, y)

    def draw(self, screen, block_size):
        for row in range(self.rows):
            for col in range(self.columns):
                cell_color = (0, 0, 0) if self.grid[row][col] == 0 else self.grid[row][col]
                cell_rect = pygame.Rect(col * block_size, row * block_size, block_size, block_size)
                pygame.draw.rect(screen, cell_color, cell_rect)
                pygame.draw.rect(screen, (128, 128, 128), cell_rect, 1)  # Add grid lines