# Create a star for pygame
import pygame

# Star class. Defaults to 5 points
class Star(Object):
    def __init__(self, x, y, points = 5):
        self.points = points
        self.x = x
        self.y = y