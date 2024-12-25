# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900
BLOCK_SIZE = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GHOST_COLOR = (128, 128, 128, 100)
COLORS = [
    (0, 255, 255),    # Cyan
    (255, 255, 0),    # Yellow
    (255, 165, 0),    # Orange
    (0, 0, 255),      # Blue
    (255, 0, 0),      # Red
    (0, 255, 0),      # Green
    (128, 0, 128)     # Purple
]

# Tetrimino shapes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

# Speed (Seconds per move on AI mode)

SPEED = 0.01