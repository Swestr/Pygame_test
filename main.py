import pygame

# Import from my files
from display import display
from constant import WIDTH, HEIGHT, FPS
from player import Player

# Initialisation sons et pygame
pygame.mixer.init()
pygame.init()

# Création de la fenêtre - doubles parenthèses car tuple
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
# Nom du jeu
pygame.display.set_caption("Burger Time")

# Horloge - pour les FPS
clock = pygame.time.Clock()

# Création du joueur
character = Player()

# Appel du display (fonction personnelle dans display.py)
display(screen, character)

# Boucle - le jeu
running = True
while running:
    # Gère les FPS
    clock.tick(FPS)

    # Récupère les évenements
    events = pygame.event.get()
    # S'il n'y a pas d'évenement,on vérifie quelle touche est toujours pressée
    if len(events) == 0:
        if character.dead:
            character.die()
        else:
            # Vérifie si une touche est encore pressée
            pressed = pygame.key.get_pressed()
            if(pressed[pygame.K_UP] or pressed[pygame.K_DOWN]
                or pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT]
                    or pressed[pygame.K_SPACE]):
                character.continue_move()
            else:
                character.stand()
    # On vérifie chacun des events
    for event in events:
        # Bouton fermer la fenêtre
        if event.type == pygame.QUIT:
            running = False

        # Gestion des touches si le perso n'est pas mort
        elif (event.type == pygame.KEYDOWN):
            if(character.dead is False):
                # HAUT
                if event.key == pygame.K_UP:
                    character.climb_up()
                # BAS
                if event.key == pygame.K_DOWN:
                    character.climb_down()
                # DROITE
                if event.key == pygame.K_RIGHT:
                    character.goRight()
                # GAUCHE
                if event.key == pygame.K_LEFT:
                    character.goLeft()
                # SPACE
                if event.key == pygame.K_SPACE:
                    character.die()
            else:
                character.die()
            # ECHAP
            if event.key == pygame.K_ESCAPE:
                running = False

    # Mis à jour de l'affichage
    display(screen, character)

pygame.quit()
