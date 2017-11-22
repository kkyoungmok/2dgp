import random

from pico2d import *


class crush:
    def __init__(self):
        self.x, self.y = 150,110
        self.dir=0
        self.image = None

    def update(self, frame_time):
        self.x += self.dir

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 50, self.y - 110, self.x +50, self.y +110

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

