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

    LEFT_D, RIGHT_D ,LEFT_RUN,RIGHT_RUN= 0,1,2,3

    def __init__(self):
        self.x, self.y = 600, 100
        self.frame = random.randint(0, 4)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir =-0.5
        self.wt = 0
        self.state = self.LEFT_RUN
        if Zombie.image == None:
            Zombie.image = load_image('zombie.png')


    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.wt+=1
        if self.wt > 100:
            if self.dir < 0:
                self.dir = 0.5
                self.state = self.RIGHT_RUN
            else:
                self.dir = -0.5
                self.state = self.LEFT_RUN
        self.wt=0


        self.life_time += frame_time
        distance = Zombie.RUN_SPEED_PPS * frame_time
        self.total_frames += Zombie.FRAMES_PER_ACTION * Zombie.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 10
        self.x += (self.dir * distance)









        self.x = clamp(0, self.x, 800)


    def draw(self):
        self.image.clip_draw(self.frame * 70, self.state * 70, 70, 70, self.x, self.y)

    def get_bb(self):

           return self.x - 20, self.y - 30, self.x + 20, self.y + 30




    def draw_bb(self):
        draw_rectangle(*self.get_bb())





