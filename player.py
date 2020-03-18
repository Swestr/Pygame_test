from pygame.image import load
from pygame.transform import flip, scale
from constant import WIDTH, HEIGHT, IMG_WIDTH, IMG_HEIGHT


def load_sprit(who, what, nb_sprites):
    path = "src/" + who + "/" + what + "/"
    sprit_images = []
    for sprite_id in range(1, nb_sprites + 1):
        img = load(path + str(sprite_id) + ".png")
        img = scale(img, (IMG_WIDTH, IMG_HEIGHT))
        sprit_images.append(img)
    return sprit_images


class Player:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.step = 10
        self.dead = False

        self.CHARACTER_STANDS = load_sprit("character", "stands", 1)[0]
        self.CHARACTER_WALK_LEFT = load_sprit("character", "walks", 3)
        self.CHARACTER_DIES = load_sprit("character", "dies", 6)
        self.CHARACTER_CLIMBS_UP = load_sprit("character", "climbs", 4)
        self.CHARACTER_CLIMBS_DOWN = load_sprit("character", "climbs", 4)
        self.CHARACTER_WALK_RIGHT = load_sprit("character", "walks", 3)
        for id in range(len(self.CHARACTER_WALK_RIGHT)):
            self.CHARACTER_WALK_RIGHT[id] = flip(self.CHARACTER_WALK_RIGHT[id],
                                                 True, False)
        self.character_state = self.CHARACTER_STANDS
        self.character_state_id = -1

    def goRight(self):
        if(self.character_state == self.CHARACTER_WALK_RIGHT):
            self.character_state_id += 1
        else:
            self.character_state_id = 0
            self.character_state = self.CHARACTER_WALK_RIGHT
        if(self.x + IMG_WIDTH <= WIDTH):
            self.x += self.step

    def goLeft(self):
        if(self.character_state == self.CHARACTER_WALK_LEFT):
            self.character_state_id += 1
        else:
            self.character_state_id = 0
            self.character_state = self.CHARACTER_WALK_LEFT
        if(self.x > 0):
            self.x -= self.step

    def climb_up(self):
        if(self.character_state == self.CHARACTER_CLIMBS_UP):
            self.character_state_id += 1
        else:
            self.character_state_id = 0
            self.character_state = self.CHARACTER_CLIMBS_UP
        if(self.y > 0):
            self.y -= self.step

    def climb_down(self):
        if(self.character_state == self.CHARACTER_CLIMBS_DOWN):
            self.character_state_id += 1
        else:
            self.character_state_id = 0
            self.character_state = self.CHARACTER_CLIMBS_DOWN
        if(self.y + IMG_HEIGHT <= HEIGHT):
            self.y += self.step

    def die(self):
        if(self.dead):
            if self.character_state_id < len(self.CHARACTER_DIES) - 1:
                self.character_state_id += 1
                self.character_state = self.CHARACTER_DIES

        else:
            self.character_state_id = 0
            self.character_state = self.CHARACTER_DIES

        self.dead = True

    def stand(self):
        self.character_state = self.CHARACTER_STANDS
        self.character_state_id = -1

    def continue_move(self):
        if(self.dead):
            self.die()
        elif self.character_state == self.CHARACTER_DIES:
            self.die()
        elif self.character_state == self.CHARACTER_WALK_LEFT:
            self.goLeft()
        elif self.character_state == self.CHARACTER_WALK_RIGHT:
            self.goRight()
        elif self.character_state == self.CHARACTER_CLIMBS_UP:
            self.climb_up()
        elif self.character_state == self.CHARACTER_CLIMBS_DOWN:
            self.climb_down()
        else:
            self.stand()
