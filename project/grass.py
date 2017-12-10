import random

from pico2d import *
from night import Night


class Grass:
    def __init__(self):
        self.image = load_image('stage_1.png')
        self.speed = 0
        self.left = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h


    def set_center_object(self, boy):
        self.center_object = boy

    def update(self, frame_time):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width // 2, self.w - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height // 2, self.h - self.canvas_height)

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0,
                                       0)






    # fill here

