from load_sprit import load_sprit
from constant import BURGER_SPOT_HEIGHT, BURGER_SPOT_WIDTH, WINDOW_HEIGHT


class Burger_spot:

    def __init__(self):
        self.BURGER_SPOT = load_sprit("Background", "BURGER_SPOT", 1,
                                      BURGER_SPOT_WIDTH, BURGER_SPOT_HEIGHT)[0]
        self.x = 50
        self.y = WINDOW_HEIGHT - 50
