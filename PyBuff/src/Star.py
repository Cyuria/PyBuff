# Create a star for pygame
import pygame
import rect

# Star class. Defaults to 5 points
class star(object):
    def __init__(self, Rect, points = 5):
        self.points = points
        self.Rect = Rect
        if (width < height):
            self.armLength = width/2
        else:
            self.armLength = height/2
    def draw(self, surface, angle, colour, width = 0):
        points = []

        pygame.draw.polygon(surface, colour, points, width)