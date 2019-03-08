from pico2d import *
import game_world, game_framework


class Bow:
    image = None

    def __init__(self):
        if Bow.image == None:
            Bow.image = load_image('./resource/bow.png')
        self.x, self.y = 0, game_framework.HEIGHT // 2
        self.mx, self.my = game_framework.WIDTH // 2, game_framework.HEIGHT // 2
        self.rad = 0

    def update(self):
        self.rad = math.atan((self.my - 300) / self.mx)

    def draw(self):
        self.image.rotate_draw(self.rad, self.x, self.y, None, None)