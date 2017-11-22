import random

from pico2d import *
from boy import Boy


class Grass:
    def __init__(self):
        self.x, self.y = 4000, 300
        self.dir = 0
        self.image = load_image('stage_1.png')

    def update(self, frame_time):
        self.x += self.dir
        boy=Boy()




    def draw(self):
        self.image.draw(self.x, self.y)


    def get_bb(self):

        return self.x  -4000, self.y - 300, self.x + 4000, self.y -230


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    # fill here

