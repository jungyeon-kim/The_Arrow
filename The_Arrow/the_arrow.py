import game_framework
import start_state
import main_state
import pico2d

pico2d.open_canvas(game_framework.WIDTH, game_framework.HEIGHT)
game_framework.run(start_state)
pico2d.close_canvas()
