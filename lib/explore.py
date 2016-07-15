from lib.rover import NaiveRover
from lib.plateau import RectangularPlateau
from lib.controller import Controller

__author__ = 't35khan'


class Explore:

    def __init__(self, input_file_path):
        controller = Controller(input_file_path)
        self.plateau = RectangularPlateau(controller.get_plateau_bounds())
        self.rover_commands = controller.get_rover_commands()
        self.rovers = []

    def run(self):
        for i in range(0, len(self.rover_commands), 2):
            if self.plateau.is_inside(self.rover_commands[i]):  # Check whether rover is inside plateau initially
                rover = NaiveRover(self.rover_commands[i])
            else:
                print('Initial location {0} outside plateau'.format(self.rover_commands[i]))
                continue
            for step in self.rover_commands[i+1][0]:            # use input command to get new location
                rover_x, rover_y, rover_orientation = rover.get_new_location(step)
                if self.plateau.is_inside([rover_x, rover_y]):  # if new location is inside plateau set location
                    rover.set_location(rover_x, rover_y, rover_orientation)
            self.rovers.append(rover)

        for rover in self.rovers:
            print(rover.x, rover.y, rover.orientation)

        return self.rovers

if __name__ == '__main__':
    path = '../test_input.txt'
    Explore(path).run()
