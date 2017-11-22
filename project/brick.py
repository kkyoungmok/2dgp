import random

from pico2d import *

class Brick:
    image = None;


    def __init__(self):
        self.x, self.y =100 , 200
        self.dir = 0.5
        if Brick.image == None:
            Brick.image = load_image('brick180x40.png')

    def update(self, frame_time):
        self.x += self.dir
        if self.x > 600:
            self.dir = -0.5
            self.x = 600
        elif self.x < 100:
            self.dir = 0.5
            self.x = 100

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x +90, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


