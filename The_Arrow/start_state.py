import game_framework
import title_state
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    if image == None:
        image = load_image('./resource/kpu_credit.png')


def exit():
    global image
    del(image)


def update():
    global logo_time
    if (logo_time > 2.0):
        logo_time = 0
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(game_framework.WIDTH // 2, game_framework.HEIGHT // 2)
    update_canvas()


def handle_events():
    events = get_events()


def pause():
    pass


def resume():
    pass