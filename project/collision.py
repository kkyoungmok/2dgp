from pico2d import *

import game_framework


from boy import Boy # import Boy class from boy.py
from ball import Ball, BigBall
from grass import Grass
from brick import Brick
from crush import Crush



name = "collision"

boy = None
balls = None
big_balls = None
grass = None
brick = None
crush = None

def create_world():
    global boy, grass, balls, big_balls, brick, crush
    boy = Boy()
    brick= Brick()

    big_balls = [BigBall() for i in range(10)]
    balls = [Ball()for i in range(10)]
    balls=big_balls+balls
    grass=Grass()
    crush=Crush()



def destroy_world():
    global boy, grass, balls, big_balls,brick, crush

    del(boy)
    del(balls)
    del(grass)
    del(big_balls)
    del(brick)
    del(crush)



def enter():
    open_canvas()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                boy.handle_event(event)



def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def collide_brick(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if top_a <= bottom_b: return False
    if left_a > right_b : return False
    if right_a < left_b : return False
    if bottom_a > top_b: return False
    return True


def update(frame_time):

    boy.update(frame_time)
    grass.update(frame_time)
    crush.update(frame_time)
#    for ball in balls:
#        ball.update(frame_time)
#
#    for ball in balls:
#        if collide(boy,ball):
#            balls.remove(ball)
##
#    for ball in big_balls:
#        if collide(grass, ball):
#            ball.stop()
#    for ball in big_balls:
#        if collide(crush, ball):
#             ball.stop()
#



#    for ball in big_balls:
#        if collide_brick(brick,ball):
#            if ball.y > brick.y+38:
#                if brick.dir<0:
#                    ball.y=brick.y+40
#                    ball.x-=0.5
#                if brick.dir>0:
#                    ball.y= brick.y+40
#                    ball.x+=0.5
 #   if collide_brick(brick,boy):
 #       if boy.y > brick.y+58:
 #           if brick.dir < 0:
 #               boy.y = brick.y + 60
 #               boy.x -= 0.5
 #           if brick.dir > 0:
 #               boy.y = brick.y + 60
 #               boy.x += 0.5
            #

    if boy.x >= 350:
        if grass.x > -3200:
            boy.x = 350
            if boy.dir==1:
                grass.dir = -0.5
                crush.dir = -0.5
            if boy.dir != 1:
                grass.dir = 0
                crush.dir = 0
    if grass.x < -3200:
        grass.dir = 0
        crush.dir = 0
        grass.x = -3200
        crush.x = -3200
    if grass.x < 4000:
        if boy.x <= 340:
            boy.x = 340
            if boy.dir == -1:
                grass.dir = 0.5
                crush.dir =0.5
            if boy.dir != -1:
                grass.dir = 0
                crush.dir = 0
    if grass.x > 4000:
        grass.dir = 0
        crush.dir = 0
        crush.x = 4000
        grass.x = 4000









def draw(frame_time):
    clear_canvas()
    grass.draw()
    boy.draw()
##   for ball in balls:
#       ball.draw()
#
    grass.draw_bb()
    boy.draw_bb()
  #  for ball in balls:
 #       ball.draw_bb()

 #   brick.draw()
 #   brick.draw_bb()
    crush.draw_bb()

    pass

    update_canvas()






