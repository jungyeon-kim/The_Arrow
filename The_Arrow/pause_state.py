from pico2d import *
import game_framework
import main_state

name = "PauseState"
image = None

blink = 0


def enter():
    global image
    image = load_image('./resource/pause.png')


def exit():
    global image
    del (image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()


def update():
    global blink
    blink = (blink + 1) % 2
    delay(0.5)


def draw():
    global blink
    clear_canvas()
    main_state.draw()
    if blink == 0:
        image.draw(game_framework.WIDTH // 2, game_framework.HEIGHT // 2)
    update_canvas()


def resume():
    pass






