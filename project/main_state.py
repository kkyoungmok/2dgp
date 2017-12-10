from pico2d import *

import game_framework
import title_state
import pause_state
import  collision

from night import Night # import Boy class from night.py
from ball import Ball, BigBall
from grass import Grass
from brick import Brick
from  zombie import Zombie




name = "main_state"

night = None
balls = None
big_balls = None
grass = None
brick = None
zombie= None


def create_world():
    global night, grass, balls, big_balls, brick, zombie
    night = Night()
    brick= Brick()
    big_balls = [BigBall() for i in range(10)]
    balls = [Ball()for i in range(10)]
    balls=big_balls+balls
    grass=Grass()
    zombie=Zombie()
    grass.set_center_object(night)
    night.set_background(grass)
    zombie.set_background(grass)

def destroy_world():
    global night, grass, balls, big_balls,brick,zombie

    del(night)
    del(balls)
    del(grass)
    del(big_balls)
    del(brick)
    del(zombie)




def enter():
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()



def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
        else:
            night.handle_event(event)





def collide_brick(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if top_a < bottom_b: return False
    if left_a > right_b : return False
    if right_a < left_b : return False
    if bottom_a > top_b: return False
    return True


def update(frame_time):

    night.update(frame_time)
    grass.update(frame_time)
    zombie.update(frame_time)

    if collide_brick(night, zombie):
        if night.state <10 and zombie.state>1:
           if night.a_t==0:
               if night.state == 9 or night.state == 7 or night.state == 5 :
                   night.state=11
                   night.dir=0
               else:
                   night.state = 10
                   night.dir = 0
           elif zombie.state==3:
               zombie.state = 1
               zombie.dir=0
           else:
               zombie.state = 0
               zombie.dir=0















def draw(frame_time):
    clear_canvas()
    grass.draw()
    night.draw()
    if zombie.x>1:
       zombie.draw()
       zombie.draw_bb()
##   for ball in balls:
#       ball.draw()
#
#    grass.draw_bb()
    night.draw_bb()
  #  for ball in balls:
 #       ball.draw_bb()

 #   brick.draw()
 #   brick.draw_bb()


    pass

    update_canvas()






