from pygame.image import load
from pygame.transform import scale


def load_sprit(who, what, nb_sprites, width, height):
    path = "src/" + who + "/" + what + "/"
    sprit_images = []
    for sprite_id in range(1, nb_sprites + 1):
        img = load(path + str(sprite_id) + ".png")
        img = scale(img, (width, height))
        sprit_images.append(img)
    return sprit_images
