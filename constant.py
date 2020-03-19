WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 10
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

MULTIPLIER = 2

CHARACTER_WIDTH = CHARACTER_HEIGHT = 16 * MULTIPLIER

BURGER_SPOT_WIDTH = 34 * MULTIPLIER
BURGER_SPOT_HEIGHT = 6 * MULTIPLIER
BURGER_SPOT_NB = 4
BURGER_LAYER_SPACE = WINDOW_WIDTH - BURGER_SPOT_NB * BURGER_SPOT_WIDTH
BURGER_LAYER_SPACE /= (BURGER_SPOT_NB + 1)

FOOD_PIECE_WIDTH = FOOD_PIECE_HEIGHT = 8 * MULTIPLIER

BACKGROUND_WIDTH = BACKGROUND_HEIGHT = 16 * MULTIPLIER

ROW = 8
COL = 21

MARGIN_LEFT = 2 * BACKGROUND_WIDTH
MARGIN_RIGHT = (2 + COL) * BACKGROUND_WIDTH
MARGIN_TOP = 2 * BACKGROUND_HEIGHT
MARGIN_BOTTOM = (2 + ROW) * BACKGROUND_HEIGHT - 8
