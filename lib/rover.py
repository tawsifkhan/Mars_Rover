__author__ = 't35khan'

# module for rovers


class NaiveRover:
    def __init__(self, args):
        self.x, self.y, self.orientation = int(args[0]), int(args[1]), args[2]
        self.possible_moves = ['L', 'R', 'M']
        self.log_of_positions = [[args[0], args[1], args[2]]]

    def get_new_location(self, step):
        move_dict = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
        left_rotate_dict = {'N': 'W', 'S': 'E', 'E': 'N', 'W': 'S'}
        right_rotate_dict = {'N': 'E', 'S': 'W', 'E': 'S', 'W': 'N'}
        if step == 'M':
            x = move_dict[self.orientation][0] + self.x
            y = move_dict[self.orientation][1] + self.y
            orientation = self.orientation
        elif step == 'L':
            x, y = self.x, self.y
            orientation = left_rotate_dict[self.orientation]
        elif step == 'R':
            x, y = self.x, self.y
            orientation = right_rotate_dict[self.orientation]
        else:
            return self.x, self.y, self.orientation
        return x, y, orientation

    def set_location(self, x, y, orientation):
        self.x, self.y, self.orientation = x, y, orientation
        self.log_of_positions.append([self.x, self.y, self.orientation])
