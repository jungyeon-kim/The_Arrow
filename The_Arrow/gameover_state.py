import game_framework
from pico2d import *


name = "GameOverState"
image = None
logo_time = 0.0


def enter():
    global image, sound, font
    if image == None:
        image = load_image('./resource/gameover.png')
        sound = load_wav('./resource/gameover.wav')
        font = load_font('./resource/ENCR10B.TTF', 30)
    sound.play()


def exit():
    global image
    del(image)


def update():
    pass


def draw():
    global image, font
    clear_canvas()
    image.draw(game_framework.WIDTH // 2, game_framework.HEIGHT // 2)
    font.draw(30, 40, 'KILL:%d' % game_framework.kill, (255, 255, 255))
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()


def pause():
    pass


def resume():
    pass