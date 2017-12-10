import random

from pico2d import *



class Zombie:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 10                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    LEFT_DIE, RIGHT_DIE,LEFT_RUN,RIGHT_RUN= 0,1,2,3

    def __init__(self):
        self.x, self.y = 600, 100
        self.frame = random.randint(0, 4)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.total_frame = 0
        self.dir = 0
        self.up = 0;
        self.run_frames = 0
        self.stand_frames = 0
        self.distance = 0
        self.height = 0;
        self.state = self.LEFT_RUN
        if Zombie.image == None:
            Zombie.image = load_image('zombie.png')

    def set_background(self, bg):
        self.bg = bg

    def handle_left_run(self):
        self.dir = -1
        self.state = self.LEFT_RUN


    def handle_right_run(self):
        self.dir = 1
        self.state = self.RIGHT_RUN
        if self.distance % 30 > 29:
            self.dir = -1
            self.state = self.LEFT_RUN

    def handle_left_die(self):
        self.dir = 0
        self.state = self.LEFT_DIE

    def handle_right_die(self):
        self.dir = 0
        self.state = self.RIGHT_DIE

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_DIE:handle_left_die,
        RIGHT_DIE:handle_right_die

    }


    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Zombie.RUN_SPEED_PPS * frame_time
        self.total_frames += Zombie.FRAMES_PER_ACTION * Zombie.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 10
        self.x += (self.dir * distance)
        self.y += (self.up * self.height)
        self.height = self.y
        self.distance = self.x
        self.handle_state[self.state](self)






    def draw(self):
        self.image.clip_draw(self.frame * 70, self.state * 70, 70, 70, self.x - self.bg.window_left, self.y - self.bg.window_bottom)

    def get_bb(self):

           return self.x - 20-self.bg.window_left, self.y - 30-self.bg.window_bottom, self.x + 20-self.bg.window_left, self.y + 30-self.bg.window_bottom




    def draw_bb(self):
        draw_rectangle(*self.get_bb())





