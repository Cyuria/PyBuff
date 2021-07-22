# Create a star for pygame
import pygame
import rect

# Star class. Defaults to 5 points
class star(object):
    def __init__(self, rect, points = 5):
        self.points = points
        self.x = rect.x
        self.y = rect.y
        self.width = rect.width
        self.height = rect.height