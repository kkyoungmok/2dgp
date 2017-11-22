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







    # fill here

