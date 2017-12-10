import random

from pico2d import *


class Crush:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    GROUND_WIDTH_METER = 3
    GROUND_HEIGHT_METER = 2.25

    GROUND_WIDTH = (GROUND_WIDTH_METER * PIXEL_PER_METER)
    GROUND_HEIGHT = (GROUND_HEIGHT_METER * PIXEL_PER_METER)

    def __init__(self):
        self.x, self.y = 50,37
        self.dir=0
        self.image = load_image('5.png')

    def update(self, frame_time):
        distance = Crush.PIXEL_PER_METER * frame_time


    def set_background(self, bg):
        self.bg = bg

    def draw(self):
        self.image.draw(self.x - self.bg.window_left, self.y - self.bg.window_bottom)

    def get_bb(self):
        return self.x - 50 - self.bg.window_left, self.y - 37 - self.bg.window_bottom, self.x + 50 - self.bg.window_left, self.y + 38 - self.bg.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

