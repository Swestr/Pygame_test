import pygame
from constant import BLACK, BLUE, WHITE


def display(screen, player):
    STATE = player.character_state
    ID = player.character_state_id
    POSITION = (player.x, player.y)

    # Le background
    screen.fill(BLUE)
    # Le personnage
    if ID == -1:
        STATE.set_colorkey(BLACK)
        screen.blit(STATE, POSITION)
    else:
        STATE[ID % len(STATE)].set_colorkey(BLACK)
        screen.blit(STATE[ID % len(STATE)], POSITION)

    # Refresh
    pygame.display.flip()
