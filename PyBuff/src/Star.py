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
    def draw(self, surface, colour = self.colour, armLength = self.armLength, innerdist = self.innerdist, width = 0, fill = false, edgeColour = (0,0,0)):
        coords = []
        for arm in range(self.points):
            coords.append(moremath.tanLen(arm * 360/self.points, armLength))
            coords.append(moremath.tanLen((arm + 0.5) * 360/self.points, innerdist))
        if fill:
            pygame.draw.polygon(surface, edgeColour, coords, width)
            pygame.draw.polygon(surface, colour, coords, 0)
        else:
            pygame.draw.polygon(surface, colour, coords, width)
        
