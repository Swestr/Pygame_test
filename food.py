from load_sprit import load_sprit
from constant import FOOD_PIECE_WIDTH, FOOD_PIECE_HEIGHT, WINDOW_HEIGHT


class Bread_bottom:

    def __init__(self):
        self.FOOD_PIECES = load_sprit("food", "bread/bottom", 4,
                                      FOOD_PIECE_WIDTH, FOOD_PIECE_HEIGHT)
        self.DIFF_WITH_SPOT_x = 2
        self.DIFF_WITH_SPOT_y = -7
