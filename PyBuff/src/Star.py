# Create a star for pygame
import pygame
import rect
import moremath

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
    # Create function to handle drawing in pygame
    def draw(self, surface, angle, colour = self.colour, width = 0, fill = false):
        coords = []
        for arm in range(self.points):
            # use Tan(deg) = y/x. multiply by x and got number
            moremath.tanLen(arm * 360/self.points, self.armLength)
            pass
        pygame.draw.polygon(surface, colour, coords, width)
        if fill:
            pygame.draw.polygon(surface, colour, coords, 0)