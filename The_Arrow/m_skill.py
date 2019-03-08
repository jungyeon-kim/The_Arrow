from pico2d import *
import game_world, game_framework

# Skill Action Speed
TIME_PER_ACTION = 0.9
ACTION_PER_TIME = 1 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

BALL_SPEED = 300


class Skill:
    hurricane = None

    def __init__(self):
        if Skill.hurricane == None:
            Skill.hurricane = load_image('./resource/skill1.png')
            self.thunder = load_image('./resource/skill2.png')
        self.sound = load_wav('./resource/skill.wav')
        self.x, self.y = game_framework.WIDTH // 2, game_framework.HEIGHT // 2
        self.rad = 0
        self.opacity, self.opacity2, self.bright = 0, 0.2, False
        self.show, self.damage_on = False, False

    def update(self):
        if self.show:
            self.rad -= game_framework.frame_time * 10
            if self.opacity <= 0.05:
                self.bright = True
            elif self.opacity >= 0.95:
                self.bright = False
            if self.rad > -40:
                if self.bright:
                    self.opacity += game_framework.frame_time * 2
                else:
                    self.opacity -= game_framework.frame_time * 2
            elif self.rad <= -40:
                self.opacity -= game_framework.frame_time * 0.5
                self.opacity2 -= game_framework.frame_time * 0.2
        if self.rad < -50:
            self.__init__()

    def draw(self):
        if self.show and self.opacity > 0:
            self.hurricane.opacify(self.opacity2)
            self.hurricane.rotate_draw(self.rad, self.x, self.y, 1500, 1500)
            self.thunder.opacify(self.opacity)
            self.thunder.draw(self.x, self.y)