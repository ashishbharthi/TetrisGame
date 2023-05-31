import unittest
from grid import TetrisGrid
from pieces import TetrisPiece

class TestTetrisGrid(unittest.TestCase):
    def test_create_empty_grid():
        grid = TetrisGrid(20, 10)
        assert len(grid.grid) == 20
        assert len(grid.grid[0]) == 10
        assert all(cell == 0 for row in grid.grid for cell in row)

    test_create_empty_grid()

    def test_check_collision():
        grid = TetrisGrid(20, 10)
        piece = TetrisPiece([(0, 1), (0, 1), (0, 1), (0, 1)]) # I

        # Test collision with the wall
        assert grid.check_collision(piece, -1, 0) == True
        assert grid.check_collision(piece, 7, 0) == True

        # Test collision with the floor
        assert grid.check_collision(piece, 5, 19) == True

        # Test collision with a piece
        grid.grid[5][5] = (255, 0, 0)
        assert grid.check_collision(piece, 4, 4) == True

        # Test no collision
        assert grid.check_collision(piece, 5, 0) == False

    test_check_collision()

    def test_merge_piece():
        grid = TetrisGrid(20, 10)
        piece = TetrisPiece([(0, 1), (0, 1), (0, 1), (0, 1)]) # I
        grid.merge_piece(piece, 5, 0)

        assert grid.grid[0][5] == piece.get_color(1)
        assert grid.grid[1][5] == piece.get_color(1)
        assert grid.grid[2][5] == piece.get_color(1)
        assert grid.grid[3][5] == piece.get_color(1)

    test_merge_piece()

    def test_clear_full_lines():
        grid = TetrisGrid(20, 10)
        grid.grid[19] = [(255, 0, 0)] * 10
        grid.grid[18] = [(255, 0, 0)] * 10
        grid.grid[17] = [(255, 0, 0)] * 10
        cleared_lines = grid.clear_full_lines()

        assert cleared_lines == 3
        assert all(cell == 0 for row in grid.grid for cell in row)

    test_clear_full_lines()

    def test_game_over():
        grid = TetrisGrid(20, 10)
        piece = TetrisPiece([(0, 1), (0, 1), (0, 1), (0, 1)]) # I
        grid.grid[0][5] = (255, 0, 0)

        spawn_x, spawn_y = grid.get_spawn_location(piece)
        assert grid.game_over(piece, spawn_x, spawn_y) == True

    test_game_over()


if __name__ == "__main__":
    unittest.main()

