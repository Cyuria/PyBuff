# Create a star for pygame
import pygame
import rect

# Star class. Defaults to 5 points
class star(object):
    def __init__(self, Rect, points = 5):
        self.points = points
        self.Rect = Rect