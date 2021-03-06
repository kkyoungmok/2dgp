import random

from pico2d import *


class Indiana:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 30.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    LEFT_JAT,RIGHT_JAT,LEFT_AT,RIGHT_AT,LEFT_JUMP, RIGHT_JUMP, LEFT_RUN,RIGHT_RUN, LEFT_STAND, RIGHT_STAND,LEFT_D, RIGHT_D = 0,1,2,3,4,5,6, 7, 8,9,10,11

    def __init__(self):
        self.x, self.y = 150, 100
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.frame = random.randint(0, 11)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0
        self.hi =0
        self.a_t = 0
        self.bef_jump=0
        self.bunji = 0
        self.life = 1
        self.bef_state=self.RIGHT_STAND
        self.state = self.RIGHT_STAND
        if Indiana.image == None:
            Indiana.image = load_image('INDIANA.png')

    def set_background(self, bg):
        self.bg = bg


    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Indiana.RUN_SPEED_PPS * frame_time
        self.total_frames += Indiana.FRAMES_PER_ACTION * Indiana.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 10
        self.x += (self.dir * distance)
        self.y += (self.hi*distance)

        self.x = clamp(0, self.x, self.bg.w)

        if self.y> (self.bef_jump+150):
            self.hi = -2
        if self.y < self.bef_jump:
            self.hi=0
            self.y -=2
            if self.state in (self.RIGHT_JUMP, self.LEFT_JUMP):
                self.state= self.bef_state

        if self.a_t > 0:
            self.a_t -=1
        if self.a_t == 0:
            if self.state in ( self.LEFT_JAT,self.RIGHT_JAT,self.LEFT_AT,self.RIGHT_AT):
                self.state= self.bef_state

        if self.state in (self.RIGHT_D,self.LEFT_D ):
            self.bef_jump +=0.5
            if self.bef_jump==100:
                 self.x,self.y=150,100
                 self.state=self.RIGHT_STAND

        self.x = clamp(120, self.x, self.bg.w)
        if self.bunji==0:
            self.y = clamp(100, self.y, self.bg.h)
        else:
            self.y = clamp(-120, self.y, self.bg.h)


        if self.x >300 and self.x<400:
            self.y = clamp(180, self.y, self.bg.h)

        if self.x >450 and self.x<650 and self.y>240:
            self.y = clamp(250, self.y, self.bg.h)

        if self.x >700 and self.x<1000:
            self.y = clamp(180, self.y, self.bg.h)

        if self.x >1700 and self.x<1800:
            self.y = clamp(180, self.y, self.bg.h)

        if self.x >1800 and self.x<1900 and self.y>240:
            self.y = clamp(250, self.y, self.bg.h)

        if self.x >1900 and self.x<2000 and self.y>310:
            self.y = clamp(320, self.y, self.bg.h)

        if self.x > 2500 and self.x < 2600:
            self.y = clamp(180, self.y, self.bg.h)

        if self.x >2600 and self.x<2800 and self.y>240:
            self.y = clamp(250, self.y, self.bg.h)

        if self.x >1500 and self.x<1600:
            self.bunji=1
        else:
            self.bunji=0



    def draw(self):

        self.image.clip_draw(self.frame * 70, self.state * 70, 70, 70, self.x - self.bg.window_left,
                             self.y - self.bg.window_bottom)

    def get_bb(self):
        if self.a_t==0:
           return self.x - 20-self.bg.window_left, self.y - 30-self.bg.window_bottom, self.x + 20-self.bg.window_left, self.y + 30-self.bg.window_bottom
        elif self.state in ( self.LEFT_JAT,self.LEFT_AT):
           return self.x - 200-self.bg.window_left, self.y - 30-self.bg.window_bottom, self.x + 20-self.bg.window_left, self.y + 30-self.bg.window_bottom
        elif self.state in (self.RIGHT_JAT,self.RIGHT_AT):
           return self.x - 20-self.bg.window_left, self.y - 30-self.bg.window_bottom, self.x + 200-self.bg.window_left, self.y + 30-self.bg.window_bottom

    def handle_event(self, event):

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.RIGHT_RUN):
                self.state = self.LEFT_RUN
                self.dir = -1
            if self.state in (self.RIGHT_JUMP, self.LEFT_JUMP):
                self.state = self.LEFT_RUN
                self.dir = -1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.LEFT_RUN):
                self.state = self.RIGHT_RUN
                self.dir = 1
            if self.state in (self.RIGHT_JUMP, self.LEFT_JUMP):
                self.state = self.RIGHT_RUN
                self.dir = 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.RIGHT_JUMP, self.LEFT_JUMP,self.LEFT_RUN,):
                self.state = self.LEFT_STAND
                self.dir = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_JUMP, self.LEFT_JUMP,self.RIGHT_RUN,):
                self.state = self.RIGHT_STAND
                self.dir = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_s):
               self.bef_state = self.state
               if self.state in (self.RIGHT_RUN,):
                   self.bef_state=self.state
                   self.state = self.RIGHT_JUMP
                   self.bef_jump=self.y
                   self.dir = 1
                   self.hi = 2
               if self.state in (self.RIGHT_STAND,):
                   self.state = self.RIGHT_JUMP
                   self.bef_jump = self.y
                   self.dir = 0
                   self.hi = 2
               if self.state in (self.LEFT_RUN,):
                   self.state = self.LEFT_JUMP
                   self.bef_jump = self.y
                   self.dir = -1
                   self.hi = 2
               if self.state in (self.LEFT_STAND,):
                   self.state = self.LEFT_JUMP
                   self.bef_jump = self.y
                   self.dir = 0
                   self.hi = 2
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
            if self.a_t ==0:
                 self.bef_state = self.state
                 self.a_t = 300
                 if self.state == self.RIGHT_STAND:
                     self.state = self.RIGHT_AT

                 if self.state in (self.RIGHT_JUMP,  self.RIGHT_RUN):
                     self.state = self.RIGHT_JAT

                 if self.state == self.LEFT_STAND:
                     self.state = self.LEFT_AT

                 if self.state in (self.LEFT_JUMP, self.LEFT_RUN):
                     self.state = self.LEFT_JAT


    def draw_bb(self):
        draw_rectangle(*self.get_bb())





