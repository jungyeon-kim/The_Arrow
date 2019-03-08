from pico2d import *
import game_world, game_framework

# Arrow Run Speed
PIXEL_PER_METER = (10.0 / 0.05)  # 10 pixel 200 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Arrow Action Speed
TIME_PER_ACTION = 0.9
ACTION_PER_TIME = 1 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6


class Arrow:
    image = None

    def __init__(self):
        if Arrow.image == None:
            Arrow.image = load_image('./resource/arrow.png')
        self.sound = load_wav('./resource/arrow.wav')
        self.x, self.y = 0, game_framework.HEIGHT // 2
        self.x2, self.y2 = 0, game_framework.HEIGHT // 2
        self.x3, self.y3 = 0, game_framework.HEIGHT // 2
        self.cx, self.cy = game_framework.WIDTH // 2, game_framework.HEIGHT // 2
        self.cx2, self.cy2 = game_framework.WIDTH // 2, game_framework.HEIGHT // 2
        self.cx3, self.cy3 = game_framework.WIDTH // 2, game_framework.HEIGHT // 2
        self.rad = 0
        self.damage = 1
        self.increase_quantity = False
        self.show, self.show2, self.show3 = False, False, False

    def update(self):
        self.rad = math.atan((self.cy - 300) / self.cx)     # 이미지 회전각
        self.rad2 = math.atan((self.cy2 - 300) / self.cx2) + 0.1
        self.rad3 = math.atan((self.cy3 - 300) / self.cx3) - 0.1
        if self.show:                               # 이동
            self.x += math.cos((self.cy - 300) / self.cx) * RUN_SPEED_PPS * game_framework.frame_time
            self.y += math.sin((self.cy - 300) / self.cx) * RUN_SPEED_PPS * game_framework.frame_time
        if self.show2 and self.increase_quantity:   # 이동
            self.x2 += math.cos((self.cy2 - 300) / self.cx2) * RUN_SPEED_PPS * game_framework.frame_time
            self.y2 += math.sin((self.cy2 - 300) / self.cx2) * RUN_SPEED_PPS * game_framework.frame_time + 60 * game_framework.frame_time
        if self.show3 and self.increase_quantity:   # 이동
            self.x3 += math.cos((self.cy3 - 300) / self.cx3) * RUN_SPEED_PPS * game_framework.frame_time
            self.y3 += math.sin((self.cy3 - 300) / self.cx3) * RUN_SPEED_PPS * game_framework.frame_time - 60 * game_framework.frame_time
        if self.x > 1100 or self.y < -100 or self.y > 700:  # 초기화
            self.show = False
            self.x, self.y = 0, game_framework.HEIGHT // 2
        if self.x2 > 1100 or self.y2 < -100 or self.y2 > 700:  # 초기화
            self.show2 = False
            self.x2, self.y2 = 0, game_framework.HEIGHT // 2
        if self.x3 > 1100 or self.y3 < -100 or self.y3 > 700:  # 초기화
            self.show3 = False
            self.x3, self.y3 = 0, game_framework.HEIGHT // 2

    def draw(self):
        if self.show:
            self.image.rotate_draw(self.rad, self.x, self.y, None, None)
        if self.show2 and self.increase_quantity:
            self.image.rotate_draw(self.rad2, self.x2, self.y2, None, None)
        if self.show3 and self.increase_quantity:
            self.image.rotate_draw(self.rad3, self.x3, self.y3, None, None)