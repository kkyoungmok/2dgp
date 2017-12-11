import game_framework
from pico2d import *

import main_state

name = "PauseState"

Pause = None
onoff=0
def enter():

    global Pause
    Pause = load_image('PAUSE.png')


def exit():
    global Pause
    del(Pause)


def handle_events(frame_time):
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()


def draw(frame_time):
    global onoff
    clear_canvas()
    if (onoff<100):
        Pause.draw(400,300)
    if (onoff==200):
         onoff=0
    main_state.player.draw()
    main_state.grass.draw()
    onoff += 1
    update_canvas()







def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass
