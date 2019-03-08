from pico2d import *
import game_world, game_framework
import main_state


class Ui:
    back_ground = None

    def __init__(self):
        if Ui.back_ground == None:
            Ui.back_ground = load_image('./resource/BACK_GROUND.png')
            self.power_ui = load_image('./resource/power_ui.png')
            self.quantity_ui = load_image('./resource/quantity_ui.png')
            self.skill_ui = load_image('./resource/skill_ui.png')
            self.gold_ui = load_image('./resource/gold_ui.png')
            self.hp_bar1 = load_image('./resource/hp_bar1.png')
            self.hp_bar2 = load_image('./resource/hp_bar2.png')
            self.font = load_font('./resource/ENCR10B.TTF', 30)
            self.hand_arrow = load_image('./resource/hand_arrow.png')
        self.sound = load_wav('./resource/click.wav')
        self.player_hp = 200
        self.gold = 100000
        self.difficulty_count = 1

    def update(self):
        pass

    def draw(self):
        self.back_ground.draw(game_framework.WIDTH // 2, game_framework.HEIGHT // 2)
        self.power_ui.draw(800, 60)
        self.quantity_ui.draw(900, 60)
        self.skill_ui.draw(500, 60)
        self.gold_ui.draw(790, 570)
        self.hp_bar1.draw(175, 60)
        self.hp_bar2.clip_draw(0, 0, int(self.player_hp), 18, 205 - (200 - int(self.player_hp)) // 2, 59)
        self.font.draw(820, 570, '%d' % self.gold, (255, 255, 255))
        self.font.draw(775, 525, 'KILL:%d' % game_framework.kill, (255, 255, 255))
        self.hand_arrow.draw(main_state.bow.mx, main_state.bow.my)