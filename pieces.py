import pygame

class TetrisPiece:

    
    def __init__(self, shape):
        self.shape = shape
        self.rotation = 0

    def get_current_shape(self):
        return self.shape[self.rotation]

    def rotate_right(self):
        self.rotation = (self.rotation + 1) % len(self.shape)

    def rotate_left(self):
        self.rotation = (self.rotation - 1) % len(self.shape)
        # print("Shape's rotation:", self.rotation)

    def draw(self, screen, x, y, block_size):
        current_shape = self.get_current_shape()

        for row, row_data in enumerate(current_shape):
            for col, cell_value in enumerate(row_data):
                if cell_value:
                    cell_color = self.get_color(cell_value)
                    cell_rect = pygame.Rect(
                        (x + col) * block_size, (y + row) * block_size, block_size, block_size
                    )
                    pygame.draw.rect(screen, cell_color, cell_rect)
                    pygame.draw.rect(screen, (128, 128, 128), cell_rect, 1)  # Add grid lines

    @staticmethod
    def get_color(value):
        colors = [
            (0, 0, 0),        # Empty cell
            (255, 128, 0),    # T
            (128, 255, 0),    # S
            (255, 0, 0),      # Z
            (255, 255, 0),    # L
            (0, 128, 255),    # J
            (0, 255, 255),    # I
            (255, 0, 255),    # O
        ]
        return colors[value]


tetris_shapes = [
    # T
     [
        [
            [1, 1, 1],
            [0, 1, 0],
        ],
        [
            [0, 1, 0],
            [1, 1, 0],
            [0, 1, 0],
        ],
        [
            [0, 1, 0],
            [1, 1, 1],
        ],
        [
            [1, 0, 0],
            [1, 1, 0],
            [1, 0, 0],
        ],
    ],
    # S
    [
        [
            [0, 2, 2],
            [2, 2, 0],
        ],
        [
            [2, 0, 0],
            [2, 2, 0],
            [0, 2, 0],
        ],
    ],
    # Z
    [
        [
            [3, 3, 0],
            [0, 3, 3],
        ],
        [
            [0, 3, 0],
            [3, 3, 0],
            [3, 0, 0],
        ],
    ],
    # L
    [
        [
            [4, 0, 0],
            [4, 4, 4],
        ],
        [
            [4, 4, 0],
            [4, 0, 0],
            [4, 0, 0],
        ],
        [
            [4, 4, 4],
            [0, 0, 4],
        ],
        [
            [0, 4, 0],
            [0, 4, 0],
            [4, 4, 0],
        ],
    ],
    # J
    [
        [
            [0, 0, 5],
            [5, 5, 5],
        ],
        [
            [5, 0, 0],
            [5, 0, 0],
            [5, 5, 0],
        ],
        [
            [5, 5,5],
            [0, 0, 5],
            ],
        [
            [0, 5, 5],
            [0, 5, 0],
            [0, 5, 0],
        ],
    ],
    # I
    [
        [
            [6, 6, 6, 6],
        ],
        [
            [6, 0, 0, 0],
            [6, 0, 0, 0],
            [6, 0, 0, 0],
            [6, 0, 0, 0],
        ],
    ],
        # O
    [
        [
            [7, 7],
            [7, 7],
        ],
    ],
]