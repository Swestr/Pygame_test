from load_sprit import load_sprit
from constant import FOOD_PIECE_WIDTH, FOOD_PIECE_HEIGHT


class Bread_bottom:
    def __init__(self):
        self.FOOD_PIECES = load_sprit("food", "bread/bottom", 4,
                                      FOOD_PIECE_WIDTH, FOOD_PIECE_HEIGHT)
        self.DIFF_WITH_SPOT_x = 2
        self.DIFF_WITH_SPOT_y = -7


class Meet:
    def __init__(self):
        self.FOOD_PIECES = load_sprit("food", "meet", 4,
                                      FOOD_PIECE_WIDTH, FOOD_PIECE_HEIGHT)
        self.DIFF_WITH_SPOT_x = 2
        self.DIFF_WITH_SPOT_y = -5 - FOOD_PIECE_HEIGHT


class Salad:
    def __init__(self):
        self.FOOD_PIECES = load_sprit("food", "salad", 4,
                                      FOOD_PIECE_WIDTH, FOOD_PIECE_HEIGHT)
        self.DIFF_WITH_SPOT_x = 2
        self.DIFF_WITH_SPOT_y = -1 - FOOD_PIECE_HEIGHT * 2


class Bread_top:
    def __init__(self):
        self.FOOD_PIECES = load_sprit("food", "bread/top", 4,
                                      FOOD_PIECE_WIDTH, FOOD_PIECE_HEIGHT)
        self.DIFF_WITH_SPOT_x = 2
        self.DIFF_WITH_SPOT_y = +1 - FOOD_PIECE_HEIGHT * 3


class Burger:
    def __init__(self):
        self.layers = [Bread_bottom(), Meet(), Salad(), Bread_top()]
