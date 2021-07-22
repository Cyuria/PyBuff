# Takes a list of [x, y, width, height] and returns a Rect from these values
def rectFromList(lst):
    return Rect(lst[0], lst[1], lst[2], lst[3])

# Rect class
class rect(object):
    def __init__(self, x = 0, y = 0, width = 0, height = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def getDiagonals(self):
        return (self.width^2 + self.height^2)^0.5