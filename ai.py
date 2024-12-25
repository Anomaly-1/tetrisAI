import copy

class AI:
    def __init__(self, heights_weight, lines_weight, holes_weight, bumpiness_weight):
        self.heights_weight = heights_weight
        self.lines_weight = lines_weight
        self.holes_weight = holes_weight
        self.bumpiness_weight = bumpiness_weight

    
    def best_move(self, game):
        best_score = None
        best_move = None
        current_piece = game.current_tetrimino

        for rotation in range(4):
            piece = copy.deepcopy(current_piece)
            for _ in range(rotation):
                piece.rotate()

            # Adjust the column loop to ensure it checks the rightmost valid position
            max_col = len(game.grid[0]) - len(piece.shape[0])
            for col in range(max_col + 1):
                piece_clone = copy.deepcopy(piece)
                piece_clone.x = col

                while not piece_clone.check_collision(game.grid, 0, 1):
                    piece_clone.y += 1

                grid_clone = self.simulate_grid(game.grid, piece_clone)
                score = self.evaluate_grid(grid_clone)

                if best_score is None or score > best_score:
                    best_score = score
                    best_move = (rotation, col)

        return best_move

    def simulate_grid(self, grid, piece):
        grid_clone = [row[:] for row in grid]
        for i, row in enumerate(piece.shape):
            for j, value in enumerate(row):
                if value:
                    grid_clone[piece.y + i][piece.x + j] = piece.color
        return grid_clone

    def evaluate_grid(self, grid):
        return (
            self.heights_weight * self.aggregate_height(grid) +
            self.lines_weight * self.complete_lines(grid) +
            self.holes_weight * self.holes(grid) +
            self.bumpiness_weight * self.bumpiness(grid)
        )

    def aggregate_height(self, grid):
        height_sum = 0
        for col in range(len(grid[0])):
            for row in range(len(grid)):
                if grid[row][col] != (0, 0, 0):  # Non-black color means filled cell
                    height_sum += len(grid) - row
                    break
        return height_sum

    def complete_lines(self, grid):
        return sum(1 for row in grid if all(cell != (0, 0, 0) for cell in row))

    def holes(self, grid):
        holes = 0
        for col in range(len(grid[0])):
            block_found = False
            for row in range(len(grid)):
                if grid[row][col] != (0, 0, 0):
                    block_found = True
                elif block_found and grid[row][col] == (0, 0, 0):
                    holes += 1
        return holes

    def bumpiness(self, grid):
        heights = []
        for col in range(len(grid[0])):
            for row in range(len(grid)):
                if grid[row][col] != (0, 0, 0):
                    heights.append(len(grid) - row)
                    break
            else:
                heights.append(0)

        bumpiness_sum = 0
        for i in range(len(heights) - 1):
            bumpiness_sum += abs(heights[i] - heights[i + 1])
        return bumpiness_sum
