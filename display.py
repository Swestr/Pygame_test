import pygame
from constant import BLACK, FOOD_PIECE_WIDTH
from constant import MARGIN_TOP, MARGIN_LEFT


def display(screen, player, background, burger_spot, burger):
    STATE = player.character_state
    ID = player.character_state_id
    POSITION = (player.x, player.y)

    # Le background
    screen.fill(BLACK)
    for piece in background:
        piece.IMAGE.set_colorkey(BLACK)
        screen.blit(piece.IMAGE, (piece.x + MARGIN_LEFT, piece.y + MARGIN_TOP))

    # Le personnage
    if ID == -1:
        STATE.set_colorkey(BLACK)
        screen.blit(STATE, POSITION)
    else:
        STATE[ID % len(STATE)].set_colorkey(BLACK)
        screen.blit(STATE[ID % len(STATE)], POSITION)

    # Emplacements à burger entier
    for burger_spot_id in range(len(burger_spot)):
        burger_spot[burger_spot_id].BURGER_SPOT.set_colorkey(BLACK)
        screen.blit(burger_spot[burger_spot_id].BURGER_SPOT,
                    (burger_spot[burger_spot_id].x, burger_spot[burger_spot_id].y))

    # Burger
    for burger_id in range(len(burger)):
        for burger_layer in range(len(burger[burger_id])):
            for burger_image in range(len(burger[burger_id][burger_layer].FOOD_PIECES)):
                burger[burger_id][burger_layer].FOOD_PIECES[burger_image].set_colorkey(
                    BLACK)
                x = burger[burger_id][burger_layer].DIFF_WITH_SPOT_x + \
                    burger_spot[burger_id].x
                y = burger[burger_id][burger_layer].DIFF_WITH_SPOT_y + \
                    burger_spot[burger_id].y
                screen.blit(burger[burger_id][burger_layer].FOOD_PIECES[burger_image],
                            (x + burger_image * FOOD_PIECE_WIDTH, y))

    # Refresh
    pygame.display.flip()
