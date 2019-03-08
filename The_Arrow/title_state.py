import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None
image2 = None
opacity, bright = 1, False


def enter():
    global image, image2, bgm
    if image == None:
        image = load_image('./resource/title.png')
        image2 = load_image('./resource/title_space.png')
        bgm = load_music('./resource/title.mp3')
    bgm.repeat_play()


def exit():
    global image, image2, bgm
    del(image)
    del(image2)
    bgm.stop()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    global opacity
    clear_canvas()
    image2.opacify(opacity)
    image.draw(game_framework.WIDTH // 2, game_framework.HEIGHT // 2)
    image2.draw(game_framework.WIDTH // 2, game_framework.HEIGHT // 2)
    update_canvas()


def update():
    global opacity, bright
    if opacity <= 0.05:
        bright = True
    elif opacity >= 0.95:
        bright = False
    if bright:
        opacity += game_framework.frame_time
    else:
        opacity -= game_framework.frame_time


def pause():
    pass


def resume():
    pass