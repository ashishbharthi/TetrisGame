import sys
import pygame
from grid import TetrisGrid
from pieces import TetrisPiece, tetris_shapes
import random

def main():
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font(pygame.font.get_default_font(), 24)

    #globals
    block_size = 30
    target_fps = 30
    grid_width = 10
    grid_height = 20
    screen_width = block_size*grid_width + (block_size*7)
    screen_height = block_size*20

    paused = False

    
    def draw_text(text, x, y, color=(255, 255, 255), background_color=(0, 0, 0)):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(topleft=(x, y))
        pygame.draw.rect(screen, background_color, text_rect)
        screen.blit(text_surface, (x, y))
    
    def draw_next_piece(piece, x, y, block_size, background_color=(0, 0, 0)):
        pygame.draw.rect(screen, background_color, (x, y, block_size * 4, block_size * 4))

        for row_idx, row in enumerate(piece.get_current_shape()):
            for col_idx, cell_value in enumerate(row):
                if cell_value:
                    cell_color = piece.get_color(cell_value)
                    pygame.draw.rect(screen, cell_color, (x + col_idx * block_size, y + row_idx * block_size, block_size - 1, block_size - 1))


    def spawn_piece():
        new_piece = TetrisPiece(random.choice(tetris_shapes))
        # new_piece = TetrisPiece(tetris_shapes[3])
        piece_x = grid_width // 2 - len(new_piece.get_current_shape()[0]) // 2
        piece_y = 0
        return new_piece, piece_x, piece_y

    score = 0

    # Set up the game window
    screen_width, screen_height = screen_width, screen_height
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Tetris")

    # Initialize clock object and set target frame rate
    clock = pygame.time.Clock()

    piece, piece_x, piece_y = spawn_piece()
    next_piece = spawn_piece()[0]

    fall_time = 0
    fall_interval = 500  # 1000 milliseconds = 1 second

    tetris_grid = TetrisGrid(grid_height, grid_width)

    running = True
    # Main game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not tetris_grid.check_collision(piece, piece_x - 1, piece_y):
                        piece_x -= 1
                elif event.key == pygame.K_RIGHT:
                    if not tetris_grid.check_collision(piece, piece_x + 1, piece_y):
                        piece_x += 1
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    piece.rotate_right()
                if event.key == pygame.K_DOWN:
                    while not tetris_grid.check_collision(piece, piece_x, piece_y + 1):
                        piece_y += 1  
                if event.key == pygame.K_p:  # Use the 'p' key to pause and resume the game
                    paused = not paused
                    if paused:
                        pygame.time.delay(100)  # Add a small delay to avoid accidental unpausing
                    continue  
        
        if not paused:
            tetris_grid.draw(screen, block_size)  # Adjust the block_size (e.g., 30) as needed

            start_time = pygame.time.get_ticks()
            # ...

            if start_time - fall_time > fall_interval:
                if not tetris_grid.check_collision(piece, piece_x, piece_y + 1):
                    print(piece_x, piece_y)
                    print("no collision")
                    piece_y += 1
                else:
                    tetris_grid.merge_piece(piece, piece_x, piece_y)
                    
                    piece = next_piece
                    piece_x, piece_y = tetris_grid.get_spawn_location(piece)
                    next_piece = spawn_piece()[0]

                    cleared_lines = tetris_grid.clear_full_lines()

                    # Update the score based on the number of cleared lines
                    if cleared_lines == 1:
                        score += 100
                    elif cleared_lines == 2:
                        score += 300
                    elif cleared_lines == 3:
                        score += 500
                    elif cleared_lines == 4:
                        score += 800
                    
                    # Print the current score (you can later display it on the screen)
                    draw_text(f"Score: {score}", block_size*10 + 10, block_size*10)
                    
                    print(piece_x, piece_y)
                    # # Check if the game is over
                    if tetris_grid.game_over(piece, piece_x, piece_y+1):
                        draw_text("Game Over", screen.get_width() // 2 - 50, screen.get_height() // 2 - 20, color=(255, 0, 0))
                        pygame.display.flip()
                        pygame.time.delay(5000)  # Show the "Game Over" message for 2 seconds
                        running = False  # Exit the game loop

                fall_time = start_time

            # print("Shape's rotation:", piece.shape, piece_x, piece_y)

            # ...
            piece.draw(screen, piece_x , piece_y , block_size)

            draw_next_piece(next_piece, tetris_grid.columns * block_size + 50, 50, block_size)

        if paused:
            draw_text("Paused", screen.get_width() // 2 - 50, screen.get_height() // 2 - 20, color=(255, 255, 0))

        # Update the display
        pygame.display.flip()

        # Limit frame rate
        clock.tick(target_fps)

if __name__ == "__main__":
    main()
