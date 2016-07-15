__author__ = 't35khan'

# module for plateaus


class RectangularPlateau:

    def __init__(self, bounding_coordinates):
        self.bound = [bounding_coordinates[0], bounding_coordinates[1],
                      bounding_coordinates[2], bounding_coordinates[3]]

    def is_inside(self, co_ordinates):
        x, y = int(co_ordinates[0]), int(co_ordinates[1])
        if ((x >= self.bound[0] and y >= self.bound[1]) and
                (x <= self.bound[2] and y <= self.bound[2])):
            return True
        else:
            return False
