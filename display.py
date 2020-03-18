import pygame
from constant import BLACK, FOOD_PIECE_WIDTH


def display(screen, player, background, food):
    STATE = player.character_state
    ID = player.character_state_id
    POSITION = (player.x, player.y)

    # Le background
    screen.fill(BLACK)
    # Le personnage
    if ID == -1:
        STATE.set_colorkey(BLACK)
        screen.blit(STATE, POSITION)
    else:
        STATE[ID % len(STATE)].set_colorkey(BLACK)
        screen.blit(STATE[ID % len(STATE)], POSITION)

    # Un emplacement à burger entier
    background.BURGER_SPOT.set_colorkey(BLACK)
    screen.blit(background.BURGER_SPOT, (background.x, background.y))

    # Un pain inférieur du burger sur l'emplacement
    for i in range(len(food.FOOD_PIECES)):
        food.FOOD_PIECES[i].set_colorkey(BLACK)
        x = food.DIFF_WITH_SPOT_x + background.x
        y = food.DIFF_WITH_SPOT_y + background.y
        screen.blit(food.FOOD_PIECES[i],
                    (x + i * FOOD_PIECE_WIDTH, y))

    # Refresh
    pygame.display.flip()
