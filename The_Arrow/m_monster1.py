from pico2d import *
import game_world, game_framework
import main_state
import random

# Monster Run Speed
PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 20 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Monster Action Speed
TIME_PER_ACTION = 0.9
ACTION_PER_TIME = 1 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6


class Monster:
    image = None

    def __init__(self):
        if Monster.image == None:
            Monster.image = load_image('./resource/monster1.png')
        self.sound = load_wav('./resource/die.wav')
        self.x, self.y = game_framework.WIDTH + 30, random.randint(100, 500)
        self.hp, self.opacity = 4, 1
        self.damage = 4
        self.frame = 0
        self.show = False

    def update(self):
        if self.show:
            # 프레임
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
            if self.x > 200:    # 이동
                self.x -= RUN_SPEED_PPS * game_framework.frame_time
            else:   # 성 체력 감소
                main_state.ui.player_hp -= self.damage * game_framework.frame_time
            for main_state.arrow in main_state.arrows:    # 충돌체크
                if main_state.arrow.x > self.x - 30 and main_state.arrow.x < self.x + 30 and \
                        main_state.arrow.y > self.y - 30 and main_state.arrow.y < self.y + 30\
                        and self.hp > 0:
                    self.hp -= main_state.arrow.damage
                    main_state.arrow.show = False
                    main_state.arrow.x, main_state.arrow.y = 0, game_framework.HEIGHT // 2
                if main_state.arrow.x2 > self.x - 30 and main_state.arrow.x2 < self.x + 30 and \
                        main_state.arrow.y2 > self.y - 30 and main_state.arrow.y2 < self.y + 30\
                        and self.hp > 0:
                    self.hp -= main_state.arrow.damage
                    main_state.arrow.show2 = False
                    main_state.arrow.x2, main_state.arrow.y2 = 0, game_framework.HEIGHT // 2
                if main_state.arrow.x3 > self.x - 30 and main_state.arrow.x3 < self.x + 30 and \
                        main_state.arrow.y3 > self.y - 30 and main_state.arrow.y3 < self.y + 30\
                        and self.hp > 0:
                    self.hp -= main_state.arrow.damage
                    main_state.arrow.show3 = False
                    main_state.arrow.x3, main_state.arrow.y3 = 0, game_framework.HEIGHT // 2
            if self.hp <= 0 and self.opacity > 0:   # 투명도 컨트롤
                self.opacity -= game_framework.frame_time * 2
            if self.opacity <= 0:   # 죽음
                main_state.ui.gold += 150
                game_framework.kill += 1
                self.sound.play(1)
                self.show = False

    def draw(self):
        self.image.opacify(self.opacity)
        if self.show:
            if self.x > 200:
                self.image.clip_draw(int(self.frame) * 52, 300, 50, 50, self.x, self.y, 70, 70)
            else:
                self.image.clip_draw(int(self.frame) * 51, 120, 50, 47, self.x, self.y, 70, 70)