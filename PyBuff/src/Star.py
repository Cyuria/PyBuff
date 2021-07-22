# Create a star for pygame
import pygame
import rect

# Star class. Defaults to a black 5 pointed star
class star(object):
    def __init__(self, Rect, points = 5, colour = (0, 0, 0)):
        self.points = points
        self.colour = colour

        # Handle rect variable
        if type(Rect) == list:
            self.Rect = rectFromList(Rect)
        elif type(Rect) != rect:
            raise TypeError("Variable Rect of class star is not a rect")
        else:
            self.Rect = Rect

        # Create ArmLength variable to simplify draw function
        if (width < height):
            self.armLength = width/2
        else:
            self.armLength = height/2
    def draw(self, surface, angle, colour = (), width = 0):
        if colour == ():
            colour = self.colour
        coords = []
        for arm in range(self.points):
            pass
        pygame.draw.polygon(surface, colour, coords, width)