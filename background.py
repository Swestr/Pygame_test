from load_sprit import load_sprit
from constant import BURGER_SPOT_HEIGHT, BURGER_SPOT_WIDTH
from constant import BACKGROUND_WIDTH, BACKGROUND_HEIGHT, COL, ROW


class Burger_spot:
    def __init__(self, x, y):
        self.BURGER_SPOT = load_sprit("background", "burger_spot", 1,
                                      BURGER_SPOT_WIDTH, BURGER_SPOT_HEIGHT)[0]
        self.x = x
        self.y = y


class Background_piece:
    def __init__(self, x, y, title):
        self.IMAGE = load_sprit(
            "background", title, 1, BACKGROUND_WIDTH, BACKGROUND_HEIGHT)[0]
        self.x = x * BACKGROUND_WIDTH
        self.y = y * BACKGROUND_HEIGHT


class Platform(Background_piece):
    def __init__(self, x, y):
        super().__init__(x, y, "platform")


class Ladder(Background_piece):
    def __init__(self, x, y):
        super().__init__(x, y, "ladder")


class PlatformLadder(Background_piece):
    def __init__(self, x, y):
        super().__init__(x, y, "ladder_platform")


# 8 lignes, 21 colonnes
def createBackground():
    background = []
    for col in range(COL):
        for row in [0, 3, 5, 7]:
            background.append(Platform(col, row))
    return background
